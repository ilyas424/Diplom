from fastapi import APIRouter

import utils

router = APIRouter()


@router.get("/ticket/priority/all")
def get_priority():
    posts = utils.get_post_priority()
    return posts


@router.get("/ticket/status/all")
def get_status():
    posts = utils.get_post_status()
    return posts


@router.get('/ticket/type/all')
def get_type():
    posts = utils.get_post_type()
    return posts


@router.get('/ticket/{id}')
def get_ticketid(id):
    posts = utils.get_post_ticketid(id)
    return posts


@router.get('/ticket/all')
def get_tickets():
    posts = utils.get_post_ticket()
    return posts


@router.delete('/ticket/{id}')
def delete_ticket(id):
    posts = utils.delete_post_ticket(id)
    return posts


@router.get('/user/all')
def get_users():
    posts = utils.get_post_users()
    return posts


@router.get('/user/{id}')
def get_user(id):
    posts = utils.get_post_usersid(id)
    return posts

@router.get('/comment/{id}')
def get_comment(id):
    posts = utils.get_post_comment(id)
    return posts