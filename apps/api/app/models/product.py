from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    DateTime,
    ForeignKey,
    Float,
    Integer,
    JSON
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.connection import Base


if TYPE_CHECKING:
    from app.models.organization import Organization


class Product(Base):

    __tablename__ = "products"


    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )


    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.id"),
        nullable=False,
        index=True
    )


    sku: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )


    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )


    brand: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )


    category: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )


    description: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )


    regular_price: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )


    sale_price: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )


    currency: Mapped[str] = mapped_column(
        String(10),
        default="BDT"
    )


    stock_status: Mapped[str] = mapped_column(
        String(50),
        default="unknown"
    )


    stock_quantity: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )


    attributes_json: Mapped[dict | None] = mapped_column(
        JSON,
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


    organization: Mapped["Organization"] = relationship(
        back_populates="products"
    )