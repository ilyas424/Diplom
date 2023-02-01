from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base


class Post(Base):
    __tablename__ = "ticket_posts"
    ticket_id = Column(Integer, primary_key=True, index=True, unique=True)
    description = Column(String(350))
    time_estimate = Column(DateTime)
    priority = Column(Integer, ForeignKey("priority.priority_id"))
    priority_id = relationship("Priority")
    type = Column(Integer, ForeignKey("type.type_id"))
    Type_id = relationship("Type")
    status = Column(Integer, ForeignKey("status.status_id"))
    status_id = relationship("Status")
    comments = Column(Integer, ForeignKey("comments.comments_id"))
    comments_id = relationship("Comments")
    reporter = Column(Integer, ForeignKey("employees.employees_id"))
    employees_id = relationship("Employees")
    assignee = Column(Integer, ForeignKey("employees.employees_id"))
    employees_id = relationship("Employees")
