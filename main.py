from fastapi import FastAPI
from app.middleware.middleware import RequestIdMiddleware
from app.routes.api import router as api_router

app = FastAPI()
app.add_middleware(RequestIdMiddleware)
app.include_router(api_router)
