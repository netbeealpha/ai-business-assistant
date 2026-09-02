from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.connection import Base



class Conversation(Base):

    __tablename__ = "conversations"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )


    organization_id: Mapped[int] = mapped_column(
        ForeignKey(
            "organizations.id"
        ),
        nullable=False
    )


    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id"
        ),
        nullable=False
    )


    title: Mapped[str | None] = mapped_column(
        String,
        nullable=True
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


    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete"
    )