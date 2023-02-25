from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(128))
    description = Column(Text)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    time_estimate = Column(DateTime)
    priority = Column(String(64), ForeignKey("ticket_priorities.title"))
    ttype = Column(String(64), ForeignKey("ticket_types.title"))
    status = Column(String(64), ForeignKey("ticket_statuses.title"))
    reporter_email = Column(String(64), ForeignKey("users.email"))
    assignee_email = Column(String(64), ForeignKey("users.email"))

    comments = relationship("TicketComment", cascade="all, delete-orphan") # add cascade delete
    reporter = relationship("User", foreign_keys=[reporter_email])
    assignee = relationship("User", foreign_keys=[assignee_email])


class TicketPriority(Base):
    __tablename__ = "ticket_priorities"

    title = Column(String(64), primary_key=True, unique=True)


class TicketStatus(Base):
    __tablename__ = "ticket_statuses"

    title = Column(String(64), primary_key=True, unique=True)


class TicketType(Base):
    __tablename__ = "ticket_types"

    title = Column(String(64), primary_key=True, unique=True)


class TicketComment(Base):
    __tablename__ = "ticket_comments"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
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
