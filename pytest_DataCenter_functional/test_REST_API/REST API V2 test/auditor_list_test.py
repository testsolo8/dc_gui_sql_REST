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

path = "http://" + base_url_dc() + ":9096/api/v2/officers"
r = requests.get(path, verify=False)


@allure.epic("REST API V2")
@allure.feature("Auditor list")
@pytest.mark.testRESTAPI
@allure.story("Получение списка аудиторов")
class TestAuditorList:
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

    @allure.title("Данные аудитора с кириллическим именем")
    def test_REST_test_user_cyrillic_as_auditor(self):
        data_dict = r.json()
        with allure.step("UPN"):
            check.equal(
                data_dict["officers"][1]["UPN"],
                "REST_test_user_cyrillic@autotest.lan",
            )
        with allure.step("SID"):
            check.equal(
                data_dict["officers"][1]["SID"],
                "S-1-5-21-4141237049-2453287432-1636914503-3106",
            )
        with allure.step("Почтовый адреса (e-mail)"):
            check.equal(
                data_dict["officers"][1]["mails"],
                ["REST_test_user_кириллик@test.lan"],
            )
        with allure.step("Состояние учетной записи аудитора"):
            check.equal(data_dict["officers"][1]["Enabled"], True)
        with allure.step("DisplayName"):
            check.equal(
                data_dict["officers"][1]["DisplayName"], "REST_test_user_кириллик"
            )
        with allure.step("GUID"):
            check.equal(
                data_dict["officers"][1]["GUID"],
                "2BFADC91-4BD5-44FE-853D-15E4814CC0D8",
            )

    @allure.title("Данные аудитора admin")
    def test_REST_test_user_admin_as_auditor(self):
        data_dict = r.json()
        with allure.step("UPN"):
            check.equal(
                data_dict["officers"][2]["UPN"], "REST_test_user_admin@autotest.lan"
            )
        with allure.step("SID"):
            check.equal(
                data_dict["officers"][2]["SID"],
                "S-1-5-21-4141237049-2453287432-1636914503-3103",
            )
        with allure.step("Почтовый адреса (e-mail)"):
            check.equal(
                data_dict["officers"][2]["mails"], ["REST_test_user_admin@test.lan"]
            )
        with allure.step("Состояние учетной записи аудитора"):
            check.equal(data_dict["officers"][2]["Enabled"], True)
        with allure.step("DisplayName"):
            check.equal(data_dict["officers"][2]["DisplayName"], "REST_test_user_admin")
        with allure.step("GUID"):
            check.equal(
                data_dict["officers"][2]["GUID"],
                "01279DC6-381E-4F6A-9E86-60AEA3514067",
            )

    @allure.title("Данные аудитора diff_param")
    def test_REST_diff_param_as_auditor(self):
        data_dict = r.json()
        with allure.step("UPN"):
            check.equal(data_dict["officers"][3]["UPN"], "REST_diff_param@autotest.lan")
        with allure.step("SID"):
            check.equal(
                data_dict["officers"][3]["SID"],
                "S-1-5-21-4141237049-2453287432-1636914503-3105",
            )
        with allure.step("Почтовый адреса (e-mail)"):
            check.equal(
                data_dict["officers"][3]["mails"],
                ["REST_test_user_diff_param@test.lan"],
            )
        with allure.step("Состояние учетной записи аудитора"):
            check.equal(data_dict["officers"][3]["Enabled"], True)
        with allure.step("DisplayName"):
            check.equal(
                data_dict["officers"][3]["DisplayName"], "REST_test_user_diff_param"
            )
        with allure.step("GUID"):
            check.equal(
                data_dict["officers"][3]["GUID"],
                "188F9AC6-91A0-42E6-9962-94B06B93236A",
            )

    @allure.title("Данные внутреннего аудитора КИБ")
    def test_REST_test_user_internal_as_auditor(self):
        data_dict = r.json()
        with allure.step("UPN"):
            check.equal(
                data_dict["officers"][0]["UPN"],
                "REST_test_user_internal@Internal.ISC",
            )
        with allure.step("SID"):
            check.equal(data_dict["officers"][0]["SID"], "")
        with allure.step("Почтовый адреса (e-mail)"):
            check.equal(data_dict["officers"][0]["mails"], [])
        with allure.step("Состояние учетной записи аудитора"):
            check.equal(data_dict["officers"][0]["Enabled"], True)
        with allure.step("DisplayName"):
            check.equal(
                data_dict["officers"][0]["DisplayName"], "REST_test_user_internal"
            )
        with allure.step("GUID"):
            check.equal(
                data_dict["officers"][0]["GUID"],
                "BE223A92-19EC-4A69-89DD-B7C840865A1A",
            )

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {"type": "object", "required": ["officers"]}
        resp = r.json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self):
        data_dict = r.json()
        error_list = []
        for row in data_dict["officers"]:
            try:
                schema_models.SchemaModelsRESTAPIV2.AuditorList.parse_obj(row)
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsRESTAPIV2.AuditorList.parse_obj(
                data_dict["officers"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
