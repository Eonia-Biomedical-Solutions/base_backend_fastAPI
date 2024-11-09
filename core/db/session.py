from typing import Iterator
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    Session,
    sessionmaker,
)
from core.db.definitions import SQLModel

from core.settings import settings


__all__ = [
    'Base',
    'create_session',
    'SessionFactory'
]

if settings.DB_DRIVER == 'sqlite':
    _db_url: str = f'{settings.DB_DRIVER}:///{settings.DB_NAME}'
else:
    _db_url: str = f'{settings.DB_DRIVER}://{settings.DB_USR}:{settings.DB_PWD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'

SessionFactory = sessionmaker(
    bind=create_engine(_db_url),
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)


def create_session() -> Iterator[Session]:
    session = SessionFactory()

    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


@contextmanager
def session_scope() -> Iterator[Session]:
    return create_session()


Base = SQLModel()
