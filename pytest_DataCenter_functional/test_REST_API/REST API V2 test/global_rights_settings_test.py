# Standart libraries
import json

# Third party packages
import allure
import pytest
import requests
from jsonschema import validate

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc

path = "http://" + base_url_dc() + ":9096/api/v2/settings"
r = requests.get(path, verify=False)


@allure.epic("REST API V2")
@allure.feature("Global rights settings")
@pytest.mark.testRESTAPI
@allure.story("Статус прав доступа")
class TestGlobalRightsSettings:
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

    @allure.title("Статус прав доступа (включены)")
    def test_global_rights(self):
        data_dict = r.json()
        assert data_dict["settings"]["AccessRightsEnabled"] == True

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "settings": {
                    "type": "object",
                    "properties": {
                        "AccessRightsEnabled": {"type": "boolean"},
                        "PasswordControllerEnabled": {"type": "boolean"},
                    },
                },
            },
            "required": ["settings"],
        }
        resp = r.json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self):
        data_dict = r.json()
        schema_models.SchemaModelsRESTAPIV2.GlobalRightsSettings.parse_obj(
            data_dict["settings"]
        )
