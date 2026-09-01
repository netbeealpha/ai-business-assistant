from sqlalchemy.orm import Session

from app.models.faq import FAQ
from app.schemas.faq import (
    FAQCreate,
    FAQUpdate
)


def create_faq(
    db: Session,
    faq_data: FAQCreate,
    organization_id: int
):

    faq = FAQ(
        organization_id=organization_id,
        **faq_data.model_dump()
    )

    db.add(faq)

    db.commit()

    db.refresh(faq)

    return faq



def get_faqs(
    db: Session,
    organization_id: int
):

    return (
        db.query(FAQ)
        .filter(
            FAQ.organization_id == organization_id
        )
        .all()
    )



def get_faq(
    db: Session,
    faq_id: int,
    organization_id: int
):

    return (
        db.query(FAQ)
        .filter(
            FAQ.id == faq_id,
            FAQ.organization_id == organization_id
        )
        .first()
    )



def update_faq(
    db: Session,
    faq: FAQ,
    faq_data: FAQUpdate
):

    update_data = faq_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(faq, key, value)

    db.commit()

    db.refresh(faq)

    return faq



def delete_faq(
    db: Session,
    faq: FAQ
):

    db.delete(faq)

    db.commit()

    return True