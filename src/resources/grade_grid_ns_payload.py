from flask_restx import fields, Namespace
from src.static.message import FIELD_NOT_BLANK


# Namespaces
grade_grid_all_ns = Namespace(
    "grandegridall", description="Route for list all grande grid"
)

grade_grid_ns = Namespace("gradegrid", description="Route for CRUD for grade grid")

# payloads
grade_grid_add_fields = grade_grid_ns.model(
    "gradeGridAddFields",
    {
        "student_id": fields.String(
            required=True, help=FIELD_NOT_BLANK.format("student_id")
        ),
        "year": fields.Integer(required=True, help=FIELD_NOT_BLANK.format("year")),
        "portuguese": fields.Float(
            required=True, help=FIELD_NOT_BLANK.format("portuguese")
        ),
        "mathematics": fields.Float(
            required=True, help=FIELD_NOT_BLANK.format("mathematics")
        ),
        "biology": fields.Float(required=True, help=FIELD_NOT_BLANK.format("biology")),
        "geography": fields.Float(
            required=True, help=FIELD_NOT_BLANK.format("geography")
        ),
        "history": fields.Float(required=True, help=FIELD_NOT_BLANK.format("history")),
    },
)

grade_grid_update_fields = grade_grid_ns.model(
    "gradeGridUpdateFields",
    {
        "subject": fields.String(required=True, help=FIELD_NOT_BLANK.format("subject")),
        "scored": fields.Float(required=True, help=FIELD_NOT_BLANK.format("scored")),
    },
)

grade_grid_update_by_student_year_fields = grade_grid_ns.model(
    "gradeGridUpdateByStudentYear",
    {
        "student_id": fields.String(
            required=True, help=FIELD_NOT_BLANK.format("student_id")
        ),
        "year": fields.Integer(required=True, help=FIELD_NOT_BLANK.format("year")),
        "subject": fields.String(
            required=True, help=FIELD_NOT_BLANK.format("student_id")
        ),
        "scored": fields.Float(required=True, help=FIELD_NOT_BLANK.format("scored")),
    },
)

grade_grid_get_by_student_year_fields = grade_grid_ns.model(
    "gradeGridGetByStudentYear",
    {
        "student_id": fields.String(
            required=True, help=FIELD_NOT_BLANK.format("student_id")
        ),
        "year": fields.Integer(required=True, help=FIELD_NOT_BLANK.format("year")),
    },
)


# Headers
token_header = grade_grid_ns.parser()
token_header.add_argument("Authorization", location="headers")
