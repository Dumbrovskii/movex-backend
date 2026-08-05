from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

settings = Setting()