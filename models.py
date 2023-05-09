from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ARRAY
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

import settings
from db import Base




class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(128))
    description = Column(Text)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    time_estimate = Column(DateTime)
    priority = Column(String(64), ForeignKey("ticket_priorities.title"))
    ttype = Column(String(64), ForeignKey("ticket_types.title"))
    reporter_email = Column(String(64), ForeignKey("users.email"))
    assignee_email = Column(String(64), ForeignKey("users.email"))
    board_id = Column(Integer, ForeignKey("boards.id", ondelete='CASCADE'), nullable=True)
    column_id = Column(String(64), nullable=True)
    
    boards = relationship("Board", backref=backref('tickets', cascade="all, delete-orphan"))
    comments = relationship("TicketComment", cascade="all, delete-orphan") # add cascade delete
    reporter = relationship("User", foreign_keys=[reporter_email])
    assignee = relationship("User", foreign_keys=[assignee_email])


class TicketPriority(Base):
    __tablename__ = "ticket_priorities"

    title = Column(String(64), primary_key=True, unique=True)


class TicketType(Base):
    __tablename__ = "ticket_types"

    title = Column(String(64), primary_key=True, unique=True)


class TicketComment(Base):
    __tablename__ = "ticket_comments"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id",ondelete='CASCADE'))
    text = Column(String(256), unique=False)   
    author_email = Column(String(64), ForeignKey("users.email"))
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    is_edited = Column(Boolean, server_default='f', nullable=False)

    ticket = relationship("Ticket", back_populates="comments")
    author = relationship("User")


class User(Base):
    __tablename__ = "users"

    email = Column(String(64), primary_key=True, index=True, unique=True)
    name = Column(String(64), unique=False)
    hash = Column(String(256))
    is_admin = Column(Boolean, server_default='f', nullable=False)


class Board(Base):
    __tablename__ = "boards"
    
    id =  Column(Integer, primary_key=True, index=True, unique=True)
    board_name = Column(String(64))
    description = Column(String(64))
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    creator_email = Column(String(64),ForeignKey("users.email"))
    is_open = Column(Boolean, default=True, nullable=False)
    columns = Column(ARRAY(String(64)))


    

