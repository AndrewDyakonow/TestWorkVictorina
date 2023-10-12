from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine


class Settings(BaseSettings):

    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST_AUTH_METHOD: str
    DB_HOST: str
    DB_PORT: int

    @property
    def create_engine(self):
        engine = create_engine(
            f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.DB_HOST}"
            f":{self.DB_PORT}/{self.POSTGRES_DB}",
            echo=True,
        )
        return engine

    model_config = SettingsConfigDict(env_file='connect_db.env')


settings = Settings()
