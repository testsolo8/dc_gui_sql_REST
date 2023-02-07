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

url_tail = "/api/v2/data_center/user_cards/work_calendar_users?selectFields=ID, DisplayName, PrincipalName, IsGroup, Type, UserType, State, ChildCount, Color, ConcatList, GUID, Exclude, CalendarID, _RowsCount, RowNum"


@allure.epic("DataService API v2 (user_cards)")
@allure.feature("List of users-groups for work calendar rules")
@pytest.mark.testRESTAPI
@allure.story("Cписок пользователей/групп для правил рабочего календаря ")
class TestListUsersGroupsForWorkCalendarRules:
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

    @allure.title("Рабочий календарь группы WorkGroups")
    def test_data_group_WorkGroups(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Идентификатор правила рабочего календаря"):
            check.equal(parsed_data["data"][0]["calendarID"], 3)
        with allure.step("Количество объектов внутри группы"):
            check.equal(parsed_data["data"][0]["childCount"], 1)
        with allure.step("Цвет профиля"):
            check.equal(parsed_data["data"][0]["color"], 0)
        with allure.step("Список идентификаторов привязанных пользователей"):
            check.is_none(parsed_data["data"][0]["concatList"])
        with allure.step("Имя группы или пользователя"):
            check.equal(parsed_data["data"][0]["displayName"], "WorkGroups")
        with allure.step("Группа или пользователь исключены из набора"):
            check.is_false(parsed_data["data"][0]["exclude"])
        with allure.step("Уникальный идентификатор пользователя/группы"):
            check.equal(
                parsed_data["data"][0]["guid"], "576F726B-0000-0000-0000-47726F757073"
            )
        with allure.step("Идентификатор группы или пользователя"):
            check.equal(parsed_data["data"][0]["id"], 93)
        with allure.step("Флаг группы"):
            check.equal(parsed_data["data"][0]["isGroup"], 1)
        with allure.step("UPN пользователя"):
            check.is_none(parsed_data["data"][0]["principalName"])
        with allure.step("Номер строки"):
            check.equal(parsed_data["data"][0]["rowNum"], 1)
        with allure.step("Статус пользователя 1 Enabled, 2 Disabled, 3 Deleted"):
            check.equal(parsed_data["data"][0]["state"], 1)
        with allure.step("Тип группы или пользователя"):
            check.equal(parsed_data["data"][0]["type"], 1)
        with allure.step(
            "Тип пользователя: 1 AD, 2 Manual, 3 Index, 4 OldUserCard, 5 IndexUnknown, 6 ReportCenter, 7 EndpointController, 8 ProgramSniffer"
        ):
            check.is_none(parsed_data["data"][0]["userType"])

    @allure.title("Рабочий календарь пользователя REST_test_user_cyrillic")
    def test_data_user_REST_test_user_cyrillic(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Идентификатор правила рабочего календаря"):
            check.equal(parsed_data["data"][1]["calendarID"], 2)
        with allure.step("Количество объектов внутри группы"):
            check.is_none(parsed_data["data"][1]["childCount"])
        with allure.step("Цвет профиля"):
            check.equal(parsed_data["data"][1]["color"], 0)
        with allure.step("Список идентификаторов привязанных пользователей"):
            check.is_none(parsed_data["data"][1]["concatList"])
        with allure.step("Имя группы или пользователя"):
            check.equal(
                parsed_data["data"][1]["displayName"], "REST_test_user_кириллик"
            )
        with allure.step("Группа или пользователь исключены из набора"):
            check.is_false(parsed_data["data"][1]["exclude"])
        with allure.step("Уникальный идентификатор пользователя/группы"):
            check.equal(
                parsed_data["data"][1]["guid"], "2BFADC91-4BD5-44FE-853D-15E4814CC0D8"
            )
        with allure.step("Идентификатор группы или пользователя"):
            check.equal(parsed_data["data"][1]["id"], 1)
        with allure.step("Флаг группы"):
            check.equal(parsed_data["data"][1]["isGroup"], 0)
        with allure.step("UPN пользователя"):
            check.equal(
                parsed_data["data"][1]["principalName"],
                "REST_test_user_cyrillic@autotest.lan",
            )
        with allure.step("Номер строки"):
            check.equal(parsed_data["data"][1]["rowNum"], 2)
        with allure.step("Статус пользователя 1 Enabled, 2 Disabled, 3 Deleted"):
            check.equal(parsed_data["data"][1]["state"], 1)
        with allure.step("Тип группы или пользователя"):
            check.equal(parsed_data["data"][1]["type"], 6)
        with allure.step(
            "Тип пользователя: 1 AD, 2 Manual, 3 Index, 4 OldUserCard, 5 IndexUnknown, 6 ReportCenter, 7 EndpointController, 8 ProgramSniffer"
        ):
            check.equal(parsed_data["data"][1]["userType"], 1)

    @allure.title("Рабочий календарь пользователя REST_test_user_admin")
    def test_data_user_REST_test_user_admin(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Идентификатор правила рабочего календаря"):
            check.equal(parsed_data["data"][2]["calendarID"], 2)
        with allure.step("Количество объектов внутри группы"):
            check.is_none(parsed_data["data"][2]["childCount"])
        with allure.step("Цвет профиля"):
            check.equal(parsed_data["data"][2]["color"], 9)
        with allure.step("Список идентификаторов привязанных пользователей"):
            check.is_none(parsed_data["data"][2]["concatList"])
        with allure.step("Имя группы или пользователя"):
            check.equal(parsed_data["data"][2]["displayName"], "REST_test_user_admin")
        with allure.step("Группа или пользователь исключены из набора"):
            check.is_false(parsed_data["data"][2]["exclude"])
        with allure.step("Уникальный идентификатор пользователя/группы"):
            check.equal(
                parsed_data["data"][2]["guid"], "01279DC6-381E-4F6A-9E86-60AEA3514067"
            )
        with allure.step("Идентификатор группы или пользователя"):
            check.equal(parsed_data["data"][2]["id"], 5)
        with allure.step("Флаг группы"):
            check.equal(parsed_data["data"][2]["isGroup"], 0)
        with allure.step("UPN пользователя"):
            check.equal(
                parsed_data["data"][2]["principalName"],
                "REST_test_user_admin@autotest.lan",
            )
        with allure.step("Номер строки"):
            check.equal(parsed_data["data"][2]["rowNum"], 3)
        with allure.step("Статус пользователя 1 Enabled, 2 Disabled, 3 Deleted"):
            check.equal(parsed_data["data"][2]["state"], 1)
        with allure.step("Тип группы или пользователя"):
            check.equal(parsed_data["data"][2]["type"], 6)
        with allure.step(
            "Тип пользователя: 1 AD, 2 Manual, 3 Index, 4 OldUserCard, 5 IndexUnknown, 6 ReportCenter, 7 EndpointController, 8 ProgramSniffer"
        ):
            check.equal(parsed_data["data"][2]["userType"], 1)

    @allure.title("Рабочий календарь пользователя REST_test_user_diff_param")
    def test_data_user_REST_test_user_diff_param(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Идентификатор правила рабочего календаря"):
            check.equal(parsed_data["data"][3]["calendarID"], 2)
        with allure.step("Количество объектов внутри группы"):
            check.is_none(parsed_data["data"][3]["childCount"])
        with allure.step("Цвет профиля"):
            check.equal(parsed_data["data"][3]["color"], 0)
        with allure.step("Список идентификаторов привязанных пользователей"):
            check.is_none(parsed_data["data"][3]["concatList"])
        with allure.step("Имя группы или пользователя"):
            check.equal(
                parsed_data["data"][3]["displayName"], "REST_test_user_diff_param"
            )
        with allure.step("Группа или пользователь исключены из набора"):
            check.is_false(parsed_data["data"][3]["exclude"])
        with allure.step("Уникальный идентификатор пользователя/группы"):
            check.equal(
                parsed_data["data"][3]["guid"], "188F9AC6-91A0-42E6-9962-94B06B93236A"
            )
        with allure.step("Идентификатор группы или пользователя"):
            check.equal(parsed_data["data"][3]["id"], 7)
        with allure.step("Флаг группы"):
            check.equal(parsed_data["data"][3]["isGroup"], 0)
        with allure.step("UPN пользователя"):
            check.equal(
                parsed_data["data"][3]["principalName"], "REST_diff_param@autotest.lan"
            )
        with allure.step("Номер строки"):
            check.equal(parsed_data["data"][3]["rowNum"], 4)
        with allure.step("Статус пользователя 1 Enabled, 2 Disabled, 3 Deleted"):
            check.equal(parsed_data["data"][3]["state"], 1)
        with allure.step("Тип группы или пользователя"):
            check.equal(parsed_data["data"][3]["type"], 6)
        with allure.step(
            "Тип пользователя: 1 AD, 2 Manual, 3 Index, 4 OldUserCard, 5 IndexUnknown, 6 ReportCenter, 7 EndpointController, 8 ProgramSniffer"
        ):
            check.equal(parsed_data["data"][3]["userType"], 1)

    @allure.title("Рабочий календарь пользователя REST_test_user_internal")
    def test_data_user_REST_test_user_internal(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Идентификатор правила рабочего календаря"):
            check.equal(parsed_data["data"][4]["calendarID"], 2)
        with allure.step("Количество объектов внутри группы"):
            check.is_none(parsed_data["data"][4]["childCount"])
        with allure.step("Цвет профиля"):
            check.equal(parsed_data["data"][4]["color"], 0)
        with allure.step("Список идентификаторов привязанных пользователей"):
            check.is_none(parsed_data["data"][4]["concatList"])
        with allure.step("Имя группы или пользователя"):
            check.equal(
                parsed_data["data"][4]["displayName"], "REST_test_user_internal"
            )
        with allure.step("Группа или пользователь исключены из набора"):
            check.is_false(parsed_data["data"][4]["exclude"])
        with allure.step("Уникальный идентификатор пользователя/группы"):
            check.equal(
                parsed_data["data"][4]["guid"], "BE223A92-19EC-4A69-89DD-B7C840865A1A"
            )
        with allure.step("Идентификатор группы или пользователя"):
            check.equal(parsed_data["data"][4]["id"], 14)
        with allure.step("Флаг группы"):
            check.equal(parsed_data["data"][4]["isGroup"], 0)
        with allure.step("UPN пользователя"):
            check.equal(
                parsed_data["data"][4]["principalName"],
                "REST_test_user_internal@Internal.ISC",
            )
        with allure.step("Номер строки"):
            check.equal(parsed_data["data"][4]["rowNum"], 5)
        with allure.step("Статус пользователя 1 Enabled, 2 Disabled, 3 Deleted"):
            check.equal(parsed_data["data"][4]["state"], 1)
        with allure.step("Тип группы или пользователя"):
            check.equal(parsed_data["data"][4]["type"], 6)
        with allure.step(
            "Тип пользователя: 1 AD, 2 Manual, 3 Index, 4 OldUserCard, 5 IndexUnknown, 6 ReportCenter, 7 EndpointController, 8 ProgramSniffer"
        ):
            check.equal(parsed_data["data"][4]["userType"], 1)

    @allure.title("Рабочий календарь пользователя workgroup_user")
    def test_data_user_workgroup_user(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Идентификатор правила рабочего календаря"):
            check.equal(parsed_data["data"][5]["calendarID"], 3)
        with allure.step("Количество объектов внутри группы"):
            check.is_none(parsed_data["data"][5]["childCount"])
        with allure.step("Цвет профиля"):
            check.equal(parsed_data["data"][5]["color"], 0)
        with allure.step("Список идентификаторов привязанных пользователей"):
            check.is_none(parsed_data["data"][5]["concatList"])
        with allure.step("Имя группы или пользователя"):
            check.equal(
                parsed_data["data"][5]["displayName"], "REST_test_workgroup_user"
            )
        with allure.step("Группа или пользователь исключены из набора"):
            check.is_true(parsed_data["data"][5]["exclude"])
        with allure.step("Уникальный идентификатор пользователя/группы"):
            check.equal(
                parsed_data["data"][5]["guid"], "0C900037-025E-460A-9D02-4840AD39036B"
            )
        with allure.step("Идентификатор группы или пользователя"):
            check.equal(parsed_data["data"][5]["id"], 15)
        with allure.step("Флаг группы"):
            check.equal(parsed_data["data"][5]["isGroup"], 0)
        with allure.step("UPN пользователя"):
            check.equal(
                parsed_data["data"][5]["principalName"],
                "REST_test_workgroup_user@autotest",
            )
        with allure.step("Номер строки"):
            check.equal(parsed_data["data"][5]["rowNum"], 6)
        with allure.step("Статус пользователя 1 Enabled, 2 Disabled, 3 Deleted"):
            check.equal(parsed_data["data"][5]["state"], 1)
        with allure.step("Тип группы или пользователя"):
            check.equal(parsed_data["data"][5]["type"], 6)
        with allure.step(
            "Тип пользователя: 1 AD, 2 Manual, 3 Index, 4 OldUserCard, 5 IndexUnknown, 6 ReportCenter, 7 EndpointController, 8 ProgramSniffer"
        ):
            check.equal(parsed_data["data"][5]["userType"], 1)

    def test_schema(self, dc_api: DcApiWithToken):
        schema = {
            "type": "object",
            "properties": {"data": {"type": "array"}},
            "required": ["data", "header"],
        }
        resp = dc_api.req_get(url_tail).json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        error_list = []
        for row in data_dict["data"]:
            try:
                schema_models.SchemaModelsDataServiceAPIv2.ListUsersGroupsForWorkCalendarRules.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.ListUsersGroupsForWorkCalendarRules.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
