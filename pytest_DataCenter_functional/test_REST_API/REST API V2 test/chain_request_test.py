# Standart libraries
import json

# Third party packages
import allure
import pytest
import pytest_check as check
import requests
from jsonschema import validate

# My packages
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc

path = "http://" + base_url_dc() + ":9096/api/v2/chains"
r = requests.get(path, verify=False)


@allure.epic("REST API V2")
@allure.feature("Chain request")
@pytest.mark.testRESTAPI
@allure.story("Получение списка индексов и БД")
class TestChainRequest:
    @allure.title("Успешность запроса")
    def test_status_code_200(self):
        assert r.status_code == 200

    @allure.title("Headers 'content-type'")
    def test_content_type(self):
        con_type = r.headers["content-type"]
        assert con_type == "application/json; charset=utf-8"

    @allure.title("Время ответа запроса")
    def test_response_time(self):
        resp_time = r.elapsed.total_seconds()
        assert resp_time <= 30

    @pytest.mark.skip(reason="в текущей реализации среды для тестов не реализовано")
    def test_index_and_db_are_exists(self):
        data_dict = r.json()
        check.greater_equal(len(data_dict["Indexes"]), 1)
        check.greater_equal(len(data_dict["DataBases"]), 1)

    @pytest.mark.skip(reason="в текущей реализации среды для тестов не реализовано")
    def test_schema(self):
        schema = {"type": "object", "required": ["Indexes", "DataBases"]}
        resp = r.json()
        validate(resp, schema=schema)
