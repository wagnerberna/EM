from src.static.message import *
from pydantic import BaseModel, validator
from typing import Optional


class UserAddDto(BaseModel):
    name: str
    login: str
    password: str
    activated: Optional[bool] = True

    @validator("*")
    def field_not_empty(cls, field):
        if field == "":
            raise ValueError(FIELD_NOT_BLANK.format(field))
        return field

    @validator("password")
    def password_lenght(cls, value):
        if len(value) < 6:
            raise ValueError(PASSWORD_LENGTH)
        return value


class UserGetDto(BaseModel):
    user_id: int
    name: str
    login: str
    activated: bool
    created_at: str


class UserUpdateStrDto(BaseModel):
    field: str
    value: str

    @validator("*")
    def field_not_empty(cls, fields):
        if fields == "":
            raise ValueError(FIELD_NOT_BLANK.format(fields))
        return fields

    @validator("field")
    def field_list(cls, value):
        fields_list = [
            "name",
            "login",
            "password",
        ]
        if value not in fields_list:
            raise ValueError(FIELD_INVALID.format(fields_list))
        return value


class UserUpdateStatusDto(BaseModel):
    login: str
    status: bool

    @validator("*")
    def field_not_empty(cls, fields):
        if fields == "":
            raise ValueError(FIELD_NOT_BLANK.format(fields))
        return fields
