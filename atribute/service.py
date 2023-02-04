from sqlalchemy.orm import Session

import ticket
from ticket.models import Post
from .schema import PostList
from .models import Priority, Type


def get_post_list(db: Session):
    return db.query(Priority).all()


def get_post_type(db: Session):
    return db.query(Type).all()


def get_post_ticket(db: Session):
    return db.query(Post).all()


def create_post_list(db: Session, item: PostList):
    post = Priority(**item.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
