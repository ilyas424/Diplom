from models import TicketType
from models import TicketStatus
from models import User
from models import Ticket
from models import TicketPriority
from models import TicketComment
from schema import TicketList
from db import SessionLocal

def get_post_priority():
    session = SessionLocal()
    return session.query(TicketPriority).all()


def get_post_type():
    session = SessionLocal()
    return session.query(TicketType).all()


def get_post_status():
    session = SessionLocal()
    return session.query(TicketStatus).all()


def get_post_ticket():
    session = SessionLocal()
    return session.query(Ticket).all()

def get_post_ticketid(id):
    session = SessionLocal()
    return session.query(Ticket).filter(Ticket.id == id).first()

def delete_post_ticket(id):
    session = SessionLocal()
    obj = session.query(Ticket).filter(Ticket.id == id).first()
    session.delete(obj)
    session.commit()
    #session.refresh(obj)
    return obj
    


def get_post_users():
    session = SessionLocal()
    return session.query(User).all()

def get_post_usersid():
    session = SessionLocal()
    return session.query(User).filter(User.id == id).all()

def get_post_comment():
    session = SessionLocal()
    return session.query(TicketComment).filter(TicketComment.id == id).all()


def create_post_list(item: TicketList):
    session = SessionLocal()
    post = TicketPriority(**item.dict())
    session.add(post)
    session.commit()
    return post
