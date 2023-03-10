# Standart libraries
import json

# Third party packages
import allure
import pytest
import pytest_check as check
import requests
from jsonschema import validate

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc
from pytest_DataCenter_functional.test_REST_API.tools.get_product_version import (
    get_file_version,
)

path = "http://" + base_url_dc() + ":9096/api/version/DCServer"
r = requests.get(path, verify=False)


@allure.epic("REST API V2")
@allure.feature("DCServer version")
@pytest.mark.testRESTAPI
@allure.story("Получение версии DC Server")
class TestDCServerVersion:
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

    @allure.title("Версия сервера ДЦ")
    def test_version(self):
        data_dict = r.json()
        with allure.step("Версия сервера"):
            path = r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCServer.exe"
            file_version = get_file_version(path)
            check.equal(data_dict["Version"], file_version)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "object",
            "properties": {"Version": {"type": "string"}},
            "required": ["Version"],
        }
        resp = r.json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self):
        data_dict = r.json()
        schema_models.SchemaModelsRESTAPIV2.DCServerVersion.parse_obj(data_dict)
