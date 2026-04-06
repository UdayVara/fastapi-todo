from pydantic import BaseModel, EmailStr, Field


class SignupBody(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=8,max_length=16)