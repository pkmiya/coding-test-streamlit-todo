from sqlalchemy.orm import Session
from SCHEMA.schema import TodoUpdateSchema
from DB.models import Todo


def get_todo_crud(db: Session):
    todos = db.query(Todo).order_by(Todo.deadline.asc()).all()
    return [TodoUpdateSchema(**todo.__dict__) for todo in todos]
