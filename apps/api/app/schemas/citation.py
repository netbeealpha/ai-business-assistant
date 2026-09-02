from pydantic import BaseModel



class Citation(BaseModel):

    source_id: int | None = None

    document: str | None = None

    title: str | None = None

    page_number: int | None = None