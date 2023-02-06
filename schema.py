from pydantic import BaseModel
from datetime import datetime


class TicketBase(BaseModel):
    name: str

class TicketList(TicketBase):
    name: str
    id: int


class TicketCreate(TicketBase):
    pass

    class Config:
        orm_mode = True
