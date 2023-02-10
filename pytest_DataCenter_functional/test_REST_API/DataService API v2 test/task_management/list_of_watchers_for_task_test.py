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

url_tail = "/api/v2/task_management/watchers?taskID=1"


@allure.epic("DataService API v2 (task_management)")
@allure.feature("List of watchers for task")
@pytest.mark.testRESTAPI
@allure.story("Получает список наблюдателей по задаче")
class TestListOfWatchersForTask:
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

    @allure.title("Список наблюдателей по задаче 1")
    def test_list_of_watchers_task_1(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with check.check, allure.step("Идентификатор пользователя 1"):
            check.equal(data_dict["data"][0]["userID"], 7886)
        with check.check, allure.step("Идентификатор пользователя 2"):
            check.equal(data_dict["data"][1]["userID"], 60705)

    @allure.title("Список наблюдателей по задаче 23")
    def test_list_of_watchers_task_23(self, dc_api: DcApiWithToken):
        url_tail = "/api/v2/task_management/watchers?taskID=23"
        data_dict = dc_api.req_get(url_tail).json()
        with check.check, allure.step("Идентификатор пользователя 1"):
            check.equal(data_dict["data"][0]["userID"], 60705)

    @allure.title("Список наблюдателей по задаче 34")
    def test_list_of_watchers_task_34(self, dc_api: DcApiWithToken):
        url_tail = "/api/v2/task_management/watchers?taskID=34"
        data_dict = dc_api.req_get(url_tail).json()
        with check.check, allure.step("Идентификатор пользователя 1"):
            check.equal(data_dict["data"][0]["userID"], 61724)

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
                schema_models.SchemaModelsDataServiceAPIv2.ListOfWatchersForTask.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.ListOfWatchersForTask.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
