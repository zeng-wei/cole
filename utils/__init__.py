import logging
from pythonjsonlogger import jsonlogger
import datetime
import socket
import os


class CustomJsonFormatter(jsonlogger.JsonFormatter):
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