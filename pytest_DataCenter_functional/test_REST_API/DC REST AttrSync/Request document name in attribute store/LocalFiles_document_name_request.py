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
body = {"protocolIds": ["7e7a1c45-3bf8-4a2f-80b3-6a55d7c6f7ad"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request document name in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени документа в хранилище атрибутов по индексу LocalFiles")
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
            "dialogi_42.txt",
            "file____c__eb882234_4reguchiy_instrument.files_image051.wmz",
            "file____c__eb882234_4reguchiy_instrument.files_image085.wmz",
            "file____c__eb882234_4reguchiy_instrument.files_image095",
            "file____c__eb882234_4reguchiy_instrument.files_image053",
            "file____c__eb882234_4reguchiy_instrument.files_image071",
            "file____c__eb882234_4reguchiy_instrument.files_image104.wmz",
            "file____c__eb882234_4reguchiy_instrument.files_image083.wmz",
            "file____c__eb882234_4reguchiy_instrument.files_image029.wmz",
            "один плюс один_page5.tiff",
            "ocr_set.htm",
            "file____c__eb882234_4reguchiy_instrument.files_image028.wmz",
            "file____c__eb882234_4reguchiy_instrument.files_image131.wmz",
            "file____c__eb882234_4reguchiy_instrument.files_image078.wmz",
            "file____c__eb882234_4reguchiy_instrument.files_image040.wmz",
            "file____c__eb882234_4reguchiy_instrument.files_image082.wmz",
            "file____c__eb882234_4reguchiy_instrument.files_image011",
            "dialogi_26.txt",
            "file____c__eb882234_4reguchiy_instrument.files_image072",
            "file____c__eb882234_4reguchiy_instrument.files_image104",
            "file____c__eb882234_4reguchiy_instrument.files_image112.wmz",
            "flim-moduloalongt-tscpc.ome.tiff",
            "file____c__eb882234_4reguchiy_instrument.files_image041.wmz",
            "file____c__eb882234_4reguchiy_instrument.files_image109.png",
            "file____c__eb882234_4reguchiy_instrument.files_image101.wmz",
            "222.xls",
        ]
        data_dict = r.json()
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(data_dict))
        with allure.step("Кол-во данных"):
            check.equal(len(data_dict), 427)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
