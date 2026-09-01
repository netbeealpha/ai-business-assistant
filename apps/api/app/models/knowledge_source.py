from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    DateTime,
    ForeignKey,
    Integer
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.connection import Base


if TYPE_CHECKING:
    from app.models.organization import Organization
    from app.models.knowledge_chunk import KnowledgeChunk


class KnowledgeSource(Base):

    __tablename__ = "knowledge_sources"


    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )


    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.id"),
        nullable=False,
        index=True
    )


    source_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )


    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )


    file_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )


    file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )


    status: Mapped[str] = mapped_column(
        String(50),
        default="uploaded"
    )


    checksum: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )


    version: Mapped[int] = mapped_column(
        Integer,
        default=1
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


    organization: Mapped["Organization"] = relationship(
        back_populates="knowledge_sources"
    )
    chunks: Mapped[list["KnowledgeChunk"]] = relationship(
        back_populates="knowledge_source"
    )