from fastapi import FastAPI
from src.api.v1.auth import router as auth_rout
from src.api.exception_handlers import register_auth_exception_handlers

app = FastAPI(
    title="MoveX API",
    version="1.0.0",
)

register_auth_exception_handlers(app)

app.include_router(
    auth_rout,
    prefix="/api/v1"
)

@app.get('/')
async def root():
    return {"message": "MoveX API is running"}