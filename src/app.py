from fastapi import FastAPI
from src.api.v1.auth import router as auth_rout


app = FastAPI(
    title="MoveX API",
    version="1.0.0",
)

app.include_router(
    auth_rout,
    prefix="/api/v1"
)

@app.get('/')
async def root():
    return {"message": "MoveX API is running"}