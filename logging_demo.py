import logging
from utils import init_logging

init_logging()

logging.info('err')

try:
    1/0
except ZeroDivisionError:
    logging.exception('')
