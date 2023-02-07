# Standart libraries
import json

# Third party packages
import allure
import pytest
import requests
from jsonschema import validate

# My packages
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc

path = (
    "https://"
    + base_url_dc()
    + ":9082/datacenter/api/v3/license/statuses?AgentID=AE2CC2A1-0350-4387-B297-07EC2EAFADB2&LicenseID=7848DC5B-7EFD-4ED2-8116-5CC43664CC4F"
)
r = requests.get(path, verify=False)


@allure.epic("REST API V3")
@allure.feature("licenses by components")
@pytest.mark.testRESTAPI
@allure.story("Получение списка аудиторов")
class TestLicensesByComponents:
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
    def test_count_of_license_not_empty(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        assert len(parsed_data) >= 1

    @pytest.mark.skip(reason="в текущей реализации среды для тестов не реализовано")
    def test_schema(self):
        schema = {"type": "array"}
        resp = r.json()
        validate(resp, schema=schema)
