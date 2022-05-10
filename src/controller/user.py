from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from src.model.user import UserModel
from src.core.user import UserCore
from src.resources.user_ns_payload import (
    user_ns,
    user_post_fields,
    user_put_fields,
    user_post_status,
    token_header,
)
from src.utils.response import Response
from src.static.message import *
from src.model.dto.user_dto import UserAddDto, UserUpdateStrDto, UserUpdateStatusDto

user_model = UserModel()
user_core = UserCore()
response = Response()

# GetAll
class UsersController(Resource):
    @jwt_required()
    def get(self):
        try:
            payload_users = user_model.get_all()

            if payload_users == None:
                return response.failed(NOT_FOUND, "User"), 404
            return payload_users, 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500


# Post
class UserAddController(Resource):
    @user_ns.expect(user_post_fields)
    def post(self):
        try:
            new_user = UserAddDto.parse_obj(request.get_json())
            payload = user_core.payload_new_user(new_user)

            if user_model.find_login(payload.login):
                return response.failed(ALREDY_EXISTS, "Login"), 409

            user_add = user_model.add(payload)
            if user_add == 0:
                return response.failed(NOT_CREATED, "User"), 409

            return response.success(CREATED, "User"), 201

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500


# GetById / Update / Delete
class UserController(Resource):
    @user_ns.expect(token_header)
    @jwt_required()
    def get(self, id):
        try:
            data_user = user_model.get_by_id(id)

            if data_user == None:
                return response.failed(NOT_FOUND, "User"), 404

            payload_user = data_user.dict()
            return payload_user, 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500

    @user_ns.expect(token_header, user_put_fields)
    @jwt_required()
    def put(self, id):
        try:
            data = UserUpdateStrDto.parse_obj(request.get_json())
            payload = user_core.payload_update_user(data)
            user_update = user_model.update(id, payload)

            if user_update == 0:
                return response.failed(NOT_FOUND, "User"), 404
            return response.success(UPDATE_SUCCESS), 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500

    @user_ns.expect(token_header)
    @jwt_required()
    def delete(self, id):
        try:
            data_delete = user_model.delete(id)

            if data_delete == 0:
                return response.failed(NOT_FOUND, "User"), 404
            return response.success(DELETED, "User"), 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500


# update status
class UserControllerStatus(Resource):
    @user_ns.expect(token_header, user_post_status)
    @jwt_required()
    def put(self):
        try:
            payload = UserUpdateStatusDto.parse_obj(request.get_json())
            if not user_model.find_login(payload.login):
                return response.failed(NOT_FOUND, "Login"), 404
            user_model.update_status(payload)
            return response.success(UPDATE_SUCCESS), 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500
