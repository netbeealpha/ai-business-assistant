from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.faq import (
    FAQCreate,
    FAQUpdate,
    FAQResponse
)
from app.services.faq import (
    create_faq,
    get_faqs,
    get_faq,
    update_faq,
    delete_faq
)
from app.dependencies.auth import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/faqs",
    tags=["FAQs"]
)


@router.post(
    "",
    response_model=FAQResponse
)
def create_new_faq(
    faq: FAQCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_faq(
        db=db,
        faq_data=faq,
        organization_id=current_user.organization_id
    )



@router.get(
    "",
    response_model=list[FAQResponse]
)
def read_faqs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_faqs(
        db=db,
        organization_id=current_user.organization_id
    )



@router.get(
    "/{faq_id}",
    response_model=FAQResponse
)
def read_faq(
    faq_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    faq = get_faq(
        db=db,
        faq_id=faq_id,
        organization_id=current_user.organization_id
    )

    if faq is None:
        raise HTTPException(
            status_code=404,
            detail="FAQ not found"
        )

    return faq



@router.put(
    "/{faq_id}",
    response_model=FAQResponse
)
def update_existing_faq(
    faq_id: int,
    faq_data: FAQUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    faq = get_faq(
        db=db,
        faq_id=faq_id,
        organization_id=current_user.organization_id
    )

    if faq is None:
        raise HTTPException(
            status_code=404,
            detail="FAQ not found"
        )

    return update_faq(
        db=db,
        faq=faq,
        faq_data=faq_data
    )



@router.delete(
    "/{faq_id}"
)
def delete_existing_faq(
    faq_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    faq = get_faq(
        db=db,
        faq_id=faq_id,
        organization_id=current_user.organization_id
    )

    if faq is None:
        raise HTTPException(
            status_code=404,
            detail="FAQ not found"
        )

    delete_faq(
        db=db,
        faq=faq
    )

    return {
        "message": "FAQ deleted successfully"
    }