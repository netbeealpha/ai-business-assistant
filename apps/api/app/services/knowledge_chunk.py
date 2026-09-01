from sqlalchemy.orm import Session

from app.models.knowledge_chunk import KnowledgeChunk

from app.schemas.knowledge_chunk import (
    KnowledgeChunkCreate,
    KnowledgeChunkUpdate
)



def create_chunk(
    db: Session,
    chunk_data: KnowledgeChunkCreate,
    organization_id: int,
    knowledge_source_id: int
):

    chunk = KnowledgeChunk(
        organization_id=organization_id,
        knowledge_source_id=knowledge_source_id,
        **chunk_data.model_dump()
    )

    db.add(chunk)

    db.commit()

    db.refresh(chunk)

    return chunk



def get_chunks(
    db: Session,
    organization_id: int,
    knowledge_source_id: int | None = None
):

    query = (
        db.query(KnowledgeChunk)
        .filter(
            KnowledgeChunk.organization_id == organization_id
        )
    )

    if knowledge_source_id:

        query = query.filter(
            KnowledgeChunk.knowledge_source_id == knowledge_source_id
        )

    return query.all()



def get_chunk(
    db: Session,
    chunk_id: int,
    organization_id: int
):

    return (
        db.query(KnowledgeChunk)
        .filter(
            KnowledgeChunk.id == chunk_id,
            KnowledgeChunk.organization_id == organization_id
        )
        .first()
    )



def update_chunk(
    db: Session,
    chunk: KnowledgeChunk,
    chunk_data: KnowledgeChunkUpdate
):

    update_data = chunk_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():

        setattr(
            chunk,
            key,
            value
        )

    db.commit()

    db.refresh(chunk)

    return chunk



def delete_chunk(
    db: Session,
    chunk: KnowledgeChunk
):

    db.delete(chunk)

    db.commit()

    return True