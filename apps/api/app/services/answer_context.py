def build_answer_context(
    result: dict
) -> str:


    parts = []


    if result.get("product_results"):

        parts.append(
            str(
                result["product_results"]
            )
        )


    if result.get("knowledge_results"):

        for item in result["knowledge_results"]:

            parts.append(
                item["text"]
            )


    return "\n\n".join(parts)