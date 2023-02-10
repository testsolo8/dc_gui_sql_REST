# Standart libraries
import json
from typing import List

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
from pytest_DataCenter_functional.test_REST_API.tools.get_product_version import (
    get_file_version,
)

path = "http://" + base_url_dc() + ":9096/api/v2/products?id=14"
r = requests.get(path, verify=False)


@allure.epic("REST API V2")
@allure.feature("WebAnalytic server list")
@pytest.mark.testRESTAPI
@allure.story("Список WebAnalytic")
class TestWebAnalyticServerList:
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

    @allure.title("Параметры подключения")
    def test_WebAnalytic_server_list_request(self):
        data_dict = r.json()
        with allure.step("UID сервера"):
            check.equal(data_dict[0]["UID"], "{0F919916-9E7C-408F-BD2B-CCF1B499D0F5}")
        with allure.step("DNSHostName сервера"):
            check.is_in("AUTOTEST", data_dict[0]["DNSHostName"])
        with allure.step("HostName сервера"):
            check.is_in("AUTOTEST", data_dict[0]["HostName"])
        with allure.step("Port сервера"):
            check.equal(data_dict[0]["Port"], 9111)
        with allure.step("Версия сервера"):
            path = r"c:\Program Files\SearchInform\SearchInform WebAnalytic\DataService.exe"
            file_version = get_file_version(path)
            check.equal(data_dict[0]["Version"], file_version)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "UID": {"type": "string"},
                    "HostName": {"type": "string"},
                    "Version": {"type": "string"},
                },
                "required": ["UID", "HostName", "Version"],
            },
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
                    List[
                        schema_models.SchemaModelsRESTAPIV2.ConnectionParametersTo_RC_OR_WA_server
                    ],
                    data_dict,
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsRESTAPIV2.ConnectionParametersTo_RC_OR_WA_server.parse_obj(
                data_dict[0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
