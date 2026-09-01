from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String, DateTime
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.connection import Base


if TYPE_CHECKING:
    from app.models.user import User
    from app.models.product import Product
    from app.models.faq import FAQ
    from app.models.knowledge_source import KnowledgeSource
    from app.models.knowledge_chunk import KnowledgeChunk


class Organization(Base):

    __tablename__ = "organizations"


    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )


    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )


    business_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )


    status: Mapped[str] = mapped_column(
        String(50),
        default="active"
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


    # Relationship with users
    users: Mapped[list["User"]] = relationship(
        back_populates="organization"
    )


    # Relationship with products
    products: Mapped[list["Product"]] = relationship(
        back_populates="organization"
    )

    faqs: Mapped[list["FAQ"]] = relationship(
        back_populates="organization"
    )

    knowledge_sources: Mapped[list["KnowledgeSource"]] = relationship(
        back_populates="organization"
    )
    knowledge_chunks: Mapped[list["KnowledgeChunk"]] = relationship(
        back_populates="organization"
    )