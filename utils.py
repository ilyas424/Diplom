from sqlalchemy.orm import Session

from models import TicketType
from models import Ticket
from models import TicketPriority
from schema import TicketList


def get_post_list(db: Session):
    return db.query(TicketPriority).all()

def get_post_type(db: Session):
    return db.query(TicketType).all()

def get_post_ticket(db: Session):
    return db.query(Ticket).all()

def create_post_list(db: Session, item: TicketList):
    post = TicketPriority(**item.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
