import os
import uuid
from pathlib import Path
import hashlib

from fastapi import UploadFile

from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.knowledge_source import KnowledgeSource


def validate_file(
    file: UploadFile
):

    extension = file.filename.split(".")[-1].lower()


    if extension not in settings.ALLOWED_FILE_TYPES:

        raise ValueError(
            "File type not allowed"
        )


    file.file.seek(0, 2)

    file_size = file.file.tell()

    file.file.seek(0)


    max_size = (
        settings.MAX_UPLOAD_SIZE_MB
        * 1024
        * 1024
    )


    if file_size > max_size:

        raise ValueError(
            "File size exceeds limit"
        )


    return extension


def calculate_checksum(
    file: UploadFile
):

    sha256 = hashlib.sha256()

    file.file.seek(0)

    while True:

        chunk = file.file.read(1024 * 1024)

        if not chunk:
            break

        sha256.update(chunk)


    file.file.seek(0)

    return sha256.hexdigest()

def save_uploaded_file(
    file: UploadFile,
    organization_id: int
):

    extension = extension = validate_file(file)

    organization_folder = Path(
        settings.UPLOAD_DIR
    ) / f"organization_{organization_id}"


    organization_folder.mkdir(
        parents=True,
        exist_ok=True
    )


    unique_filename = (
        f"{uuid.uuid4().hex}.{extension}"
    )


    file_path = (
        organization_folder /
        unique_filename
    )


    with open(file_path, "wb") as buffer:

        buffer.write(
            file.file.read()
        )


    return {
        "file_name": file.filename,
        "stored_name": unique_filename,
        "file_path": str(file_path),
        "extension": extension
    }



def create_knowledge_source_record(
    db: Session,
    file_info: dict,
    organization_id: int
):

    source = KnowledgeSource(
        organization_id=organization_id,
        source_type=file_info["extension"],
        title=file_info["file_name"],
        file_name=file_info["file_name"],
        file_path=file_info["file_path"],
        status="uploaded",
        checksum=file_info.get("checksum")
    )


    db.add(source)

    db.commit()

    db.refresh(source)

    return source