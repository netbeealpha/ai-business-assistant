from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import (ProductCreate, ProductUpdate)




def create_product(
    db: Session,
    product_data: ProductCreate,
    organization_id: int
):

    product = Product(
        organization_id=organization_id,
        **product_data.model_dump()
    )

    db.add(product)

    db.commit()

    db.refresh(product)

    return product


def get_products(
    db: Session,
    organization_id: int
):

    return (
        db.query(Product)
        .filter(
            Product.organization_id == organization_id
        )
        .all()
    )

def get_product(
    db: Session,
    product_id: int,
    organization_id: int
):

   return (
        db.query(Product)
        .filter(
            Product.id == product_id,
            Product.organization_id == organization_id
        )
        .first()
    )


def update_product(
    db:Session,
    product:Product,
    product_data: ProductUpdate

):
    update_data = product_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(product, key, value)

    db.commit()

    db.refresh(product)

    return product

def delete_product(
    db: Session,
    product: Product
):

    db.delete(product)

    db.commit()

    return True