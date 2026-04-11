from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.todo.model import Todo


def create_todo_service(body, db: Session, current_user):
    todo = Todo(
        title=body.title,
        description=body.description,
        user_id=current_user  # ✅ FIXED
    )

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo


def get_todos_service(db: Session, current_user):
    return db.query(Todo).filter(
        Todo.user_id == current_user  # ✅ FIXED
    ).all()


def get_todo_service(todo_id: str, db: Session, current_user):
    todo = db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == current_user
    ).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo


def update_todo_service(todo_id: str, body, db: Session, current_user):
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


def delete_todo_service(todo_id: str, db: Session, current_user):
    todo = db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == current_user
    ).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo)
    db.commit()

    return {"message": "Todo deleted"}