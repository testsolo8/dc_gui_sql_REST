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
body = {"protocolIds": ["9ff5dd77-debb-4c06-9241-84400d967fa9"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request filename in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени файла в хранилище атрибутов по индексу YandexDisk")
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
            "/ffffffffffffff/xxx1.7z.130",
            "/загрузки/soft_huawei-modem-3.5_(04.12.2014).rar:soft huawei modem 3.5.exe:data.bin:common\\core.dll",
            "/загрузки/soft_huawei-modem-3.5_(04.12.2014).rar:soft huawei modem 3.5.exe:data.bin:common\\driver\\driver\\x64\\ewmdm2k.inf",
            "wvm33o4m;/ffffffffffffff/333.zip.001.multipart:test88888.txt",
            "/загрузки/soft_huawei-modem-3.5_(04.12.2014).rar:soft huawei modem 3.5.exe:data.bin:common\\skin\\default\\images\\title_bar.png",
            "/загрузки/soft_huawei-modem-3.5_(04.12.2014).rar:soft huawei modem 3.5.exe:data.bin:common\\plugins\\language\\1045.ini",
            "/загрузки/soft_huawei-modem-3.5_(04.12.2014).rar:soft huawei modem 3.5.exe:data.bin:common\\skin\\default\\images\\tree_widget_bg_line_curve_box.png",
            "/загрузки/soft_huawei-modem-3.5_(04.12.2014).rar:soft huawei modem 3.5.exe:data.bin:common\\driver\\driver\\x86\\ew_cdcecm.sys",
            "/ffffffffffffff/xxx1.7z.008",
            "/загрузки/soft_huawei-modem-3.5_(04.12.2014).rar:soft huawei modem 3.5.exe:data.bin:common\\skin\\default\\images\\tool_child_hover.png",
            "/загрузки/soft_huawei-modem-3.5_(04.12.2014).rar:soft huawei modem 3.5.exe:data.bin:common\\plugins\\callloguiplugin\\tab_callhistory_send message.png",
            "/загрузки/soft_huawei-modem-3.5_(04.12.2014).rar:soft huawei modem 3.5.exe:data.bin:common\\skin\\default\\images\\tool_child_press.png",
            "/загрузки/soft_huawei-modem-3.5_(04.12.2014).rar:soft huawei modem 3.5.exe:data.bin:common\\driver\\driver\\x64\\ew_juwwanecm.inf",
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
