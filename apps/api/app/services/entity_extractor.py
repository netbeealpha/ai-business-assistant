import re



def extract_product_entity(
    query: str
) -> str:

    query_lower = query.lower()


    remove_patterns = [
        "what is the price of",
        "what's the price of",
        "price of",
        "how much is",
        "cost of",
        "tell me about",
        "show me"
    ]


    cleaned_query = query_lower


    for pattern in remove_patterns:

        cleaned_query = cleaned_query.replace(
            pattern,
            ""
        )


    return cleaned_query.strip().rstrip("?!.,").title()