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

path = "http://" + base_url_dc() + ":9096/api/v2/products?id=5"
path_with_dbParam = "http://" + base_url_dc() + ":9096/api/v2/products/withDB?id=5"
r = requests.get(path, verify=False)


@allure.epic("REST API V2")
@allure.feature("ReportCenter server list")
@pytest.mark.testRESTAPI
@allure.story("Список ReportCenter")
class TestReportCenterServerList:
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
    def test_ReportCenter_server_list_request(self):
        data_dict = r.json()
        with allure.step("UID сервера"):
            check.equal(data_dict[0]["UID"], "{0F919916-9E7C-408F-BD2B-CCF1B499D0F5}")
        with allure.step("DNSHostName сервера"):
            check.is_in("AUTOTEST", data_dict[0]["DNSHostName"])
        with allure.step("HostName сервера"):
            check.is_in("AUTOTEST", data_dict[0]["HostName"])
        with allure.step("Port сервера"):
            check.equal(data_dict[0]["Port"], 9099)
        with allure.step("Версия сервера"):
            path = r"c:\Program Files (x86)\SearchInform\SearchInform ReportCenter\RC_Sync.exe"
            file_version = get_file_version(path)
            check.equal(data_dict[0]["Version"], file_version)

    @allure.title("Параметры подключения со строкой подключения к БД")
    def test_ReportCenter_server_list_request_with_dbParam(self):
        data_dict = requests.get(path_with_dbParam, verify=False).json()
        with allure.step("UID сервера"):
            check.equal(data_dict[0]["UID"], "{0F919916-9E7C-408F-BD2B-CCF1B499D0F5}")
        with allure.step("DNSHostName сервера"):
            check.is_in("AUTOTEST", data_dict[0]["DNSHostName"])
        with allure.step("Параметры подключения к БД"):
            check.equal(
                data_dict[0]["DBParams"],
                "TgAsACAAAAAGACgABgB7ADMAQQA2ADYAQgAxADcAOAAtADEAQgA0AEEALQA0AGEAOAAwAC0AOAAwAEYAMQAtADkANwAyAEUAMwA1AEEAMAA4ADYANAA1AH0AAABSAGUAcABvAHIAdABDAGUAbgB0AGUAcgBfAGYAbwByAF8AUgBFAFMAVAAAAFcASQBOAC0ARQBFAEMAUwBUAEMAQQBTAEEATgBTAAAAcwBhAAAAAQBDADgAQQA4AEMAMQAzADgANgAxADAAQQBFAEEARgA4AEUANQAAAE4AbwAAAA==",
            )
        with allure.step("HostName сервера"):
            check.is_in("AUTOTEST", data_dict[0]["HostName"])
        with allure.step("Port сервера"):
            check.equal(data_dict[0]["Port"], 9099)
        with allure.step("Версия сервера"):
            path = r"c:\Program Files (x86)\SearchInform\SearchInform ReportCenter\RC_Sync.exe"
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
        data_dict = requests.get(path_with_dbParam, verify=False).json()
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
