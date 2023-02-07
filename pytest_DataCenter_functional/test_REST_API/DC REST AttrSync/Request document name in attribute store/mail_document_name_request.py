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
body = {"protocolIds": ["e005b28a-f9eb-4855-aaad-b69a80e710b8"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request document name in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени документа в хранилище атрибутов по индексу Mail")
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
            "499 стр - искусство как вид жизни.doc",
            "200.pdf",
            "965 стр - операция рагнарек.docx",
            "лермонтов_25.txt",
            "682 стр - сердце единорога.doc",
            "istorii_4.txt",
            "peppershnein_pavel__slovar_terminov_moskovskoi_konceptualnoi_shkoly_www.litmir.net_97447.txt",
            "записки психиатра_часть15.pdf",
            "748 стр - граф монте-кристо.doc",
            "zolotaya_planeta_18.txt",
            "vojna_i_mir._tom_2.txt",
            "2726 стр - полное собрание трагедии в одном томе.docx",
            "184.txt",
            "95.jpg",
            "449.jpg",
            "869 стр - трактат о космическом огне.docx",
            "253.txt",
            "187.jpg",
            "306.pdf",
            "kononenko_maksim__vladimir_vladimirovich_www.litmir.net_88219.txt",
            "пароль password внутри архив с паролем 12345 в котором txt.rar",
            "283.pdf",
            "34.docx",
            "179.jpg",
            "тихии дон.txt",
            "пароль 12345 внутри архив с паролем password в котором txt.zip",
            "пушкин_13_pass_password.zip",
            "99.doc",
            "лермонтов_24.txt",
            "246.pdf",
            "161.pdf",
            "ermishin_oleg__aforizmy_www.litmir.net_275.txt",
            "2150 стр - 1000 и одна ночь.docx",
            "toinbi_arnold__postichenie_istorii_www.litmir.net_71869.txt",
            "в архиве архив в котором txt.rar",
            "244.txt",
            "333 стр - мировои кризис.doc",
            "383.pdf",
            "64.txt",
            "535 стр - the-children-of-zegandaria.docx",
        ]
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(parsed_data))
        with allure.step("Кол-во данных"):
            check.equal(len(parsed_data), 490)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
