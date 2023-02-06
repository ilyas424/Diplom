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
    description = Column(Text)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())  # @TODO set server_default
    time_estimate = Column(DateTime)
    priority_id = Column(Integer, ForeignKey("ticket_priorities.id"))
    type_id = Column(Integer, ForeignKey("ticket_types.id"))
    status_id = Column(Integer, ForeignKey("ticket_statuses.id"))
    reporter_id = Column(Integer, ForeignKey("users.id"))
    assignee_id = Column(Integer, ForeignKey("users.id"))

    priority = relationship("TicketPriority")
    type = relationship("TicketType")
    status = relationship("TicketStatus")
    comments = relationship("TicketComment")
    reporter = relationship("User", foreign_keys=[reporter_id])
    assignee = relationship("User", foreign_keys=[assignee_id])


class TicketPriority(Base):
    __tablename__ = "ticket_priorities"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(40), unique=True)


class TicketStatus(Base):
    __tablename__ = "ticket_statuses"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(40), unique=True)


class TicketType(Base):
    __tablename__ = "ticket_types"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(40), unique=True)


class TicketComment(Base):
    __tablename__ = "ticket_comments"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    text = Column(String(350), unique=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    is_edited = Column(Boolean, server_default='f', nullable=False)

    ticket = relationship("Ticket", back_populates="comments")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(40), unique=True)
