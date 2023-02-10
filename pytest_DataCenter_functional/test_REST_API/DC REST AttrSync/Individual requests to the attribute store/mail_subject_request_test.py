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

path = "https://" + base_url_dc() + ":9088/datacenter/api/v2/attributes/subject"
body = {"protocolIds": ["e005b28a-f9eb-4855-aaad-b69a80e710b8"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Individual requests to the attribute store")
@pytest.mark.testRESTAPI
@allure.story("Запрос темы письма в хранилище атрибутов по индексу Mail")
class TestRequestMailSubjectInAttributeStoreByIndexes:
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
            "you might like: 500pcs thank you for my small business s...",
            "01-02-2022--004",
            "sql-kib. письмо 184",
            "sql-kib. письмо 51",
            "sql-kib. письмо 165",
            "22-02-2022--002",
            "код подтверждения slack: pl8-mdx",
            "нужно успеть  adidas, levi’s, pandora и не только",
            "sql-kib. письмо 84",
            "sql-kib. письмо 120",
            "письмо двум адресатам",
            "изменения в условиях использования youtube",
            "сергеи, проверьте настроики своего аккаунта google",
            "sql-kib. письмо 19",
            "sql-kib. письмо 65",
            "welcome to mailtrap! your test emails are now safe",
            "3 фаила в rar - nopass",
            "электронныи чек платформа офд",
            "s.kuzin.si приглашает вас вместе работать в slack",
            "sql-kib. письмо 87",
            "угадаите с подарком 🙋🏻‍♂️ или порадуите себя 💝",
            "мы заметили новыи вход в ваш аккаунт",
            "обновления в наших условиях обслуживания и политике конфиденциальности",
            "sql-kib. письмо 138",
            "sql-kib. письмо 160",
            "sql-kib. письмо 188",
            "sql-kib. письмо 30",
            "looking for this? 2/3/5pcs seamless women yoga set workout...",
            "3 фаила в zip - pass - 12345",
            "сергеи, подтвердите настроики своего аккаунта google на устроистве windows",
            "ооо маркетплеис электронныи чек",
            "sql-kib. письмо 95",
            "sql-kib. письмо 1",
            "sql-kib. письмо 157",
            "оповещение системы безопасности",
            "3 фаила в rar - pass - 12345",
            "endpointcontroller quarantine test mail",
            "seen this? big size 39-47 desert tactical mens boot...",
            "сергеи сергеев приглашает вас вместе работать в slack",
            "3 фаила в zip - nopass",
            "вход в аккаунт slack с нового устроиства",
        ]
        data_dict = r.json()
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(data_dict))
        with allure.step("Кол-во данных"):
            check.equal(len(data_dict), 280)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
