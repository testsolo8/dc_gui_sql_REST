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

url_tail = "/api/v2/task_management/tags"


@allure.epic("DataService API v2 (task_management)")
@allure.feature("List of tags")
@pytest.mark.testRESTAPI
@allure.story("Получает список меток")
class TestListOfTags:
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

    @allure.title("Список меток")
    def test_list_of_tags(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with check.check, allure.step("Цвет метки (Important)"):
            check.equal(parsed_data["data"][0]["tagColor"], 1)
        with check.check, allure.step("Идентификатор метки (Important)"):
            check.equal(parsed_data["data"][0]["tagID"], 1)
        with check.check, allure.step("Название метки (Important)"):
            check.equal(parsed_data["data"][0]["tagName"], "Important")
        with check.check, allure.step("Цвет метки (Verify)"):
            check.equal(parsed_data["data"][1]["tagColor"], 2)
        with check.check, allure.step("Идентификатор метки (Verify)"):
            check.equal(parsed_data["data"][1]["tagID"], 2)
        with check.check, allure.step("Название метки (Verify)"):
            check.equal(parsed_data["data"][1]["tagName"], "Verify")
        with check.check, allure.step("Цвет метки (Note)"):
            check.equal(parsed_data["data"][2]["tagColor"], 3)
        with check.check, allure.step("Идентификатор метки (Note)"):
            check.equal(parsed_data["data"][2]["tagID"], 3)
        with check.check, allure.step("Название метки (Note)"):
            check.equal(parsed_data["data"][2]["tagName"], "Note")

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
                schema_models.SchemaModelsDataServiceAPIv2.ListOfTags.parse_obj(row)
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.ListOfTags.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
