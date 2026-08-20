from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    #APP
    TITLE: str
    VERSION: str
    ALLOW_ORIGINS: List[str]
    ALLOW_CREDENTIALS: bool
    ALLOW_METHODS: List[str]
    ALLOW_HEADERS: List[str]
    ROUTER_PREFIX: str


    # PostgreSQL
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    # Redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB_NAME: int

    # JWT
    JWT_SECRET: str
    JWT_ALGORITHM: str

    # Auth
    VERIFICATION_CODE_LENGTH: int
    VERIFICATION_CODE_TTL_SECONDS: int
    MAX_VERIFICATION_ATTEMPTS: int

    ACCESS_TOKEN_TTL_MINUTES: int
    REFRESH_TOKEN_TTL_DAYS: int

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

settings = Settings()