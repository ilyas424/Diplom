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
    reporter_email: EmailStr
    assignee_email: Union[EmailStr, None] = None
    board_id: Union[int, None] = None
    column_id: Union[str, None] = None


class TicketOutputSchema(BaseModel):
    id: int
    title: str
    description: str
    creation_date: datetime
    time_estimate: Union[datetime, None] = None
    priority: Union[str, None] = None
    ttype: Union[str, None] = None
    reporter_email: EmailStr
    assignee_email: Union[EmailStr, None] = None
    board_id: Union[int, None] = None
    column_id: Union[str, None] = None


class BoardInputSchema(BaseModel):
    board_name: str
    description: Union[str, None] = None
    creator_email: EmailStr
    columns: list


class BoardOutputSchema(BaseModel):
    id: int
    board_name: str
    description: Union[str, None] = None
    creation_date: datetime
    creator_email: EmailStr
    is_open: bool
    columns: list


class CommentInputSchema(BaseModel):
    text: str
    author_email: EmailStr
    

class CommentOutputSchema(BaseModel):
    id: int
    ticket_id: int
    text: str
    author_email: EmailStr
    creation_date: datetime
    is_edited: bool


class CommentUpdateSchema(BaseModel):
    text: str


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

class UserEmailSchema(BaseModel):
    email: EmailStr
    is_admin: bool
