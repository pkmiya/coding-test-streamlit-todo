from sqlalchemy.orm import Session
from DB.models import Todo


def delete_todo_crud(db: Session, todo_id: int):
    todo_item = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo_item:
        db.delete(todo_item)
        db.commit()
        return {"message": "Todo deleted successfully"}
    else:
        raise Exception("Todo not found")
