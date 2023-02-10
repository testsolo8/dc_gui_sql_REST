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
body = {"protocolIds": ["9ff5dd77-debb-4c06-9241-84400d967fa9"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request document name in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени документа в хранилище атрибутов по индексу YandexDisk")
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
            "common\\plugins\\language\\1046.ini",
            "xxx1.7z.024",
            "common\\plugins\\addrbookuiplugin\\pb_icon_delect.png",
            "common\\plugins\\settinguiplugin\\settinguiplugin_en-us.lang",
            "common\\skin\\default\\images\\sel_radio_button_disabled.png",
            "mixed(24).jpg",
            "data.bin",
            "doc\\rtf-spec-1.7.rtf",
            "common\\skin\\default\\images\\call_button_pressed.png",
            "common\\plugins\\calluiplugin\\callvoice.wav",
            "xxx1.7z.128",
            "common\\plugins\\ussduiplugin\\ussduiplugin_en-us.lang",
            "common\\plugins\\language\\1034.ini",
            "xxx1.7z.101",
            "qqq.txt",
            "common\\driver\\driver\\x86\\ewsmartcard.cat",
            "xxx1.7z.012",
            "xxx1.7z.001",
            "common\\plugins\\smsuiplugin\\sms_reply.png",
            "common\\plugins\\statusbarmgrplugin\\switchermainmouseover.png",
            "common\\plugins\\statusbarmgrplugin\\status bar_icon_upload.png",
            "sample.odp",
            "common\\plugins\\dialupuiplugin\\seamless_button_profile_focus.bmp",
            "common\\plugins\\smsuiplugin\\sms_new.png",
            "common\\config\\sdkplugins.xml",
            "common\\autorun\\autorununinstall.exe",
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
