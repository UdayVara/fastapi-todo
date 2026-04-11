from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.todo.dto.postDtos import CreateTodoDTO, UpdateTodoDTO
from src.utils.db import get_db
from src.Guards.authGuard import get_current_user

from src.todo.controller import (
    create_todo_service,
    get_todos_service,
    get_todo_service,
    update_todo_service,
    delete_todo_service
)

router = APIRouter(
    prefix="/todos",
    tags=["todo"],
)


@router.post("/")
def create_todo(
    body: CreateTodoDTO,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_todo_service(body, db, current_user)


@router.get("/")
def get_todos(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_todos_service(db, current_user)


@router.get("/{todo_id}")
def get_todo(
    todo_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_todo_service(todo_id, db, current_user)


@router.put("/{todo_id}")
def update_todo(
    todo_id: str,
    body: UpdateTodoDTO,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return update_todo_service(todo_id, body, db, current_user)


@router.delete("/{todo_id}")
def delete_todo(
    todo_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return delete_todo_service(todo_id, db, current_user)