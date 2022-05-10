from pydantic import BaseModel, validator
from src.static.message import *


class FilterWordDto(BaseModel):
    field: str
    word: str

    @validator("*")
    def field_not_empty(cls, fields):
        if fields == "":
            raise ValueError(FIELD_NOT_BLANK.format(fields))
        return fields

    @validator("field")
    def field_list(cls, value):
        fields_list = [
            "name",
            "address",
            "tutor_name",
            "tutor_email",
        ]
        if value not in fields_list:
            raise ValueError(FIELD_INVALID.format(fields_list))
        return value
