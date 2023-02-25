from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings


SQLALCHEMY_DATABASE_URL = f"""\
postgresql://\
{settings.CEDAR_DB_USER_NAME}:{settings.CEDAR_DB_USER_PASSWORD}@\
{settings.CEDAR_DB_HOST}/{settings.CEDAR_DB_NAME}\
"""

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
