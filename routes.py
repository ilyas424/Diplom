from fastapi import Depends
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import exc
from starlette.requests import Request

import utils
import schemas
from settings import logger
from settings import feed_logger
from models import AuthHandler


logger.info("APIRouter creating")
auth_handler = AuthHandler()
router = APIRouter()


@router.get("/ticket/priorities", tags=["Priority"])
async def get_ticket_priorities(request: Request) -> list[str]:
    session = request.state.db
    priorities = utils.get_ticket_priorities_from_db(session)
    priorities_resp = [priority.title for priority in priorities]
    return JSONResponse(jsonable_encoder(priorities_resp))


@router.get("/ticket/statuses", tags=["Status"])
def get_ticket_status_all(request: Request) -> list[str]:
    session = request.state.db
    statuses = utils.get_ticket_statuses_from_db(session)
    statuses_resp = [status.title for status in statuses]
    return JSONResponse(jsonable_encoder(statuses_resp))


@router.get('/ticket/types', tags=["Type"])
def get_ticket_type_all(request: Request) -> list[str]:
    session = request.state.db
    types = utils.get_ticket_types_from_db(session)
    types_resp = [type.title for type in types]
    return JSONResponse(jsonable_encoder(types_resp))


@router.get('/ticket/all', tags=["Ticket"])
def get_ticket_all(request: Request) -> list[schemas.TicketOutputSchema]:
    session = request.state.db
    tickets = utils.get_tickets_from_db(session)
    tickets_resp = []
    for ticket in tickets:
        tickets_resp.append(utils.serialize_ticket_from_model_to_schema(ticket))
    return JSONResponse(jsonable_encoder(tickets_resp))


@router.get('/ticket/{id}', tags=["Ticket"])
def get_ticket_by_id(request: Request, id: int) -> schemas.TicketOutputSchema:
    session = request.state.db
    ticket = utils.get_ticket_from_db(session, id)
    if ticket is None:
        return utils.GENERIC_404_RESPONSE
    ticket_resp = utils.serialize_ticket_from_model_to_schema(ticket)
    return JSONResponse(jsonable_encoder(ticket_resp))


@router.post('/ticket',tags=["Ticket"])
def post_ticket(request: Request, ticket_req: schemas.TicketInputSchema) -> schemas.TicketOutputSchema:
    session = request.state.db
    ticket = utils.serialize_ticket_schema_to_model(ticket_req)
    ticket = utils.create_ticket_into_db(session, ticket)
    ticket_resp = utils.serialize_ticket_from_model_to_schema(ticket)
    return JSONResponse(jsonable_encoder(ticket_resp))


@router.patch('/ticket/{id}', tags=["Ticket"])
def patch_ticket(request: Request, id: int, ticket_update_req: schemas.TicketInputSchema) -> schemas.TicketOutputSchema:
    session = request.state.db
    result = utils.update_ticket_from_db(session, id, ticket_update_req)
    if result == None:
         return utils.GENERIC_404_RESPONSE
    ticket_resp = utils.serialize_ticket_from_model_to_schema(result)
    return JSONResponse(jsonable_encoder(ticket_resp))
        

# TODO PUT
@router.delete('/ticket/{id}', tags=["Ticket"])
def delete_ticket_by_id(request: Request, id: int): 
    session = request.state.db
    result = utils.delete_ticket_from_db(session, id)
    if result == None:  
            return utils.GENERIC_404_RESPONSE
    return JSONResponse(jsonable_encoder({'id':id}))


@router.get('/ticket/{id}/comment/all', tags=["Comment"])
def get_comments_by_ticket_id(request: Request, id: int) -> list[schemas.CommentOutputSchema]:
    session = request.state.db
    comments = utils.get_comments_by_ticket_id_from_db(session, id)
    ticket = utils.get_ticket_from_db(session, id)
    if ticket == None:  
            return utils.GENERIC_404_RESPONSE
    comments_resp = []
    for comment in comments:
        comments_resp.append(utils.serialize_comment_from_model_to_schema(comment))
    return JSONResponse(jsonable_encoder(comments_resp))


