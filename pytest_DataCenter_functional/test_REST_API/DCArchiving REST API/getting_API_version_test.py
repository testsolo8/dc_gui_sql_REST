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

path = "https://" + base_url_dc() + ":9082/archiving/api/version"
r = requests.get(path, verify=False)


@allure.epic("DCArchiving REST API")
@allure.feature("Getting API version")
@pytest.mark.testRESTAPI
@allure.story("Получение версии API")
class TestGettingAPIVersion:
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

    @allure.title("Получение версии API")
    def test_api_version(self):
        data_dict = r.json()
        with allure.step("Минимальная поддерживаемая версия"):
            check.equal(data_dict["MinSupported"], 1)
        with allure.step("Максимальная поддерживаемая версия"):
            check.equal(data_dict["MaxSupported"], 1)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "object",
            "required": ["MinSupported", "MaxSupported"],
        }
        resp = r.json()
        validate(resp, schema=schema)
