from app.services.llm.groq_provider import GroqLLMService



llm = GroqLLMService()



def generate_answer(
    question: str,
    context: str
) -> str:


    prompt = f"""
You are an AI business assistant.

Answer the user's question using ONLY the provided information.

Be:
- accurate
- concise
- professional

Do not mention chunks or internal data.

User question:

{question}


Available information:

{context}


Generate the final answer.
"""


    return llm.generate(
        prompt
    )