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
body = {"protocolIds": ["04d1b18b-6b6c-4d2f-b096-a4165dca5eed"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request filename in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени файла в хранилище атрибутов по индексу IM")
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
            "wallhaven-0j28xm.jpg",
            "pavlov_leningrad-v-blokade_rulit_me_554505 (5).docx",
            "amy smart.jpg",
            "margulis_photoshop-dlya-professionalov-klassicheskoe-rukovodstvo-po-cvetokorrekci-_rulit_me_589293 (4).docx",
            "slovar_11.txt",
            "tysyacha_7.txt",
            "tysyacha_1.txt",
            "52 стр - baron_saga-ob-eskkare_3_konflikt-imperiy_rulit_me_671974 (6).docx",
            "pavlov_leningrad-v-blokade_rulit_me_554505 (8).docx",
            "b3_6pak.png",
            "wallhaven-0pvdym.jpg",
            "jf3.jpg",
            "pavlov_leningrad-v-blokade_rulit_me_554505 (7).docx",
            "пушкин.jpg",
            "pavlov_leningrad-v-blokade_rulit_me_554505 (4).docx",
            "contacts.txt",
            "ural_master_120x85_2l-01.jpg",
            "th8.jpg",
            "pavlov_leningrad-v-blokade_rulit_me_554505 (6).docx",
        ]
        data_dict = r.json()
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(data_dict))
        with allure.step("Кол-во данных"):
            check.equal(len(data_dict), 19)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
