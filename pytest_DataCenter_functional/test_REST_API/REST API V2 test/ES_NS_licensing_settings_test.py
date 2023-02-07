# Standart libraries
import json
from datetime import datetime

# Third party packages
import allure
import pytest
import pytest_check as check
import requests
from jsonschema import validate
from pydantic import ValidationError, parse_obj_as

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc

path = "http://" + base_url_dc() + ":9096/api/v2/license/extserver"
r = requests.get(path)


@allure.epic("REST API V2")
@allure.feature("ES/NS licensing settings")
@pytest.mark.testRESTAPI
@allure.story(
    "Настройки лицензирования ES/NS (запрос службы DCRESTAPI через которую осуществляется лицензирование ES/NS)"
)
class TestESNSLicensingSettings:
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

    @allure.title("Лицензия на вычитку паролей из данных перехвата")
    def test_password_license(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Окончание лицензии"):
            check.greater(
                datetime.utcfromtimestamp(
                    parsed_data["PasswordLicense"]["Expire_Date"]
                ),
                datetime.now(),
            )
        with allure.step("UniqueID лицензии"):
            check.equal(
                parsed_data["PasswordLicense"]["UniqueID"],
                "{456ED2B8-A757-11DE-9196-988056D89593}",
            )
        with allure.step("Колличество лицензий"):
            check.equal(parsed_data["PasswordLicense"]["LicensesCount"], 1000)

    @allure.title("Лицензия на распознавание перехвата микрофона")
    def test_microphone_to_text(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Окончание лицензии"):
            check.greater(
                datetime.utcfromtimestamp(
                    parsed_data["MicrophoneToText"]["Expire_Date"]
                ),
                datetime.now(),
            )
        with allure.step("UniqueID лицензии"):
            check.equal(
                parsed_data["MicrophoneToText"]["UniqueID"],
                "{ACC50121-7668-4FB2-AAA1-D085152B9953}",
            )
        with allure.step("Колличество лицензий"):
            check.equal(parsed_data["PasswordLicense"]["LicensesCount"], 1000)

    @allure.title("Лицензия на external API")
    def test_external_API_license(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Окончание лицензии"):
            check.greater(
                datetime.utcfromtimestamp(
                    parsed_data["ExternalAPILicense"]["Expire_Date"]
                ),
                datetime.now(),
            )
        with allure.step("UniqueID лицензии"):
            check.equal(
                parsed_data["ExternalAPILicense"]["UniqueID"],
                "{2D7BD076-0E24-403C-97F1-449705B1F976}",
            )
        with allure.step("Колличество лицензий"):
            check.equal(parsed_data["ExternalAPILicense"]["LicensesCount"], 1)

    @allure.title("Другие параметры запроса")
    def test_other_data(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Тех. поддержка до"):
            check.greater(
                datetime.utcfromtimestamp(parsed_data["SupportTo"]), datetime.now()
            )
        with allure.step("E-mail тех. поддержки"):
            check.equal(parsed_data["Contact_Person_EMail"], "test@test.com")

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "SearchInform_Licence": {"type": "array"},
                "PasswordLicense": {"type": "object"},
                "HardwareID": {"type": "string"},
            },
            "required": ["SearchInform_Licence", "HardwareID"],
        }
        resp = r.json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self):
        data_dict = r.json()
        error_list = []
        for row in data_dict:
            try:
                parse_obj_as(
                    schema_models.SchemaModelsRESTAPIV2.ESNSLicensingSettings, data_dict
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsRESTAPIV2.ESNSLicensingSettings.PasswordLicense.parse_obj(
                data_dict["PasswordLicense"]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
