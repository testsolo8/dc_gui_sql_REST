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

path = "https://" + base_url_dc() + ":9088/datacenter/api/v2/attributes/doc_name"
body = {"protocolIds": ["0e28e287-5c61-4124-b1de-bccef5b1abad"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request document name in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени документа в хранилище атрибутов по индексу FileAudit")
class TestRequestDocumentNameInAttributeStoreByIndexes:
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
        check.greater_equal(len(data_dict), 1)
        check.less_equal(len(data_dict), 1000)

    @allure.title("Возвращаемые данные")
    def test_return_data(self):
        data = [
            "istorii_69_pass_12345.7z",
            "лермонтов_64_pass_qwerty.rar",
            "istorii_20_pass_12345.7z",
            "пушкин_22_pass_password.zip",
            "istorii_93_pass_12345.7z",
            "пушкин_28_pass_password.zip",
            "istorii_49_pass_12345.7z",
            "лермонтов_27_pass_qwerty.rar",
            "лермонтов_11_pass_qwerty.rar",
            "лермонтов_47_pass_qwerty.rar",
            "пушкин_57_pass_password.zip",
            "лермонтов_29_pass_qwerty.rar",
            "пушкин_101_pass_password.zip",
            "istorii_34_pass_12345.7z",
            "пушкин_90_pass_password.zip",
            "istorii_99_pass_12345.7z",
            "istorii_94_pass_12345.7z",
            "лермонтов_51_pass_qwerty.rar",
            "лермонтов_59_pass_qwerty.rar",
            "лермонтов_67_pass_qwerty.rar",
            "лермонтов_36_pass_qwerty.rar",
            "vojna_i_mir._tom_4_pass - password.zip",
            "пушкин_21_pass_password.zip",
            "istorii_66_pass_12345.7z",
            "istorii_13_pass_12345.7z",
            "лермонтов_97_pass_qwerty.rar",
            "пушкин_8_pass_password.zip",
            "istorii_19_pass_12345.7z",
            "пушкин_24_pass_password.zip",
            "пушкин_70_pass_password.zip",
            "istorii_67_pass_12345.7z",
            "istorii_89_pass_12345.7z",
            "лермонтов_76_pass_qwerty.rar",
            "лермонтов_79_pass_qwerty.rar",
            "пушкин_67_pass_password.zip",
            "лермонтов_83_pass_qwerty.rar",
            "istorii_50_pass_12345.7z",
            "лермонтов_15_pass_qwerty.rar",
            "лермонтов_10_pass_qwerty.rar",
        ]
        data_dict = r.json()
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(data_dict))
        with allure.step("Кол-во данных"):
            check.equal(len(data_dict), 312)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
