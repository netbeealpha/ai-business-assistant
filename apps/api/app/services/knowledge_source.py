from sqlalchemy.orm import Session

from app.models.knowledge_source import KnowledgeSource

from app.schemas.knowledge_source import (
    KnowledgeSourceCreate,
    KnowledgeSourceUpdate
)



def create_knowledge_source(
    db: Session,
    source_data: KnowledgeSourceCreate,
    organization_id: int
):

    source = KnowledgeSource(
        organization_id=organization_id,
        **source_data.model_dump()
    )

    db.add(source)

    db.commit()

    db.refresh(source)

    return source



def get_knowledge_sources(
    db: Session,
    organization_id: int
):

    return (
        db.query(KnowledgeSource)
        .filter(
            KnowledgeSource.organization_id == organization_id
        )
        .all()
    )



def get_knowledge_source(
    db: Session,
    source_id: int,
    organization_id: int
):

    return (
        db.query(KnowledgeSource)
        .filter(
            KnowledgeSource.id == source_id,
            KnowledgeSource.organization_id == organization_id
        )
        .first()
    )



def update_knowledge_source(
    db: Session,
    source: KnowledgeSource,
    source_data: KnowledgeSourceUpdate
):

    update_data = source_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(source, key, value)

    db.commit()

    db.refresh(source)

    return source



def delete_knowledge_source(
    db: Session,
    source: KnowledgeSource
):

    db.delete(source)

    db.commit()

    return True