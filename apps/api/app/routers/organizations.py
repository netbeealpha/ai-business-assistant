from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.database.session import get_db
from app.models.organization import Organization
from app.models.user import User
from app.schemas.organization import OrganizationRegister
from app.services.auth import hash_password


router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"]
)


@router.post("/register")
def register_organization(
    data: OrganizationRegister,
    db: Session = Depends(get_db)
):

    organization = Organization(
        name=data.business_name,
        business_type=data.business_type
    )

    db.add(organization)

    db.commit()

    db.refresh(organization)


    user = User(
        organization_id=organization.id,
        email=data.email,
        full_name=data.owner_name,
        hashed_password=hash_password(data.password),
        role="owner"
    )


    db.add(user)

    db.commit()


    return {
        "message": "Organization created successfully",
        "organization_id": organization.id,
        "user_id": user.id
    }