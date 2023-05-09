import sys
import logging
import functools
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import exc
from fastapi import  status
from fastapi import HTTPException
from fastapi.responses import Response

import schemas
from models import User
from models import Ticket
from models import TicketType
from models import TicketComment
from models import TicketPriority
from models import Board

from Auth import AuthHandler

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


def get_ticket_types_from_db(session: Session) -> list[TicketType]:
    return session.query(TicketType).all()


def get_ticket_from_db(session: Session, id: int) -> Ticket:
    return session.query(Ticket).filter(Ticket.id == id).first()

def get_tickets_from_db_by_board_id(session: Session, id: int) -> Ticket:
    return session.query(Ticket).filter(Ticket.board_id == id).all()


def create_ticket_into_db(session: Session, ticket: Ticket) -> Ticket: 
    res = session.query(Board).filter(Board.id == ticket.board_id).first()
    if  (ticket.column_id == None and ticket.board_id == None) :
        session.add(ticket)
        try:
            session.commit()
        except exc.IntegrityError:
            raise HTTPException(status_code=400)
        return ticket
    if (ticket.column_id == None or ticket.board_id == None):
        raise HTTPException(status_code=400)
    if res == None:
        raise HTTPException(status_code=400)
    if (ticket.column_id in res.columns and ticket.board_id != None):
        session.add(ticket)
        try:
            session.commit()
        except exc.IntegrityError:
            raise HTTPException(status_code=400)
        return ticket
    else:
        raise HTTPException(status_code=400)
        
    

def get_tickets_from_db(session: Session) -> list[Ticket]:
    return session.query(Ticket).all()

def get_tickets_in_backlog_from_db(session: Session) -> list[Ticket]:
    return session.query(Ticket).filter(Ticket.board_id == None).all()


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
    x["creation_date"] = datetime.datetime.now()
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


def post_create_board(session: Session, board: Board):
    session.add(board)
    try:
        session.commit()
    except exc.IntegrityError:
        raise HTTPException(status_code=400)
    return board


def update_board_from_db(session: Session, id: int):
    try:
        board = session.query(Board).filter(Board.id == id).first()
        if board.is_open:   
            session.query(Board).filter(Board.id == id).update({"is_open":False})
        else:
            session.query(Board).filter(Board.id == id).update({"is_open":True})
    except exc.IntegrityError:
        raise HTTPException(status_code=400)
    session.commit()
    board_edited = session.query(Board).filter((Board.id == id)).first()
    return board_edited


def delete_board_from_db(session: Session, id: int):
    obj = session.query(Board).filter((Board.id == id)).first()
    if obj == None:
        return None
    session.delete(obj)
    session.commit()
    return id

def delete_user_from_db(session: Session, email: str):
    obj = session.query(User).filter((User.email == email)).first()
    if obj == None:
        return None
    session.delete(obj)
    session.commit()
    return id


def user_login(session: Session, user: User):
    user = session.query(User).filter(User.email == user.email).first()
    if user == None:
         raise HTTPException(status_code=400, detail='Неверный пароль и/или логин ')
    return user



def get_board_from_db(session: Session, id: int):
    return session.query(Board).filter(Board.id == id).first()

def get_boards_from_db(session: Session):
    return session.query(Board).all()


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


def verify_email_from_board(session: Session, email, id):
    x = session.query(Board).filter(Board.id == id).first()
    if x.creator_email == email:
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
        reporter_email=ticket.reporter_email,
        assignee_email=ticket.assignee_email,
        board_id=ticket.board_id,
        column_id=ticket.column_id
    )


def serialize_ticket_schema_to_model(ticket_schema: schemas.TicketInputSchema) -> Ticket:
    return Ticket(
        title=ticket_schema.title,
        description=ticket_schema.description,
        time_estimate=ticket_schema.time_estimate,
        priority=ticket_schema.priority,
        ttype=ticket_schema.ttype,
        reporter_email=ticket_schema.reporter_email,
        assignee_email=ticket_schema.assignee_email,
        board_id=ticket_schema.board_id,
        column_id=ticket_schema.column_id
    )


def serialize_board_schema_to_model(board_schema: schemas.BoardInputSchema) -> Board:
    return Board(
        board_name=board_schema.board_name,
        description=board_schema.description,
        creator_email=board_schema.creator_email,
        columns=board_schema.columns
    )


def all_info_board_from_model_to_schema(board: Board, tickets) -> schemas.BoardOutputSchema:
    cols = {}
    for col in board.columns:
        for ticket in tickets:
            if (col in cols) and (col == ticket.column_id):
                cols[col] += [ticket]
            elif (col not in cols) and (col == ticket.column_id):
                cols[col] = [ticket]
        if (col not in cols):
            cols[col] = []
    return schemas.BoardOutputSchema(
        id=board.id,
        board_name=board.board_name,
        description=board.description,
        creator_email=board.creator_email,
        creation_date=board.creation_date,
        is_open=board.is_open,
        columns=[cols]
    )


def serialize_board_from_model_to_schema(board: Board) -> schemas.BoardOutputSchema:
    return schemas.BoardOutputSchema(
        id=board.id,
        board_name=board.board_name,
        description=board.description,
        creator_email=board.creator_email,
        creation_date=board.creation_date,
        is_open=board.is_open,
        columns=board.columns
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
        is_admin=user_schema.is_admin
    )

def serialize_user_schema_to_model_input(user_schema: schemas.UserInputSchema) -> User:
    return User(
        email=user_schema.email,
        name=user_schema.name,
        hash=user_schema.hash
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

