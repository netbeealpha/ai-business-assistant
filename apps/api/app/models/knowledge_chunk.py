from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    DateTime,
    ForeignKey,
    Integer,
    Boolean,
    JSON,
    Text
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.connection import Base


if TYPE_CHECKING:
    from app.models.organization import Organization
    from app.models.knowledge_source import KnowledgeSource


class KnowledgeChunk(Base):

    __tablename__ = "knowledge_chunks"


    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )


    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.id"),
        nullable=False,
        index=True
    )


    knowledge_source_id: Mapped[int] = mapped_column(
        ForeignKey("knowledge_sources.id"),
        nullable=False,
        index=True
    )


    text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )


    embedding: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True
    )


    metadata_json: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True
    )


    page_number: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )


    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


    organization: Mapped["Organization"] = relationship(
        back_populates="knowledge_chunks"
    )


    knowledge_source: Mapped["KnowledgeSource"] = relationship(
        back_populates="chunks"
    )