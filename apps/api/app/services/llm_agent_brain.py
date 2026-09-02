import json

from app.services.llm.groq_provider import (
    GroqLLMService
)

from app.schemas.agent import AgentDecision



llm = GroqLLMService()



def decide_with_llm(
    query: str
) -> AgentDecision:


    prompt = f"""
    You are an AI business assistant.

    Your job is to decide which business tool should answer the user.

    Available tools:

    product_search:
    Use for:
    - products
    - price
    - cost
    - stock
    - availability
    - SKU

    knowledge_search:
    Use for:
    - company information
    - documents
    - policies
    - manuals
    - explanations


    Return ONLY valid JSON.

    Format:

    {{
        "intent": "",
        "entity": "",
        "tool": ""
    }}


    Examples:

    Question:
    "What is the price of Oud Royale?"

    Output:
    {{
        "intent": "price",
        "entity": "Oud Royale",
        "tool": "product_search"
    }}


    Question:
    "What is ElevenLabs?"

    Output:
    {{
        "intent": "knowledge",
        "entity": "ElevenLabs",
        "tool": "knowledge_search"
    }}


    User question:

    {query}
    """


    response = llm.generate(
        prompt
    )


    data = json.loads(
        response
    )


    return AgentDecision(
        intent=data["intent"],
        entity=data.get("entity"),
        tool=data.get("tool")
    )