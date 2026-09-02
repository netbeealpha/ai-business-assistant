from typing import Any



class LLMService:


    def generate(
        self,
        prompt: str,
        **kwargs: Any
    ) -> str:

        raise NotImplementedError(
            "LLM provider must implement generate()"
        )