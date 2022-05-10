import pytest
from pytest import fixture
from src.utils.normalize import NormalizeFields


class TestNormalizeFields:
    @fixture
    def my_setup(self, mocker):
        self.mocker = mocker
        self.mock_normalize_fields = NormalizeFields()


class TestProcessFields(TestNormalizeFields):
    def test_process_string(self, my_setup):
        text = " BrúCê Wãine "
        response_expected = "bruce waine"
        response_result = self.mock_normalize_fields.string(text)
        assert response_expected == response_result

    def test_process_cpf(self, my_setup):
        cpf = " 100.200.300-40 "
        response_expected = "10020030040"
        response_result = self.mock_normalize_fields.cpf(cpf)
        assert response_expected == response_result
