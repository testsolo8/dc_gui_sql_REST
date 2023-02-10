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
body = {"protocolIds": ["726d061e-b58a-49c7-ab21-6dc32e165a92"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request filename in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени файла в хранилище атрибутов по индексу FTP")
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
            "\\482 стр - о.генри. том 3 (2006)_1 стр.9.pdf",
            "\\01 track 03.wav",
            "\\15.jpg",
            "\\01 track 07.wav",
            "\\01 track 01.wav",
            "\\01 - yellow submarine.mp3",
            "\\01 track 06.wav",
            "\\01 track 04.wav",
            "\\01 track 02.wav",
            "\\05 track 04.wav",
            "\\16.jpg",
            "\\14.jpg",
            "\\482 стр - о.генри. том 3 (2006)_1 стр.11.pdf",
            "\\01 track 05.wav",
            "\\searchinform_x_bondarenko.pdf",
            "\\482 стр - о.генри. том 3 (2006)_1 стр.10.pdf",
        ]
        data_dict = r.json()
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(data_dict))
        with allure.step("Кол-во данных"):
            check.equal(len(data_dict), 16)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
