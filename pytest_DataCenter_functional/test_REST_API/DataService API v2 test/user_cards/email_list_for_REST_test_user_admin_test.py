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
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import DcApiWithToken

url_tail = "/api/v2/data_center/user_cards/contacts/e_mails?userID=5"


@allure.epic("DataService API v2 (user_cards)")
@allure.feature("Email list for REST_test_user_admin")
@pytest.mark.testRESTAPI
@allure.story("Почтовые адреса пользователя REST_test_user_admin")
class TestEmailListForUser:
    @allure.title("Успешность запроса")
    def test_status_code_200(self, dc_api: DcApiWithToken):
        r = dc_api.req_get(url_tail)
        assert r.status_code == 200

    @allure.title("Headers 'content-type'")
    def test_content_type(self, dc_api: DcApiWithToken):
        con_type = dc_api.req_get(url_tail).headers["content-type"]
        assert con_type == r"application/json; charset=utf-8"

    @allure.title("Время ответа запроса")
    def test_response_time(self, dc_api: DcApiWithToken):
        resp_time = dc_api.req_get(url_tail).elapsed.total_seconds()
        assert resp_time <= 30

    @allure.title("Почтовый адрес gmail.com")
    def test_gmail_com(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Идентификатор документа в индексе"):
            check.is_none(parsed_data["data"][0]["docID"])
        with allure.step("Отображать в шапке"):
            check.is_none(parsed_data["data"][0]["inHeader"])
        with allure.step("Почтовый адрес"):
            check.equal(
                parsed_data["data"][0]["mailAddress"], "REST_test_user_admin@gmail.com"
            )
        with allure.step("Идентификатор почтового адреса"):
            check.equal(parsed_data["data"][0]["mailID"], 5)
        with allure.step("Тип почтового адреса"):
            check.equal(parsed_data["data"][0]["mailType"], 1)
        with allure.step("UDL документа"):
            check.is_none(parsed_data["data"][0]["signID"])

    @allure.title("Почтовый адрес test.lan")
    def test_test_lan(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Идентификатор документа в индексе"):
            check.equal(
                parsed_data["data"][1]["docID"], "01279DC6-381E-4F6A-9E86-60AEA3514067"
            )
        with allure.step("Отображать в шапке"):
            check.is_true(parsed_data["data"][1]["inHeader"])
        with allure.step("Почтовый адрес"):
            check.equal(
                parsed_data["data"][1]["mailAddress"], "REST_test_user_admin@test.lan"
            )
        with allure.step("Идентификатор почтового адреса"):
            check.equal(parsed_data["data"][1]["mailID"], 1)
        with allure.step("Тип почтового адреса"):
            check.equal(parsed_data["data"][1]["mailType"], 1)
        with allure.step("UDL документа"):
            check.equal(
                parsed_data["data"][1]["signID"], "01279DC6-381E-4F6A-9E86-60AEA3514067"
            )

    @allure.title("Почтовый адрес ya.ru")
    def test_ya_ru(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Идентификатор документа в индексе"):
            check.is_none(parsed_data["data"][2]["docID"])
        with allure.step("Отображать в шапке"):
            check.is_none(parsed_data["data"][2]["inHeader"])
        with allure.step("Почтовый адрес"):
            check.equal(
                parsed_data["data"][2]["mailAddress"], "REST_test_user_admin@ya.ru"
            )
        with allure.step("Идентификатор почтового адреса"):
            check.equal(parsed_data["data"][2]["mailID"], 4)
        with allure.step("Тип почтового адреса"):
            check.equal(parsed_data["data"][2]["mailType"], 1)
        with allure.step("UDL документа"):
            check.is_none(parsed_data["data"][2]["signID"])

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self, dc_api: DcApiWithToken):
        schema = {
            "type": "object",
            "properties": {"data": {"type": "array"}},
            "required": ["data"],
        }
        resp = dc_api.req_get(url_tail).json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        error_list = []
        for row in data_dict["data"]:
            try:
                schema_models.SchemaModelsDataServiceAPIv2.EmailListForUser.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.EmailListForUser.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
