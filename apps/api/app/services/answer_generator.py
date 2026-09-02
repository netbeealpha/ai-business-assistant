from app.services.llm.groq_provider import GroqLLMService



llm = GroqLLMService()



def generate_answer(
    question: str,
    context: str
) -> str:


    prompt = f"""
You are an AI business assistant.

Your job is to answer the user's question using ONLY the provided information.

Rules:

1. Use only the given information.
2. Do not make assumptions.
3. Do not invent facts.
4. Do not mention internal chunk IDs or database IDs.
5. If source information is provided, include a short source reference at the end.
6. Keep the answer clear, concise, and professional.


User question:

{question}


Available information:

{context}


Generate the final business answer.

If sources are available, format them like:

Sources:
- Document name (Page number)

"""
    

    return llm.generate(
        prompt
    )