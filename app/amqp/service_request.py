from __future__ import annotations

import asyncio
import json
import uuid
from typing import Any, Generator, Tuple

import aio_pika

from app.config import app_config
from app.context import request_id
from app.amqp.base import RabbitMqHandlerBase
from app.logging.graylog import logger


class ServiceHandler(RabbitMqHandlerBase):
    @classmethod
    async def call_service(cls, send_queue_name, payload: Any = None) -> Generator[Any, None, None]:
        data = json.dumps({
            'request_id': request_id.get()
        }).encode('utf-8')
        await cls.basic_send(send_queue_name, data, correlation_id=request_id.get())

        def parse_result(incoming_message: aio_pika.Message) -> Tuple[Any, bool]:
            message = json.loads(incoming_message.body.decode('utf-8'))
            logger.debug(f"New message {message}")
            return message, True

        try:
            async for chunk in cls.basic_receive(request_id.get(), exclusive_queue=True, timeout=60, parser_callback=parse_result, delete_queue=True):
                yield chunk
        except (asyncio.TimeoutError, asyncio.CancelledError):
            pass
