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

url_tail = "/api/v2/task_management/comments?taskID=23"


@allure.epic("DataService API v2 (task_management)")
@allure.feature("All comments on task")
@pytest.mark.testRESTAPI
@allure.story("Выборка всех комментариев по задаче ")
class TestAllCommentsOnTask:
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

    @allure.title("Задача 23")
    def test_task_id_23(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with check.check, allure.step("Идентификатор комментария (комментарий 1)"):
            assert_that(parsed_data["data"][0]["commentID"]).is_equal_to(3)
        with check.check, allure.step("Дата создания (комментарий 1)"):
            assert_that(parsed_data["data"][0]["createDateTime"]).is_equal_to(1650378045)
        with check.check, allure.step("Текст комментария (комментарий 1)"):
            assert_that(parsed_data["data"][0]["msg"]).is_equal_to("комментарий 1")
        with check.check, allure.step("Идентификатор пользователя (комментарий 1)"):
            assert_that(parsed_data["data"][0]["userID"]).is_equal_to(60705)
        with check.check, allure.step("Идентификатор комментария (комментарий 2)"):
            assert_that(parsed_data["data"][1]["commentID"]).is_equal_to(4)
        with check.check, allure.step("Дата создания (комментарий 2)"):
            assert_that(parsed_data["data"][1]["createDateTime"]).is_equal_to(1650378045)
        with check.check, allure.step("Текст комментария (комментарий 2)"):
            assert_that(parsed_data["data"][1]["msg"]).is_equal_to("комментарий 2")
        with check.check, allure.step("Идентификатор пользователя (комментарий 2)"):
            assert_that(parsed_data["data"][1]["userID"]).is_equal_to(60705)

    @allure.title("Задача 28")
    def test_task_id_28(self, dc_api: DcApiWithToken):
        url_tail = "/api/v2/task_management/comments?taskID=28"
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with check.check, allure.step("Идентификатор комментария (комментарий 1)"):
            assert_that(parsed_data["data"][0]["commentID"]).is_equal_to(7)
        with check.check, allure.step("Дата создания (комментарий 1)"):
            assert_that(parsed_data["data"][0]["createDateTime"]).is_equal_to(1660571204)
        with check.check, allure.step("Текст комментария (комментарий 1)"):
            assert_that(parsed_data["data"][0]["msg"]).is_equal_to("\nплополб")
        with check.check, allure.step("Идентификатор пользователя (комментарий 1)"):
            assert_that(parsed_data["data"][0]["userID"]).is_equal_to(7886)
        with check.check, allure.step("Идентификатор комментария (комментарий 2)"):
            assert_that(parsed_data["data"][1]["commentID"]).is_equal_to(8)
        with check.check, allure.step("Дата создания (комментарий 2)"):
            assert_that(parsed_data["data"][1]["createDateTime"]).is_equal_to(1660571229)
        with check.check, allure.step("Текст комментария (комментарий 2)"):
            assert_that(parsed_data["data"][1]["msg"]).is_equal_to("смпррм\n")
        with check.check, allure.step("Идентификатор пользователя (комментарий 2)"):
            assert_that(parsed_data["data"][1]["userID"]).is_equal_to(7886)
        with check.check, allure.step("Идентификатор комментария (комментарий 3)"):
            assert_that(parsed_data["data"][2]["commentID"]).is_equal_to(9)
        with check.check, allure.step("Дата создания (комментарий 3)"):
            assert_that(parsed_data["data"][2]["createDateTime"]).is_equal_to(1660571737)
        with check.check, allure.step("Текст комментария (комментарий 3)"):
            assert_that(
                parsed_data["data"][2]["msg"]).is_equal_to(
                "рпоап\nапропро\nмоьрмрои\n\nпрмролор\n\nопрьор\n\n\nрмо\n\n\nрмомоло\nололо\n\nлоло\n\n\nорморло\n",
            )
        with check.check, allure.step("Идентификатор пользователя (комментарий 3)"):
            assert_that(parsed_data["data"][2]["userID"]).is_equal_to(7886)
        with check.check, allure.step("Идентификатор комментария (комментарий 4)"):
            assert_that(parsed_data["data"][3]["commentID"]).is_equal_to(10)
        with check.check, allure.step("Дата создания (комментарий 4)"):
            assert_that(parsed_data["data"][3]["createDateTime"]).is_equal_to(1660571737)
        with check.check, allure.step("Текст комментария (комментарий 4)"):
            assert_that(
                parsed_data["data"][3]["msg"]).is_equal_to(
                "1\n2\n3\n4\n5\n6\nолоооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооо",
            )
        with check.check, allure.step("Идентификатор пользователя (комментарий 4)"):
            assert_that(parsed_data["data"][3]["userID"]).is_equal_to(7886)
        with check.check, allure.step("Идентификатор комментария (комментарий 5)"):
            assert_that(parsed_data["data"][4]["commentID"]).is_equal_to(11)
        with check.check, allure.step("Дата создания (комментарий 5)"):
            assert_that(parsed_data["data"][4]["createDateTime"]).is_equal_to(1660571737)
        with check.check, allure.step("Текст комментария (комментарий 5)"):
            assert_that(
                parsed_data["data"][4]["msg"]).is_equal_to(
                "ывапыва ывапывапыв аавыпаывапиывап ывап ывапы вап ывапыва ывап ывап ывап ывапывапыва ыва пывап ыва пывап ыва пывап ывап ывап ывап ывап ывап ",
            )
        with check.check, allure.step("Идентификатор пользователя (комментарий 5)"):
            assert_that(parsed_data["data"][4]["userID"]).is_equal_to(7886)
        with check.check, allure.step("Идентификатор комментария (комментарий 6)"):
            assert_that(parsed_data["data"][5]["commentID"]).is_equal_to(12)
        with check.check, allure.step("Дата создания (комментарий 6)"):
            assert_that(parsed_data["data"][5]["createDateTime"]).is_equal_to(1660571737)
        with check.check, allure.step("Текст комментария (комментарий 6)"):
            assert_that(
                parsed_data["data"][5]["msg"]).is_equal_to(
                "ыавпывап\nывпа\nыапы\nап\nып\nы\nапы\nп\nы\nп\nып\nы\nп\nы\nпы\nпа\nы\nпаы\nп\n\nып\nы\nп\nы\nп\nы\nпы\nп\nы\nпа\nы\nпы\nп\nы\nапы\nап\nы\nап\nцкп\nцы\nавп\nцк\nп",
            )
        with check.check, allure.step("Идентификатор пользователя (комментарий 6)"):
            assert_that(parsed_data["data"][5]["userID"]).is_equal_to(7886)
        with check.check, allure.step("Идентификатор комментария (комментарий 7)"):
            assert_that(parsed_data["data"][6]["commentID"]).is_equal_to(13)
        with check.check, allure.step("Дата создания (комментарий 7)"):
            assert_that(parsed_data["data"][6]["createDateTime"]).is_equal_to(1660571737)
        with check.check, allure.step("Текст комментария (комментарий 7)"):
            assert_that(
                parsed_data["data"][6]["msg"]).is_equal_to("фмачыамм ыапаывпыапыпыпыпыапы\nыы"
            )
        with check.check, allure.step("Идентификатор пользователя (комментарий 7)"):
            assert_that(parsed_data["data"][6]["userID"]).is_equal_to(7886)

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
                schema_models.SchemaModelsDataServiceAPIv2.AllCommentsOnTask.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.AllCommentsOnTask.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
