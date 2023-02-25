from datetime import datetime

from typing import Union
from pydantic import BaseModel


class TicketInputSchema(BaseModel):
    title: str
    description: str
    time_estimate: Union[datetime, None] = None
    priority: Union[str, None] = None
    ttype: Union[str, None] = None
    status: Union[str, None] = None
    reporter_email: str
    assignee_email: Union[str, None] = None


class TicketOutputSchema(BaseModel):
    id: int
    title: str
    description: str
    creation_date: datetime
    time_estimate: Union[datetime, None] = None
    priority: Union[str, None] = None
    ttype: Union[str, None] = None
    status: Union[str, None] = None
    reporter_email: str
    assignee_email: Union[str, None] = None


# class TicketCommentSchema(BaseModel):
#     id: int
#     ticket_id: int
#     text: str
#     author_id: int
#     creation_date: datetime
#     is_edited: bool


# class UserSchema(BaseModel):
#     email: str
#     name: str
