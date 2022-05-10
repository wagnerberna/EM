from flask_restx import fields, Namespace
from src.static.message import FIELD_NOT_BLANK


# Namespaces
students_ns = Namespace("students", description="Route for list all students")

student_ns = Namespace("student", description="Route for CRUD for student")

# payloads
student_post_fields = student_ns.model(
    "StudentAddFields",
    {
        "name": fields.String(required=True, help=FIELD_NOT_BLANK.format("name")),
        "birth_date": fields.Date(
            required=True, help=FIELD_NOT_BLANK.format("birth_date")
        ),
        "address": fields.String(required=True, help=FIELD_NOT_BLANK.format("address")),
        "tutor_name": fields.String(
            required=True, help=FIELD_NOT_BLANK.format("tutor_name")
        ),
        "cpf_tutor": fields.String(
            required=True, help=FIELD_NOT_BLANK.format("cpf_tutor")
        ),
        "tutor_email": fields.String(
            required=True, help=FIELD_NOT_BLANK.format("tutor_email")
        ),
    },
)

student_put_fields = student_ns.model(
    "StudentUpdateFields",
    {
        "field": fields.String(required=True, help=FIELD_NOT_BLANK.format("field")),
        "value": fields.String(required=True, help=FIELD_NOT_BLANK.format("value")),
    },
)

# Headers
token_header = student_ns.parser()
token_header.add_argument("Authorization", location="headers")
