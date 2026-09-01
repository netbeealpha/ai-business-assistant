from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):

    sku: str | None = None

    name: str

    brand: str | None = None

    category: str | None = None

    description: str | None = None

    regular_price: float | None = None

    sale_price: float | None = None

    currency: str = "BDT"

    stock_status: str = "unknown"

    stock_quantity: int | None = None

    attributes_json: dict | None = None



class ProductCreate(ProductBase):
    pass



class ProductUpdate(BaseModel):

    sku: str | None = None

    name: str | None = None

    brand: str | None = None

    category: str | None = None

    description: str | None = None

    regular_price: float | None = None

    sale_price: float | None = None

    currency: str | None = None

    stock_status: str | None = None

    stock_quantity: int | None = None

    attributes_json: dict | None = None



class ProductResponse(ProductBase):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    organization_id: int

    created_at: datetime

    updated_at: datetime