from fastapi import APIRouter
from starlette.requests import Request
from schema import Ticketcomment
from schema import  TicketCreate

import utils


router = APIRouter()


@router.get("/ticket/priority/all")
def get_ticket_priority_all(request: Request):
    result = {}
    session = request.state.db
    result = utils.get_ticket_priorities_from_db(session)
    return result


@router.get("/ticket/status/all")
def get_ticket_status_all(request: Request):
    result = {}
    session = request.state.db
    result = utils.get_ticket_statuses_from_db(session)
    return result


@router.get('/ticket/type/all')
def get_ticket_type_all(request: Request):
    result = {}
    session = request.state.db
    result = utils.get_ticket_types_from_db(session)
    return result

@router.get('/ticket/all')
def get_ticket_all(request: Request):
    result = {}
    session = request.state.db
    obj = utils.get_tickets_from_db(session)
    result = [{"description": val[0], "creation_date": val[1], "time_estimate": val[2],"priority": val[3], "type": val[4], "status": val[5], "reporter": val[6], "assigneee": val[7] } for val in obj]
    return result

@router.post('/ticket/create')
def post_ticket_create(request: Request, item: TicketCreate):
    result = {}
    session = request.state.db
    result = utils.create_ticket_from_db(session,item)
    return result


@router.get('/ticket/{id}')
def get_ticket_by_id(request: Request, id: int):
    result = {}
    session = request.state.db
    result = utils.get_ticket_from_db(session, id)
    return result


@router.delete('/ticket/{id}')
def delete_ticket_by_id(request: Request, id: int):
    result = {}
    session = request.state.db
    result = utils.delete_ticket_from_db(session, id)
    return result


@router.get('/ticket/{id}/comment/all')
def get_comments_by_ticket_id(request: Request, id: int):
    result = {}
    session = request.state.db
    result = utils.get_ticket_comments_by_ticket_from_db(session, id)
    return result

@router.get('/ticket/{id}/comment/{comment_id}')
def get_comment_by_ticket_id(request: Request, id: int, comment_id: int):
    result = {}
    session = request.state.db
    result = utils.get_ticket_comment_by_ticket_from_db(session, id,comment_id)
    return result

@router.delete('/ticket/{id}/comment/{comment_id}')
def get_comment_by_ticket_id(request: Request, id: int, comment_id: int):
    result = {}
    session = request.state.db
    result = utils.delete_ticket_comment_by_ticket_from_db(session, id,comment_id)
    return result

@router.patch('/ticket/{id}/comment/{comment_id}')
def patch_comment_by_ticket_id(request: Request, id: int, comment_id: int, item: Ticketcomment):
    result = {}
    session = request.state.db
    result = utils.patch_ticket_comment_by_ticket_from_db(session, id,comment_id,item)
    return result


@router.get('/user/all')
def get_user_all(request: Request):
    result = {}
    session = request.state.db
    result = utils.get_users_from_db(session)
    return result


@router.get('/user/{id}')
def get_user_by_id(request: Request, id: int):
    result = {}
    session = request.state.db
    result = utils.get_user_from_db(session, id)
    return result
