from groq import Groq

from app.core.config import settings

from app.services.llm.llm_service import LLMService



class GroqLLMService(LLMService):


    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )


    def generate(
        self,
        prompt: str,
        **kwargs
    ) -> str:


        response = self.client.chat.completions.create(
            model="qwen/qwen3.8-27b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )


        return (
            response
            .choices[0]
            .message
            .content
        )