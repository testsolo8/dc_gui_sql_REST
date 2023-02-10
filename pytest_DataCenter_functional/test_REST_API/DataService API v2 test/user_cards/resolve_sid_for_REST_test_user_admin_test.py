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

url_tail = "/api/v2/data_center/user_cards/batch/resolve_sid"
body = [{"objectList": "REST_test_user_admin@autotest.lan<>Администраторы домена"}]


@allure.epic("DataService API v2 (user_cards)")
@allure.feature("Resolve SID for REST_test_user_admin_test")
@pytest.mark.testRESTAPI
@allure.story("Процедура получения SID для списка пользователей и групп")
class TestResolveSIDForUser:
    @allure.title("Успешность запроса")
    def test_status_code_200(self, dc_api: DcApiWithToken):
        r = dc_api.req_post(url=url_tail, body=body)
        assert r.status_code == 200

    @allure.title("Headers 'content-type'")
    def test_content_type(self, dc_api: DcApiWithToken):
        con_type = dc_api.req_post(url=url_tail, body=body).headers["content-type"]
        assert con_type == r"application/json; charset=utf-8"

    @allure.title("Время ответа запроса")
    def test_response_time(self, dc_api: DcApiWithToken):
        resp_time = dc_api.req_post(url=url_tail, body=body).elapsed.total_seconds()
        assert resp_time <= 30

    @allure.title("Данные по REST_test_user_admin")
    def test_SID_REST_test_user_admin_test(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_post(url=url_tail, body=body).json()
        with allure.step("Входные данные, название группы / UPN пользователя"):
            check.equal(
                data_dict["data"][0]["inputName"], "REST_test_user_admin@autotest.lan"
            )
        with allure.step("Флаг группы"):
            check.equal(data_dict["data"][0]["isGroup"], 0)
        with allure.step("Идентификатор пользователя / группы в карточке"):
            check.equal(data_dict["data"][0]["objectID"], 5)
        with allure.step("уникальный идентификатор пользователя / группы SID"):
            check.equal(
                data_dict["data"][0]["sID"],
                "S-1-5-21-4141237049-2453287432-1636914503-3103",
            )

    @allure.title("Данные по группе Администраторы домена")
    def test_group_adminisnrators_domen_test(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_post(url=url_tail, body=body).json()
        with allure.step("Входные данные, название группы / UPN пользователя"):
            check.equal(data_dict["data"][1]["inputName"], "Администраторы домена")
        with allure.step("Флаг группы"):
            check.equal(data_dict["data"][1]["isGroup"], 1)
        with allure.step("Идентификатор пользователя / группы в карточке"):
            check.equal(data_dict["data"][1]["objectID"], 38)
        with allure.step("уникальный идентификатор пользователя / группы SID"):
            check.equal(
                data_dict["data"][1]["sID"],
                "S-1-5-21-4141237049-2453287432-1636914503-512",
            )

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self, dc_api: DcApiWithToken):
        schema = {
            "type": "object",
            "properties": {"data": {"type": "array"}},
            "required": ["data"],
        }
        resp = dc_api.req_post(url=url_tail, body=body).json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_post(url=url_tail, body=body).json()
        error_list = []
        for row in data_dict["data"]:
            try:
                schema_models.SchemaModelsDataServiceAPIv2.EmailListForUser.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.ResolveSIDForUser.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
