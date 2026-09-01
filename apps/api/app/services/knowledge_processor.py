from pathlib import Path
from app.services.document import (
    extract_text_from_txt,
    extract_text_from_pdf,
    extract_text_from_docx
)
from app.services.chunking import split_text_into_chunks
from sqlalchemy.orm import Session

from app.models.knowledge_chunk import KnowledgeChunk

def detect_file_type(
    file_path: str
) -> str:

    extension = (
        Path(file_path)
        .suffix
        .lower()
        .replace(".", "")
    )

    return extension


def extract_document_text(
    file_path: str
):

    file_type = detect_file_type(file_path)


    if file_type == "txt":

        return extract_text_from_txt(
            file_path
        )


    elif file_type == "pdf":

        return extract_text_from_pdf(
            file_path
        )


    elif file_type == "docx":

        return extract_text_from_docx(
            file_path
        )


    else:

        raise ValueError(
            "Unsupported file type"
        )


def normalize_extracted_text(
    extracted_data
) -> list[dict]:

    if isinstance(extracted_data, list):

        return extracted_data


    return [
        {
            "page_number": None,
            "text": extracted_data
        }
    ]



def create_text_chunks(
    normalized_pages: list[dict]
) -> list[dict]:

    chunks = []


    for page in normalized_pages:

        text_chunks = split_text_into_chunks(
            page["text"]
        )


        for chunk in text_chunks:

            chunks.append(
                {
                    "text": chunk,
                    "page_number": page["page_number"]
                }
            )


    return chunks



def save_chunks_to_database(
    db: Session,
    chunks: list[dict],
    organization_id: int,
    knowledge_source_id: int
):

    saved_chunks = []


    for chunk in chunks:

        knowledge_chunk = KnowledgeChunk(
            organization_id=organization_id,
            knowledge_source_id=knowledge_source_id,
            text=chunk["text"],
            page_number=chunk["page_number"],
            metadata_json={}
        )

        db.add(
            knowledge_chunk
        )

        saved_chunks.append(
            knowledge_chunk
        )


    db.commit()


    for chunk in saved_chunks:

        db.refresh(chunk)


    return saved_chunks


def process_knowledge_source(
    db: Session,
    knowledge_source
):

    extracted_data = extract_document_text(
        knowledge_source.file_path
    )


    normalized_data = normalize_extracted_text(
        extracted_data
    )


    chunks = create_text_chunks(
        normalized_data
    )


    saved_chunks = save_chunks_to_database(
        db=db,
        chunks=chunks,
        organization_id=knowledge_source.organization_id,
        knowledge_source_id=knowledge_source.id
    )


    return saved_chunks