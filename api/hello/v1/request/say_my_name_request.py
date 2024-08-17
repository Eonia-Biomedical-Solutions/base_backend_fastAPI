import datetime
from uuid import uuid4
from pydantic import Field

from core.base import BaseSchema


class SayNameRequest(BaseSchema):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    petition_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc))
