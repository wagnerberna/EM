from flask_restx import fields, Namespace
from src.static.message import FIELD_NOT_BLANK

# Namespaces
filters_ns = Namespace("filters", description="Route for filters students")

# payloads
filter_get_field_word = filters_ns.model(
    "getByFieldWord",
    {
        "field": fields.String(required=True, help=FIELD_NOT_BLANK.format("field")),
        "word": fields.String(required=True, help=FIELD_NOT_BLANK.format("word")),
    },
)

# Headers
token_header = filters_ns.parser()
token_header.add_argument("Authorization", location="headers")
