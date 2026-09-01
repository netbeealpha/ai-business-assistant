from datetime import datetime

from pydantic import BaseModel



class UploadResponse(BaseModel):

    message: str

    file_name: str

    source_id: int

    status: str



class UploadedFileInfo(BaseModel):

    file_name: str

    file_size: int

    content_type: str

    uploaded_at: datetime