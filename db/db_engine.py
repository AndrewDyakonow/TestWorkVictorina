from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine, Engine

from settings import PATH_DB_SETTINGS


class Settings(BaseSettings):

    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST_AUTH_METHOD: str
    DB_HOST: str
    DB_PORT: int

    @property
    def create_engine(self) -> Engine:
        engine = create_engine(
            f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.DB_HOST}"
            f":{self.DB_PORT}/{self.POSTGRES_DB}",
            echo=False,
        )

        return engine

    model_config = SettingsConfigDict(env_file=PATH_DB_SETTINGS)


settings = Settings()
