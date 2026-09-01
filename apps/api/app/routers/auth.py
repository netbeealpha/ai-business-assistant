from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.schemas.auth import LoginRequest
from app.services.auth import verify_password
from app.services.jwt import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.email == data.email)
        .first()
    )


    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )


    password_valid = verify_password(
        data.password,
        user.hashed_password
    )


    if not password_valid:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )


    token = create_access_token(
        {
            "user_id": user.id,
            "organization_id": user.organization_id,
            "role": user.role
        }
    )


    return {
        "access_token": token,
        "token_type": "bearer"
    }