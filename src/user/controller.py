from tabnanny import check

import jwt
from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from src.user.model import UserModel
from src.user.dto.signupdto import SignupBody
from src.utils.config import Settings


def signup(signup_data: SignupBody,db:Session):
    try:
        check_user = db.query(UserModel).filter((UserModel.name == signup_data.name) | (UserModel.email == signup_data.email)).first()
        if check_user:
            return {"error": "User with this name or email already exists"}

        password_hash = PasswordHash.recommended()

        hashed_Password = password_hash.hash(signup_data.password)
        new_user = UserModel(
            name=signup_data.name,
            email=signup_data.email,
            password=hashed_Password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        token = jwt.encode({"user_id": str(new_user.id)}, Settings.SECRET_KEY, algorithm=Settings.ALGORITHM)
        return {"message": "User created successfully", "user_id": str(new_user.id)}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
