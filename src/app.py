from fastapi import FastAPI
from src.api.v1.auth import router as auth_rout
from src.api.exception_handlers import register_auth_exception_handlers
from fastapi.middleware.cors import CORSMiddleware
from src.config.settings import settings

app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
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
    auth_rout,
    prefix=settings.ROUTER_PREFIX
)

@app.get('/')
async def root():
    return {"message": f"{settings.TITLE} is running"}