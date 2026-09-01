from datetime import datetime

from pydantic import BaseModel, ConfigDict



class KnowledgeSourceBase(BaseModel):

    source_type: str

    title: str

    file_name: str

    file_path: str

    status: str = "uploaded"

    checksum: str | None = None

    version: int = 1



class KnowledgeSourceCreate(KnowledgeSourceBase):
    pass



class KnowledgeSourceUpdate(BaseModel):

    status: str | None = None

    checksum: str | None = None

    version: int | None = None



class KnowledgeSourceResponse(KnowledgeSourceBase):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    organization_id: int

    created_at: datetime

    updated_at: datetime