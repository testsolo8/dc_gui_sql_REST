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

path = "http://" + base_url_dc() + ":9096/api/v2/products?id=0"
path_with_dbParam = "http://" + base_url_dc() + ":9096/api/v2/products/withDB?id=0"
r = requests.get(path, verify=False)


@allure.epic("REST API V2")
@allure.feature("Connection parameters to DCserver")
@pytest.mark.testRESTAPI
@allure.story("Параметры подключения к серверу DC")
class TestConnectionParametersToDCserver:
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
    def test_connection_parameters_to_DCserver(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Порт APIv3"):
            check.equal(parsed_data[0]["Ports"]["APIv3"], 9082)
        with allure.step("Порт SIProxyDC"):
            check.equal(parsed_data[0]["Ports"]["SIProxyDC"], 9088)
        with allure.step("Порт UserCard"):
            check.equal(parsed_data[0]["Ports"]["UserCardDS"], 9072)
        with allure.step("UID сервера"):
            check.equal(parsed_data[0]["UID"], "{124645B2-4B96-4675-868A-1E1958018B42}")
        with allure.step("HostName сервера"):
            check.is_in("AUTOTEST", parsed_data[0]["HostName"])
        with allure.step("Версия сервера"):
            check.greater(parsed_data[0]["Version"], "2.50.0.0")

    @allure.title("Параметры подключения со строкой подключения к БД")
    def test_connection_parameters_to_DCserver_with_dbParam(self):
        data_dict = requests.get(path_with_dbParam, verify=False).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Порт APIv3"):
            check.equal(parsed_data[0]["Ports"]["APIv3"], 9082)
        with allure.step("Порт SIProxyDC"):
            check.equal(parsed_data[0]["Ports"]["SIProxyDC"], 9088)
        with allure.step("Порт UserCard"):
            check.equal(parsed_data[0]["Ports"]["UserCardDS"], 9072)
        with allure.step("UID сервера"):
            check.equal(parsed_data[0]["UID"], "{124645B2-4B96-4675-868A-1E1958018B42}")
        with allure.step("Параметры подключения к БД"):
            check.equal(
                parsed_data[0]["DBParams"],
                "TgAoACAAAAAGACgABgB7ADMAQQA2ADYAQgAxADcAOAAtADEAQgA0AEEALQA0AGEAOAAwAC0AOAAwAEYAMQAtADkANwAyAEUAMwA1AEEAMAA4ADYANAA1AH0AAABEAGEAdABhAEMAZQBuAHQAZQByAF8AZgBvAHIAXwBSAEUAUwBUAAAAVwBJAE4ALQBFAEUAQwBTAFQAQwBBAFMAQQBOAFMAAABzAGEAAAABAEMAOABBADgAQwAxADMAOAA2ADEAMABBAEUAQQBGADgARQA1AAAATgBvAAAA",
            )
        with allure.step("HostName сервера"):
            check.is_in("AUTOTEST", parsed_data[0]["HostName"])
        with allure.step("Версия сервера"):
            check.greater(parsed_data[0]["Version"], "2.50.0.0")

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
                        schema_models.SchemaModelsRESTAPIV2.ConnectionParametersToDCserver
                    ],
                    data_dict,
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsRESTAPIV2.ConnectionParametersToDCserver.parse_obj(
                data_dict[0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
