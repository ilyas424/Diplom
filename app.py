import sys
import traceback

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

import settings
from settings import logger
from settings import feed_logger
from routes import router as router_app
from db import SessionLocal
from fastapi.middleware.cors import CORSMiddleware


logger.info(f"FastAPI application creating")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


logger.info("FastAPI general exception handler setup")
@app.exception_handler(Exception)
async def fastapi_general_exception_handler(request: Request, exc: Exception):
    logger.error("FastAPI general exception handler caught exception!")
    exc_info = traceback.format_exc()
    logger.error(exc_info)
    logger.error("An unexpected error occured during request: {0}".format(str(exc_info)))
    # TODO try to get all info from exc object, not traceback module
    feed_logger.error(repr(exc_info)[1:-1].replace('"',r'\"'))
    return Response(status_code=500)


logger.info("Middleware 'http' setup")
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        logger.info("New connection")
        request.state.db = SessionLocal()
        response = await call_next(request)
    except Exception as e:
        logger.error("Session middleware caught exception!")
        logger.error("An unexpected error occured during request: {0}".format(str(e)))
        exc_info = traceback.format_exc()
        logger.error(exc_info)
        feed_logger.error(repr(exc_info)[1:-1].replace('"',r'\"'))
        return Response(status_code=500)
    finally:
        request.state.db.close()
    return response


logger.info("Include routes")
app.include_router(router_app)


