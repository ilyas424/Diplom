from jose import jwt
from jose import ExpiredSignatureError
from jwt import InvalidTokenError
from datetime import timedelta
from datetime import datetime
from fastapi import HTTPException
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from passlib.context import CryptContext
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
    hash = Column(String(256))
    is_admin = Column(Boolean, server_default='f', nullable=False)


class Board(Base):
    __tablename__ = "board"
    
    board =  Column(String(64), primary_key=True, index=True, unique=True)
    toDo = Column(ARRAY(int))
    in_Progress = Column(ARRAY(int))
    done = Column(ARRAY(int))
    closed = Column(ARRAY(int))

    

    


class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = settings.Secret

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, user_email):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=5),
            'iat': datetime.utcnow(),
            'sub': user_email
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm='HS256'
        )

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Signature has expired')
        except InvalidTokenError as e:
            raise HTTPException(status_code=401, detail='Invalid token')
        except jwt.JWTError:
            raise HTTPException(status_code=401, detail='Not enough segments')

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)