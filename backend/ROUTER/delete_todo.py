from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from DB import db
from CRUD import delete_todo_crud

router = APIRouter()


@router.delete("/todos/{todo_id}", tags=['todos'], description='Delete a TODO item by ID')
def delete_todo(todo_id: int, db: Session = Depends(db.get_db)):
    try:
        result = delete_todo_crud.delete_todo_crud(db, todo_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
