from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    DateTime,
    ForeignKey,
    Integer,
    Boolean
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.connection import Base


if TYPE_CHECKING:
    from app.models.organization import Organization


class FAQ(Base):

    __tablename__ = "faqs"


    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )


    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.id"),
        nullable=False,
        index=True
    )


    question: Mapped[str] = mapped_column(
        String,
        nullable=False
    )


    answer: Mapped[str] = mapped_column(
        String,
        nullable=False
    )


    category: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )


    priority: Mapped[int] = mapped_column(
        Integer,
        default=0
    )


    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
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
        back_populates="faqs"
    )