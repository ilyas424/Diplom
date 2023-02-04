from sqlalchemy import Column, String, Integer
from core.db import Base


class Priority(Base):
    __tablename__ = "priority"

    priority_id = Column(Integer, primary_key=True, index=True, unique=True)
    priority_name = Column(String(40), unique=True)


class Status(Base):
    __tablename__ = "status"

    status_id = Column(Integer, primary_key=True, index=True, unique=True)
    status_name = Column(String(40), unique=True)


class Type(Base):
    __tablename__ = "type"

    type_id = Column(Integer, primary_key=True, index=True, unique=True)
    type_name = Column(String(40), unique=True)


class Employees(Base):
    __tablename__ = "employees"

    employees_id = Column(Integer, primary_key=True, index=True, unique=True)
    Full_name = Column(String(40), unique=True)


class Comments(Base):
    __tablename__ = "comments"

    comments_id = Column(Integer, primary_key=True, index=True, unique=True)
    Comments_name = Column(String(350), unique=True)

