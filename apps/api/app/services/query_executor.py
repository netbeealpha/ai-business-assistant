from sqlalchemy.orm import Session

from app.services.query_router import classify_query

from app.services.product_tool import search_products

from app.services.retrieval import retrieve_relevant_chunks



def execute_query(
    db: Session,
    query: str,
    organization_id: int
):

    query_type = classify_query(
        query
    )


    if query_type == "product":

        return {
            "type": "product",
            "results": search_products(
                db=db,
                query=query,
                organization_id=organization_id
            )
        }


    else:

        return {
            "type": "knowledge",
            "results": retrieve_relevant_chunks(
                db=db,
                query=query,
                organization_id=organization_id
            )
        }