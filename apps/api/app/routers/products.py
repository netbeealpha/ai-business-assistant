from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.product import ProductCreate, ProductResponse
from app.services.product import (create_product, get_products, get_product)
from app.dependencies.auth import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post(
    "",
    response_model=ProductResponse
)
def create_new_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_product(
        db=db,
        product_data=product,
        organization_id=current_user.organization_id
    )


@router.get(
    "",
    response_model=list[ProductResponse]
)
def read_products(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_products(
        db=db,
        organization_id=current_user.organization_id
    )


@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def read_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    product = get_product(
        db=db,
        product_id=product_id,
        organization_id=current_user.organization_id
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product