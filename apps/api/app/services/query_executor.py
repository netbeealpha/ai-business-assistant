from sqlalchemy.orm import Session

from app.services.query_router import classify_query
from app.services.product_tool import search_products
from app.services.retrieval import retrieve_relevant_chunks
from app.services.entity_extractor import extract_product_entity



def execute_query(
    db: Session,
    query: str,
    organization_id: int,
    followup_intent: str = "general"
):

    intent = classify_query(
        query
    )

    print(
        "EXECUTOR FOLLOWUP INTENT:",
        followup_intent
    )
    response = {
        "product_results": [],
        "knowledge_results": [],
        "followup_intent": followup_intent
    }


    if (
        not intent.is_product
        and not intent.is_knowledge
        and len(query.split()) <= 3
    ):
        intent.is_product = True


    if intent.is_product:

        print("PRODUCT INTENT DETECTED")


        product_query = extract_product_entity(
            query
        )


        print(
            "EXTRACTED PRODUCT:",
            product_query
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