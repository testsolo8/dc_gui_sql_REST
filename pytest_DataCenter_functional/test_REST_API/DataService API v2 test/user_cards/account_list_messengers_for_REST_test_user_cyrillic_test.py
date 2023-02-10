# Standart libraries
import json

# Third party packages
import allure
import pytest
import pytest_check as check
from jsonschema import validate
from pydantic import ValidationError

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import DcApiWithToken

url_tail = "/api/v2/data_center/user_cards/contacts/accounts?userID=1&contactTypeID=3"


@allure.epic("DataService API v2 (user_cards)")
@allure.feature("Account list messengers for REST_test_user_cyrillic")
@pytest.mark.testRESTAPI
@allure.story("Мессенджеры пользователя REST_test_user_cyrillic")
class TestAccountListMessengersForUser:
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

    @allure.title("Viber аккаунт")
    def test_skype_account(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Идентификатор аккаунта"):
            check.equal(data_dict["data"][0]["accountID"], 10)
        with allure.step("Логин"):
            check.equal(
                data_dict["data"][0]["accountName"], "Viber_REST_test_user_cyrillic"
            )
        with allure.step("Тип аккаунта - UC_AccountsType"):
            check.equal(data_dict["data"][0]["accountTypeID"], 3)
        with allure.step("Тип контакта: 3 Мессенджеры, 4 Соц.Сети, 5 Другие"):
            check.equal(data_dict["data"][0]["contactTypeID"], 3)
        with allure.step("Имя аккаунта"):
            check.equal(
                data_dict["data"][0]["displayName"], "Viber_REST_test_user_cyrillic"
            )
        with allure.step("Идентификатор документа в индексе"):
            check.is_none(data_dict["data"][0]["docID"])
        with allure.step("Отображать в шапке"):
            check.is_none(data_dict["data"][0]["inHeader"])
        with allure.step("Дата последнего входа"):
            check.is_none(data_dict["data"][0]["lastLogon"])
        with allure.step("UDL документа"):
            check.is_none(data_dict["data"][0]["signID"])

    @allure.title("Mail.ru аккаунт")
    def test_icq_account(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Идентификатор аккаунта"):
            check.equal(data_dict["data"][1]["accountID"], 9)
        with allure.step("Логин"):
            check.equal(
                data_dict["data"][1]["accountName"],
                "Mail.ru Agent_REST_test_user_cyrillic",
            )
        with allure.step("Тип аккаунта - UC_AccountsType"):
            check.equal(data_dict["data"][1]["accountTypeID"], 5)
        with allure.step("Тип контакта: 3 Мессенджеры, 4 Соц.Сети, 5 Другие"):
            check.equal(data_dict["data"][1]["contactTypeID"], 3)
        with allure.step("Имя аккаунта"):
            check.equal(
                data_dict["data"][1]["displayName"],
                "Mail.ru Agent_REST_test_user_cyrillic",
            )
        with allure.step("Идентификатор документа в индексе"):
            check.is_none(data_dict["data"][1]["docID"])
        with allure.step("Отображать в шапке"):
            check.is_none(data_dict["data"][1]["inHeader"])
        with allure.step("Дата последнего входа"):
            check.is_none(data_dict["data"][1]["lastLogon"])
        with allure.step("UDL документа"):
            check.is_none(data_dict["data"][1]["signID"])

    @allure.title("WhatsApp аккаунт")
    def test_icq_account(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Идентификатор аккаунта"):
            check.equal(data_dict["data"][2]["accountID"], 8)
        with allure.step("Логин"):
            check.equal(
                data_dict["data"][2]["accountName"],
                "WhatsApp_REST_test_user_cyrillic",
            )
        with allure.step("Тип аккаунта - UC_AccountsType"):
            check.equal(data_dict["data"][2]["accountTypeID"], 13)
        with allure.step("Тип контакта: 3 Мессенджеры, 4 Соц.Сети, 5 Другие"):
            check.equal(data_dict["data"][2]["contactTypeID"], 3)
        with allure.step("Имя аккаунта"):
            check.equal(
                data_dict["data"][2]["displayName"],
                "WhatsApp_REST_test_user_cyrillic",
            )
        with allure.step("Идентификатор документа в индексе"):
            check.is_none(data_dict["data"][2]["docID"])
        with allure.step("Отображать в шапке"):
            check.is_none(data_dict["data"][2]["inHeader"])
        with allure.step("Дата последнего входа"):
            check.is_none(data_dict["data"][2]["lastLogon"])
        with allure.step("UDL документа"):
            check.is_none(data_dict["data"][2]["signID"])

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
                schema_models.SchemaModelsDataServiceAPIv2.AccountListMessengersAndSocialNetworksForUser.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.AccountListMessengersAndSocialNetworksForUser.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
