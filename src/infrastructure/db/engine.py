from sqlalchemy.ext.asyncio import create_async_engine

from src.config.database import database

engine = create_async_engine(
    database.url,
    echo=False,
)