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

path = "https://" + base_url_dc() + ":9088/datacenter/api/v2/attributes/recipients"
body = {"protocolIds": ["e005b28a-f9eb-4855-aaad-b69a80e710b8"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Individual requests to the attribute store")
@pytest.mark.testRESTAPI
@allure.story("Запрос всех получателей в хранилище атрибутов по индексу Mail")
class TestRequestMailAllRecipientsInAttributeStoreByIndexes:
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
            "sand.m.an.k.uz.in@gmail.com",
            "sand.m.an.k.uz.i.n@gmail.com",
            "sakuzin131@gmail.com",
            "sakuzin131 \u003csakuzin131@gmail.com\u003e",
            "sand.m.an.k.uzi.n@gmail.com",
            "si_kuzin \u003csi_kuzin@bk.ru\u003e",
            "si_kuzin@bk.ru",
            "sand.ma.n.k.uz.i.n@gmail.com",
            "sandman.kuzin@gmail.com",
            "sandman.k.u.z.i.n@gmail.com",
            "san.dman.ku.z.i.n@gmail.com",
            "sand.m.a.n.ku.zi.n@gmail.com",
            "admin1@test.net",
            "sand.m.a.n.kuzi.n@gmail.com",
            "admin2@test.net",
            "sandman.k.u.zi.n@gmail.com",
            "s.kuzin.si@yandex.ru",
            "sand.ma.n.kuzi.n@gmail.com",
            "сергеи сергеев \u003cs.kuzin.rnd@rambler.ru\u003e",
            "sand.ma.n.k.u.z.i.n@gmail.com",
            "sand.m.a.n.kuz.i.n@gmail.com",
            "sand.m.an.k.u.zi.n@gmail.com",
            "иван иванов \u003cadmin1@test.net\u003e",
            "sandma.n.k.uzin@gmail.com",
        ]
        data_dict = r.json()
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(data_dict))
        with allure.step("Кол-во данных"):
            check.equal(len(data_dict), 24)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
