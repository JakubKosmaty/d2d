from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    DB_NAME: str
    DB_ECHO: bool
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str

    class Config:
        env_file = ".env"


settings = Settings()