from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from DB import db
from CRUD import insert_todo_crud
from SCHEMA.schema import TodoCreateSchema

router = APIRouter()


@router.post("/todos", response_model=TodoCreateSchema, tags=['todos'], description='Insert a new TODO item')
def insert_todo(todo_data: TodoCreateSchema, db: Session = Depends(db.get_db)):
    try:
        new_todo = insert_todo_crud.insert_todo_crud(db, todo_data)
        return new_todo
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
