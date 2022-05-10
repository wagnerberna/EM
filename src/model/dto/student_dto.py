from datetime import date
from src.static.message import *
from pydantic import BaseModel, validator, EmailStr


class StudentAddDto(BaseModel):
    name: str
    birth_date: date
    address: str
    tutor_name: str
    cpf_tutor: str
    tutor_email: EmailStr

    @validator("*")
    def field_not_empty(cls, field):
        if field == "":
            raise ValueError(FIELD_NOT_BLANK.format(field))
        return field


class StudentGetDto(BaseModel):
    student_id: int
    name: str
    birth_date: str
    address: str
    tutor_name: str
    cpf_tutor: str
    tutor_email: EmailStr
    created_at: str


class StudentUpdateDto(BaseModel):
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
            "birth_date",
            "address",
            "tutor_name",
            "cpf_tutor",
            "tutor_email",
        ]
        if value not in fields_list:
            raise ValueError(FIELD_INVALID.format(fields_list))
        return value


class StudentUpdateBirthDateDto(BaseModel):
    field: str
    value: date


class StudentDtoUpdateEmail(BaseModel):
    field: str
    value: EmailStr
