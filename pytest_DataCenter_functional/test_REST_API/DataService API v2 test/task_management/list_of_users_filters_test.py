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

url_tail = "/api/v2/task_management/filters?userID=0"


@allure.epic("DataService API v2 (task_management)")
@allure.feature("List of user's filters")
@pytest.mark.testRESTAPI
@allure.story("Получает список фильтров пользователя")
class TestListOfUsersFilters:
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

    @allure.title("Фильтр")
    def test_filter(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with check.check, allure.step("Описание фильтра"):
            check.equal(data_dict["data"][0]["description"], "тест для реста")
        with check.check, allure.step("Идентификатор типа"):
            check.equal(data_dict["data"][0]["filterID"], 1)
        with check.check, allure.step("Название типа задачи"):
            check.equal(data_dict["data"][0]["filterName"], "test for rest")
        with check.check, allure.step("Параметры фильтра Base64"):
            check.equal(
                data_dict["data"][0]["value"],
                "eyJwYXJlbnRUYXNrSUQiOjAsInNlYXJjaFRleHQiOiIiLCJ0YXNrU3RhdGVJRExpc3QiOiIxLDIiLCJwcmlvcml0eUlETGlzdCI6I"
                "jEsMiw1IiwidGFnSURMaXN0IjoiMSwyIiwidGFza1R5cGVJRExpc3QiOiIyIiwiZXhlY1VzZXJJRExpc3QiOlsxNSwxNCw1LDddLCJj"
                "cmVhdGVVc2VySURMaXN0IjpbMTVdLCJwZXJzb25JRExpc3QiOlsxMCw2LDgsMTMsMiw0LDUsNywxLDMsMTIsMTEsOV0sImNyZW"
                "F0ZURhdGVGcm9tIjoxNjYxOTkwNDAwLCJjcmVhdGVEYXRlVG8iOjE2NjIyNDk2MDAsImNoYW5nZURhdGVGcm9tIjoxNjU2NjMzN"
                "jAwLCJjaGFuZ2VEYXRlVG8iOjE2NjI4NTQ0MDAsImNvbXBsZXRlRGF0ZUZyb20iOjB9",
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
                schema_models.SchemaModelsDataServiceAPIv2.ListOfUsersFilters.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.ListOfUsersFilters.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
