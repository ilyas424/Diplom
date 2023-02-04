from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from . import service
from .schema import PostCreate, PostList

router = APIRouter()


@router.get("/priority")
def post_list(db: Session = Depends(get_db)):
    posts = service.get_post_list(db)
    return posts


@router.post("/priority")
def post_list(item: PostList, db: Session = Depends(get_db)):
    posts = service.create_post_list(db, item)
    return posts


@router.get('/type')
def post_list(db: Session = Depends(get_db)):
    posts = service.get_post_type(db)
    return posts


@router.get('/')
def post_list(db: Session = Depends(get_db)):
    posts = service.get_post_ticket(db)
    return posts
