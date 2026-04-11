import uuid
from sqlalchemy import UUID, Boolean, Column, String
from sqlalchemy.orm import relationship

from src.utils.db import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID,primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, default=True)

    todos = relationship("Todo", back_populates="user")