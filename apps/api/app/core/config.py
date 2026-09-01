from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str

    JWT_SECRET_KEY: str

    JWT_ALGORITHM: str = "HS256",
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    UPLOAD_DIR: str = "uploads"

    MAX_UPLOAD_SIZE_MB: int = 10

    ALLOWED_FILE_TYPES: list[str] = [
        "pdf",
        "docx",
        "txt",
        "csv",
        "xlsx"
    ]

    class Config:
        env_file = ".env"


settings = Settings()