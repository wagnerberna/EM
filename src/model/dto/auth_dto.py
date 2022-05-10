from pydantic import BaseModel, validator
from src.static.message import *


class AuthDto(BaseModel):
    login: str
    password: str

    @validator("*")
    def field_not_empty(cls, field):
        if field == "":
            raise ValueError(FIELD_NOT_BLANK.format(field))
        return field


class AuthDtoGet(BaseModel):
    login: str
    password: str
    activated: bool
