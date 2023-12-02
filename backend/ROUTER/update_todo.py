from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from DB import db
from CRUD import update_todo_crud
from SCHEMA.schema import TodoUpdateSchema

router = APIRouter()


@router.patch("/todos/{id}", response_model=TodoUpdateSchema, tags=['todos'], description='Update a TODO item')
def update_todo(id: int, todo_data: TodoUpdateSchema, db: Session = Depends(db.get_db)):
    try:
        # データの更新処理
        updated_todo = update_todo_crud.update_todo_crud(db, id, todo_data)
        return updated_todo
    except Exception as e:
        # エラーの場合は詳細を返す
        raise HTTPException(status_code=400, detail=str(e))
