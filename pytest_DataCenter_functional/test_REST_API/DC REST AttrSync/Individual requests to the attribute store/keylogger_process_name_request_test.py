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

path = "https://" + base_url_dc() + ":9088/datacenter/api/v2/attributes/prog"
body = {"protocolIds": ["d7b99489-e21d-478d-9b9e-ff363f8af447"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Individual requests to the attribute store")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени процесса в хранилище атрибутов по индексу Keylogger")
class TestRequestKeyloggerProcessNameInAttributeStoreByIndexes:
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
            "c:\\windows\\system32\\stikynot.exe",
            "c:\\windows\\system32\\cmd.exe",
            "c:\\program files\\microsoft office\\root\\office16\\winword.exe",
            "c:\\program files\\the bat!\\thebat.exe",
            "c:\\windows\\system32\\rdpclip.exe",
            "c:\\windows\\system32\\windowspowershell\\v1.0\\powershell_ise.exe",
            "c:\\program files\\google\\chrome\\application\\chrome.exe",
            "c:\\program files\\notepad++\\notepad++.exe",
            "c:\\program files (x86)\\total commander\\totalcmd.exe",
            "c:\\users\\admin2\\appdata\\roaming\\icq\\bin\\icq.exe",
            "c:\\windows\\systemapps\\microsoft.windows.search_cw5n1h2txyewy\\searchapp.exe",
            "c:\\windows\\systemapps\\microsoftwindows.client.cbs_cw5n1h2txyewy\\searchhost.exe",
        ]
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(parsed_data))
        with allure.step("Кол-во данных"):
            check.equal(len(parsed_data), 12)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
