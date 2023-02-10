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
body = {"protocolIds": ["7e7a1c45-3bf8-4a2f-80b3-6a55d7c6f7ad"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request filename in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени файла в хранилище атрибутов по индексу LocalFiles")
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
            "c:\\files misc file types\\html\\4reguchiy_instrument.mht:file____c__eb882234_4reguchiy_instrument.files_image029.wmz:file____c__eb882234_4reguchiy_instrument.files_image029",
            "c:\\files misc file types\\html\\4reguchiy_instrument.mht:file____c__eb882234_4reguchiy_instrument.files_image067.wmz",
            "c:\\files misc file types\\html\\4reguchiy_instrument.mht:file____c__eb882234_4reguchiy_instrument.files_image072.wmz",
            "c:\\files misc file types\\html\\4reguchiy_instrument.mht:file____c__eb882234_4reguchiy_instrument.files_image033.wmz",
            "c:\\files misc file types\\архивы\\zip\\from 7z\\пропавшая экспедиция.zip.001",
            "c:\\files misc file types\\html\\4reguchiy_instrument.mht:file____c__eb882234_4reguchiy_instrument.files_image002.png",
            "c:\\files misc file types\\html\\4reguchiy_instrument.mht:file____c__eb882234_4reguchiy_instrument.files_image111.wmz:file____c__eb882234_4reguchiy_instrument.files_image111",
            "c:\\files misc file types\\html\\4reguchiy_instrument.mht:file____c__eb882234_4reguchiy_instrument.files_image043.wmz",
            "c:\\files misc file types\\xls\\ods_sample.ods",
            "y40pmifs;c:\\files misc file types\\архивы\\zip\\zip.zip.001.multipart:dialogi_41.txt",
            "c:\\files misc file types\\eml\\backup2.pst:6:test00000.gif",
            "c:\\files misc file types\\eml\\backup2.pst:28:message01.eml:test11111.xls",
        ]
        data_dict = r.json()
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(data_dict))
        with allure.step("Кол-во данных"):
            check.equal(len(data_dict), 477)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
