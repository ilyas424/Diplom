from sqlalchemy.orm import Session

from models import User
from models import Ticket
from models import TicketType
from models import TicketStatus
from models import TicketComment
from models import TicketPriority
from schema import TicketComment
from schema import TicketCreate


def get_ticket_priorities_from_db(session: Session):
    return session.query(TicketPriority).all()


def get_ticket_statuses_from_db(session: Session):
    return session.query(TicketStatus).all()


def get_ticket_types_from_db(session: Session):
    return session.query(TicketType).all()


def get_ticket_from_db(session: Session, id: int):
    return session.query(Ticket).filter(Ticket.id == id).first()

def create_ticket_into_db(session: Session, ticket_json: TicketCreate):
    ticket = Ticket(**ticket_json.dict())
    session.add(ticket)
    session.commit()
    return ticket


def get_tickets_from_db(session: Session) -> list[Ticket]:
    obj = session.query(Ticket).all()
    return obj


def delete_ticket_from_db(session: Session, id: int):
    obj = session.query(Ticket).filter(Ticket.id == id).first()
    session.delete(obj)
    session.commit()
    return obj


def get_comments_by_ticket_id_from_db(session: Session, id: int):
    return session.query(TicketComment).filter(TicketComment.ticket_id == id).all()


def get_comment_by_ticket_id_from_db(session: Session, id: int, comment_id: int):
    return session.query(TicketComment).filter(
        (TicketComment.ticket_id == id) & (TicketComment.id == comment_id)
    ).all()


def delete_comment_by_ticket_id_from_db(session: Session, id: int, comment_id: int):
    obj = session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).first()
    session.delete(obj)
    session.commit()
    return obj

def update_comment_by_ticket_id_from_db(session: Session, id: int, comment_id: int, item: TicketComment):
    session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).update(item.dict())
    session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).update({"is_edited":True})
    session.commit()
    obj = session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).first()
    return obj

def get_users_from_db(session: Session):
    return session.query(User).all()


def get_user_from_db(session: Session, id: int):
    return session.query(User).filter(User.id == id).all()


def convert_ticket_object_to_json(ticket: Ticket) -> dict:
    return {
        "description": ticket.description,
        "creation_date": ticket.creation_date,
        "time_estimate": ticket.time_estimate,
        "priority": ticket.priority.name,
        "type": ticket.type.name,
        "status": ticket.status.name,
        "reporter": ticket.reporter.name,
        "assignee": ticket.assignee.name

    }

