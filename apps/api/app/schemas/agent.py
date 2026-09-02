from pydantic import BaseModel



class AgentDecision(BaseModel):

    intent: str

    entity: str | None = None

    tool: str | None = None