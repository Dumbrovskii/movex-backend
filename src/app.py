from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI
from src.api.v1.auth import router as auth_router
from src.api.v1.rides import router as rides_router
from src.api.exception_handlers import register_auth_exception_handlers
from fastapi.middleware.cors import CORSMiddleware
from src.config.settings import settings


@asynccontextmanager
async def lifespan(application: FastAPI):
    application.state.http_client = httpx.AsyncClient()

    yield

    await application.state.http_client.aclose()


app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    lifespan=lifespan,
)

register_auth_exception_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=settings.ALLOW_CREDENTIALS,
    allow_methods=settings.ALLOW_METHODS,
    allow_headers=settings.ALLOW_HEADERS,
)

app.include_router(
    auth_router,
    prefix=settings.ROUTER_PREFIX,
)

app.include_router(
    rides_router,
    prefix=settings.ROUTER_PREFIX,
)

@app.get('/')
async def root():
    return {"message": f"{settings.TITLE} is running"}
