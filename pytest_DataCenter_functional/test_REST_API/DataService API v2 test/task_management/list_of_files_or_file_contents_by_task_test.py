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

url_tail = "/api/v2/task_management/attached_files?taskID=1"


@allure.epic("DataService API v2 (task_management)")
@allure.feature("List of files or file contents by task")
@pytest.mark.testRESTAPI
@allure.story("Получает список файлов или содержимое файла по задаче")
class TestListFilesOrFileContentsByTask:
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

    @allure.title("Задача 1")
    def test_task_id_1(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with check.check, allure.step("Дата создания (файл 1)"):
            assert_that(parsed_data["data"][0]["createDateTime"]).is_equal_to(1662713423)
        with check.check, allure.step("Комментарий (файл 1)"):
            assert_that(parsed_data["data"][0]["description"]).is_equal_to("файл vxd")
        with check.check, allure.step("Идентификатор аккаунта (файл 1)"):
            assert_that(parsed_data["data"][0]["fileID"]).is_equal_to(12)
        with check.check, allure.step("Имя файла (файл 1)"):
            assert_that(parsed_data["data"][0]["fileName"]).is_equal_to("CGLPT9X.VXD")
        with check.check, allure.step("Размер файла (файл 1)"):
            assert_that(parsed_data["data"][0]["fileSize"]).is_equal_to(7259)
        with check.check, allure.step("Дата создания (файл 2)"):
            assert_that(parsed_data["data"][1]["createDateTime"]).is_equal_to(1662713423)
        with check.check, allure.step("Комментарий (файл 2)"):
            assert_that(parsed_data["data"][1]["description"]).is_equal_to("файл bat")
        with check.check, allure.step("Идентификатор аккаунта (файл 2)"):
            assert_that(parsed_data["data"][1]["fileID"]).is_equal_to(13)
        with check.check, allure.step("Имя файла (файл 2)"):
            assert_that(parsed_data["data"][1]["fileName"]).is_equal_to("WinInteg.bat")
        with check.check, allure.step("Размер файла (файл 2)"):
            assert_that(parsed_data["data"][1]["fileSize"]).is_equal_to(9892)

    @allure.title("Задача 3")
    def test_task_id_3(self, dc_api: DcApiWithToken):
        url_tail = "/api/v2/task_management/attached_files?taskID=3"
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with check.check, allure.step("Дата создания (файл 1)"):
            assert_that(parsed_data["data"][0]["createDateTime"]).is_equal_to(1660570428)
        with check.check, allure.step("Комментарий (файл 1)"):
            assert_that(parsed_data["data"][0]["description"]).is_equal_to("")
        with check.check, allure.step("Идентификатор аккаунта (файл 1)"):
            assert_that(parsed_data["data"][0]["fileID"]).is_equal_to(5)
        with check.check, allure.step("Имя файла (файл 1)"):
            assert_that(parsed_data["data"][0]["fileName"]).is_equal_to("7z.dll")
        with check.check, allure.step("Размер файла (файл 1)"):
            assert_that(parsed_data["data"][0]["fileSize"]).is_equal_to(1236480)
        with check.check, allure.step("Дата создания (файл 2)"):
            assert_that(parsed_data["data"][1]["createDateTime"]).is_equal_to(1660570717)
        with check.check, allure.step("Комментарий (файл 2)"):
            assert_that(parsed_data["data"][1]["description"]).is_equal_to("")
        with check.check, allure.step("Идентификатор аккаунта (файл 2)"):
            assert_that(parsed_data["data"][1]["fileID"]).is_equal_to(9)
        with check.check, allure.step("Имя файла (файл 2)"):
            assert_that(parsed_data["data"][1]["fileName"]).is_equal_to("7z64.dll")
        with check.check, allure.step("Размер файла (файл 2)"):
            assert_that(parsed_data["data"][1]["fileSize"]).is_equal_to(1814016)
        with check.check, allure.step("Дата создания (файл 3)"):
            assert_that(parsed_data["data"][2]["createDateTime"]).is_equal_to(1660570717)
        with check.check, allure.step("Комментарий (файл 3)"):
            assert_that(parsed_data["data"][2]["description"]).is_equal_to("")
        with check.check, allure.step("Идентификатор аккаунта (файл 3)"):
            assert_that(parsed_data["data"][2]["fileID"]).is_equal_to(10)
        with check.check, allure.step("Имя файла (файл 3)"):
            assert_that(parsed_data["data"][2]["fileName"]).is_equal_to("7z64.dll")
        with check.check, allure.step("Размер файла (файл 3)"):
            assert_that(parsed_data["data"][2]["fileSize"]).is_equal_to(1814016)
        with check.check, allure.step("Дата создания (файл 4)"):
            assert_that(parsed_data["data"][3]["createDateTime"]).is_equal_to(1660570482)
        with check.check, allure.step("Комментарий (файл 4)"):
            assert_that(parsed_data["data"][3]["description"]).is_equal_to("")
        with check.check, allure.step("Идентификатор аккаунта (файл 4)"):
            assert_that(parsed_data["data"][3]["fileID"]).is_equal_to(7)
        with check.check, allure.step("Имя файла (файл 4)"):
            assert_that(parsed_data["data"][3]["fileName"]).is_equal_to("operations.txt")
        with check.check, allure.step("Размер файла (файл 4)"):
            assert_that(parsed_data["data"][3]["fileSize"]).is_equal_to(395)
        with check.check, allure.step("Дата создания (файл 5)"):
            assert_that(parsed_data["data"][4]["createDateTime"]).is_equal_to(1660570482)
        with check.check, allure.step("Комментарий (файл 5)"):
            assert_that(parsed_data["data"][4]["description"]).is_equal_to("")
        with check.check, allure.step("Идентификатор аккаунта (файл 5)"):
            assert_that(parsed_data["data"][4]["fileID"]).is_equal_to(8)
        with check.check, allure.step("Имя файла (файл 5)"):
            assert_that(parsed_data["data"][4]["fileName"]).is_equal_to("siissproc.dll")
        with check.check, allure.step("Размер файла (файл 5)"):
            assert_that(parsed_data["data"][4]["fileSize"]).is_equal_to(496136)

    @allure.title("Задача 23")
    def test_task_id_23(self, dc_api: DcApiWithToken):
        url_tail = "/api/v2/task_management/attached_files?taskID=23"
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with check.check, allure.step("Дата создания (файл 1)"):
            assert_that(parsed_data["data"][0]["createDateTime"]).is_equal_to(1657101040)
        with check.check, allure.step("Комментарий (файл 1)"):
            assert_that(parsed_data["data"][0]["description"]).is_equal_to("")
        with check.check, allure.step("Идентификатор аккаунта (файл 1)"):
            assert_that(parsed_data["data"][0]["fileID"]).is_equal_to(1)
        with check.check, allure.step("Имя файла (файл 1)"):
            assert_that(
                parsed_data["data"][0]["fileName"]).is_equal_to(
                "dsk0002.company.net_user2_company.net_06_06_2022 92745_06_06_2022 93111_5_2.vid",
            )
        with check.check, allure.step("Размер файла (файл 1)"):
            assert_that(parsed_data["data"][0]["fileSize"]).is_equal_to(37999)
        with check.check, allure.step("Дата создания (файл 2)"):
            assert_that(parsed_data["data"][1]["createDateTime"]).is_equal_to(1657101040)
        with check.check, allure.step("Комментарий (файл 2)"):
            assert_that(parsed_data["data"][1]["description"]).is_equal_to("")
        with check.check, allure.step("Идентификатор аккаунта (файл 2)"):
            assert_that(parsed_data["data"][1]["fileID"]).is_equal_to(2)
        with check.check, allure.step("Имя файла (файл 2)"):
            assert_that(
                parsed_data["data"][1]["fileName"]).is_equal_to(
                "Троицкий _ Исследование paботы сварного рамного узла _выборочно_ _1977_.pdf",
            )
        with check.check, allure.step("Размер файла (файл 2)"):
            assert_that(parsed_data["data"][1]["fileSize"]).is_equal_to(1549366)

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
                schema_models.SchemaModelsDataServiceAPIv2.ListFilesOrFileContentsByTask.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.ListFilesOrFileContentsByTask.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
