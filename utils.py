import sys
import logging
import functools

from sqlalchemy.orm import Session
from fastapi import  status
from fastapi.responses import Response

import schemas
from models import User
from models import Ticket
from models import TicketType
from models import TicketStatus
from models import TicketComment
from models import TicketPriority


GENERIC_404_RESPONSE = Response(
    status_code=status.HTTP_404_NOT_FOUND,
    content="Resource not found"
)


def get_ticket_priorities_from_db(session: Session) -> list[TicketPriority]:
    return session.query(TicketPriority).all()


def get_ticket_statuses_from_db(session: Session) -> list[TicketStatus]:
    return session.query(TicketStatus).all()


def get_ticket_types_from_db(session: Session) -> list[TicketType]:
    return session.query(TicketType).all()


def get_ticket_from_db(session: Session, id: int) -> Ticket:
    return session.query(Ticket).filter(Ticket.id == id).first()


def create_ticket_into_db(session: Session, ticket: Ticket) -> Ticket:
    session.add(ticket)
    session.commit()
    return ticket


def get_tickets_from_db(session: Session) -> list[Ticket]:
    return session.query(Ticket).all()


# def delete_ticket_from_db(session: Session, id: int):
#     obj = session.query(Ticket).filter(Ticket.id == id).first()
#     if obj == None:
#         return None
#     else:
#         session.delete(obj)
#         session.commit()
#         return obj


# def get_comments_by_ticket_id_from_db(session: Session, id: int):
#     return session.query(TicketComment).filter(TicketComment.ticket_id == id).all()


# def get_comment_by_ticket_id_from_db(session: Session, id: int, comment_id: int):
#     return session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)
# ).first()


# def create_comment_by_ticket_id_into_db(session: Session, id: int, item: CreateComment):
#     x = item.dict()
#     x["ticket_id"] = id
#     comment = TicketComment(**x)
#     session.add(comment)
#     session.commit()
#     return comment


# def delete_comment_by_ticket_id_from_db(session: Session, id: int, comment_id: int):
#     obj = session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).first()
#     session.delete(obj)
#     session.commit()
#     return obj

# def update_comment_by_ticket_id_from_db(session: Session, id: int, comment_id: int, item: CommentText):
#     session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).update(item.dict())
#     session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).update({"is_edited":True})
#     session.commit()
#     obj = session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).first()
#     return obj

# def update_ticket_from_db(session: Session, id: int, item: UpdateTicket):
#     session.query(Ticket).filter((Ticket.id == id)).update(item.dict())
#     session.commit()
#     obj = session.query(Ticket).filter((Ticket.id == id)).first()
#     return obj

# def get_users_from_db(session: Session):
#     return session.query(User).all()


# def get_user_from_db(session: Session, id: int):
#     return session.query(User).filter(User.id == id).all()


def serialize_ticket_from_model_to_schema(ticket: Ticket) -> schemas.TicketOutputSchema:
    return schemas.TicketOutputSchema(
        id=ticket.id,
        title=ticket.title,
        description=ticket.description,
        creation_date=ticket.creation_date,
        time_estimate=ticket.time_estimate,
        priority=ticket.priority,
        ttype=ticket.ttype,
        status=ticket.status,
        reporter_email=ticket.reporter_email,
        assignee_email=ticket.assignee_email
    )

def serialize_ticket_schema_to_model(ticket_schema: schemas.TicketInputSchema) -> Ticket:
    return Ticket(
        title=ticket_schema.title,
        description=ticket_schema.description,
        time_estimate=ticket_schema.time_estimate,
        priority=ticket_schema.priority,
        ttype=ticket_schema.ttype,
        status=ticket_schema.status,
        reporter_email=ticket_schema.reporter_email,
        assignee_email=ticket_schema.assignee_email
    )
