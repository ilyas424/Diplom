from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    description = Column(String(350))
    creation_date = Column(DateTime) #@TODO set server_default
    time_estimate = Column(DateTime)
    priority_id = Column(Integer, ForeignKey("ticket_priorities.id"))
    type_id = Column(Integer, ForeignKey("ticket_types.id"))
    status_id = Column(Integer, ForeignKey("ticket_statuses.id"))
    reporter_id = Column(Integer, ForeignKey("employees.id"))
    assignee_id = Column(Integer, ForeignKey("employees.id"))

    priority = relationship("TicketPriority")
    type = relationship("TicketType")
    status = relationship("TicketStatus")
    comments = relationship("TicketComment")
    # reporter = relationship("Employee")
    # assignee = relationship("Employee")


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
    author_id = Column(Integer, ForeignKey("employees.id"))
    creation_date = Column(DateTime) #@TODO default
    #@TODO was_edited field

    ticket = relationship("Ticket", back_populates="comments")


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(40), unique=True)
