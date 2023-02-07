# Standart libraries
import json

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

path = (
    "http://"
    + base_url_dc()
    + ":9096/api/v2/users/188F9AC6-91A0-42E6-9962-94B06B93236A/rights"
)
r = requests.get(path)


@allure.epic("REST API V2")
@allure.feature("Rights for user diff param")
@pytest.mark.testRESTAPI
@allure.story("Настройки прав для аудитора REST_test_user_diff_param")
class TestRightsUserDiffParam:
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

    @allure.title("Продукты КИБ разрешенные к просмотру")
    def test_product_rights(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        assert parsed_data["productrights"]["AllowedProducts"] == 29891870639

    @allure.title(
        "Функции разрешенные к просмотру в разрешенных продуктах КИБ (список проверяется не полностью)"
    )
    def test_feature_rights(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Разрешения для SearchServer"):
            check.is_true(parsed_data["featurerights"]["SS"]["CanChangeLogin"])
            check.is_true(parsed_data["featurerights"]["SS"]["CanViewLogin"])
        with allure.step("Разрешения для NetworkController"):
            check.is_true(
                parsed_data["featurerights"]["NS"]["CanChangeSMTPIntegration"]
            )
            check.is_true(parsed_data["featurerights"]["NS"]["CanViewSMTPIntegration"])
            check.is_true(
                parsed_data["featurerights"]["NS"]["CanChangeSynchronization"]
            )
            check.is_true(parsed_data["featurerights"]["NS"]["CanViewSynchronization"])
            check.is_true(parsed_data["featurerights"]["NS"]["CanChangeLicence"])
            check.is_true(parsed_data["featurerights"]["NS"]["CanViewLicence"])
        with allure.step("Разрешения для EndpointController"):
            check.is_true(
                parsed_data["featurerights"]["ES"]["CanViewPendingListsOnServer"]
            )
            check.is_true(
                parsed_data["featurerights"]["ES"]["CanViewAgentsRequestsLog"]
            )
            check.is_true(
                parsed_data["featurerights"]["ES"]["CanChangePendingListsOnServer"]
            )
            check.is_true(
                parsed_data["featurerights"]["ES"]["CanChangeAgentsRequestsLog"]
            )
            check.is_true(
                parsed_data["featurerights"]["ES"]["CanViewPendingListsOnAgents"]
            )
            check.is_true(
                parsed_data["featurerights"]["ES"]["CanChangePendingListsOnAgents"]
            )
        with allure.step("Разрешения для DataCenter"):
            check.is_true(
                parsed_data["featurerights"]["DC"]["CanChangeRVisionGosSOPKASettings"]
            )
            check.is_true(
                parsed_data["featurerights"]["DC"]["CanViewFingerprintSettings"]
            )
            check.is_true(
                parsed_data["featurerights"]["DC"]["CanViewComponentsManagement"]
            )
            check.is_true(
                parsed_data["featurerights"]["DC"]["CanChangeTaskManagementSettings"]
            )
            check.is_true(
                parsed_data["featurerights"]["DC"]["CanViewRVisionGosSOPKASettings"]
            )
            check.is_true(
                parsed_data["featurerights"]["DC"]["CanChangeComponentsManagement"]
            )
        with allure.step("Разрешения для AnalyticConsole"):
            check.is_true(parsed_data["featurerights"]["CA"]["CanChangeLiveView"])
            check.is_true(
                parsed_data["featurerights"]["CA"][
                    "CanChangeAccessNotificationsReports"
                ]
            )
            check.is_true(parsed_data["featurerights"]["CA"]["CanViewTMDescriptions"])
            check.is_true(parsed_data["featurerights"]["CA"]["CanChangeActivity"])
            check.is_true(
                parsed_data["featurerights"]["CA"]["CanViewGosSOPKAInteraction"]
            )
            check.is_true(parsed_data["featurerights"]["CA"]["CanChangeLiveCam"])
        with allure.step("Разрешения для AlertCenter"):
            check.is_true(parsed_data["featurerights"]["AC"]["CanViewLoginToConsole"])
            check.is_true(parsed_data["featurerights"]["AC"]["CanViewUseWebAccess"])
            check.is_true(parsed_data["featurerights"]["AC"]["CanChangeUseWebAccess"])
            check.is_true(parsed_data["featurerights"]["AC"]["CanChangeLoginToConsole"])
        with allure.step("Разрешения для SIEM"):
            check.is_true(
                parsed_data["featurerights"]["SIEM"][
                    "CanChangeCrossCorrelationOfEvents"
                ]
            )
            check.is_true(parsed_data["featurerights"]["SIEM"]["CanViewDashboardTab"])
            check.is_true(parsed_data["featurerights"]["SIEM"]["CanChangeDashboardTab"])
            check.is_true(
                parsed_data["featurerights"]["SIEM"]["CanChangeExclusionLists"]
            )
            check.is_true(parsed_data["featurerights"]["SIEM"]["CanViewExclusionLists"])
            check.is_true(
                parsed_data["featurerights"]["SIEM"]["CanViewCrossCorrelationOfEvents"]
            )

    @allure.title(
        "Данные разрешенные к просмотру в разрешенных продуктах КИБ (список проверяется не полностью) + тип доступа"
    )
    def test_data_rights(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Данные доступные к просмотру по компьютерам"):
            check.equal(
                parsed_data["datarights"]["ComputersList"][0]["SID"],
                "S-1-5-21-4141237049-2453287432-1636914503-1000",
            )
            check.equal(
                parsed_data["datarights"]["ComputersList"][0]["DNS"], "DC.autotest.lan"
            )
            check.equal(
                parsed_data["datarights"]["ComputersList"][0]["DisplayName"], "DC"
            )
            check.equal(parsed_data["datarights"]["ComputersList"][0]["Name"], "DC")
            check.equal(
                parsed_data["datarights"]["ComputersList"][0]["GUID"],
                "{07F69C41-692C-405B-A295-2D5A1426C52D}",
            )
            check.equal(
                parsed_data["datarights"]["ComputersList"][1]["SID"],
                "S-1-5-21-4141237049-2453287432-1636914503-2608",
            )
            check.equal(
                parsed_data["datarights"]["ComputersList"][1]["DNS"], "dc2.autotest.lan"
            )
            check.equal(
                parsed_data["datarights"]["ComputersList"][1]["DisplayName"], "DC2"
            )
            check.equal(parsed_data["datarights"]["ComputersList"][1]["Name"], "DC2")
            check.equal(
                parsed_data["datarights"]["ComputersList"][1]["GUID"],
                "{81CC5FE5-2A02-4EEB-BA3E-C059145C9DAA}",
            )
        with allure.step("Данные доступные к просмотру по пользователям"):
            check.equal(
                parsed_data["datarights"]["UsersList"][0]["UPN"],
                "REST_test_user_cyrillic@autotest.lan",
            )
            check.equal(
                parsed_data["datarights"]["UsersList"][0]["SID"],
                "S-1-5-21-4141237049-2453287432-1636914503-3106",
            )
            check.equal(
                parsed_data["datarights"]["UsersList"][0]["DisplayName"],
                "REST_test_user_кириллик",
            )
            check.equal(
                parsed_data["datarights"]["UsersList"][0]["Name"],
                "REST_test_user_кириллик",
            )
            check.equal(
                parsed_data["datarights"]["UsersList"][0]["GUID"],
                "{2BFADC91-4BD5-44FE-853D-15E4814CC0D8}",
            )
            check.equal(
                parsed_data["datarights"]["UsersList"][1]["UPN"],
                "REST_test_user_admin@autotest.lan",
            )
            check.equal(
                parsed_data["datarights"]["UsersList"][1]["SID"],
                "S-1-5-21-4141237049-2453287432-1636914503-3103",
            )
            check.equal(
                parsed_data["datarights"]["UsersList"][1]["DisplayName"],
                "REST_test_user_admin",
            )
            check.equal(
                parsed_data["datarights"]["UsersList"][1]["Name"],
                "REST_test_user_admin",
            )
            check.equal(
                parsed_data["datarights"]["UsersList"][1]["GUID"],
                "{01279DC6-381E-4F6A-9E86-60AEA3514067}",
            )
            with allure.step("Тип доступа 'Разрешено смотреть только указанных'"):
                check.equal(parsed_data["datarights"]["AccessMode"], 3)

    @allure.title("Сервера КИБ разрешенные к просмотру")
    def test_server_rights(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        check.equal(
            parsed_data["serverrights"][1], "342042FB-E791-482B-98F4-61E78B1B1715"
        )

    def test_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "featurerights": {"type": "object"},
                "productrights": {"type": "object"},
                "datarights": {"type": "object"},
            },
            "required": ["featurerights", "productrights", "datarights"],
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
                    schema_models.SchemaModelsRESTAPIV2.RightsUserDiffParam, data_dict
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsRESTAPIV2.RightsUserDiffParam.DataRights.parse_obj(
                data_dict["datarights"]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
