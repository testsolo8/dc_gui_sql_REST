# Standart libraries
import json

# Third party packages
import allure
import pytest
import pytest_check as check
from assertpy import assert_that
from jsonschema import validate
from pydantic import ValidationError

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import DcApiWithToken

url_tail = "/api/v2/task_management/incidents?selectFields=IncidentID, CreateDateTime, RawName, RawBody, TextBody, Attributes, Comment, IncidentUDL, ProductID, _RowsCount, RowNum&taskID=3"


@allure.epic("DataService API v2 (task_management)")
@allure.feature("List of incidents or incident body by task")
@pytest.mark.testRESTAPI
@allure.story("Получает список инцидентов или тело инцидента по задаче")
class TestListOfIncidentsOrIncidentBodyByTask:
    @allure.title("Успешность запроса")
    def test_status_code_200(self, dc_api: DcApiWithToken):
        r = dc_api.req_get(url_tail)
        assert_that(r.status_code).is_equal_to(200)

    @allure.title("Headers 'content-type'")
    def test_content_type(self, dc_api: DcApiWithToken):
        con_type = dc_api.req_get(url_tail).headers["content-type"]
        assert_that(con_type).is_equal_to(r"application/json; charset=utf-8")

    @allure.title("Время ответа запроса")
    def test_response_time(self, dc_api: DcApiWithToken):
        resp_time = dc_api.req_get(url_tail).elapsed.total_seconds()
        assert_that(resp_time).is_less_than_or_equal_to(30)

    @allure.title("Список инцидентов по задаче 3")
    def test_task_3(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with check.check, allure.step("Атрибуты инцидента"):
            assert_that(data_dict["data"][0]["attributes"]).is_equal_to("")
        with check.check, allure.step("Комментарий к инциденту"):
            assert_that(data_dict["data"][0]["comment"]).is_none()
        with check.check, allure.step("Дата создания"):
            assert_that(data_dict["data"][0]["createDateTime"]).is_equal_to(1637740654)
        with check.check, allure.step("Идентификатор аккаунта"):
            assert_that(data_dict["data"][0]["incidentID"]).is_equal_to(8)
        with check.check, allure.step("Уникальный идентификатор инцидента JSON"):
            assert_that(data_dict["data"][0]["incidentUDL"]).is_equal_to(
                "<607.75.15402891><DB&ser08_pol_local_ec_files~202105140904#15402891@11&1><23>",
            )
        with check.check, allure.step(
            "Продукт: 6 - AlertCenter, 11 - SIEM, 250 - AnalyticConsole"
        ):
            assert_that(data_dict["data"][0]["productID"]).is_equal_to(250)
        with check.check, allure.step("Текст инцидента"):
            assert_that(data_dict["data"][0]["rawBody"]).is_equal_to("")
        with check.check, allure.step("Название файла инцидента в родном формате"):
            assert_that(data_dict["data"][0]["rawName"]).is_equal_to("")
        with check.check, allure.step("Номер строки"):
            assert_that(data_dict["data"][0]["rowNum"]).is_equal_to(1)
        with check.check, allure.step("Текст инцидента"):
            assert_that(data_dict["data"][0]["textBody"]).is_equal_to("")

    @allure.title("Список инцидентов по задаче 37")
    def test_task_37(self, dc_api: DcApiWithToken):
        url_tail = "/api/v2/task_management/incidents?selectFields=IncidentID, CreateDateTime, RawName, RawBody, TextBody, Attributes, Comment, IncidentUDL, ProductID, _RowsCount, RowNum&taskID=37"
        data_dict = dc_api.req_get(url_tail).json()
        with check.check, allure.step("Атрибуты инцидента"):
            assert_that(data_dict["data"][0]["attributes"]).is_equal_to("")
        with check.check, allure.step("Комментарий к инциденту"):
            assert_that(data_dict["data"][0]["comment"]).is_equal_to("")
        with check.check, allure.step("Дата создания"):
            assert_that(data_dict["data"][0]["createDateTime"]).is_equal_to(1659015383)
        with check.check, allure.step("Идентификатор аккаунта"):
            assert_that(data_dict["data"][0]["incidentID"]).is_equal_to(188)
        with check.check, allure.step("Уникальный идентификатор инцидента JSON"):
            assert_that(data_dict["data"][0]["incidentUDL"]).is_none()
        with check.check, allure.step(
            "Продукт: 6 - AlertCenter, 11 - SIEM, 250 - AnalyticConsole"
        ):
            assert_that(data_dict["data"][0]["productID"]).is_equal_to(11)
        with check.check, allure.step("Текст инцидента"):
            assert_that(data_dict["data"][0]["rawBody"]).is_equal_to(
                "eyJmaWVsZHMiOlsiMTEuMDcuMjAyMiA5OjM0OjQ5IiwiQUQuINCf0YDQsNCy0LAg0LTQvtGB0YLRg9C/0LAiLCLQntC/0LXRgNCw0YbQuNC4INC90LDQtCDRg9GH0LXRgtC90L7QuSDQt9Cw0L/QuNGB0YzRjiIsIiIsIkZEQy5jb21wYW55Lm5ldCIsIiJdLCJpbmNpZGVudCI6eyJDb2xsZWN0aW9uIjoiQWRBY2NvdW50T3BlcmF0aW9ucyIsIkNyZWF0ZWQiOiIxMS4wNy4yMDIyIDk6MzQ6NDkiLCJJZCI6IjYyY2JjNDg5ZDc2ZTRmZjVjMTY0MDQ1ZiIsIkRiIjoic2llbSMxMS0wNy0yMDIyIiwiR3VpZCI6IntBMTE4NUZDMy1BRTc1LTQ3ODQtQjhENy1ERjVBMjk0OTQ1MjB9IiwiQ2xvbmUiOjB9LCJkZXRhaWwiOlt7InZhbHVlIjoi0J7QsdC90LDRgNGD0LbQtdC90Ysg0L7Qv9C10YDQsNGG0LjQuCDQvdCw0LQg0YPRh9C10YLQvdC+0Lkg0LfQsNC/0LjRgdGM0Y4iLCJkaXNwbGF5TmFtZSI6IiAgICAifSx7InZhbHVlIjoiIEZEQy5jb21wYW55Lm5ldCIsImRpc3BsYXlOYW1lIjoi0JrQvtC90YLRgNC+0LvQu9C10YAg0LTQvtC80LXQvdCwIn0seyJ2YWx1ZSI6Ils0NzM4XSDQo9GH0LXRgtC90LDRjyDQt9Cw0L/QuNGB0Ywg0L/QvtC70YzQt9C+0LLQsNGC0LXQu9GPINC40LfQvNC10L3QtdC90LAiLCJkaXNwbGF5TmFtZSI6IiAgICAifSx7InZhbHVlIjoiIGV4Y2hhbmdlIChFWENIQU5HRSkiLCJkaXNwbGF5TmFtZSI6ItCQ0LTQvNC40L3QuNGB0YLRgNCw0YLQvtGAIn0seyJ2YWx1ZSI6IiBoZWFsdGhtYWlsYm94ZTM4MmIxMShIZWFsdGhNYWlsYm94LUV4Y2hhbmdlLVBEMDEpIiwiZGlzcGxheU5hbWUiOiLQptC10LvQtdCy0L7QuSDQv9C+0LvRjNC30L7QstCw0YLQtdC70YwifV19",
            )
        with check.check, allure.step("Название файла инцидента в родном формате"):
            assert_that(data_dict["data"][0]["rawName"]).is_equal_to("")
        with check.check, allure.step("Номер строки"):
            assert_that(data_dict["data"][0]["rowNum"]).is_equal_to(1)
        with check.check, allure.step("Текст инцидента"):
            assert_that(data_dict["data"][0]["textBody"]).is_equal_to("")

    @allure.title("Список инцидентов по задаче 48")
    def test_task_48(self, dc_api: DcApiWithToken):
        url_tail = "/api/v2/task_management/incidents?selectFields=IncidentID, CreateDateTime, RawName, RawBody, TextBody, Attributes, Comment, IncidentUDL, ProductID, _RowsCount, RowNum&taskID=48"
        data_dict = dc_api.req_get(url_tail).json()
        with check.check, allure.step("Атрибуты инцидента (инцидент 1)"):
            assert_that(data_dict["data"][0]["attributes"]).is_equal_to("")
        with check.check, allure.step("Комментарий к инциденту (инцидент 1)"):
            assert_that(data_dict["data"][0]["comment"]).is_none()
        with check.check, allure.step("Дата создания (инцидент 1)"):
            assert_that(data_dict["data"][0]["createDateTime"]).is_equal_to(1661442148)
        with check.check, allure.step("Идентификатор аккаунта (инцидент 1)"):
            assert_that(data_dict["data"][0]["incidentID"]).is_equal_to(234)
        with check.check, allure.step(
            "Уникальный идентификатор инцидента JSON (инцидент 1)"
        ):
            assert_that(data_dict["data"][0]["incidentUDL"]).is_equal_to(
                '{"id":"1206.61.0","udl":"DB&pg_es_program_6_2_0_6#3#cmd.exe#7#1661385600@14&1","product":[27],"indexName":"DB:pg_es_program_6_2_0_6","docDate":"25.08.2022 00:00:00"}',
            )
        with check.check, allure.step(
            "Продукт: 6 - AlertCenter, 11 - SIEM, 250 - AnalyticConsole (инцидент 1)"
        ):
            assert_that(data_dict["data"][0]["productID"]).is_equal_to(250)
        with check.check, allure.step("Текст инцидента (инцидент 1)"):
            assert_that(data_dict["data"][0]["rawBody"]).is_equal_to("")
        with check.check, allure.step(
            "Название файла инцидента в родном формате (инцидент 1)"
        ):
            assert_that(data_dict["data"][0]["rawName"]).is_equal_to("")
        with check.check, allure.step("Номер строки (инцидент 1)"):
            assert_that(data_dict["data"][0]["rowNum"]).is_equal_to(1)
        with check.check, allure.step("Текст инцидента (инцидент 1)"):
            assert_that(data_dict["data"][0]["textBody"]).is_equal_to("")
        with check.check, allure.step("Атрибуты инцидента (инцидент 2)"):
            assert_that(data_dict["data"][1]["attributes"]).is_equal_to("")
        with check.check, allure.step("Комментарий к инциденту (инцидент 2)"):
            assert_that(data_dict["data"][1]["comment"]).is_none()
        with check.check, allure.step("Дата создания (инцидент 2)"):
            assert_that(data_dict["data"][1]["createDateTime"]).is_equal_to(1661442148)
        with check.check, allure.step("Идентификатор аккаунта (инцидент 2)"):
            assert_that(data_dict["data"][1]["incidentID"]).is_equal_to(235)
        with check.check, allure.step(
            "Уникальный идентификатор инцидента JSON (инцидент 2)"
        ):
            assert_that(data_dict["data"][1]["incidentUDL"]).is_equal_to(
                '{"id":"1206.61.0","udl":"DB&pg_es_program_6_2_0_6#3#explorer.exe#7#1661385600@14&1","product":[27],"indexName":"DB:pg_es_program_6_2_0_6","docDate":"25.08.2022 00:00:00"}',
            )
        with check.check, allure.step(
            "Продукт: 6 - AlertCenter, 11 - SIEM, 250 - AnalyticConsole (инцидент 2)"
        ):
            assert_that(data_dict["data"][1]["productID"]).is_equal_to(250)
        with check.check, allure.step("Текст инцидента (инцидент 2)"):
            assert_that(data_dict["data"][1]["rawBody"]).is_equal_to("")
        with check.check, allure.step(
            "Название файла инцидента в родном формате (инцидент 2)"
        ):
            assert_that(data_dict["data"][1]["rawName"]).is_equal_to("")
        with check.check, allure.step("Номер строки (инцидент 2)"):
            assert_that(data_dict["data"][1]["rowNum"]).is_equal_to(2)
        with check.check, allure.step("Текст инцидента (инцидент 2)"):
            assert_that(data_dict["data"][1]["textBody"]).is_equal_to("")
        with check.check, allure.step("Атрибуты инцидента (инцидент 3)"):
            assert_that(data_dict["data"][2]["attributes"]).is_equal_to("")
        with check.check, allure.step("Комментарий к инциденту (инцидент 3)"):
            assert_that(data_dict["data"][2]["comment"]).is_none()
        with check.check, allure.step("Дата создания (инцидент 3)"):
            assert_that(data_dict["data"][2]["createDateTime"]).is_equal_to(1661442149)
        with check.check, allure.step("Идентификатор аккаунта (инцидент 3)"):
            assert_that(data_dict["data"][2]["incidentID"]).is_equal_to(236)
        with check.check, allure.step(
            "Уникальный идентификатор инцидента JSON (инцидент 3)"
        ):
            assert_that(data_dict["data"][2]["incidentUDL"]).is_equal_to(
                '{"id":"1206.61.0","udl":"DB&pg_es_program_6_2_0_6#3#kmsauto x64.exe#7#1661385600@14&1","product":[27],"indexName":"DB:pg_es_program_6_2_0_6","docDate":"25.08.2022 00:00:00"}',
            )
        with check.check, allure.step(
            "Продукт: 6 - AlertCenter, 11 - SIEM, 250 - AnalyticConsole (инцидент 3)"
        ):
            assert_that(data_dict["data"][2]["productID"]).is_equal_to(250)
        with check.check, allure.step("Текст инцидента (инцидент 3)"):
            assert_that(data_dict["data"][2]["rawBody"]).is_equal_to("")
        with check.check, allure.step(
            "Название файла инцидента в родном формате (инцидент 3)"
        ):
            assert_that(data_dict["data"][2]["rawName"]).is_equal_to("")
        with check.check, allure.step("Номер строки (инцидент 3)"):
            assert_that(data_dict["data"][2]["rowNum"]).is_equal_to(3)
        with check.check, allure.step("Текст инцидента (инцидент 3)"):
            assert_that(data_dict["data"][2]["textBody"]).is_equal_to("")
        with check.check, allure.step("Атрибуты инцидента (инцидент 4)"):
            assert_that(data_dict["data"][3]["attributes"]).is_equal_to("")
        with check.check, allure.step("Комментарий к инциденту (инцидент 4)"):
            assert_that(data_dict["data"][3]["comment"]).is_none()
        with check.check, allure.step("Дата создания (инцидент 4)"):
            assert_that(data_dict["data"][3]["createDateTime"]).is_equal_to(1661442149)
        with check.check, allure.step("Идентификатор аккаунта (инцидент 4)"):
            assert_that(data_dict["data"][3]["incidentID"]).is_equal_to(237)
        with check.check, allure.step(
            "Уникальный идентификатор инцидента JSON (инцидент 4)"
        ):
            assert_that(data_dict["data"][3]["incidentUDL"]).is_equal_to(
                '{"id":"1206.61.0","udl":"DB&pg_es_program_6_2_0_6#3#kmstools.exe#7#1661385600@14&1","product":[27],"indexName":"DB:pg_es_program_6_2_0_6","docDate":"25.08.2022 00:00:00"}',
            )
        with check.check, allure.step(
            "Продукт: 6 - AlertCenter, 11 - SIEM, 250 - AnalyticConsole (инцидент 4)"
        ):
            assert_that(data_dict["data"][3]["productID"]).is_equal_to(250)
        with check.check, allure.step("Текст инцидента (инцидент 4)"):
            assert_that(data_dict["data"][3]["rawBody"]).is_equal_to("")
        with check.check, allure.step(
            "Название файла инцидента в родном формате (инцидент 4)"
        ):
            assert_that(data_dict["data"][3]["rawName"]).is_equal_to("")
        with check.check, allure.step("Номер строки (инцидент 4)"):
            assert_that(data_dict["data"][3]["rowNum"]).is_equal_to(4)
        with check.check, allure.step("Текст инцидента (инцидент 4)"):
            assert_that(data_dict["data"][3]["textBody"]).is_equal_to("")
        with check.check, allure.step("Атрибуты инцидента (инцидент 5)"):
            assert_that(data_dict["data"][4]["attributes"]).is_equal_to("")
        with check.check, allure.step("Комментарий к инциденту (инцидент 5)"):
            assert_that(data_dict["data"][4]["comment"]).is_none()
        with check.check, allure.step("Дата создания (инцидент 5)"):
            assert_that(data_dict["data"][4]["createDateTime"]).is_equal_to(1661442149)
        with check.check, allure.step("Идентификатор аккаунта (инцидент 5)"):
            assert_that(data_dict["data"][4]["incidentID"]).is_equal_to(238)
        with check.check, allure.step(
            "Уникальный идентификатор инцидента JSON (инцидент 5)"
        ):
            assert_that(data_dict["data"][4]["incidentUDL"]).is_equal_to(
                '{"id":"1206.61.0","udl":"DB&pg_es_program_6_2_0_6#3#licmgr.exe#7#1661385600@14&1","product":[27],"indexName":"DB:pg_es_program_6_2_0_6","docDate":"25.08.2022 00:00:00"}',
            )
        with check.check, allure.step(
            "Продукт: 6 - AlertCenter, 11 - SIEM, 250 - AnalyticConsole (инцидент 5)"
        ):
            assert_that(data_dict["data"][4]["productID"]).is_equal_to(250)
        with check.check, allure.step("Текст инцидента (инцидент 5)"):
            assert_that(data_dict["data"][4]["rawBody"]).is_equal_to("")
        with check.check, allure.step(
            "Название файла инцидента в родном формате (инцидент 5)"
        ):
            assert_that(data_dict["data"][4]["rawName"]).is_equal_to("")
        with check.check, allure.step("Номер строки (инцидент 5)"):
            assert_that(data_dict["data"][4]["rowNum"]).is_equal_to(5)
        with check.check, allure.step("Текст инцидента (инцидент 5)"):
            assert_that(data_dict["data"][4]["textBody"]).is_equal_to("")

    @allure.title("Проверка возвращаемой схемы JSON")
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
        for row in data_dict:
            try:
                schema_models.SchemaModelsDataServiceAPIv2.ListOfIncidentsOrIncidentBodyByTask.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.ListOfIncidentsOrIncidentBodyByTask.Data.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
