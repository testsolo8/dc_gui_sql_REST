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

path = "https://" + base_url_dc() + ":9088/datacenter/api/v2/attributes/comp"
body = {"protocolIds": ["04d1b18b-6b6c-4d2f-b096-a4165dca5eed"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request computer name in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени компьютера в хранилище атрибутов по индексу IM")
class TestRequestComputerNameInAttributeStoreByIndexes:
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
        data = ["station1.test.net", "station2.test.net", "station3.test.net"]
        data_dict = r.json()
        check.equal(set(data), set(data_dict))

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
