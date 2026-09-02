from app.schemas.query import QueryIntent



def classify_query(
    query: str
) -> QueryIntent:


    query_lower = query.lower()


    product_keywords = [
        "price",
        "cost",
        "sku",
        "stock",
        "available",
        "quantity",
        "buy",
        "product"
    ]


    knowledge_keywords = [
        "who is",
        "how to",
        "policy",
        "manual",
        "guide",
        "company",
        "information",
        "explain"
    ]


    is_product = any(
        keyword in query_lower
        for keyword in product_keywords
    )


    is_knowledge = any(
        keyword in query_lower
        for keyword in knowledge_keywords
    )


    # Handle general "what is" knowledge questions
    if (
        "what is" in query_lower
        and not is_product
    ):
        is_knowledge = True


    # Product queries have priority
    if is_product:
        is_knowledge = False

    return QueryIntent(
        is_product=is_product,
        is_knowledge=is_knowledge
    )