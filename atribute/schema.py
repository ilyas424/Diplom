from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    name: str


class PostList(PostBase):
    name: str
    id: int


class PostCreate(PostBase):
    pass

    class Config:
        orm_mode = True
