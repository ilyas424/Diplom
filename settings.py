import os
import sys
import logging
from logging.config import fileConfig
import functools


LOGGER_CONFIG_FILE = 'logging.ini'
logging.config.fileConfig(LOGGER_CONFIG_FILE, disable_existing_loggers=False)
logger = logging.getLogger('cedar')
feed_logger = logging.getLogger('feed')


CEDAR_DB_HOST = os.environ["CEDAR_DB_HOST"]
CEDAR_DB_NAME = os.environ["CEDAR_DB_NAME"]
CEDAR_DB_USER_NAME = os.environ["CEDAR_DB_USER_NAME"]
CEDAR_DB_USER_PASSWORD = os.environ["CEDAR_DB_USER_PASSWORD"]
