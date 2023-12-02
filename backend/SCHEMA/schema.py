from pydantic import BaseModel
import datetime


from pydantic import BaseModel
import datetime


class TodoCreateSchema(BaseModel):
    deadline: datetime.date
    todo: str
    priority: int
    genre: str
    is_done: bool = False
    created_at: datetime.date = datetime.date.today()

    # enable ORM mode for SQLAlchemy
    class Config:
        orm_mode = True


class TodoUpdateSchema(BaseModel):
    id: int
    deadline: datetime.date
    todo: str
    priority: int
    genre: str
    is_done: bool
    created_at: datetime.date

    # enable ORM mode for SQLAlchemy
    class Config:
        orm_mode = True

