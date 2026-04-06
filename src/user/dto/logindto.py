from pydantic import BaseModel, Field


class loginDTO(BaseModel):
    email: str
    password: str = Field(..., min_length=8,max_length=16)