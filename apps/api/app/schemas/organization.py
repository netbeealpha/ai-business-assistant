from pydantic import BaseModel, EmailStr


class OrganizationRegister(BaseModel):

    business_name: str

    business_type: str | None = None

    owner_name: str

    email: EmailStr

    password: str