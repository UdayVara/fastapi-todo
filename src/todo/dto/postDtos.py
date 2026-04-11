from pydantic import BaseModel, Field
from typing import Optional


class CreateTodoDTO(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None


class UpdateTodoDTO(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None

