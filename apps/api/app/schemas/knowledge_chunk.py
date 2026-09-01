from datetime import datetime

from pydantic import BaseModel, ConfigDict



class KnowledgeChunkBase(BaseModel):

    text: str

    embedding: list | None = None

    metadata_json: dict | None = None

    page_number: int | None = None

    is_active: bool = True



class KnowledgeChunkCreate(KnowledgeChunkBase):
    pass



class KnowledgeChunkUpdate(BaseModel):

    text: str | None = None

    embedding: list | None = None

    metadata_json: dict | None = None

    page_number: int | None = None

    is_active: bool | None = None



class KnowledgeChunkResponse(KnowledgeChunkBase):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    organization_id: int

    knowledge_source_id: int

    created_at: datetime