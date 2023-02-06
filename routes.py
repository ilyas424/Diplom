from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

import utils
from db import get_db
from schema import TicketCreate
from schema import TicketList

router = APIRouter()


@router.get("/ticket/priority/all")
def get_priority(db: Session = Depends(get_db)):
    posts = utils.get_post_priority(db)
    return posts


@router.get("/ticket/status/all")
def get_status(db: Session = Depends(get_db)):
    posts = utils.get_post_status(db)
    return posts


@router.get('/ticket/type/all')
def get_type(db: Session = Depends(get_db)):
    posts = utils.get_post_type(db)
    return posts


@router.get('/ticket/{ids}')
def get_ticketid(ids,db: Session = Depends(get_db)):
    posts = utils.get_post_ticketid(ids,db)
    return posts


@router.get('/ticket/all')
def get_tickets(db: Session = Depends(get_db)):
    posts = utils.get_post_ticket(db)
    return posts


@router.delete('/ticket/{ids}')
def delete_ticket(ids, db: Session = Depends(get_db)):
    posts = utils.delete_post_ticket(ids,db)
    return posts


@router.get('/user/all')
def get_users(db: Session = Depends(get_db)):
    posts = utils.get_post_users(db)
    return posts


@router.get('/user/{ids}')
def get_user(ids,db: Session = Depends(get_db)):
    posts = utils.get_post_usersid(ids,db)
    return posts

@router.get('/comment/{ids}')
def get_comment(ids,db: Session = Depends(get_db)):
    posts = utils.get_post_comment(ids,db)
    return posts