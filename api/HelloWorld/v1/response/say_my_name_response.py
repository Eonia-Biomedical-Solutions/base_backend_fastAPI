from uuid import uuid4
from pydantic import Field

from core.base import BaseSchema


class SayNameResponse(BaseSchema):
    id: str = Field(default_factory=lambda: str(uuid4()))
    msg: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status_code": 200,
                    "errors": {},
                    "messages": [
                        ""
                    ],
                    "data": {
                        "id": str(uuid4()),
                        "msg": "Hello Alan"
                    }
                }
            ]
        }
    }

