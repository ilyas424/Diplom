from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

import settings
from settings import logger
import routes
from db import SessionLocal


logger.info(f"{'='*10} FastAPI application creating {'='*10}")
app = FastAPI()
logger.info("FastAPI application created")

logger.info("'http' middlware setup")
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        logger.info("New connection")
        request.state.db = SessionLocal()
        response = await call_next(request)
    except Exception as e:
        import traceback
        exc = traceback.format_exc()
        logger.error(
            repr(exc)[1:-1].replace('"',r'\"')
        )
        pass
    finally:
        request.state.db.close()
    return response

logger.info("include routes")
app.include_router(routes.router)
