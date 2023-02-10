# Standart libraries
import json
from datetime import datetime

# Third party packages
import allure
import pytest
import pytest_check as check
import requests
from jsonschema import validate
from pydantic import ValidationError

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc

path = "http://" + base_url_dc() + ":9096/api/v2/domains"
r = requests.get(path, verify=False)


@allure.epic("REST API V2")
@allure.feature("Domain list")
@pytest.mark.testRESTAPI
@allure.story("Список добавленных доменов")
class TestDomainList:
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

    @allure.title("Домен autotest.lan")
    def test_domain_autotest(self):
        data_dict = r.json()
        with allure.step("Последняя синхронизация"):
            check.greater(
                datetime.utcfromtimestamp(data_dict["Domains"][2]["LastSync"]),
                datetime.utcfromtimestamp(1660867202),
            )
        with allure.step("Имя домена"):
            check.equal(data_dict["Domains"][2]["Domain"], "autotest.lan")
        with allure.step("GUID"):
            check.equal(
                data_dict["Domains"][2]["GUID"],
                "{BC925BAC-F94F-405D-B94B-5FE29498645C}",
            )

    @allure.title("Домен WorkGroups")
    def test_domain_internal(self):
        data_dict = r.json()
        with allure.step("Последняя синхронизация"):
            check.is_(type(data_dict["Domains"][1]["LastSync"]), int)
        with allure.step("Имя домена"):
            check.equal(data_dict["Domains"][1]["Domain"], "WorkGroups")
        with allure.step("GUID"):
            check.equal(
                data_dict["Domains"][1]["GUID"],
                "{576F726B-0000-0000-0000-47726F757073}",
            )

    @allure.title("Домен Internal.ISC")
    def test_domain_internal(self):
        data_dict = r.json()
        with allure.step("Последняя синхронизация"):
            check.is_(type(data_dict["Domains"][0]["LastSync"]), int)
        with allure.step("Имя домена"):
            check.equal(data_dict["Domains"][0]["Domain"], "Internal.ISC")
        with allure.step("GUID"):
            check.equal(
                data_dict["Domains"][0]["GUID"],
                "{58416765-6E74-0000-0000-47726F757073}",
            )

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "object",
            "properties": {"Domains": {"type": "array"}},
            "required": ["Domains"],
        }
        resp = r.json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self):
        data_dict = r.json()
        error_list = []
        for row in data_dict["Domains"]:
            try:
                schema_models.SchemaModelsRESTAPIV2.DomainList.parse_obj(row)
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsRESTAPIV2.DomainList.parse_obj(
                data_dict["Domains"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
