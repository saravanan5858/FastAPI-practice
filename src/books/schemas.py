from pydantic import BaseModel


class Book(BaseModel):
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

class BookUpdateModel(BaseModel):
    title:str
    author:str
    publisher:str
    pages:int
    website:str  