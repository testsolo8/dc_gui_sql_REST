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
body = {"protocolIds": ["4d132b55-772b-43a4-87b1-0798e7f0b07c"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request document name in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени документа в хранилище атрибутов по индексу Print")
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
            "истоки нашего режима_1070.txt – блокнот",
            "vojna_i_mir(7).txt – блокнот",
            "vojna_i_mir(87).txt – блокнот",
            "vojna_i_mir(158).txt – блокнот",
            "истоки нашего режима_1285.txt – блокнот",
            "microsoft word - 801 х 1 стр - время перемен-1.docx",
            "истоки нашего режима_1285.txt – блокнот:page_1.jpg",
            "vojna_i_mir(158).txt – блокнот:page_1.jpg",
            "eskriva_hosemariya__put_www.litmir.txt – блокнот:page_1.jpg",
            "toinbi_arnold__postichenie_istorii_www.litmir(168).txt – блокнот:page_1.jpg",
            "истоки нашего режима_1542.txt – блокнот",
            "eskriva_hosemariya__put_www.litmir(1).txt – блокнот:page_1.jpg",
            "открытие мира (1035).txt – блокнот:page_1.jpg",
            "vojna_i_mir(7).txt – блокнот:page_1.jpg",
            "открытие мира (1014).txt – блокнот:page_1.jpg",
            "eskriva_hosemariya__put_www.litmir.txt – блокнот",
            "истоки нашего режима_1285.txt – блокнот:page_2.jpg",
            "vojna_i_mir(27).txt – блокнот:page_1.jpg",
            "vojna_i_mir(1).txt – блокнот:page_1.jpg",
            "истоки нашего режима_1059.txt – блокнот",
            "eskriva_hosemariya__put_www.litmir(1).txt – блокнот",
            "открытие мира (1035).txt – блокнот",
            "page_2.jpg",
            "toinbi_arnold__postichenie_istorii_www.litmir(168).txt – блокнот",
            "vojna_i_mir(27).txt – блокнот",
            "vojna_i_mir.txt – блокнот",
            "vojna_i_mir.txt – блокнот:page_1.jpg",
            "vojna_i_mir(1).txt – блокнот",
            "vojna_i_mir(119).txt – блокнот",
            "истоки нашего режима_1070.txt – блокнот:page_1.jpg",
            "page_1.jpg",
            "открытие мира (1014).txt – блокнот",
        ]
        data_dict = r.json()
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(data_dict))
        with allure.step("Кол-во данных"):
            check.equal(len(data_dict), 32)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
