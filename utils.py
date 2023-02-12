from sqlalchemy.orm import Session

from models import User
from models import Ticket
from models import TicketType
from models import TicketStatus
from models import TicketComment
from models import TicketPriority
from schema import Ticketcomment
from schema import TicketCreate


def get_ticket_priorities_from_db(session: Session):
    return session.query(TicketPriority).all()


def get_ticket_statuses_from_db(session: Session):
    return session.query(TicketStatus).all()


def get_ticket_types_from_db(session: Session):
    return session.query(TicketType).all()


def get_ticket_from_db(session: Session, id: int):
    return session.query(Ticket).filter(Ticket.id == id).first()

def create_ticket_from_db(session: Session, item: TicketCreate):
     obj = Ticket(**item.dict())
     session.add(obj)
     session.commit()
     return obj


def get_tickets_from_db(session: Session):
    obj =  session.query(Ticket.description, Ticket.creation_date, Ticket.time_estimate, TicketPriority.name,
                        TicketType.name, TicketStatus.name, User.name, User.name).join(
                         TicketType, Ticket.type_id == TicketType.id).join(
                         TicketPriority, Ticket.priority_id == TicketPriority.id).join(
                         TicketStatus, Ticket.status_id == TicketStatus.id).join(
                         User,Ticket.assignee_id == User.id).all()
    return obj


def delete_ticket_from_db(session: Session, id: int):
    obj = session.query(Ticket).filter(Ticket.id == id).first()
    session.delete(obj)
    session.commit()
    return obj


def get_ticket_comments_by_ticket_from_db(session: Session, id: int):
    return session.query(TicketComment).filter(TicketComment.ticket_id == id).all()


def get_ticket_comment_by_ticket_from_db(session: Session, id: int, comment_id: int):
    return session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).all()


def delete_ticket_comment_by_ticket_from_db(session: Session, id: int, comment_id: int):
    obj = session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).first()
    session.delete(obj)
    session.commit()
    return obj

def patch_ticket_comment_by_ticket_from_db(session: Session, id: int, comment_id: int, item: Ticketcomment):
    session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).update(item.dict())
    session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).update({"is_edited":True})
    session.commit()
    obj = session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).first()
    return obj

def get_users_from_db(session: Session):
    return session.query(User).all()


def get_user_from_db(session: Session, id: int):
    return session.query(User).filter(User.id == id).all()


# def create_post_list(session: Session, item: TicketList):
#     post = TicketPriority(**item.dict())
#     session.add(post)
#     session.commit()
#     return post
