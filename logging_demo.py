import logging
import logging.config

__version__ = '0.0.1'

logging.config.fileConfig('logging_conf.ini', defaults={'logfilename': 'mylog.log'})
logger = logging.getLogger('custom')

logger.info('test')

try:
    1/0
except ZeroDivisionError:
    logger.exception('')
