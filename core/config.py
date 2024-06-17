import os

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ENV: str = "local"
    DEBUG: bool = True
    APP_HOST: str = "localhost"
    APP_PORT: int = 8080
    JWT_SECRET_KEY: str = "fastapi"
    JWT_ALGORITHM: str = "HS256"


class DevelopmentConfig(Config):
    DB_URL: str = f"sqlite:///test.db"


class LocalConfig(Config):
    DB_URL: str = f"sqlite:///test.db"


# TODO: change url for postgrest driver
class ProductionConfig(Config):
    DEBUG: bool = False
    DB_URL: str = f"sqlite:///test.db"


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "development": DevelopmentConfig(),
        "local": LocalConfig(),
        "production": ProductionConfig(),
    }
    return config_type[env]


config = get_config()
