from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from src.utils.response import Response
from src.static.message import *
from src.model.filters import FiltersModel
from src.resources.filters_ns_payload import (
    filters_ns,
    filter_get_field_word,
    token_header,
)
from src.model.dto.filters_dto import FilterWordDto

filters_model = FiltersModel()
response = Response()


@filters_ns.expect(token_header, filter_get_field_word)
class FilterFieldWordCotroller(Resource):
    @jwt_required()
    def get(self):
        try:
            data = FilterWordDto.parse_obj(request.get_json())
            filter_db = filters_model.find_field_word(data)
            if filter_db == None:
                return response.failed(NOTHING_FILTER), 404

            return filter_db, 200

        except Exception as error:
            return response.failed(INTERNAL_ERROR, error), 500
