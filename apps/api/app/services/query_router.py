def classify_query(
    query: str
) -> str:

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


    for keyword in product_keywords:

        if keyword in query_lower:

            return "product"


    return "knowledge"