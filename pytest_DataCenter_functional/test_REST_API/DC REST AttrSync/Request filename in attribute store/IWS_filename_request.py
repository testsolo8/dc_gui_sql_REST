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
body = {"protocolIds": ["27a7d932-1968-4de2-9700-9c06f104e4c7"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request filename in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени файла в хранилище атрибутов по индексу IWS")
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
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        check.greater_equal(len(parsed_data), 1)
        check.less_equal(len(parsed_data), 1000)

    @allure.title("Возвращаемые данные")
    def test_return_data(self):
        data = [
            "c:\\iws5\\ars-label6.bmp",
            "c:\\iws2\\books2010.accdb",
            "c:\\iws2\\books2010.accdb:jobs",
            "c:\\iws2\\books2010.accdb:allstate",
            "c:\\iws2\\books2010.accdb:bookauthor",
            "c:\\iws3\\dialogi_1.txt",
            "c:\\iws2\\books2010.accdb:~tmpclp407071",
            "c:\\iws3\\222.xls",
            "c:\\iws1\\1 стр - income.pdf",
            "c:\\iws1\\141 стр - ognennaya-reka_rulit_me_668901 (1).doc",
            "c:\\iws2\\calendar_2010.mpp",
            "c:\\iws5\\dialogi_1.7z",
            "c:\\iws5\\example.odt",
            "c:\\iws2\\books2010.accdb:authors",
            "c:\\iws2\\books2010.accdb:books",
            "c:\\iws2\\books2010.accdb:allsubject",
            "c:\\iws3\\timeline.vsd",
            "c:\\iws1\\досье (с колонтитулами).xlsx",
            "c:\\iws2\\books2010.accdb:employees",
            "c:\\iws2\\суд ускоренного режима.htm",
            "c:\\iws5\\dialogi_1.7z:dialogi_1.txt",
            "c:\\iws3\\ods_sample.ods",
            "c:\\iws2\\books2010.accdb:publishers",
            "c:\\iws2\\books2010.accdb:allsex",
        ]
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(parsed_data))
        with allure.step("Кол-во данных"):
            check.equal(len(parsed_data), 24)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
