from pydantic import BaseModel
from datetime import datetime


class CommentText(BaseModel):
    text: str

class UpdateTicket(BaseModel):
    description: str
    priority_id: int
    type_id: int
    status_id: int
    assignee_id: int

class CreateComment(BaseModel):
    text: str
    author_id: int

class TicketCreate(BaseModel):
    description: str
    priority_id: int
    type_id: int
    status_id: int
    reporter_id: int
    assignee_id: int

    class Config:
        orm_mode = True
