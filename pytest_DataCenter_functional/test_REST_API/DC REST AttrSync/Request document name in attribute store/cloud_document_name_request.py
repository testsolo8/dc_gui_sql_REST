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
body = {"protocolIds": ["9b6ff2e2-565e-4adf-945f-52c1332079d4"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request document name in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени документа в хранилище атрибутов по индексу Cloud")
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
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        check.greater_equal(len(parsed_data), 1)
        check.less_equal(len(parsed_data), 1000)

    @allure.title("Возвращаемые данные")
    def test_return_data(self):
        data = [
            "1000va-price.xlsx\u0026ved=2ahukewjwgrho7-j4ahvpvpedhvefc3i4kbawegqigrab",
            "0dvfj7kbhxt541yv2l51a655i2hde5f6.xlsx\u0026ved=2ahukewir2nlz7-j4ahxovfedhvxmcee4fbawegqiahab",
            "anketa-2021.xlsx\u0026ved=2ahukewijpfrj8ej4ahuaqpedhxlwcnc4chawegqiahab",
            "93.jpg",
            "заявление-анкета+согласие клиента на обработку пдн2 (2).xlsm\u0026ved=2ahukewj6mdky8ej4ahu-qfedhssybmu4kbawegqifbab",
            "65.jpg",
            "260 стр - козлов с.в.  - баики офицерского кафе (малая серия)-2003_часть31.pdf",
            "standaloneupdate_2022-01-30_091218_6876-7192.log",
            "standaloneupdater-2022-02-03.0956.11412.1.odl",
            "price-bukhgalterskie-uslugi-baliot.xlsx\u0026ved=2ahukewiqqynj8uj4ahuhxvedhzk5a1iqfnoecaqqaq",
            "mk49i2gljeai1779uaexm22p6zcsyykv.xlsx\u0026ved=2ahukewjr0mgw8uj4ahwwx_edhyf4cp84hhawegqifbab",
            "dacffac0886c45d5aee4a2221b8da928_1",
            "134.jpg",
            "settingsicon.svg",
            "59.jpg",
            "anketanapodkluchenieiskepsv42.xlsx\u0026ved=2ahukewirrj-i8uj4ahvuxvedhshta844fbawegqibrab",
            "45.jpg",
            "kopiya-anketa-zamestitelya-rukovoditelya-kompanii-otvechayushchego-za-tekhnologicheskoe-i-innovatsionnoe-razvitie_26-08-2019.xlsx\u0026ved=2ahukewi_ykyp8oj4ahwgvjuchs2fass4chawegqibrab",
            "standaloneupdate_2022-01-28_085223_11608-696.log",
        ]
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(parsed_data))
        with allure.step("Кол-во данных"):
            check.equal(len(parsed_data), 474)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
