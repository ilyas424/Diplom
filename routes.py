from fastapi import Depends
from fastapi import APIRouter
from fastapi import Response
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
from sqlalchemy import exc
from starlette.requests import Request

import utils
import schemas
from settings import logger
from settings import feed_logger
from utils import AuthHandler



logger.info("APIRouter creating")
auth_handler = AuthHandler()
router = APIRouter()



@router.get("/")
def home():
    return "Hello, World!"


@router.get("/ticket/priorities", tags=["Priority"])
async def get_ticket_priorities(request: Request) -> list[str]:
    session = request.state.db
    priorities = utils.get_ticket_priorities_from_db(session)
    priorities_resp = [priority.title for priority in priorities]
    return JSONResponse(jsonable_encoder(priorities_resp))


@router.get('/ticket/types', tags=["Type"])
def get_ticket_type_all(request: Request) -> list[str]:
    session = request.state.db
    types = utils.get_ticket_types_from_db(session)
    types_resp = [type.title for type in types]
    return JSONResponse(jsonable_encoder(types_resp))


@router.get('/ticket/all', tags=["Ticket"])
def get_ticket_all(request: Request, useremail=Depends(auth_handler.auth_wrapper)) -> list[schemas.TicketOutputSchema]:
    session = request.state.db
    tickets = utils.get_tickets_from_db(session)
    tickets_resp = []
    for ticket in tickets:
        tickets_resp.append(utils.serialize_ticket_from_model_to_schema(ticket))
    return JSONResponse(jsonable_encoder(tickets_resp))


@router.get('/ticket/backlog', tags=["Ticket"])
def get_ticket_all(request: Request, useremail=Depends(auth_handler.auth_wrapper)) -> list[schemas.TicketOutputSchema]:
    session = request.state.db
    tickets = utils.get_tickets_in_backlog_from_db(session)
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
def patch_ticket(request: Request, id: int, ticket_update_req: schemas.TicketInputSchema, useremail=Depends(auth_handler.auth_wrapper)) -> schemas.TicketOutputSchema:
    session = request.state.db
    if utils.verify_role(session, useremail) or utils.verify_email_from_ticket(session, useremail, id):
        result = utils.update_ticket_from_db(session, id, ticket_update_req)
        if result == None:
            return utils.GENERIC_404_RESPONSE
        ticket_resp = utils.serialize_ticket_from_model_to_schema(result)
        return JSONResponse(jsonable_encoder(ticket_resp))
    else:
        raise HTTPException(status_code=403, detail='Недостаточно прав доступа')
        

# TODO PUT
@router.delete('/ticket/{id}', tags=["Ticket"])
def delete_ticket_by_id(request: Request, id: int, useremail=Depends(auth_handler.auth_wrapper)): 
    session = request.state.db
    if utils.verify_role(session, useremail) or utils.verify_email_from_ticket(session, useremail, id):
        result = utils.delete_ticket_from_db(session, id)
        if result == None:  
            return utils.GENERIC_404_RESPONSE
        return JSONResponse(jsonable_encoder({'id':id}))
    else:
        raise HTTPException(status_code=403, detail='Недостаточно прав доступа')
    


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
def delete_comment_by_ticket_id(request: Request, id: int, comment_id: int, useremail=Depends(auth_handler.auth_wrapper)):
    session = request.state.db
    ticket = utils.get_ticket_from_db(session, id)
    comment_chek = utils.get_comment_by_ticket_id_from_db(session, id, comment_id)
    if utils.verify_role(session, useremail) or utils.verify_email_from_comment(session, useremail, comment_id):
        comment = utils.delete_comment_by_ticket_id_from_db(session, id, comment_id)
        if comment == None or ticket == None:
            return utils.GENERIC_404_RESPONSE
        return JSONResponse(jsonable_encoder({'ticket_id': id, "comment_id": comment_id}))
    if comment_chek == None or ticket == None:
        return utils.GENERIC_404_RESPONSE
    raise HTTPException(status_code=403, detail='Недостаточно прав доступа')
    
    

@router.patch('/ticket/{id}/comment/{comment_id}', tags=["Comment"])
def patch_comment_by_ticket_id(request: Request, id: int, comment_id: int, comment_req: schemas.CommentUpdateSchema, useremail=Depends(auth_handler.auth_wrapper)):
    session = request.state.db
    ticket = utils.get_ticket_from_db(session, id)
    comment_chek = utils.get_comment_by_ticket_id_from_db(session, id, comment_id)
    comment = utils.serialize_comment_schema_to_model(comment_req)
    if utils.verify_role(session, useremail) or utils.verify_email_from_comment(session, useremail, comment_id):
        comment = utils.update_comment_by_ticket_id_from_db(session, id, comment_id, comment_req)
        if comment == None or ticket == None:
            return utils.GENERIC_404_RESPONSE
        comment_resp = utils.serialize_comment_from_model_to_schema(comment)
        return JSONResponse(jsonable_encoder(comment_resp))
    if comment_chek == None or ticket == None:
        return utils.GENERIC_404_RESPONSE
    raise HTTPException(status_code=403, detail='Недостаточно прав доступа')


