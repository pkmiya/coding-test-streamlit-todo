from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from DB import db
from CRUD import get_todo
from SCHEMA.schema import TodoUpdateSchema

router = APIRouter()


@router.get("/todos", response_model=list[TodoUpdateSchema])
def read_todos(db_session: Session = Depends(db.get_db)):
    todos = get_todo.get_todos(db_session)
    return todos
