# Standart libraries
import json

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

path = "http://" + base_url_dc() + ":9096/api/v2/users"
r = requests.get(path, verify=False)


@allure.epic("REST API V2")
@allure.feature("Users list")
@pytest.mark.testRESTAPI
@allure.story("Получение списка пользователей")
class TestUsersList:
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

    @allure.title("Пользователь REST_test_user_cyrillic")
    def test_REST_test_user_cyrillic(self):
        data_dict = r.json()
        with allure.step("UPN"):
            check.equal(
                data_dict["users"][2]["UPN"], "REST_test_user_cyrillic@autotest.lan"
            )
        with allure.step("SID"):
            check.equal(
                data_dict["users"][2]["SID"],
                "S-1-5-21-4141237049-2453287432-1636914503-3106",
            )
        with allure.step("Статус пользователя"):
            check.equal(data_dict["users"][2]["UserState"], 1)
        with allure.step("DisplayName"):
            check.equal(data_dict["users"][2]["DisplayName"], "REST_test_user_кириллик")
        with allure.step("Name"):
            check.equal(data_dict["users"][2]["Name"], "REST_test_user_кириллик")
        with allure.step("GUID"):
            check.equal(
                data_dict["users"][2]["GUID"], "2BFADC91-4BD5-44FE-853D-15E4814CC0D8"
            )

    @allure.title("Пользователь REST_test_user_admin")
    def test_REST_test_user_admin(self):
        data_dict = r.json()
        with allure.step("UPN"):
            check.equal(
                data_dict["users"][6]["UPN"], "REST_test_user_admin@autotest.lan"
            )
        with allure.step("SID"):
            check.equal(
                data_dict["users"][6]["SID"],
                "S-1-5-21-4141237049-2453287432-1636914503-3103",
            )
        with allure.step("Статус пользователя"):
            check.equal(data_dict["users"][6]["UserState"], 1)
        with allure.step("DisplayName"):
            check.equal(data_dict["users"][6]["DisplayName"], "REST_test_user_admin")
        with allure.step("Name"):
            check.equal(data_dict["users"][6]["Name"], "REST_test_user_admin")
        with allure.step("GUID"):
            check.equal(
                data_dict["users"][6]["GUID"], "01279DC6-381E-4F6A-9E86-60AEA3514067"
            )

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "object",
            "properties": {"objects": {"type": "array"}},
            "required": ["users"],
        }
        resp = r.json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self):
        data_dict = r.json()
        error_list = []
        for row in data_dict["users"]:
            try:
                schema_models.SchemaModelsRESTAPIV2.UsersList.parse_obj(row)
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsRESTAPIV2.UsersList.parse_obj(
                data_dict["users"][2]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
