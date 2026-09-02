def detect_followup_intent(
    query: str
) -> str:


    query_lower = query.lower()


    if any(
        word in query_lower
        for word in [
            "available",
            "stock",
            "in stock",
            "have"
        ]
    ):

        return "availability"


    if any(
        word in query_lower
        for word in [
            "price",
            "cost",
            "how much"
        ]
    ):

        return "price"


    if any(
        word in query_lower
        for word in [
            "details",
            "information",
            "tell me about"
        ]
    ):

        return "details"


    return "general"