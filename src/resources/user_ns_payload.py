from flask_restx import fields, Namespace
from src.static.message import FIELD_NOT_BLANK


# Namespaces
users_ns = Namespace("users", description="Route for list all users")

user_ns = Namespace("user", description="Route for CRUD and updtate status for user")

# payloads
user_post_fields = user_ns.model(
    "userAddFields",
    {
        "name": fields.String(required=True, help=FIELD_NOT_BLANK.format("name")),
        "login": fields.String(required=True, help=FIELD_NOT_BLANK.format("login")),
        "password": fields.String(
            required=True, help=FIELD_NOT_BLANK.format("password")
        ),
    },
)

user_put_fields = user_ns.model(
    "userUpdateFields",
    {
        "field": fields.String(required=True, help=FIELD_NOT_BLANK.format("field")),
        "value": fields.String(required=True, help=FIELD_NOT_BLANK.format("value")),
    },
)

user_post_status = user_ns.model(
    "userUpdateStatus",
    {
        "login": fields.String(required=True, help=FIELD_NOT_BLANK.format("login")),
        "status": fields.Boolean(required=True, help=FIELD_NOT_BLANK.format("status")),
    },
)

# Headers
token_header = user_ns.parser()
token_header.add_argument("Authorization", location="headers")
