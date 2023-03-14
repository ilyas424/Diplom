import sys
import logging
import functools

from sqlalchemy.orm import Session
from sqlalchemy import exc
from fastapi import  status
from fastapi import HTTPException
from fastapi.responses import Response

import schemas
from models import User
from models import Ticket
from models import TicketType
from models import TicketStatus
from models import TicketComment
from models import TicketPriority
from models import AuthHandler

auth_handler = AuthHandler()


GENERIC_404_RESPONSE = Response(
    status_code=status.HTTP_404_NOT_FOUND,
    content="Resource not found"
)

GENERIC_400_RESPONSE = Response(
    status_code=status.HTTP_400_BAD_REQUEST,
    content="Bad request"
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
    try:
        session.commit()
    except exc.IntegrityError:
        raise HTTPException(status_code=400)
    return ticket


def get_tickets_from_db(session: Session) -> list[Ticket]:
    return session.query(Ticket).all()


def delete_ticket_from_db(session: Session, id: int):
    obj = session.query(Ticket).filter(Ticket.id == id).first()
    if obj == None:
        return None
    session.delete(obj)
    session.commit()
    return obj


def get_comments_by_ticket_id_from_db(session: Session, id: int):
    return session.query(TicketComment).filter(TicketComment.ticket_id == id).all()


def get_comment_by_ticket_id_from_db(session: Session, id: int, comment_id: int):
    return session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)
).first()


def create_comment_by_ticket_id_into_db(session: Session, id: int, item: TicketComment):
    x = item.dict()
    x["ticket_id"] = id
    comment = TicketComment(**x)
    session.add(comment)
    try:
        session.commit()
    except exc.IntegrityError:
        raise HTTPException(status_code=400)
    return comment


def delete_comment_by_ticket_id_from_db(session: Session, id: int, comment_id: int):
    obj = session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).first()
    if obj == None:
        return obj
    session.delete(obj)
    session.commit()
    return obj

def update_comment_by_ticket_id_from_db(session: Session, id: int, comment_id: int, item: TicketComment):
    try:
        session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).update(item.dict())
    except exc.IntegrityError:
        raise HTTPException(status_code=400)
    session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).update({"is_edited":True})
    session.commit()
    obj = session.query(TicketComment).filter((TicketComment.ticket_id == id) & (TicketComment.id == comment_id)).first()
    return obj

def update_ticket_from_db(session: Session, id: int, item: TicketComment):
    try:
        session.query(Ticket).filter((Ticket.id == id)).update(item.dict())
    except exc.IntegrityError:
        raise HTTPException(status_code=400)
    session.commit()
    obj = session.query(Ticket).filter((Ticket.id == id)).first()
    return obj

def get_users_from_db(session: Session):
    return session.query(User).all()


def get_user_from_db(session: Session, email: str):
    return session.query(User).filter(User.email == email).first()


def post_create_user(session: Session, user: User):
    hashed_password = auth_handler.get_password_hash(user.hash)
    x = user.dict()
    x['hash'] = hashed_password
    post = User(**x)
    session.add(post)
    session.commit()
    return post


def user_login(session: Session, user: User ):
    return session.query(User).filter(User.email == user.email).first()

def verify_role(session: Session, email ):
    user = session.query(User).filter(User.email == email).first()
    if user.is_admin == True:
        return True
    return False


def verify_email_from_ticket(session: Session, email, id):
    x = session.query(Ticket).filter(Ticket.id == id).first()
    if x.reporter_email == email:
        return True
    return False


def verify_email_from_comment(session: Session, email, id):
    x = session.query(TicketComment).filter(TicketComment.id == id).first()
    if x.author_email == email:
        return True
    return False



def update_user_role_from_db(session: Session, item: User):
    try:
        session.query(User).filter((User.email == item.email)).update(item.dict())
    except exc.IntegrityError:
        raise HTTPException(status_code=400)
    session.commit()
    obj = session.query(User).filter((User.email == item.email)).first()
    return obj


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


def serialize_comment_from_model_to_schema(comment: TicketComment) -> schemas.CommentOutputSchema:
    return schemas.CommentOutputSchema(
        id=comment.id,
        ticket_id=comment.ticket_id,
        text=comment.text,
        author_email=comment.author_email,
        creation_date=comment.creation_date,
        is_edited=comment.is_edited
    )


def serialize_comment_schema_to_model(comment_schema: schemas.CommentInputSchema) -> TicketComment:
    return TicketComment(
        text=comment_schema.text
    )


def serialize_user_schema_to_model(user_schema: schemas.UserOutputSchema) -> User:
    return User(
        email=user_schema.email,
        name=user_schema.name,
    )

def serialize_user_from_model_to_schema(user_schema: User) -> schemas.UserOutputSchema:
    return schemas.UserOutputSchema(
        email=user_schema.email,
        name=user_schema.name,
        hash=user_schema.hash
    )

def serialize_user_auth_schema_to_model(user_schema: User) -> schemas.UserAuthSchema:
    return schemas.UserAuthSchema(
        email=user_schema.email,
        hash=user_schema.hash
    )

