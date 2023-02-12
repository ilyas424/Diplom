from pydantic import BaseModel
from datetime import datetime


class TicketComment(BaseModel):
    text: str


class TicketCreate(BaseModel):
    description: str
    priority_id: int
    type_id: int
    status_id: int
    reporter_id: int
    assignee_id: int

    class Config:
        orm_mode = True
