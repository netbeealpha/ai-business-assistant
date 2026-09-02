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

    print("1. executor started")


    query_type = classify_query(
        query
    )

    print("2. query type:", query_type)


    if query_type == "product":

        print("3. extracting product entity")


        product_query = extract_product_entity(
            query
        )

        print("4. extracted:", product_query)


        print("5. searching product")


        results = search_products(
            db=db,
            query=product_query,
            organization_id=organization_id
        )


        print("6. product search completed")


        return {
            "type": "product",
            "results": results
        }


    else:

        print("knowledge path")

        return {
            "type": "knowledge",
            "results": retrieve_relevant_chunks(
                db=db,
                query=query,
                organization_id=organization_id
            )
        }