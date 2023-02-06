from sqlalchemy.orm import Session

from models import TicketType
from models import TicketStatus
from models import User
from models import Ticket
from models import TicketPriority
from models import TicketComment
from schema import TicketList


def get_post_priority(db: Session):
    return db.query(TicketPriority).all()


def get_post_type(db: Session):
    return db.query(TicketType).all()


def get_post_status(db: Session):
    return db.query(TicketStatus).all()


def get_post_ticket(db: Session):
    return db.query(Ticket).all()

def get_post_ticketid(ids,db: Session):
    return db.query(Ticket).filter(Ticket.id == ids).first()

def delete_post_ticket(ids, db: Session):
    obj = db.query(Ticket).filter(Ticket.id == ids).first()
    db.delete(obj)
    db.commit()
    db.refresh(obj)
    return obj
    


def get_post_users(db: Session):
    return db.query(User).all()

def get_post_usersid(ids, db: Session):
    return db.query(User).filter(User.id == ids).all()

def get_post_comment(ids, db: Session):
    return db.query(TicketComment).filter(TicketComment.id == ids).all()


def create_post_list(db: Session, item: TicketList):
    post = TicketPriority(**item.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
