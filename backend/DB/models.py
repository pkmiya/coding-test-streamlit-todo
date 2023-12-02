from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Todo(Base):
    __tablename__ = 'todo_list'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    deadline = Column(Date)
    todo = Column(String)
    priority = Column(Integer)
    genre = Column(String)
    is_done = Column(Boolean, default=False)
    created_at = Column(Date)
