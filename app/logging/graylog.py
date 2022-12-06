import logging
from pygelf import GelfTcpHandler
from app.context import request_id
from app.config import app_config


class ContextFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id.get()
        record.service = app_config.service_name
        return True


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("api")
logger.addHandler(GelfTcpHandler(host=app_config.graylog_address, port=app_config.graylog_port, include_extra_fields=True))
logger.addFilter(ContextFilter())
