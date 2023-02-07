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

path = "https://" + base_url_dc() + ":9088/datacenter/api/v2/attributes/caption"
body = {"protocolIds": ["fd165b6f-63ca-413d-a3c0-109a9906a491"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Individual requests to the attribute store")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени заголовка в хранилище атрибутов по бд Program")
class TestRequestProgramHeaderNameInAttributeStoreByIndexes:
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
            "Microsoft Start — Рабочий: Microsoft​ Edge",
            "Lister - [c:\\DIST\\Скрипты\\SendMail - exact formats.ps1]",
            "Microsoft Office LTSC 2021 Professional Plus  Standard + Visio + Project 16.0.14332.20255 (2022.03).iso - Добавить новый торрент",
            "Slack   Сергей Сергеев   Test-SI",
            "μTorrent 3.5.5  (build 45798) [32-bit]",
            "Hola VPN - The Website Unblocker - Интернет-магазин Chrome - Google Chrome",
            "Lister - [c:\\Users\\admin1.TEST\\Downloads\\dbforgesql58ent\\dbforgesql58ent\\Crack\\Readme.txt]",
            "dbForge Studio 2019 for SQL Server - CustomBase1(KIB).dgen*",
            "0dvfj7kbhxt541yv2l51a655i2hde5f6.xlsx  [Защищенный просмотр] - Excel",
            "Управление дисками",
            "dbForge Studio 2019 for SQL Server - Start Page",
            "Slack   Иван Иванов   Test-SI",
            "DevInsp_p_20220902_128.log – Блокнот",
            "SQL Server Tools   SQL Database Management Software - Google Chrome",
            "2016_MSP_Prilozhenie_12.xlsx  [Защищенный просмотр] - Excel",
            "Gmail - Google Chrome",
            "666.xlsx - Excel",
            "Uninstall - Devart dbForge Studio 2019 for PostgreSQL",
            "Купить новые Toyota Land Cruiser по цене от 11 890 000 рублей в Ростове-на-Дону - более 78 Тойота Ленд Крузер новых на Авто.ру - Google Chrome",
            "Свойства: Office 2016.xlsx",
            "Office 2016 -OpenXML-.docx - Word",
            "dbForge Studio for PostgreSQL - Download - Google Chrome",
            "Сохранение документа",
            "555.xlsx [восстановлен] - Excel",
            "Resolve libraries",
            "Получение номера версии программы Office и сведений о компьютере - Google Chrome",
        ]
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(parsed_data))
        with allure.step("Кол-во данных"):
            check.equal(len(parsed_data), 264)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
