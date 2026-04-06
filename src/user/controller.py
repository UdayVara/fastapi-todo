from sqlalchemy.orm import Session
from src.user.model import UserModel
from src.user.dto.signupdto import SignupBody


def signup(signup_data: SignupBody,db:Session):
    try:
        return {"message": "success"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
