from sqlalchemy.orm import Session

from app.services.query_router import classify_query

from app.services.product_tool import search_products

from app.services.retrieval import retrieve_relevant_chunks

from app.services.entity_extractor import (
    extract_product_entity
)



def execute_query(
    db: Session,
    query: str,
    organization_id: int
):

    intent = classify_query(
        query
    )


    response = {
        "product_results": [],
        "knowledge_results": []
    }


    if intent.is_product:

        product_query = extract_product_entity(
            query
        )


        response["product_results"] = search_products(
            db=db,
            query=product_query,
            organization_id=organization_id
        )


    if intent.is_knowledge:

        response["knowledge_results"] = retrieve_relevant_chunks(
            db=db,
            query=query,
            organization_id=organization_id
        )


    return response