from fastapi import APIRouter

import ticket
from atribute import test

routes = APIRouter()

routes.include_router(test.router, prefix='/ticket')

