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
body = {"protocolIds": ["0e28e287-5c61-4124-b1de-bccef5b1abad"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request filename in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени файла в хранилище атрибутов по индексу FileAudit")
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
            "\\\\station1.test.net\\c$\\fa1\\1\\100 фаилов rar - pass - qwerty\\лермонтов_76_pass_qwerty.rar",
            "\\\\station1.test.net\\c$\\fa1\\1\\100 фаилов rar - pass - qwerty\\лермонтов_87_pass_qwerty.rar",
            "\\\\station1.test.net\\c$\\fa1\\1\\100 фаилов zip - pass - password\\пушкин_11_pass_password.zip",
            "\\\\station1.test.net\\c$\\fa1\\password\\100 фаилов zip - pass - password\\пушкин_7_pass_password.zip",
            "\\\\station1.test.net\\c$\\fa1\\password\\100 фаилов zip - pass - password\\пушкин_40_pass_password.zip",
            "\\\\station1.test.net\\c$\\fa1\\1\\100 фаилов 7z - pass - 12345\\istorii_97_pass_12345.7z",
            "\\\\station1.test.net\\c$\\fa1\\100 фаилов 7z - pass - 12345\\istorii_37_pass_12345.7z",
        ]
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(parsed_data))
        with allure.step("Кол-во данных"):
            check.equal(len(parsed_data), 713)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
