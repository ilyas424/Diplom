import os
import sys
import logging
from logging.config import fileConfig
import functools


LOGGER_CONFIG_FILE = 'logging.ini'
logging.config.fileConfig(LOGGER_CONFIG_FILE, disable_existing_loggers=False)
logger = logging.getLogger('cedar')
feed_logger = logging.getLogger('feed')


# CEDAR_DB_HOST = os.environ["CEDAR_DB_HOST"]
# CEDAR_DB_NAME = os.environ["CEDAR_DB_NAME"]
# CEDAR_DB_USER_NAME = os.environ["CEDAR_DB_USER_NAME"]
# CEDAR_DB_USER_PASSWORD = os.environ["CEDAR_DB_USER_PASSWORD"]

CEDAR_DB_HOST="127.0.0.1"
CEDAR_DB_NAME="JIRA"
CEDAR_DB_USER_NAME="postgres"
CEDAR_DB_USER_PASSWORD="ilyas13!A"


TELEGRAM_TOKEN_TOKEN = '6213725379:AAE42uYg72tcPFFpuuY0m8A4bGWy7H0gakI'
support_ids = ['415817424']

Secret = '455622bc59d800ad8b78e4f74483015ad20d4166823780bee0565e0e43e4805d'