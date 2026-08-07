from sqlalchemy import create_engine

from src.config.database import database

engine = create_engine(
    database.sync_url,
    echo=False,
)