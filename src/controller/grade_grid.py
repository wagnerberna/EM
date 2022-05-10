from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from src.model.grade_grid import GradeGridModel
from src.core.grade_grid import GradeGridCore
from src.resources.grade_grid_ns_payload import (
    grade_grid_ns,
    grade_grid_add_fields,
    grade_grid_add_fields,
    token_header,
)
from src.utils.response import Response
from src.static.message import *
from src.model.dto.grade_grid_dto import (
    GradeGridAddDto,
    GradeGridUpdateDto,
    GradeGridGetByStudentYearDto,
    GradeGridUpdateByStudentYearDto,
)

grade_grid_model = GradeGridModel()
grade_grid_core = GradeGridCore()
response = Response()

# GetAll
class GradeGridAllController(Resource):
    def get(self):
        try:
            payload_grade_grid_all = grade_grid_model.get_all()

            if payload_grade_grid_all == None:
                return response.failed(NOT_FOUND, "Grade grid"), 404
            return payload_grade_grid_all, 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500


# Post
class GradeGridAddController(Resource):
    @grade_grid_ns.expect(grade_grid_add_fields)
    def post(self):
        try:
            new_scored = GradeGridAddDto.parse_obj(request.get_json())
            payload = grade_grid_core.payload_add(new_scored)
            find_student = grade_grid_model.find_student(payload.student_id)
            if not find_student:
                return response.failed(NOT_FOUND, "Student")

            check_db_conflict = grade_grid_model.find_student_and_year(
                payload.student_id,
                payload.year,
            )

            if check_db_conflict:
                return response.failed(ALREDY_EXISTS, "Student and year"), 409

            scored_add = grade_grid_model.add(payload)
            if scored_add == 0:
                return response.failed(NOT_CREATED, "Scored"), 409

            return response.success(CREATED, "Scored"), 201

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500


# GetById / Update / Delete
class GradeGridController(Resource):
    def get(self, id):
        try:
            data_scored = grade_grid_model.get_by_id(id)

            if data_scored == None:
                return response.failed(NOT_FOUND, "Scored"), 404

            payload_scored = data_scored.dict()
            return payload_scored, 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500

    # @jwt_required()
    @grade_grid_ns.expect(token_header, grade_grid_add_fields)
    def put(self, id):
        try:
            data = GradeGridUpdateDto.parse_obj(request.get_json())
            payload_scored = grade_grid_core.payload_update(data)
            scored_update = grade_grid_model.update(id, payload_scored)

            if scored_update == 0:
                return response.failed(NOT_FOUND, "Scored"), 404
            return response.success(UPDATE_SUCCESS), 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500

    # @jwt_required()
    @grade_grid_ns.expect(token_header)
    def delete(self, id):
        try:
            data_delete = grade_grid_model.delete(id)

            if data_delete == 0:
                return response.failed(NOT_FOUND, "Scored"), 404
            return response.success(DELETED, "Scored"), 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500


class GradeGridAdvancedController(Resource):
    def get(self):
        try:
            data = GradeGridGetByStudentYearDto.parse_obj(request.get_json())
            data_scored = grade_grid_model.get_by_student_and_year(
                data.student_id, data.year
            )

            if data_scored == None:
                return response.failed(NOT_FOUND, "Scored"), 404

            payload_scored = data_scored.dict()
            return payload_scored, 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500

    # @jwt_required()
    @grade_grid_ns.expect(token_header, grade_grid_add_fields)
    def put(self):
        try:
            data = GradeGridUpdateByStudentYearDto.parse_obj(request.get_json())
            payload_scored = grade_grid_core.payload_update_by_student_year(data)
            scored_update = grade_grid_model.update_by_student_year(payload_scored)

            if scored_update == 0:
                return response.failed(NOT_FOUND, "Scored"), 404
            return response.success(UPDATE_SUCCESS), 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500
