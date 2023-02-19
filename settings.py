import os
import logging
from logging.config import fileConfig
import functools


LOGGER_CONFIG_FILE = 'logging.ini'
logging.config.fileConfig(LOGGER_CONFIG_FILE) #, disable_existing_loggers=True)
logger = logging.getLogger('app')

# def escaper(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwrags):
#         message = args[0]
#         message = message.replace('"', r'\"')
#         return func(message)

#         # message, etc_args = args[0], args[1:]
#         # message = args[0].replace('"', r'\"')
#         # return func(message, *etc_args, **kwrags)
#     return wrapper

# logging.debug = escaper(logging.debug)
# logging.info = escaper(logging.info)
# logging.warning = escaper(logging.warning)
# logging.error = escaper(logging.error)
# logging.critical = escaper(logging.critical)
# logging.exception = escaper(logging.exception)


# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="app.log",
#     filemode="a",
#     format="%(asctime)s %(levelname)s %(message)s"
# )

DB_HOST = os.environ["DB_HOST"]
DB_NAME = os.environ["DB_NAME"]
DB_USER_NAME = os.environ["DB_USER_NAME"]
DB_USER_PASSWORD = os.environ["DB_USER_PASSWORD"]
