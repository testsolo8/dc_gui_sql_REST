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

path = (
    "https://"
    + base_url_dc()
    + ":9082/datacenter/api/v3/license/mode?AgentID=342042FB-E791-482B-98F4-61E78B1B1715&ComponentID=5"
)
r = requests.get(path, verify=False)


@allure.epic("REST API V3")
@allure.feature("Get operating mode of selected server group")
@pytest.mark.testRESTAPI
@allure.story("Запрос на получение режима работы выбранной группы серверов")
class TestGetOperatingModeSelectedServerGroup:
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

    @allure.title("Режим работы сервера EndpointController")
    def test_working_mode2(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        assert parsed_data["Mode"] == 2

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "object",
            "properties": {"Expire_Date": {"Mode": "number"}},
            "required": ["Mode"],
        }
        resp = r.json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self):
        data_dict = r.json()
        schema_models.SchemaModelsRESTAPIV3.GetOperatingModeSelectedServerGroup.parse_obj(
            data_dict
        )
