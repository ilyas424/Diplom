from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

import utils
from db import get_db
from schema import TicketCreate
from schema import TicketList


router = APIRouter()

@router.get("/priority")
def post_list(db: Session = Depends(get_db)):
    posts = utils.get_post_list(db)
    return posts


@router.post("/priority")
def post_list(item: TicketList, db: Session = Depends(get_db)):
    posts = utils.create_post_list(db, item)
    return posts


@router.get('/type')
def post_list(db: Session = Depends(get_db)):
    posts = utils.get_post_type(db)
    return posts


@router.get('/')
def post_list(db: Session = Depends(get_db)):
    posts = utils.get_post_ticket(db)
    return posts
