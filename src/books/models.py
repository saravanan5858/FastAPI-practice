from sqlmodel import SQLModel
from datetime import datetime

class Book(SQLModel, table=True):
    id:int
    isbn:str
    title:str
    subtitle:str
    author:str
    published:str
    publisher:str
    pages:int
    description:str
    website:str
    created_at: datetime
    updated_at: datetime