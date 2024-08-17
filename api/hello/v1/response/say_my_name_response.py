import datetime
from uuid import uuid4
from pydantic import Field

from core.base import BaseSchema


class SayNameResponse(BaseSchema):
    id: str = Field(default_factory=lambda: str(uuid4()))
    msg: str
