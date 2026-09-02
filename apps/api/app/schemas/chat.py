from pydantic import BaseModel

from app.schemas.citation import Citation



class ChatRequest(BaseModel):

    conversation_id: int | None = None

    message: str



class ChatResponse(BaseModel):

    conversation_id: int

    answer: str

    sources: list[Citation] = []