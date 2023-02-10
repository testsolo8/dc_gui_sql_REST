# Standart libraries
import json

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

path = "http://" + base_url_dc() + ":9096/api/v2/MailDefaultSettings"
r = requests.get(path, verify=False)


@allure.epic("REST API V2")
@allure.feature("Mail notification settings")
@pytest.mark.testRESTAPI
@allure.story("Настройки почтовых уведомлений")
class TestMailNotificationSettings:
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

    @allure.title("Основные настройки")
    def test_main_settings(self):
        data_dict = r.json()
        with allure.step("Уведомления по SearchServer не настроены"):
            check.is_false(data_dict["SearchServer"]["Enabled"])
        with allure.step("Уведомления по Endpoint не настроены"):
            check.is_false(data_dict["Endpoint"]["Enabled"])
        with allure.step("Уведомления по IntegrationSMTP не настроены"):
            check.is_false(data_dict["IntegrationSMTP"]["Enabled"])
        with allure.step("Уведомления по IntegrationMail не настроены"):
            check.is_false(data_dict["IntegrationMail"]["Enabled"])
        with allure.step("Уведомления по Network не настроены"):
            check.is_false(data_dict["Network"]["Enabled"])
        with allure.step("Уведомления не включены"):
            check.is_false(data_dict["Enabled"])
        with allure.step("Адрес отправки уведомлений"):
            check.equal(data_dict["AddressTo"], "b@test.com")
        with allure.step("Язык отправки уведомлений"):
            check.equal(data_dict["LanguageID"], "RUS")

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "SearchServer": {"type": "object"},
                "Endpoint": {"type": "object"},
                "Enabled": {"type": "boolean"},
                "AddressTo": {"type": "string"},
            },
            "required": ["SearchServer", "Endpoint", "Enabled", "AddressTo"],
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
                    schema_models.SchemaModelsRESTAPIV2.MailNotificationSettings,
                    data_dict,
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsRESTAPIV2.MailNotificationSettings.SearchServer.parse_obj(
                data_dict["SearchServer"]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
