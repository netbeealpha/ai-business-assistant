from sqlalchemy.orm import Session

from app.models.knowledge_chunk import KnowledgeChunk

from app.services.embedding import generate_embedding



def search_similar_chunks(
    db: Session,
    query_text: str,
    organization_id: int,
    limit: int = 5
):

    query_embedding = generate_embedding(
        query_text
    )


    results = (
        db.query(KnowledgeChunk)
        .filter(
            KnowledgeChunk.organization_id == organization_id
        )
        .order_by(
            KnowledgeChunk.embedding.cosine_distance(
                query_embedding
            )
        )
        .limit(limit)
        .all()
    )


    return results