from sqlalchemy.orm import Session
from DB.models import Todo


def update_todo(db: Session, id: int, todo_data: Todo):
    try:
        # データの取得と更新
        todo_to_update = db.query(Todo).filter(Todo.id == id).first()
        if todo_to_update:
            for key, value in todo_data.dict().items():
                setattr(todo_to_update, key, value)
            db.commit()
            db.refresh(todo_to_update)  # 更新されたTODOアイテムの情報をリフレッシュ
            return todo_to_update
        else:
            return None  # IDに対応するTODOアイテムが見つからない場合
    except Exception as e:
        # エラーの場合は詳細を返す
        raise e
