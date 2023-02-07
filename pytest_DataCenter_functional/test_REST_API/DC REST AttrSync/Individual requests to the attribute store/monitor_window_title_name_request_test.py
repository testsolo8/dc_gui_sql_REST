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

path = "https://" + base_url_dc() + ":9088/datacenter/api/v2/attributes/title"
body = {"protocolIds": ["1888d8a9-00fe-449d-b35b-94ed7b46501e"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Individual requests to the attribute store")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени заголовка окна в хранилище атрибутов по бд Monitor")
class TestRequestMonitorWindowTitleNameInAttributeStoreByIndexes:
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
            "Обзор аккумуляторного мультитула (реноватора, осцилляторного резака) makita dtm51z - google chrome",
            "как узнать версию офиса — Яндекс: нашлось 11 млн результатов - google chrome",
            "Как восстановить содержимое поврежденной базы microsoft sql server - google chrome",
            "Приложения и утилиты - google chrome",
            "«Известия»: автоконцерны начали определяться с планами насчёт России - google chrome",
            "Акустическая система sven ms-1821 уже в России / Блог компании sven / Компании / ixbt live - google chrome",
            "Можно ли спасти безнадежный rar-архив: восстанавливаем повреждённый файл - google chrome",
            "Новости технологий, обзоры гаджетов, смартфонов, бытовой техники и автомобилей - google chrome",
            "sven ms-1821 — Яндекс: нашёлся 1 млн результатов - google chrome",
            "create sql server database with powershell - google chrome",
        ]
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(parsed_data))
        with allure.step("Кол-во данных"):
            check.equal(len(parsed_data), 10)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
