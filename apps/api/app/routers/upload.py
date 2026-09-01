from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.upload import UploadResponse

from app.services.upload import (
    calculate_checksum,
    save_uploaded_file,
    create_knowledge_source_record
)
from app.services.knowledge_processor import (
    process_knowledge_source
)

from app.dependencies.auth import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post(
    "",
    response_model=UploadResponse
)
def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    try:

        checksum = calculate_checksum(file)
        file_info = save_uploaded_file(
            file=file,
            organization_id=current_user.organization_id
        )
        file_info["checksum"] = checksum

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


    source = create_knowledge_source_record(
        db=db,
        file_info=file_info,
        organization_id=current_user.organization_id
    )
    db.refresh(source)

    process_knowledge_source(
        db=db,
        knowledge_source=source
    )


    return {
        "message": "File uploaded successfully",
        "file_name": source.file_name,
        "source_id": source.id,
        "status": source.status
    }