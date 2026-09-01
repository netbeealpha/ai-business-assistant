from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.knowledge_source import (
    KnowledgeSourceCreate,
    KnowledgeSourceUpdate,
    KnowledgeSourceResponse
)

from app.services.knowledge_source import (
    create_knowledge_source,
    get_knowledge_sources,
    get_knowledge_source,
    update_knowledge_source,
    delete_knowledge_source
)

from app.dependencies.auth import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/knowledge-sources",
    tags=["Knowledge Sources"]
)


@router.post(
    "",
    response_model=KnowledgeSourceResponse
)
def create_new_source(
    source: KnowledgeSourceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_knowledge_source(
        db=db,
        source_data=source,
        organization_id=current_user.organization_id
    )



@router.get(
    "",
    response_model=list[KnowledgeSourceResponse]
)
def read_sources(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_knowledge_sources(
        db=db,
        organization_id=current_user.organization_id
    )



@router.get(
    "/{source_id}",
    response_model=KnowledgeSourceResponse
)
def read_source(
    source_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    source = get_knowledge_source(
        db=db,
        source_id=source_id,
        organization_id=current_user.organization_id
    )

    if source is None:
        raise HTTPException(
            status_code=404,
            detail="Knowledge source not found"
        )

    return source



@router.put(
    "/{source_id}",
    response_model=KnowledgeSourceResponse
)
def update_existing_source(
    source_id: int,
    source_data: KnowledgeSourceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    source = get_knowledge_source(
        db=db,
        source_id=source_id,
        organization_id=current_user.organization_id
    )

    if source is None:
        raise HTTPException(
            status_code=404,
            detail="Knowledge source not found"
        )

    return update_knowledge_source(
        db=db,
        source=source,
        source_data=source_data
    )



@router.delete(
    "/{source_id}"
)
def delete_existing_source(
    source_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    source = get_knowledge_source(
        db=db,
        source_id=source_id,
        organization_id=current_user.organization_id
    )

    if source is None:
        raise HTTPException(
            status_code=404,
            detail="Knowledge source not found"
        )

    delete_knowledge_source(
        db=db,
        source=source
    )

    return {
        "message": "Knowledge source deleted successfully"
    }