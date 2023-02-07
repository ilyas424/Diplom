from fastapi import APIRouter
from starlette.requests import Request

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


@router.get('/ticket/{id}')
def get_ticket_by_id(request: Request, id: int):
    result = {}
    session = request.state.db
    result = utils.get_ticket_from_db(session, id)
    return result


@router.get('/ticket/all')
def get_ticket_all(request: Request):
    result = {}
    session = request.state.db
    result = utils.get_tickets_from_db(session)
    return result


@router.delete('/ticket/{id}')
def delete_ticket_by_id(request: Request, id: int):
    result = {}
    session = request.state.db
    result = utils.delete_ticket_from_db(session, id)
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


@router.get('/comment/{id}')
def get_comment_by_id(request: Request, id: int):
    result = {}
    session = request.state.db
    result = utils.get_ticket_comment_from_db(session, id)
    return result
