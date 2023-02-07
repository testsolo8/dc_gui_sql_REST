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
body = {"protocolIds": ["bec53488-3333-4234-9653-1b6c0f3ebf14"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request filename in attribute store by DB")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени файла в хранилище атрибутов по бд File")
class TestRequestFilenameInAttributeStoreByDB:
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
            "C:\\DIST\\SQLDataGenerator\\Files\\468 стр - Слово о полку Игореве_417.pdf",
            "C:\\FA2\\100 файлов RAR - pass - qwerty\\Лермонтов_29_pass_qwerty.rar",
            "\\\\dc\\SOFT\\__Файлы для перехвата\\_DOC, DOCX, ODT, SXW, STW, OTT, FODT, RTF, FB2, FR3\\DOCX\\721 х 1 стр - Вершина мира\\721 х 1 стр - Вершина мира-234.docx",
            "C:\\DIST\\SQLDataGenerator\\Files\\468 стр - Слово о полку Игореве_100.pdf",
            "C:\\DIST\\SQLDataGenerator\\Files\\468 стр - Слово о полку Игореве_200.pdf",
            "C:\\DIST\\SQLDataGenerator\\Files\\721 х 1 стр - Вершина мира-629.docx",
            "\\\\dc\\SOFT\\__Файлы для перехвата\\___OCR\\_PDF\\Файлы по 1 странице\\481 стр - О.Генри. Том 3 (2006)\\482 стр - О.Генри. Том 3 (2006)_1 стр.329.pdf",
            "C:\\DIST\\SQLDataGenerator\\Files\\482 стр - О.Генри. Том 3 (2006)_1 стр.323.pdf",
            "C:\\FA2\\100 файлов RAR - pass - qwerty\\Лермонтов_24_pass_qwerty.rar",
            "C:\\DIST\\SQLDataGenerator\\Files\\721 х 1 стр - Вершина мира-624.docx",
            "\\\\dc\\SOFT\\__Файлы для перехвата\\_DOC, DOCX, ODT, SXW, STW, OTT, FODT, RTF, FB2, FR3\\DOCX\\721 х 1 стр - Вершина мира\\721 х 1 стр - Вершина мира-518.docx",
            "C:\\FA2\\1\\100 файлов ZIP - pass - password\\Пушкин_56_pass_password.zip",
        ]
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(parsed_data))
        with allure.step("Кол-во данных"):
            check.greater_equal(len(parsed_data), 1000)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
