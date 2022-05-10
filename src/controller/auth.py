from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, create_access_token
from flask_jwt_extended.utils import get_jwt
from blacklist import BLACKLIST
from src.model.auth import AuthModel
from src.utils.passwords import compare_password
from src.resources.auth_ns_payload import auth_ns, token_header, auth_fields
from src.utils.response import Response
from src.static.message import *
from src.model.dto.auth_dto import AuthDto

auth_model = AuthModel()
response = Response()

# Login
@auth_ns.expect(auth_fields, validate=True)
class AuthLoginController(Resource):
    def post(self):
        try:
            data = AuthDto.parse_obj(request.get_json())
            login_db = auth_model.find_login(data.login.lower())

            if not login_db:
                return response.failed(AUTH_FAILED), 401

            if login_db.activated == False:
                return response.failed(LOGIN_INACTIVE), 409

            check_password = compare_password(data.password, login_db.password)
            if check_password == False:
                return response.failed(AUTH_FAILED), 401

            token = create_access_token(identity=login_db.login)
            return {"token": token}, 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500


# Logout
@auth_ns.expect(token_header)
class AuthLogoutController(Resource):
    @jwt_required()
    def post(self):
        try:
            jwt_id = get_jwt()["jti"]
            BLACKLIST.add(jwt_id)
            return LOGGED_SUCCESSFUL, 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500