@router.post('/ticket/{id}/comment/all', status_code=201,  tags=["Comment"])
def post_comment_by_ticket_id(request: Request, id: int, comment_req: schemas.CommentInputSchema):
    session = request.state.db
    comments = utils.serialize_comment_schema_to_model(comment_req)
    ticket = utils.get_ticket_from_db(session, id)
    if ticket == None:
        return utils.GENERIC_404_RESPONSE
    comments = utils.create_comment_by_ticket_id_into_db(session, id, comment_req)
    comments_resp = utils.serialize_comment_from_model_to_schema(comments)
    return JSONResponse(jsonable_encoder(comments_resp))    
    
         
@router.get('/ticket/{id}/comment/{comment_id}', tags=["Comment"])
def get_comment_by_ticket_id(request: Request, id: int, comment_id: int) -> schemas.CommentOutputSchema:
    session = request.state.db
    comment = utils.get_comment_by_ticket_id_from_db(session, id, comment_id)
    ticket = utils.get_ticket_from_db(session, id)
    if ticket == None or comment == None:  
            return utils.GENERIC_404_RESPONSE
    comment_resp = utils.serialize_comment_from_model_to_schema(comment)
    return JSONResponse(jsonable_encoder(comment_resp))


@router.delete('/ticket/{id}/comment/{comment_id}', tags=["Comment"])
def delete_comment_by_ticket_id(request: Request, id: int, comment_id: int):
    session = request.state.db
    comment = utils.delete_comment_by_ticket_id_from_db(session, id, comment_id)
    ticket = utils.get_ticket_from_db(session, id)
    if comment == None or ticket == None:
         return utils.GENERIC_404_RESPONSE
    return JSONResponse(jsonable_encoder({'ticket_id': id, "comment_id": comment_id}))
    


@router.patch('/ticket/{id}/comment/{comment_id}', tags=["Comment"])
def patch_comment_by_ticket_id(request: Request, id: int, comment_id: int, comment_req: schemas.CommentInputSchema):
    session = request.state.db
    comment = utils.serialize_comment_schema_to_model(comment_req)
    comment = utils.update_comment_by_ticket_id_from_db(session, id, comment_id, comment_req)
    ticket = utils.get_ticket_from_db(session, id)
    if comment == None or ticket == None:
        return utils.GENERIC_404_RESPONSE
    comment_resp = utils.serialize_comment_from_model_to_schema(comment)
    return JSONResponse(jsonable_encoder(comment_resp))



@router.get('/user/all', tags=["User"])
def get_user_all(request: Request) -> list[schemas.UserOutputSchema]:
    session = request.state.db
    users = utils.get_users_from_db(session)
    users_resp = []
    for user in users:
        users_resp.append(utils.serialize_user_schema_to_model(user))
    return JSONResponse(jsonable_encoder(users_resp))


@router.get('/user/{email}', tags=["User"])
def get_user_by_id(request: Request, email: str) -> schemas.UserOutputSchema:
    session = request.state.db
    user = utils.get_user_from_db(session, email)
    if user == None:
         return utils.GENERIC_404_RESPONSE
    user_resp = utils.serialize_user_schema_to_model(user)
    return JSONResponse(jsonable_encoder(user_resp))    


@router.post('/register', status_code=201, tags=["User"])
def register(request: Request, user_req: schemas.UserInputSchema):
    session = request.state.db   
    user = utils.serialize_user_schema_to_model(user_req)
    try:
        user = utils.post_create_user(session, user_req)
    except exc.IntegrityError:
        raise HTTPException(status_code=400, detail='пользователь с таким логином уже существует')
    user_resp = utils.serialize_user_from_model_to_schema(user)
    return JSONResponse(jsonable_encoder(user_resp))



@router.post('/login', tags=["Auth"])
def login(request: Request, user_req: schemas.UserAuthSchema):
    session = request.state.db   
    user = utils.serialize_user_auth_schema_to_model(user_req)
    user = utils.user_login(session, user_req)
    if user.email == user_req.email and auth_handler.verify_password(user_req.hash, user.hash):
        token = auth_handler.encode_token(user.email)
        return JSONResponse(jsonable_encoder({'token': token }))
    raise HTTPException(status_code=401, detail='Неверный пароль и/или логин ')


@router.get('/testendpoint', tags=["Test"])
def protected(username=Depends(auth_handler.auth_wrapper)):
    return JSONResponse(jsonable_encoder({'вход': username }))