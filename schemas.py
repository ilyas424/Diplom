from datetime import datetime
from pydantic import EmailStr
from typing import Union
from pydantic import BaseModel


class TicketInputSchema(BaseModel):
    title: str
    description: str
    time_estimate: Union[datetime, None] = None
    priority: Union[str, None] = None
    ttype: Union[str, None] = None
    status: Union[str, None] = None
    reporter_email: EmailStr
    assignee_email: Union[EmailStr, None] = None


class TicketOutputSchema(BaseModel):
    id: int
    title: str
    description: str
    creation_date: datetime
    time_estimate: Union[datetime, None] = None
    priority: Union[str, None] = None
    ttype: Union[str, None] = None
    status: Union[str, None] = None
    reporter_email: EmailStr
    assignee_email: Union[EmailStr, None] = None


class CommentInputSchema(BaseModel):
    text: str
    


class CommentOutputSchema(BaseModel):
    id: int
    ticket_id: int
    text: str
    author_email: EmailStr
    creation_date: datetime
    is_edited: bool


class UserInputSchema(BaseModel):
    email: EmailStr
    name: str
    hash: str


class UserOutputSchema(BaseModel):
    email: EmailStr
    name: str


class UserAuthSchema(BaseModel):
    email: EmailStr
    hash: str
