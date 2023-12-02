from sqlalchemy.orm import Session
from DB.models import Todo


def insert_todo_crud(db: Session, todo_data: Todo):
    try:
        todo = Todo(**todo_data.dict())
        db.add(todo)
        db.commit()
        db.refresh(todo)
        return todo
    except Exception as e:
        raise e
