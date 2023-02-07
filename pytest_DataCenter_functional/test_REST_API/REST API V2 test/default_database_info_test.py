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

path = "http://" + base_url_dc() + ":9096/api/v2/defaultdatabaseinfo"
r = requests.get(path)


@allure.epic("REST API V2")
@allure.feature("Default database info")
@pytest.mark.testRESTAPI
@allure.story("Получение списка БД настроенных в консоли ДЦ")
class TestDefaultDatabaseInfo:
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

    @allure.title("Имена БД по умолчанию")
    def test_default_db(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("DefaultPG"):
            check.equal(parsed_data["DefaultPG"][0], "DC-AUTOTest")
        with allure.step("DefaultMSSQL"):
            check.equal(parsed_data["DefaultMSSQL"][0], "DC-AUTOTest")

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "DefaultPG": {"type": "array"},
                "DefaultMSSQL": {"type": "array"},
            },
            "required": ["DefaultPG", "DefaultMSSQL"],
        }
        resp = r.json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self):
        data_dict = r.json()
        schema_models.SchemaModelsRESTAPIV2.DefaultDatabaseInfo.parse_obj(data_dict)
