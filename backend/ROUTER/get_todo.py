from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from DB import db
from CRUD import get_todo_crud
from SCHEMA.schema import TodoUpdateSchema

router = APIRouter()


@router.get("/todos", response_model=list[TodoUpdateSchema])
def get_todo(db_session: Session = Depends(db.get_db)):
    todos = get_todo_crud.get_todo_crud(db_session)
    return todos
