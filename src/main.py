from fastapi import FastAPI

from src.utils.db import Base,engine
from src.models.model import *


app = FastAPI()

Base.metadata.create_all(bind=engine)

from src.user.router import user_router

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(router=user_router)