def normalize_agent_response(
    agent_result: dict
) -> dict:


    decision = agent_result.get(
        "decision"
    )

    result = agent_result.get(
        "result",
        []
    )


    response = {
        "product_results": [],
        "knowledge_results": [],
        "followup_intent": "general"
    }


    if not decision:
        return response


    if decision.tool == "product_search":

        response["product_results"] = result


    elif decision.tool == "knowledge_search":

        response["knowledge_results"] = result


    return response