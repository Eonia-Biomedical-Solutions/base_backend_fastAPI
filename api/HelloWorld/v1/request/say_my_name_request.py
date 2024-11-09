import datetime
from uuid import uuid4
from pydantic import Field

from typing import Optional

from core.base import BaseSchema


class SayNameRequest(BaseSchema):
    id: str= Field(
        default_factory=lambda: str(uuid4())

    )
    name: str
    petition_at: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Alan",
                }
            ]
        }
    }
