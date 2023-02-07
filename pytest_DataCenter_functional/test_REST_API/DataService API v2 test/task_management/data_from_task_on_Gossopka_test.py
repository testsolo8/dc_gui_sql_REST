# Standart libraries
import json

# Third party packages
import allure
import pytest
import pytest_check as check
from jsonschema import validate
from pydantic import ValidationError
from assertpy import assert_that

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import DcApiWithToken

url_tail = "/api/v2/task_management/gossopka?taskID=23"


@allure.epic("DataService API v2 (task_management)")
@allure.feature("Data from task on Gossopka")
@pytest.mark.testRESTAPI
@allure.story("Получает из задачи данные по Госсопке")
class TestDataFromTaskOnGossopka:
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

    @allure.title("Данные по Госсопке из задачи 23")
    def test_task_id_23(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with check.check, allure.step("JSON с данными"):
            assert_that(
                parsed_data["data"][0]["data"]).is_equal_to(
                '{"uuid":"d9b75c84-3674-4d52-84ee-59c8290095bd","identifier":"22-04-20",'
                '"category":"Уведомление о компьютерном инциденте","type":"Вовлечение контролируемого ресурса в инфраструктуру ВПО"'
                ',"activitystatus":"Меры приняты","eventdescription":"тут краткое описание проблемы",'
                '"detecttime":"2022-04-20T20:59:00.000Z","tlp":"TLP:GREEN","affectedsystemname":"",'
                '"affectedsystemcategory":"","affectedsystemfunction":"","location":"RU","productinfo":[]}',
            )

    @allure.title("Данные по Госсопке из задачи 25")
    def test_task_id_25(self, dc_api: DcApiWithToken):
        url_tail = "/api/v2/task_management/gossopka?taskID=25"
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with check.check, allure.step("JSON с данными"):
            assert_that(
                parsed_data["data"][0]["data"]).is_equal_to(
                '{"uuid":"30dab63a-1066-48b0-91d3-d55e023d2593","identifier":"22-04-19",'
                '"category":"Уведомление о компьютерном инциденте","type":"Заражение ВПО","activitystatus":"",'
                '"eventdescription":"zxbvzxcv","detecttime":"2022-04-20T20:59:00.000Z","tlp":"TLP:AMBER",'
                '"affectedsystemname":"","affectedsystemcategory":"","affectedsystemfunction":"","location":"RU","productinfo":[]}',
            )

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
                schema_models.SchemaModelsDataServiceAPIv2.DataFromTaskOnGossopka.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.DataFromTaskOnGossopka.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
