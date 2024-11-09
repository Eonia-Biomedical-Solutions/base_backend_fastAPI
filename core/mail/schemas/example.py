from pydantic import EmailStr

from core.base import BaseSchema


class EmailSchema(BaseSchema):
    email: EmailStr
    subject: str
    content: str
    