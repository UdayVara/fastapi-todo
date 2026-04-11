from uuid import uuid4

from sqlalchemy import UUID, Column, ForeignKey, String, desc
from sqlalchemy.orm import relationship

from src.utils.db import Base


class Todo(Base):
    __tablename__ = "todo"

    id = Column(UUID,primary_key=True, default=uuid4, index=True)
    user_id = Column(UUID, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    
    user = relationship("UserModel", back_populates="todos")