from sqlalchemy.orm import Session

from app.models.product import Product



def search_products(
    db: Session,
    query: str,
    organization_id: int,
    limit: int = 5
):

    search_term = f"%{query}%"


    products = (
        db.query(Product)
        .filter(
            Product.organization_id == organization_id,
            (
                Product.name.ilike(search_term)
                |
                Product.sku.ilike(search_term)
                |
                Product.brand.ilike(search_term)
                |
                Product.category.ilike(search_term)
            )
        )
        .limit(limit)
        .all()
    )


    results = []


    for product in products:

        results.append(
            {
                "id": product.id,
                "sku": product.sku,
                "name": product.name,
                "brand": product.brand,
                "category": product.category,
                "regular_price": product.regular_price,
                "sale_price": product.sale_price,
                "currency": product.currency,
                "stock_status": product.stock_status,
                "stock_quantity": product.stock_quantity
            }
        )


    return results