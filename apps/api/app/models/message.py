from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    DateTime,
    ForeignKey,
    Text
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.connection import Base



class Message(Base):

    __tablename__ = "messages"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )


    conversation_id: Mapped[int] = mapped_column(
        ForeignKey(
            "conversations.id"
        ),
        nullable=False
    )


    role: Mapped[str] = mapped_column(
        String,
        nullable=False
    )


    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )