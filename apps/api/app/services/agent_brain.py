from app.schemas.agent import AgentDecision
from app.services.entity_extractor import extract_product_entity


def decide(
    query: str
) -> AgentDecision:


    query_lower = query.lower()


    if any(
        word in query_lower
        for word in [
            "price",
            "cost",
            "stock",
            "available",
            "buy"
        ]
    ):

        return AgentDecision(
            intent="product",
            entity=extract_product_entity(query),
            tool="product_search"
        )


    return AgentDecision(
        intent="knowledge",
        entity=query,
        tool="knowledge_search"
    )