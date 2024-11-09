import os
import dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Config(BaseSettings):
    APP_HOST: str = "localhost"
    APP_PORT: int = 5000


class DevelopmentConfig(Config):
    ENV: str = 'development'
    DEBUG: bool = True
    DB_DRIVER: str = 'sqlite'
    DB_HOST: str = ''
    DB_PORT: str = ''
    DB_NAME: str = 'development.db'
    DB_PWD: str = ''
    DB_USR: str = ''


class ProductionConfig(Config):
    ENV: str = 'production'
    DEBUG: bool = False
    DB_DRIVER: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_PWD: str
    DB_USR: str

    model_config = SettingsConfigDict(env_file=DOTENV)


def get_config():
    dotenv.load_dotenv(dotenv_path=DOTENV)
    env = os.getenv("ENV", 'development')
    config_type = {
        "development": DevelopmentConfig(),
        # "production": ProductionConfig(),
    }

    return config_type[env]


settings = get_config()
