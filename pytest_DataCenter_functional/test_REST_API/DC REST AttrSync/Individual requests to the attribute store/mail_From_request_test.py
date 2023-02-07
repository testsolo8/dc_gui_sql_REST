# Standart libraries
import json

# Third party packages
import allure
import pytest
import pytest_check as check
import requests
from jsonschema import validate

# My packages
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc

path = "https://" + base_url_dc() + ":9088/datacenter/api/v2/attributes/from"
body = {"protocolIds": ["e005b28a-f9eb-4855-aaad-b69a80e710b8"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Individual requests to the attribute store")
@pytest.mark.testRESTAPI
@allure.story("Запрос 'От кого' в хранилище атрибутов по индексу Mail")
class TestRequestMailFromInAttributeStoreByIndexes:
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

    @allure.title("Ограничение на кол-во возвращаемых данных")
    def test_number_of_strings(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        check.greater_equal(len(parsed_data), 1)
        check.less_equal(len(parsed_data), 1000)

    @allure.title("Возвращаемые данные")
    def test_return_data(self):
        data = [
            "firefox accounts \u003caccounts@firefox.com\u003e",
            "aliexpress \u003ccare26@aliexpress.com\u003e",
            "no-reply@dropbox.com",
            "feedback@slack.com",
            "aliexpress \u003ccare16@aliexpress.com\u003e",
            "slack \u003cno-reply-jzbsbiuruxluey8xr5ykvyxp@slack.com\u003e",
            "сергеи кузин \u003csi_kuzin@bk.ru\u003e",
            "aliexpress \u003ccare07@aliexpress.com\u003e",
            "aliexpress \u003ccare25@aliexpress.com\u003e",
            "andriy@mailtrap.io",
            "account-se...@accountprotection.microsoft.com",
            "сбер id \u003cnoreply@sber.ru\u003e",
            "aliexpress \u003ccare23@aliexpress.com\u003e",
            "aliexpress \u003ccare13@aliexpress.com\u003e",
            "slack \u003cfeedback@slack.com\u003e",
            "aliexpress \u003ccare21@aliexpress.com\u003e",
            "aliexpress \u003cnotice@info.aliexpress.com\u003e",
            "si_kuzin@bk.ru",
        ]
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(parsed_data))
        with allure.step("Кол-во данных"):
            check.equal(len(parsed_data), 44)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
