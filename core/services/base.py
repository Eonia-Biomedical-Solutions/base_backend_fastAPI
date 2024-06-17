from typing import (Any,
                    List,
                    Sequence)

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import Executable


__all__ = [
    'SessionMixin',
    'BaseService',
    'BaseDataManager'
]


class SessionMixin:

    def __init__(self, session: Session) -> None:
        self.session = session


class BaseService(SessionMixin):
    ...


class BaseDataManager(SessionMixin):

    def add_one(self, model: Any) -> None:
        self.session.add(model)

    def delete_one(self, model: Any) -> None:
        self.session.delete(model)

    def add_all(self, models: Sequence[Any]) -> None:
        self.session.add_all(models)

    def get_one(self, select_stmt: Executable) -> Any:
        return self.session.scalar(select_stmt)

    def get_all(self, select_stmt: Executable) -> List[Any]:
        return list(self.session.scalars(select_stmt).all())
