from sqlalchemy.orm import Session
from DB.models import Todo


def update_todo_crud(db: Session, id: int, todo_data: Todo):
    try:
        todo_to_update = db.query(Todo).filter(Todo.id == id).first()
        if todo_to_update:
            for key, value in todo_data.dict().items():
                setattr(todo_to_update, key, value)
            db.commit()
            db.refresh(todo_to_update)
            return todo_to_update
        else:
            return None
    except Exception as e:
        raise e
