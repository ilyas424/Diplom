import logging

from fastapi import status
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from starlette.requests import Request

import utils
from models import User
from models import Ticket
from models import TicketType
from models import TicketStatus
from models import TicketComment
from models import TicketPriority
from schema import UserSchema
from schema import TicketSchema
from schema import TicketTypeSchema
from schema import TicketStatusSchema
from schema import TicketCommentSchema
from schema import TicketPrioritySchema

import settings


router = APIRouter()

@router.get("/ticket/priorities")
async def get_ticket_priority_all(request: Request): # -> list[TicketPrioritySchema]:
    result = {}
    session = request.state.db
    result = utils.get_ticket_priorities_from_db(session)
    return result


# @router.get("/ticket/status/all")
# def get_ticket_status_all(request: Request):
#     result = {}
#     session = request.state.db
#     result = utils.get_ticket_statuses_from_db(session)
#     return result


# @router.get('/ticket/type/all')
# def get_ticket_type_all(request: Request):
#     result = {}
#     session = request.state.db
#     result = utils.get_ticket_types_from_db(session)
#     return result


# @router.get('/ticket/all')
# def get_ticket_all(request: Request):
#     result = []
#     session = request.state.db
#     tickets = utils.get_tickets_from_db(session)
#     for ticket in tickets:
#         result.append(utils.convert_ticket_object_to_json(ticket))
#     return result


# @router.post('/ticket')
# def post_ticket(request: Request, ticket_json: TicketCreate):
#     result = {}
#     session = request.state.db
#     result = utils.create_ticket_into_db(session, ticket_json)
#     if result == None:
#          return JSONResponse(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 content = utils.Response_json_400()
#         )
#     else:     
#         return result


# @router.patch('/ticket/{id}')
# def patch_ticket(request: Request, id: int, update_ticket_json: UpdateTicket):
#     result = {}
#     session = request.state.db
#     try:
#         result = utils.update_ticket_from_db(session, id, update_ticket_json)
#         if result == None:
#             return JSONResponse(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 content = utils.Response_json_404()
#         )
#         else:
#              return "Тикет изменен"
#     except :
#          return JSONResponse(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 content = utils.Response_json_400()
#         )
         
    


# @router.get('/ticket/{id}')
# def get_ticket_by_id(request: Request, id: int):
#     result = {}
#     session = request.state.db
#     ticket = utils.get_ticket_from_db(session, id)
#     if ticket == None:  
#             return JSONResponse(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 content = utils.Response_json_404()
#         )
#     else:
#         result = utils.convert_ticket_object_to_json(ticket)
#     return result


# @router.delete('/ticket/{id}')
# def delete_ticket_by_id(request: Request, id: int):
#     result = {}
#     session = request.state.db
#     result = utils.delete_ticket_from_db(session, id)
#     if result == None:  
#             return JSONResponse(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 content = utils.Response_json_404()
#         )
#     else:
#         return "Тикет успешно удален"
    


# @router.get('/ticket/{id}/comment/all')
# def get_comments_by_ticket_id(request: Request, id: int):
#     result = []
#     session = request.state.db
#     comments = utils.get_comments_by_ticket_id_from_db(session, id)
#     if comments == []:  
#             return JSONResponse(
#                 status_code=status.HTTP_404_NOT_FOUND, 
#                 content = utils.Response_json_404()
#         )
#     else:
#         for comment in comments:
#             result.append(utils.convert_comment_object_to_json(comment))
#     return result


# @router.post('/ticket/{id}/comment/all')
# def post_comment_by_ticket_id(request: Request, id: int, item: CreateComment):
#     result = {}
#     session = request.state.db
#     try:
#         result = utils.create_comment_by_ticket_id_into_db(session, id, item)
#         if result == None:
#              return JSONResponse(
#                 status_code=status.HTTP_404_NOT_FOUND, 
#                 content = utils.Response_json_404()
#         )
#         else:
#              return "Тикет добавлен"
#     except:
#          return JSONResponse(
#                 status_code=status.HTTP_400_BAD_REQUEST, 
#                 content = utils.Response_json_400()
#         )
         
         


# @router.get('/ticket/{id}/comment/{comment_id}')
# def get_comment_by_ticket_id(request: Request, id: int, comment_id: int):
#     result = {}
#     session = request.state.db
#     comment = (utils.get_comment_by_ticket_id_from_db(session, id, comment_id))
#     if comment == None:  
#             return JSONResponse(
#                 status_code=status.HTTP_404_NOT_FOUND, 
#                 content = utils.Response_json_404()
#         )
#     else:
#          result = utils.convert_comment_object_to_json(comment)
#     return result
   



# @router.delete('/ticket/{id}/comment/{comment_id}')
# def get_comment_by_ticket_id(request: Request, id: int, comment_id: int):
#     result = {}
#     session = request.state.db
#     result = utils.delete_comment_by_ticket_id_from_db(session, id,comment_id)
#     return result


# @router.patch('/ticket/{id}/comment/{comment_id}')
# def patch_comment_by_ticket_id(request: Request, id: int, comment_id: int, item: CommentText):
#     result = {}
#     session = request.state.db
#     try:
#         result = utils.update_comment_by_ticket_id_from_db(session, id,comment_id, item)
#         if result is None:
#             return JSONResponse(
#                 status_code=status.HTTP_404_NOT_FOUND, 
#                 content = utils.Response_json_404()
#         )
#         return "коментарий изменен"
#     except:
#          return JSONResponse(
#                 status_code=status.HTTP_400_BAD_REQUEST, 
#                 content = utils.Response_json_400()
#         )
         
    


# @router.get('/user/all')
# def get_user_all(request: Request):
#     result = {}
#     session = request.state.db
#     result = utils.get_users_from_db(session)
#     return result


# @router.get('/user/{id}')
# def get_user_by_id(request: Request, id: int):
#     result = {}
#     session = request.state.db
#     result = utils.get_user_from_db(session, id)
#     if result == []:
#          return JSONResponse(
#                 status_code=status.HTTP_404_NOT_FOUND, 
#                 content = utils.Response_json_404()
#         )
#     return result
