from sqlalchemy.orm import Session

from models import User
from models import Ticket
from models import TicketType
from models import TicketStatus
from models import TicketComment
from models import TicketPriority
# from schema import TicketList


def get_ticket_priorities_from_db(session: Session):
    return session.query(TicketPriority).all()


def get_ticket_statuses_from_db(session: Session):
    return session.query(TicketStatus).all()


def get_ticket_types_from_db(session: Session):
    return session.query(TicketType).all()


def get_ticket_from_db(session: Session, id: int):
    return session.query(Ticket).filter(Ticket.id == id).first()


def get_tickets_from_db(session: Session):
    return session.query(Ticket).all()


def delete_ticket_from_db(session: Session, id: int):
    obj = session.query(Ticket).filter(Ticket.id == id).first()
    session.delete(obj)
    session.commit()
    return obj


def get_users_from_db(session: Session):
    return session.query(User).all()


def get_user_from_db(session: Session, id: int):
    return session.query(User).filter(User.id == id).all()


def get_ticket_comment_from_db(session: Session, id: int):
    return session.query(TicketComment).filter(TicketComment.id == id).all()


# def create_post_list(session: Session, item: TicketList):
#     post = TicketPriority(**item.dict())
#     session.add(post)
#     session.commit()
#     return post
