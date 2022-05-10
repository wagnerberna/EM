from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from src.model.student import StudentModel
from src.core.student import StudentCore
from src.resources.student_ns_payload import (
    student_ns,
    student_post_fields,
    student_put_fields,
    token_header,
)
from src.utils.response import Response
from src.static.message import *
from src.model.dto.student_dto import StudentAddDto, StudentUpdateDto

student_model = StudentModel()
student_core = StudentCore()
response = Response()

# GetAll
class StudentsController(Resource):
    @jwt_required()
    def get(self):
        try:
            payload_students = student_model.get_all()

            if payload_students == None:
                return response.failed(NOT_FOUND, "Student"), 404
            return payload_students, 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500


# Post
class StudentAddController(Resource):
    @jwt_required()
    @student_ns.expect(token_header, student_post_fields)
    def post(self):
        try:
            new_student = StudentAddDto.parse_obj(request.get_json())
            payload = student_core.payload_new_student(new_student)

            student_add = student_model.add(payload)
            if student_add == 0:
                return response.failed(NOT_CREATED, "Student"), 409

            return response.success(CREATED, "Student"), 201

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500


# GetById / Update / Delete
class StudentController(Resource):
    @student_ns.expect(token_header)
    @jwt_required()
    def get(self, id):
        try:
            data_student = student_model.get_by_id(id)

            if data_student == None:
                return response.failed(NOT_FOUND, "Student"), 404

            payload_student = data_student.dict()
            return payload_student, 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500

    @student_ns.expect(token_header, student_put_fields)
    @jwt_required()
    def put(self, id):
        try:
            data = StudentUpdateDto.parse_obj(request.get_json())
            payload = student_core.payload_update_student(data)
            student_update = student_model.update(id, payload)

            if student_update == 0:
                return response.failed(NOT_FOUND, "Student"), 404
            return response.success(UPDATE_SUCCESS), 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500

    @student_ns.expect(token_header)
    @jwt_required()
    def delete(self, id):
        try:
            data_delete = student_model.delete(id)

            if data_delete == 0:
                return response.failed(NOT_FOUND, "Student"), 404
            return response.success(DELETED, "Student"), 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500
