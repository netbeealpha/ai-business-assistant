from app.services.llm.llm_service import LLMService



class MockLLMService(LLMService):


    def generate(
        self,
        prompt: str,
        **kwargs
    ) -> str:

        return "mock llm response"