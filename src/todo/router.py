from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.todo.dto.postDtos import CreateTodoDTO, UpdateTodoDTO
from src.utils.db import get_db
from src.todo.model import Todo

from src.Guards.authGuard import get_current_user

router = APIRouter(
    prefix="/todos",
    tags=["todo"],
)

@router.post("/")
def create_todo(
    body:CreateTodoDTO,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    todo = Todo(
        title=body.title,
        description=body.description,
        user_id=current_user
    )

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo



@router.get("/")
def get_todos(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    todos = db.query(Todo).filter(
        Todo.user_id == current_user
    ).all()

    return todos



@router.get("/{todo_id}")
def get_todo(
    todo_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    todo = db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == current_user
    ).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo


@router.put("/{todo_id}")
def update_todo(
    todo_id: str,
    body: UpdateTodoDTO,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    todo = db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == current_user
    ).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    if body.title is not None:
        todo.title = body.title

    if body.description is not None:
        todo.description = body.description

    db.commit()
    db.refresh(todo)

    return todo

@router.delete("/{todo_id}")
def delete_todo(
    todo_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    todo = db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == current_user
    ).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo)
    db.commit()

    return {"message": "Todo deleted"}

