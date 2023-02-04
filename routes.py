from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

import utils
from db import get_db
from schema import TicketCreate
from schema import TicketList


router = APIRouter()

@router.get("/ticket/priority/all")
def post_list(db: Session = Depends(get_db)):
    posts = utils.get_post_list(db)
    return posts


@router.get('/ticket/type/all')
def post_list(db: Session = Depends(get_db)):
    posts = utils.get_post_type(db)
    return posts


@router.get('/ticket/all')
def post_list(db: Session = Depends(get_db)):
    posts = utils.get_post_ticket(db)
    return posts
