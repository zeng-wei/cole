import logging
from pythonjsonlogger import jsonlogger
import datetime
import socket
import os


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    # def parse(self):
    #     return self._fmt.split(';')
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            # this doesn't use record.created, so it is slightly off
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname
        host_name = socket.gethostname()
        ip = socket.gethostbyname(host_name)
        log_record['host'] = host_name
        log_record['ip'] = ip
        log_record['process'] = os.getpid()


def init_logging():
    import getopt
    import sys
    file_name = None
    try:
        opts = getopt.getopt(sys.argv[1:], 'f:')[0]  # -f 日志文件名称
        file_name, symbols_range = None, None
        for o in opts:
            if o[0] == '-f':
                file_name = o[1]
    except IndexError:
        pass
    logger = logging.getLogger('')
    logger.setLevel(logging.INFO)
    local_log_format = '%(asctime)s %(levelname)s %(message)s'
    if file_name:
        if logger.handlers:
            return
        path = './'
        local_handler = logging.FileHandler('{}{:%Y-%m}.log'.format(path+'local_'+file_name, datetime.datetime.now()))
        local_handler.setLevel(logging.WARNING)
        local_handler.setFormatter(logging.Formatter(local_log_format))
        logger.addHandler(local_handler)
        f = '(message) (timestamp) (level) (host) (process) (market)'
        elk_formatter = CustomJsonFormatter(f)
        handler = logging.FileHandler('{}{:%Y-%m}.log'.format(path+file_name, datetime.datetime.now()))
        handler.setLevel(logging.INFO)
        handler.setFormatter(elk_formatter)
        logger.addHandler(handler)
        # logging.Logger = logger
        logging.warning('??')
    else:
        logging.basicConfig(
            level=logging.INFO,
            format=local_log_format
        )

init_logging()