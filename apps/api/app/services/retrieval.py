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

        source = chunk.knowledge_source


        results.append(
            {
                "text": chunk.text,

                "citation": {
                    "source_id": source.id,
                    "title": source.title,
                    "document": source.file_name,
                    "page_number": chunk.page_number,
                    "version": source.version
                }
            }
        )


    return results