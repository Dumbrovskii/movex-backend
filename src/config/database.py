from pydantic_settings import BaseSettings, SettingsConfigDict

class DatabaseSettings(BaseSettings):
    host: str
    port: str
    db_name: str
    user: str
    password: str

    model_config = SettingsConfigDict(
        env_prefix="POSTGRES_",
        env_file=".env",
        extra="ignore",
    )

    @property
    def url(self) -> str:
        return (
            f"postgresql+psycopg://"
            f"{self.user}:{self.password}@"
            f"{self.host}:{self.port}/{self.db_name}"
        )


database = DatabaseSettings()
