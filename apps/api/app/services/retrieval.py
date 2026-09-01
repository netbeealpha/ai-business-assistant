from sqlalchemy.orm import Session

from app.services.vector_search import search_similar_chunks



def retrieve_relevant_chunks(
    db: Session,
    query: str,
    organization_id: int,
    top_k: int = 5
):

    chunks = search_similar_chunks(
        db=db,
        query_text=query,
        organization_id=organization_id,
        limit=top_k
    )


    results = []


    for chunk in chunks:

        results.append(
            {
                "chunk_id": chunk.id,
                "source_id": chunk.knowledge_source_id,
                "text": chunk.text,
                "page_number": chunk.page_number
            }
        )


    return results