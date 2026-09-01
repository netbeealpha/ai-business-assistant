
from datetime import datetime

from sqlalchemy import (
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
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.organization import Organization

class User(Base):

    __tablename__ = "users"


    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )


    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.id"),
        nullable=False
    )


    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )


    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )


    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )


    role: Mapped[str] = mapped_column(
        String(50),
        default="staff"
    )


    status: Mapped[str] = mapped_column(
        String(50),
        default="active"
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
    
    organization: Mapped["Organization"] = relationship(
        back_populates="users"
    )