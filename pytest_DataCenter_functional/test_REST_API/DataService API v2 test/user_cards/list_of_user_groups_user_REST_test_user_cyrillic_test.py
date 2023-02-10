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

url_tail = "/api/v2/data_center/user_cards/groups_user?userID=1&inGroup=1"


@allure.epic("DataService API v2 (user_cards)")
@allure.feature("List of user groups REST_test_user_cyrillic")
@pytest.mark.testRESTAPI
@allure.story("Список групп пользователя REST_test_user_cyrillic")
class TestListOfUserGroups:
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

    @allure.title("Группа Users")
    def test_users_group(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step(
            "Тип ветки: 1 Internal Group, 2 External Group, 3 Custom Group, 4 Specials Control Groups"
        ):
            check.equal(data_dict["data"][0]["branch"], 1)
        with allure.step("Цвет профиля"):
            check.equal(data_dict["data"][0]["color"], 0)
        with allure.step("Имя группы"):
            check.equal(data_dict["data"][0]["displayName"], "Users")
        with allure.step("Идентификатор группы"):
            check.equal(data_dict["data"][0]["groupID"], 74)
        with allure.step("Флаг, находится ли пользователь в группе"):
            check.is_true(data_dict["data"][0]["inGroup"])
        with allure.step("Родитель группы"):
            check.equal(data_dict["data"][0]["parentID"], 32)
        with allure.step("Тип группы"):
            check.equal(data_dict["data"][0]["type"], 2)

    @allure.title("Группа Пользователи домена")
    def test_domain_users_group(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step(
            "Тип ветки: 1 Internal Group, 2 External Group, 3 Custom Group, 4 Specials Control Groups"
        ):
            check.equal(data_dict["data"][1]["branch"], 1)
        with allure.step("Цвет профиля"):
            check.equal(data_dict["data"][1]["color"], 0)
        with allure.step("Имя группы"):
            check.equal(data_dict["data"][1]["displayName"], "Пользователи домена")
        with allure.step("Идентификатор группы"):
            check.equal(data_dict["data"][1]["groupID"], 67)
        with allure.step("Флаг, находится ли пользователь в группе"):
            check.is_true(data_dict["data"][1]["inGroup"])
        with allure.step("Родитель группы"):
            check.equal(data_dict["data"][1]["parentID"], 74)
        with allure.step("Тип группы"):
            check.equal(data_dict["data"][1]["type"], 4)

    @allure.title("Группа Пользователи домена 2")
    def test_domain_users_group2(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step(
            "Тип ветки: 1 Internal Group, 2 External Group, 3 Custom Group, 4 Specials Control Groups"
        ):
            check.equal(data_dict["data"][2]["branch"], 1)
        with allure.step("Цвет профиля"):
            check.equal(data_dict["data"][2]["color"], 0)
        with allure.step("Имя группы"):
            check.equal(data_dict["data"][2]["displayName"], "Пользователи домена")
        with allure.step("Идентификатор группы"):
            check.equal(data_dict["data"][2]["groupID"], 67)
        with allure.step("Флаг, находится ли пользователь в группе"):
            check.is_true(data_dict["data"][2]["inGroup"])
        with allure.step("Родитель группы"):
            check.equal(data_dict["data"][2]["parentID"], 86)
        with allure.step("Тип группы"):
            check.equal(data_dict["data"][2]["type"], 4)

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
                schema_models.SchemaModelsDataServiceAPIv2.ListOfUserGroups.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.ListOfUserGroups.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
