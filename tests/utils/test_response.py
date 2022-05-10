import pytest
from pytest import fixture
from src.utils.response import Response


class TestResponse:
    @fixture
    def my_setup(self, mocker):
        self.mocker = mocker
        self.response = Response()


class TestProcessResponse(TestResponse):
    def test_response_success_message(self, my_setup):
        CREATED = "{} created."
        response_expected = {"Message": "User created."}
        response_result = self.response.success(CREATED, "User")
        assert response_expected == response_result

    def test_response_success(self, my_setup):
        UPDATE_SUCCESS = "Successfully update"
        response_expected = {"Message": "Successfully update"}
        response_result = self.response.success(UPDATE_SUCCESS)
        assert response_expected == response_result

    def test_response_fail_error(self, my_setup):
        NOT_FOUND = "{} not found."
        response_expected = {"Error": "User not found."}
        response_result = self.response.failed(NOT_FOUND, "User")
        assert response_expected == response_result

    def test_response_fail(self, my_setup):
        NOTHING_FILTER = "No results found"
        response_expected = {"Error": "No results found"}
        response_result = self.response.failed(NOTHING_FILTER)
        assert response_expected == response_result
