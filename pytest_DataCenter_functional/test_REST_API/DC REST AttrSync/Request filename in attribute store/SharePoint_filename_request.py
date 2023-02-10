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
body = {"protocolIds": ["c86efe1c-9503-4317-92dd-a9ea09b3a1fd"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request filename in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени файла в хранилище атрибутов по индексу SharePoint")
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
            "http://10.0.2.175/documents/txt/_1000 фаилов txt/dialogi_615.txt",
            "http://10.0.2.175/documents/txt/_1000 фаилов txt/dialogi_884.txt",
            "http://10.0.2.175/documents/zip/_тестовыи пакет 1 (jpg + pdf).zip.005",
            "http://10.0.2.175/documents/txt/_1000 фаилов txt/dialogi_452.txt",
            "http://10.0.2.175/documents/txt/_1000 фаилов txt/dialogi_386.txt",
            "http://10.0.2.175/documents/txt/_1000 фаилов txt/dialogi_716.txt",
            "http://10.0.2.175/documents/txt/_1000 фаилов txt/dialogi_545.txt",
            "http://10.0.2.175/documents/txt/_1000 фаилов txt/dialogi_869.txt",
            "http://10.0.2.175/documents/txt/_1000 фаилов txt/dialogi_753.txt",
            "http://10.0.2.175/documents/txt/_1000 фаилов txt/dialogi_573.txt",
            "http://10.0.2.175/style library/xsl style sheets/header.xsl",
            "http://10.0.2.175/documents/txt/_1000 фаилов txt/dialogi_952.txt",
            "http://10.0.2.175/documents/zip/chlyabinskoe.zip:chlyabinskoe\\chel_live_120x85_1l-01.jpg",
            "http://10.0.2.175/documents/txt/_1000 фаилов txt/dialogi_161.txt",
        ]
        data_dict = r.json()
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(data_dict))
        with allure.step("Кол-во данных"):
            check.greater_equal(len(data_dict), 1000)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
