from src.config import settings

class Database:
    @property
    def url(self) -> str:
        return (
            f"postgresql+psycopg://"
            f"{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@"
            f"{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/"
            f"{settings.POSTGRES_DB_NAME}"
        )

database = Database()
