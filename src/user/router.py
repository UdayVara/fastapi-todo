from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.user.controller import login, signup
from src.user.dto.logindto import loginDTO
from src.user.dto.signupdto import SignupBody
from src.utils.db import get_db


user_router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@user_router.post("/signup",status_code=201)
def signupRoute(body: SignupBody,db:Session = Depends(get_db)):
    return signup(body,db)

@user_router.post("/login")
def loginRoute(body: loginDTO,db:Session = Depends(get_db)):
    return login(body,db)