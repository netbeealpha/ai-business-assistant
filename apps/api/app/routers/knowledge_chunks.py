from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.knowledge_chunk import (
    KnowledgeChunkCreate,
    KnowledgeChunkUpdate,
    KnowledgeChunkResponse
)

from app.services.knowledge_chunk import (
    create_chunk,
    get_chunks,
    get_chunk,
    update_chunk,
    delete_chunk
)

from app.dependencies.auth import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/knowledge-chunks",
    tags=["Knowledge Chunks"]
)


@router.post(
    "",
    response_model=KnowledgeChunkResponse
)
def create_new_chunk(
    chunk: KnowledgeChunkCreate,
    knowledge_source_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_chunk(
        db=db,
        chunk_data=chunk,
        organization_id=current_user.organization_id,
        knowledge_source_id=knowledge_source_id
    )



@router.get(
    "",
    response_model=list[KnowledgeChunkResponse]
)
def read_chunks(
    knowledge_source_id: int | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_chunks(
        db=db,
        organization_id=current_user.organization_id,
        knowledge_source_id=knowledge_source_id
    )



@router.get(
    "/{chunk_id}",
    response_model=KnowledgeChunkResponse
)
def read_chunk(
    chunk_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    chunk = get_chunk(
        db=db,
        chunk_id=chunk_id,
        organization_id=current_user.organization_id
    )

    if chunk is None:
        raise HTTPException(
            status_code=404,
            detail="Knowledge chunk not found"
        )

    return chunk



@router.put(
    "/{chunk_id}",
    response_model=KnowledgeChunkResponse
)
def update_existing_chunk(
    chunk_id: int,
    chunk_data: KnowledgeChunkUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    chunk = get_chunk(
        db=db,
        chunk_id=chunk_id,
        organization_id=current_user.organization_id
    )

    if chunk is None:
        raise HTTPException(
            status_code=404,
            detail="Knowledge chunk not found"
        )

    return update_chunk(
        db=db,
        chunk=chunk,
        chunk_data=chunk_data
    )



@router.delete(
    "/{chunk_id}"
)
def delete_existing_chunk(
    chunk_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    chunk = get_chunk(
        db=db,
        chunk_id=chunk_id,
        organization_id=current_user.organization_id
    )

    if chunk is None:
        raise HTTPException(
            status_code=404,
            detail="Knowledge chunk not found"
        )

    delete_chunk(
        db=db,
        chunk=chunk
    )

    return {
        "message": "Knowledge chunk deleted successfully"
    }