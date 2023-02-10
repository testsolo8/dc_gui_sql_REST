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

url_tail = "/api/v2/data_center/user_cards/work_calendar"


@allure.epic("DataService API v2 (user_cards)")
@allure.feature("List of work calendar rules")
@pytest.mark.testRESTAPI
@allure.story("Список правил рабочего календаря ")
class TestListWorkCalendarRules:
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

    @allure.title("Рабочий календарь Пользователь рабочих групп")
    def test_list_of_work_calendar_workgrupuser(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Идентификатор правила рабочего календаря"):
            check.equal(data_dict["data"][0]["calendarID"], 3)
        with allure.step("Включено/выключено правило"):
            check.is_true(data_dict["data"][0]["checked"])
        with allure.step("Данные правила в JSON формате"):
            check.equal(
                data_dict["data"][0]["jsonData"],
                r'{"checked":true,"days":[{"isWork":true,"begin":32400,"end":64800,"breaks":[{"begin":46800,"end":50400,"description":"Перерыв"}]},{"isWork":true,"begin":32400,"end":64800,"breaks":[{"begin":46800,"end":50400,"description":"Перерыв"}]},{"isWork":true,"begin":32400,"end":64800,"breaks":[{"begin":46800,"end":50400,"description":"Перерыв"}]},{"isWork":true,"begin":32400,"end":64800,"breaks":[]}],"typeWorkingWeek":1,"allDaysWeek":true,"startCalculation":1640908800,"displayName":"Пользователь рабочих групп"}',
            )
        with allure.step("Название правила"):
            check.equal(data_dict["data"][0]["name"], "Пользователь рабочих групп")
        with allure.step("Приоритет правила"):
            check.equal(data_dict["data"][0]["orderID"], 3)

    @allure.title("Рабочий календарь По выходным")
    def test_list_of_work_calendar_weekends(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Идентификатор правила рабочего календаря"):
            check.equal(data_dict["data"][1]["calendarID"], 2)
        with allure.step("Включено/выключено правило"):
            check.is_true(data_dict["data"][1]["checked"])
        with allure.step("Данные правила в JSON формате"):
            check.equal(
                data_dict["data"][1]["jsonData"],
                r'{"checked":true,"days":[{"isWork":true,"begin":32400,"end":64800,"breaks":[{"begin":46800,"end":50400,"description":"Перерыв"}]},{"isWork":true,"begin":32400,"end":64800,"breaks":[{"begin":46800,"end":50400,"description":"Перерыв"}]},{"isWork":false,"begin":0,"end":86399,"breaks":[]},{"isWork":false,"begin":0,"end":86399,"breaks":[]}],"typeWorkingWeek":1,"allDaysWeek":false,"startCalculation":1640908800,"displayName":"По выходным"}',
            )
        with allure.step("Название правила"):
            check.equal(data_dict["data"][1]["name"], "По выходным")
        with allure.step("Приоритет правила"):
            check.equal(data_dict["data"][1]["orderID"], 2)

    @allure.title("Рабочий календарь default")
    def test_list_of_work_calendar_default(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Идентификатор правила рабочего календаря"):
            check.equal(data_dict["data"][2]["calendarID"], 1)
        with allure.step("Включено/выключено правило"):
            check.is_true(data_dict["data"][2]["checked"])
        with allure.step("Данные правила в JSON формате"):
            check.equal(
                data_dict["data"][2]["jsonData"],
                r'{"days":[{"isWork":true,"begin":32400,"end":64800,"breaks":[{"begin":46800,"end":50400,"description":"Перерыв"}]},{"isWork":true,"begin":32400,"end":64800,"breaks":[{"begin":46800,"end":50400,"description":"Перерыв"}]},{"isWork":true,"begin":32400,"end":64800,"breaks":[{"begin":46800,"end":50400,"description":"Перерыв"}]},{"isWork":true,"begin":32400,"end":64800,"breaks":[{"begin":46800,"end":50400,"description":"Перерыв"}]},{"isWork":true,"begin":32400,"end":64800,"breaks":[{"begin":46800,"end":50400,"description":"Перерыв"}]},{"isWork":true,"begin":32400,"end":64800,"breaks":[{"begin":46800,"end":50400,"description":"Перерыв"}]},{"isWork":false,"begin":0,"end":86399,"breaks":[]},{"isWork":false,"begin":0,"end":86399,"breaks":[]}],"activity":18000,"inOut":10,"typeWorkingWeek":0,"allDaysWeek":true,"startCalculation":1609459200,"holidays":[{"date":1661472000,"dayType":1,"displayName":"","isWork":true,"begin":32400,"end":64800,"breaks":[{"begin":46800,"end":50400,"description":"Перерыв"}]},{"date":1661558400,"dayType":2,"displayName":"","isWork":true,"begin":32400,"end":64800,"breaks":[{"begin":46800,"end":50400,"description":"Перерыв"}]}],"checked":true,"displayName":"По умолчанию"}',
            )
        with allure.step("Название правила"):
            check.equal(data_dict["data"][2]["name"], "default")
        with allure.step("Приоритет правила"):
            check.equal(data_dict["data"][2]["orderID"], 1)

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
                schema_models.SchemaModelsDataServiceAPIv2.ListWorkCalendarRules.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.ListWorkCalendarRules.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
