# Standart libraries
import json
from datetime import datetime

# Third party packages
import allure
import pytest
import pytest_check as check
import requests
from jsonschema import validate
from pydantic import ValidationError, parse_obj_as

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc

path = "http://" + base_url_dc() + ":9096/api/v2/license/profile"
r = requests.get(path, verify=False)


@allure.epic("REST API V2")
@allure.feature("List of profiling licenses")
@pytest.mark.testRESTAPI
@allure.story("Список лицензий профайлинга")
class TestListProfilingLicenses:
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

    @allure.title("Основные настройки")
    def test_general_settings(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Кол-во неиспользованных лицензий"):
            check.equal(parsed_data["License"]["FreeCount"], 1000)
        with allure.step("Окончание лицензии"):
            check.greater(
                datetime.utcfromtimestamp(parsed_data["License"]["ExpireDate"]),
                datetime.now(),
            )
        with allure.step("Колличество лицензий"):
            check.equal(parsed_data["License"]["Count"], 1000)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "License": {
                    "type": "object",
                    "properties": {
                        "FreeCount": {"type": "integer"},
                        "ExpireDate": {"type": "integer"},
                        "Count": {"type": "integer"},
                    },
                    "required": ["ExpireDate", "Count"],
                },
                "Accounts": {"type": "array"},
            },
            "required": ["License", "Accounts"],
        }
        resp = r.json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self):
        data_dict = r.json()
        error_list = []
        for row in data_dict:
            try:
                parse_obj_as(
                    schema_models.SchemaModelsRESTAPIV2.ListProfilingLicenses, data_dict
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsRESTAPIV2.ListProfilingLicenses.License.parse_obj(
                data_dict["License"]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
