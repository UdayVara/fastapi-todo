from tabnanny import check

from fastapi import HTTPException
import jwt
from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from src.user.dto.logindto import loginDTO
from src.user.model import UserModel
from src.user.dto.signupdto import SignupBody
from src.utils.config import Settings


def signup(signup_data: SignupBody,db:Session):
    try:
        check_user = db.query(UserModel).filter((UserModel.name == signup_data.name) | (UserModel.email == signup_data.email)).first()
        if check_user:
            raise HTTPException(status_code=400, detail="User with this name or email already exists")

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
        return {"message": "User created successfully", "token": token}
    except Exception as e:
        return HTTPException(status_code=e.status_code if isinstance(e, HTTPException) else 500, detail=str(e))
    

def login(loginBody:loginDTO,db:Session):
    try:
        user = db.query(UserModel).filter(UserModel.email == loginBody.email).first()
        if not user:
            raise HTTPException(status_code=400, detail="Invalid email or password")
        
        password_hash = PasswordHash.recommended()
        if not password_hash.verify(loginBody.password, user.password):
            raise HTTPException(status_code=400, detail="Invalid email or password")
        
        token = jwt.encode({"user_id": str(user.id)}, Settings.SECRET_KEY, algorithm=Settings.ALGORITHM)
        return {"message": "Login successful", "token": token}
    except Exception as e:
        raise HTTPException(status_code=e.status_code if isinstance(e, HTTPException) else 500, detail=str(e))
