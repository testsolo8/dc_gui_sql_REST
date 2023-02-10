# Standart libraries
import json

# Third party packages
import allure
import pytest
import pytest_check as check
from jsonschema import validate
from pydantic import ValidationError

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import DcApiWithToken

url_tail = (
    "/api/v2/data_center/user_cards/resolve?contact=REST_test_user_cyrillic@autotest.lan&contactTypeID=0&"
    "accountTypeID=1"
)


@allure.epic("DataService API v2 (user_cards)")
@allure.feature("Procedure for obtaining UPN by contact REST_test_user_cyrillic")
@pytest.mark.testRESTAPI
@allure.story("Процедура получения UPN по контакту REST_test_user_cyrillic")
class TestProcedureForObtainingUPNByContact:
    @allure.title("Успешность запроса")
    def test_status_code_200(self, dc_api: DcApiWithToken):
        r = dc_api.req_get(url_tail)
        assert r.status_code == 200

    @allure.title("Headers 'content-type'")
    def test_content_type(self, dc_api: DcApiWithToken):
        con_type = dc_api.req_get(url_tail).headers["content-type"]
        assert con_type == r"application/json; charset=utf-8"

    @allure.title("Время ответа запроса")
    def test_response_time(self, dc_api: DcApiWithToken):
        resp_time = dc_api.req_get(url_tail).elapsed.total_seconds()
        assert resp_time <= 30

    @allure.title("Процедура получения UPN по контакту (AccountTypeID=1)")
    def test_UPN_Mitsko(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Количество объектов внутри группы"):
            check.is_none(data_dict["data"][0]["childCount"])
        with allure.step("Цвет профиля"):
            check.equal(data_dict["data"][0]["color"], 0)
        with allure.step("Список идентификаторов привязанных пользователей"):
            check.is_none(data_dict["data"][0]["concatList"])
        with allure.step("Имя группы или пользователя"):
            check.equal(data_dict["data"][0]["displayName"], "REST_test_user_кириллик")
        with allure.step("Уникальный идентификатор группы или пользователя"):
            check.equal(
                data_dict["data"][0]["guid"], "2BFADC91-4BD5-44FE-853D-15E4814CC0D8"
            )
        with allure.step("Идентификатор группы или пользователя"):
            check.equal(data_dict["data"][0]["id"], 1)
        with allure.step("Флаг группы"):
            check.equal(data_dict["data"][0]["isGroup"], 0)
        with allure.step("Логин пользователя"):
            check.equal(
                data_dict["data"][0]["principalName"],
                "REST_test_user_cyrillic@autotest.lan",
            )
        with allure.step("Статус пользователя 1 Enabled, 2 Disabled, 3 Deleted"):
            check.equal(data_dict["data"][0]["state"], 1)
        with allure.step("Тип пользователя или группы (для иконки)"):
            check.equal(data_dict["data"][0]["type"], 6)
        with allure.step(
            "Тип пользователя: 1 AD, 2 Manual, 3 Index, 4 OldUserCard, 5 IndexUnknown, 6 ReportCenter, 7 EndpointController, 8 ProgramSniffer"
        ):
            check.equal(data_dict["data"][0]["userType"], 1)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self, dc_api: DcApiWithToken):
        schema = {
            "type": "object",
            "properties": {"data": {"type": "array"}},
            "required": ["data"],
        }
        resp = dc_api.req_get(url_tail).json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        error_list = []
        for row in data_dict["data"]:
            try:
                schema_models.SchemaModelsDataServiceAPIv2.ProcedureForObtainingUPNByContact.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.ProcedureForObtainingUPNByContact.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
