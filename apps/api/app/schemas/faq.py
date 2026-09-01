from datetime import datetime

from pydantic import BaseModel, ConfigDict



class FAQBase(BaseModel):

    question: str

    answer: str

    category: str | None = None

    priority: int = 0

    is_active: bool = True



class FAQCreate(FAQBase):
    pass



class FAQUpdate(BaseModel):

    question: str | None = None

    answer: str | None = None

    category: str | None = None

    priority: int | None = None

    is_active: bool | None = None



class FAQResponse(FAQBase):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    organization_id: int

    created_at: datetime

    updated_at: datetime