@router.get('/board/all', tags=["Board"])
def get_boards(request: Request) -> list[schemas.BoardOutputSchema]:
    session = request.state.db
    boards = utils.get_boards_from_db(session)
    boards_resp = []
    for board in boards:
        boards_resp.append(utils.serialize_board_from_model_to_schema(board))
    return JSONResponse(jsonable_encoder(boards_resp))


@router.get('/board/{id}', tags=["Board"])
def get_board_by_id(request: Request, id: int):
    session = request.state.db
    board = utils.get_board_from_db(session, id)
    tickets = utils.get_tickets_from_db_by_board_id(session,id)       
    if board == None:
        return utils.GENERIC_404_RESPONSE
    board_resp = utils.all_info_board_from_model_to_schema(board, tickets)
    return JSONResponse(jsonable_encoder(board_resp))


@router.post('/board', tags=["Board"])
def post_board(request: Request, user_req: schemas.BoardInputSchema):
    session = request.state.db
    board = utils.serialize_board_schema_to_model(user_req)
    board = utils.post_create_board(session, board)
    board_resp = utils.serialize_board_from_model_to_schema(board)
    return JSONResponse(jsonable_encoder(board_resp))


@router.patch('/board/{id}', tags=["Board"])
def update_board(request: Request, id: int, useremail=Depends(auth_handler.auth_wrapper)):
    session = request.state.db
    chek_board = utils.get_board_from_db(session, id)
    if chek_board == None:
        return utils.GENERIC_404_RESPONSE
    if utils.verify_role(session, useremail) or utils.verify_email_from_board(session, useremail, id):
        board = utils.update_board_from_db(session, id)
        if board == None:
            return utils.GENERIC_404_RESPONSE
        board_resp = utils.serialize_board_from_model_to_schema(board)
        return JSONResponse(jsonable_encoder(board_resp))
    raise HTTPException(status_code=403, detail='Недостаточно прав доступа')


@router.delete('/board/{id}', tags=["Board"])
def delete_board(request: Request, id: int, useremail=Depends(auth_handler.auth_wrapper)):
    session = request.state.db
    chek_board = utils.get_board_from_db(session, id)
    if chek_board == None:
        return utils.GENERIC_404_RESPONSE
    if utils.verify_role(session, useremail) or utils.verify_email_from_board(session, useremail, id):
        board = utils.delete_board_from_db(session, id)
        if board == None:
            return utils.GENERIC_404_RESPONSE
        board_resp = {'board_id': id}
        return JSONResponse(jsonable_encoder(board_resp))
    raise HTTPException(status_code=403, detail='Недостаточно прав доступа')




@router.delete('/user/{email}', tags=["User"])
def delete_user(request: Request, email: str, useremail=Depends(auth_handler.auth_wrapper)):
    session = request.state.db
    chek_user = utils.get_user_from_db(session, email)
    if chek_user == None:
        return utils.GENERIC_404_RESPONSE
    if utils.verify_role(session, useremail):
        user = utils.delete_user_from_db(session, email)
        if user == None:
            return utils.GENERIC_404_RESPONSE
        user_resp = {'user': email}
        return JSONResponse(jsonable_encoder(user_resp))
    raise HTTPException(status_code=403, detail='Недостаточно прав доступа')


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
    user = utils.serialize_user_schema_to_model_input(user_req)
    try:
        user = utils.post_create_user(session, user_req)
    except exc.IntegrityError:
        raise HTTPException(status_code=400, detail='пользователь с таким логином уже существует')
    user_resp = utils.serialize_user_auth_schema_to_model(user)
    return JSONResponse(jsonable_encoder(user_resp))



@router.post('/login', tags=["Auth"])
def create_user(request: Request, user_req: schemas.UserAuthSchema):
    session = request.state.db   
    user = utils.serialize_user_auth_schema_to_model(user_req)
    user = utils.user_login(session, user_req)
    if user.email == user_req.email and auth_handler.verify_password(user_req.hash, user.hash) :
        token = auth_handler.encode_token(user.email)
        return JSONResponse(jsonable_encoder({'token': token }))
    raise HTTPException(status_code=400, detail='Неверный пароль и/или логин ')



@router.post('/role', tags=["User"])
def role_modification(request: Request, user_req: schemas.UserEmailSchema , useremail=Depends(auth_handler.auth_wrapper)):
     session = request.state.db
     if utils.verify_role(session, useremail):
         result = utils.update_user_role_from_db(session, user_req)
         if result == None:
            return utils.GENERIC_400_RESPONSE
         return JSONResponse(jsonable_encoder(result.email))
     else:              
        raise HTTPException(status_code=403, detail='Недостаточно прав доступа')



@router.get('/testendpoint', tags=["Test"])
def protected(useremail=Depends(auth_handler.auth_wrapper)):
    return JSONResponse(jsonable_encoder({'вход': useremail }))