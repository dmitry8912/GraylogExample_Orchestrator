from fastapi import APIRouter
from starlette.requests import Request
from app.logging.graylog import logger
from app.amqp.service_request import ServiceHandler
router = APIRouter()


@router.get("/")
async def process_request(request: Request):
    logger.info("Request started")
    async for r in ServiceHandler.call_service('service_1'):
        logger.debug(f"Received {r}")
        logger.info("Sending response")
        return r
