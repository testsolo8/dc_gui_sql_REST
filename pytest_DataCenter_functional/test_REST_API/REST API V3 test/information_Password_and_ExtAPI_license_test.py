# Standart libraries
import json
from datetime import datetime

# Third party packages
import allure
import pytest
import pytest_check as check
import requests
from jsonschema import validate

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc

pathPassword = (
    "https://"
    + base_url_dc()
    + ":9082/datacenter/api/v3/license/special/456ED2B8-A757-11DE-9196-988056D89593"
)
pathExternalAPI = (
    "https://"
    + base_url_dc()
    + ":9082/datacenter/api/v3/license/special/2D7BD076-0E24-403C-97F1-449705B1F976"
)
r_password = requests.get(pathPassword, verify=False)
r_ExternalAPI = requests.get(pathExternalAPI, verify=False)


@allure.epic("REST API V3")
@allure.feature("All information Password and ExtAPI license")
@pytest.mark.testRESTAPI
@allure.story("Данные о лицензиях Password и ExternalAPI")
class TestInformationPasswordExtAPILicense:
    @allure.title("Успешность запроса")
    def test_status_code_200(self):
        assert r_password.status_code == 200

    @allure.title("Headers 'content-type'")
    def test_content_type(self):
        con_type = r_password.headers["content-type"]
        assert con_type == "application/json; charset=utf-8"

    @allure.title("Время ответа запроса")
    def test_response_time(self):
        resp_time = r_password.elapsed.total_seconds()
        assert resp_time <= 30

    @allure.title("Информация о лицензии Password")
    def test_information_about_password_license(self):
        data_dict = r_password.json()
        with allure.step("Окончание лицензии"):
            check.greater(
                datetime.utcfromtimestamp(data_dict["Expire_Date"]), datetime.now()
            )
        with allure.step("Начало лицензии"):
            check.equal(data_dict["Start_Date"], 0)
        with allure.step("UniqueID продукта Password"):
            check.equal(data_dict["UniqueID"], "{456ED2B8-A757-11DE-9196-988056D89593}")
        with allure.step("Колличество лицензий"):
            check.equal(data_dict["LicensesCount"], 1000)

    @allure.title("Информация о лицензии ExternalAPI")
    def test_information_about_externalAPI_license(self):
        data_dict = r_ExternalAPI.json()
        with allure.step("Окончание лицензии"):
            check.greater(
                datetime.utcfromtimestamp(data_dict["Expire_Date"]), datetime.now()
            )
        with allure.step("Начало лицензии"):
            check.equal(data_dict["Start_Date"], 0)
        with allure.step("UniqueID продукта Password"):
            check.equal(data_dict["UniqueID"], "{2D7BD076-0E24-403C-97F1-449705B1F976}")
        with allure.step("Колличество лицензий"):
            check.equal(data_dict["LicensesCount"], 1)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "Expire_Date": {"type": "number"},
                "Start_Date": {"type": "number"},
                "UniqueID": {"type": "string"},
                "LicensesCount": {"type": "number"},
            },
            "required": ["Expire_Date", "UniqueID", "LicensesCount"],
        }
        resp = r_password.json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema_password(self):
        data_dict = r_password.json()
        schema_models.SchemaModelsRESTAPIV3.InformationPasswordExtAPILicense.parse_obj(
            data_dict
        )

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema_external_API(self):
        data_dict = r_ExternalAPI.json()
        schema_models.SchemaModelsRESTAPIV3.InformationPasswordExtAPILicense.parse_obj(
            data_dict
        )
