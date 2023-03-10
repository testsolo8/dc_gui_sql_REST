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

path = "https://" + base_url_dc() + ":9088/datacenter/api/v2/attributes/filename"
body = {"protocolIds": ["e005b28a-f9eb-4855-aaad-b69a80e710b8"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request filename in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени файла в хранилище атрибутов по индексу Mail")
class TestRequestFilenameInAttributeStoreByIndexes:
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
            "468 стр - visual basic 6.doc",
            "284.pdf",
            "3 фаила - pass - 12345.zip:пушкин_15.txt",
            "vojna_i_mir._tom_4.txt",
            "vojna_i_mir._tom_1.txt",
            "pdf не текст 2 - pass - 12345.rar",
            "208.pdf",
            "pdf не текст 2 - pass - 12345.zip:записки психиатра_часть10.pdf",
            "149.doc",
            "pdf не текст - pass - 12345.zip:анекдоты 2014_часть3.pdf",
            "pdf не текст 2 - pass - 12345.zip",
            "лермонтов_10_pass_qwerty.rar:лермонтов_10.txt",
            "пароль 12345 внутри архив с паролем password в котором txt.zip",
            "berrouz_edgar__tarzan_sbornik_rasskazov_www.litmir.net_3396.txt",
        ]
        data_dict = r.json()
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(data_dict))
        with allure.step("Кол-во данных"):
            check.equal(len(data_dict), 494)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
