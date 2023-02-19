from datetime import datetime

from typing import Union
from pydantic import BaseModel


class TicketSchema(BaseModel):
    id: int
    description: str
    creation_date: datetime
    time_estimate: datetime
    priority: Union[str, None] = None
    ttype: Union[str, None] = None
    status: Union[str, None] = None
    reporter: str
    assignee: str


class TicketPrioritySchema(BaseModel):
    title: str


class TicketTypeSchema(BaseModel):
    title: str


class TicketStatusSchema(BaseModel):
    title: str


class TicketCommentSchema(BaseModel):
    id: int
    ticket_id: int
    text: str
    author_id: int
    creation_date: datetime
    is_edited: bool


class UserSchema(BaseModel):
    id: int
    name: str
    email: str


# class CommentText(BaseModel):
#     text: str

# class UpdateTicket(BaseModel):
#     description: str
#     priority_id: int
#     type_id: int
#     status_id: int
#     assignee_id: int

# class CreateComment(BaseModel):
#     text: str
#     author_id: int

# class TicketCreate(BaseModel):
#     description: str
#     priority_id: int
#     type_id: int
#     status_id: int
#     reporter_id: int
#     assignee_id: int

#     class Config:
#         orm_mode = True
