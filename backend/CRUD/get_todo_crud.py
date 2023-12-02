from sqlalchemy.orm import Session
from SCHEMA.schema import TodoUpdateSchema
from DB.models import Todo


def get_todos(db: Session):
    # Get all todo items from database and return them as a list of TodoUpdateSchema objects
    todos = db.query(Todo).order_by(Todo.deadline.asc()).all()
    return [TodoUpdateSchema(**todo.__dict__) for todo in todos]
