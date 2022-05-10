from src.static.message import *
from pydantic import BaseModel, validator
from typing import Optional


class GradeGridAddDto(BaseModel):
    student_id: Optional[int]
    year: Optional[int]
    portuguese: Optional[float]
    mathematics: Optional[float]
    biology: Optional[float]
    geography: Optional[float]
    history: Optional[float]

    @validator("year")
    def check_year(cls, value):
        if value < 2000:
            raise ValueError(VALUE_MIN.format("Year", "2000"))
        return value

    @validator("portuguese", "mathematics", "biology", "geography", "history")
    def check_scored(cls, value):
        if value < 0:
            raise ValueError(VALUE_MIN.format("Scored", "0"))
        return value


class GradeGridGetDto(BaseModel):
    scored_id: int
    student_id: int
    year: int
    portuguese: Optional[float]
    mathematics: Optional[float]
    biology: Optional[float]
    geography: Optional[float]
    history: Optional[float]
    created_at: str


class GradeGridUpdateDto(BaseModel):
    subject: str
    scored: float

    @validator("*")
    def field_not_empty(cls, field):
        if field == "":
            raise ValueError(FIELD_NOT_BLANK.format(field))
        return field

    @validator("subject")
    def field_list(cls, value):
        fields_list = [
            "portuguese",
            "mathematics",
            "biology",
            "geography",
            "history",
        ]
        if value not in fields_list:
            raise ValueError(FIELD_INVALID.format(fields_list))
        return value

    @validator("scored")
    def check_scored(cls, value):
        if value < 0:
            raise ValueError(VALUE_MIN.format("Scored", "0"))
        return value


class GradeGridUpdateByStudentYearDto(BaseModel):
    student_id: int
    year: int
    subject: str
    scored: float

    @validator("*")
    def field_not_empty(cls, field):
        if field == "":
            raise ValueError(FIELD_NOT_BLANK.format(field))
        return field

    @validator("year")
    def check_year(cls, value):
        if value < 2000:
            raise ValueError(VALUE_MIN.format("Year", "2000"))
        return value

    @validator("subject")
    def field_list(cls, value):
        fields_list = [
            "portuguese",
            "mathematics",
            "biology",
            "geography",
            "history",
        ]
        if value not in fields_list:
            raise ValueError(FIELD_INVALID.format(fields_list))
        return value

    @validator("scored")
    def check_scored(cls, value):
        if value < 0:
            raise ValueError(VALUE_MIN.format("Scored", "0"))
        return value


class GradeGridGetByStudentYearDto(BaseModel):
    student_id: int
    year: int

    @validator("*")
    def field_not_empty(cls, field):
        if field == "":
            raise ValueError(FIELD_NOT_BLANK.format(field))
        return field

    @validator("year")
    def check_year(cls, value):
        if value < 2000:
            raise ValueError(VALUE_MIN.format("Year", "2000"))
        return value
