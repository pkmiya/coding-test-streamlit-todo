from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from DB import db
from CRUD import delete_todo

router = APIRouter()


@router.delete("/todos/{todo_id}", tags=['todos'], description='Delete a TODO item by ID')
def delete_todos(todo_id: int, db: Session = Depends(db.get_db)):
    try:
        # IDに基づいてtodoアイテムを削除する処理
        result = delete_todo.delete_todo_by_id(db, todo_id)
        return result
    except Exception as e:
        # エラーの場合は詳細を返す
        raise HTTPException(status_code=400, detail=str(e))
