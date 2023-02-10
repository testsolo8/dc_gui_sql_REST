# Standart libraries
import json

# Third party packages
import allure
import pytest
import pytest_check as check
import requests
from jsonschema import validate
from pydantic import ValidationError

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc

path = "http://" + base_url_dc() + ":9096/api/v2/objects"
r = requests.get(path, verify=False)


@allure.epic("REST API V2")
@allure.feature("Objects list")
@pytest.mark.testRESTAPI
@allure.story(
    "Возвращает список объектов (может быть пустым), соответствующий указанным поисковым параметрам"
)
class TestObjectsList:
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

    @allure.title("Атрибуты объекта домен")
    def test_object_DN(self):
        data_dict = r.json()
        with allure.step("SID"):
            check.equal(
                data_dict["objects"][2]["SID"],
                "S-1-5-21-4141237049-2453287432-1636914503",
            )
        with allure.step("DisplayName"):
            check.equal(data_dict["objects"][2]["DisplayName"], "autotest.lan")
        with allure.step("GUID"):
            check.equal(
                data_dict["objects"][2]["GUID"],
                "BC925BAC-F94F-405D-B94B-5FE29498645C",
            )
        with allure.step("Тип объекта"):
            check.equal(data_dict["objects"][2]["ObjectType"], "dn")

    @allure.title("Атрибуты объекта контейнер Active Directory")
    def test_object_CN(self):
        data_dict = r.json()
        with allure.step("DisplayName"):
            check.equal(data_dict["objects"][7]["DisplayName"], "Users")
        with allure.step("Name"):
            check.equal(data_dict["objects"][7]["Name"], "Users")
        with allure.step("GUID"):
            check.equal(
                data_dict["objects"][7]["GUID"],
                "2315D583-A472-400F-9128-C9F90B9EE2CB",
            )
        with allure.step("Тип объекта"):
            check.equal(data_dict["objects"][6]["ObjectType"], "cn")

    @allure.title("Атрибуты объекта подразделение Active Directory")
    def test_object_OU(self):
        data_dict = r.json()
        with allure.step("DisplayName"):
            check.equal(data_dict["objects"][9]["DisplayName"], "Domain Controllers")
        with allure.step("GUID"):
            check.equal(
                data_dict["objects"][9]["GUID"],
                "25A7CE81-54E6-4D02-AD7C-DC21C8B9B159",
            )
        with allure.step("Тип объекта"):
            check.equal(data_dict["objects"][9]["ObjectType"], "ou")

    @allure.title("Атрибуты объекта группа")
    def test_object_GP(self):
        data_dict = r.json()
        with allure.step("UPN"):
            check.equal(
                data_dict["objects"][15]["UPN"], "Администраторы домена@autotest.lan"
            )
        with allure.step("SID"):
            check.equal(
                data_dict["objects"][15]["SID"],
                "S-1-5-21-4141237049-2453287432-1636914503-512",
            )
        with allure.step("DisplayName"):
            check.equal(
                data_dict["objects"][15]["DisplayName"], "Администраторы домена"
            )
        with allure.step("Name"):
            check.equal(data_dict["objects"][15]["Name"], "Администраторы домена")
        with allure.step("GUID"):
            check.equal(
                data_dict["objects"][15]["GUID"],
                "29427C48-4AB1-40B1-97E5-29F76E41E00F",
            )
        with allure.step("Тип объекта"):
            check.equal(data_dict["objects"][15]["ObjectType"], "gp")

    @allure.title("Атрибуты объекта пользователь")
    def test_object_US(self):
        data_dict = r.json()
        with allure.step("UPN"):
            check.equal(
                data_dict["objects"][81]["UPN"], "REST_test_user_admin@autotest.lan"
            )
        with allure.step("SID"):
            check.equal(
                data_dict["objects"][81]["SID"],
                "S-1-5-21-4141237049-2453287432-1636914503-3103",
            )
        with allure.step("DisplayName"):
            check.equal(data_dict["objects"][81]["DisplayName"], "REST_test_user_admin")
        with allure.step("Name"):
            check.equal(data_dict["objects"][81]["Name"], "REST_test_user_admin")
        with allure.step("GUID"):
            check.equal(
                data_dict["objects"][81]["GUID"],
                "01279DC6-381E-4F6A-9E86-60AEA3514067",
            )
        with allure.step("Тип объекта"):
            check.equal(data_dict["objects"][81]["ObjectType"], "us")

    @allure.title("Атрибуты объекта компьютер")
    def test_object_PC(self):
        data_dict = r.json()
        with allure.step("SID"):
            check.equal(
                data_dict["objects"][62]["SID"],
                "S-1-5-21-4141237049-2453287432-1636914503-1906",
            )
        with allure.step("DNS"):
            check.equal(data_dict["objects"][63]["DNS"], "DC.autotest.lan")
        with allure.step("DisplayName"):
            check.equal(data_dict["objects"][63]["DisplayName"], "DC")
        with allure.step("Name"):
            check.equal(data_dict["objects"][63]["Name"], "DC")
        with allure.step("GUID"):
            check.equal(
                data_dict["objects"][63]["GUID"],
                "07F69C41-692C-405B-A295-2D5A1426C52D",
            )
        with allure.step("Тип объекта"):
            check.equal(data_dict["objects"][63]["ObjectType"], "pc")

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "object",
            "properties": {"objects": {"type": "array"}},
            "required": ["objects"],
        }
        resp = r.json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self):
        data_dict = r.json()
        error_list = []
        for row in data_dict["objects"]:
            try:
                schema_models.SchemaModelsRESTAPIV2.ObjectsList.parse_obj(row)
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsRESTAPIV2.ObjectsList.parse_obj(
                data_dict["objects"][2]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
