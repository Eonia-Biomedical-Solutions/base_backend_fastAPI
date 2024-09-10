from pydantic import EmailStr

from core.base import BaseSchema


class EmailSchema(BaseSchema):
    email: EmailStr
    asunto: str
    tarea: str
    token: str
