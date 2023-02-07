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

url_tail = "/api/v2/task_management/persons?taskID=1"


@allure.epic("DataService API v2 (task_management)")
@allure.feature("List of persons involved in the incident or task")
@pytest.mark.testRESTAPI
@allure.story("Выводит список фигурантов из инцидента/задачи")
class TestListOfPersonsInvolvedInIncidentOrTask:
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

    @allure.title("Список фигурантов по задаче 1")
    def test_person_for_task_3(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 1)"
        ):
            check.equal(parsed_data["data"][0]["incidentID"], 73)
        with check.check, allure.step("Идентификатор пользователя (фигурант 1)"):
            check.equal(parsed_data["data"][0]["userID"], -160121)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 2)"
        ):
            check.equal(parsed_data["data"][1]["incidentID"], 73)
        with check.check, allure.step("Идентификатор пользователя (фигурант 2)"):
            check.equal(parsed_data["data"][1]["userID"], -160120)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 3)"
        ):
            check.equal(parsed_data["data"][2]["incidentID"], 73)
        with check.check, allure.step("Идентификатор пользователя (фигурант 3)"):
            check.equal(parsed_data["data"][2]["userID"], -160119)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 4)"
        ):
            check.equal(parsed_data["data"][3]["incidentID"], 1)
        with check.check, allure.step("Идентификатор пользователя (фигурант 4)"):
            check.equal(parsed_data["data"][3]["userID"], 5)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 5)"
        ):
            check.equal(parsed_data["data"][4]["incidentID"], 73)
        with check.check, allure.step("Идентификатор пользователя (фигурант 5)"):
            check.equal(parsed_data["data"][4]["userID"], 3880)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 6)"
        ):
            check.equal(parsed_data["data"][5]["incidentID"], 73)
        with check.check, allure.step("Идентификатор пользователя (фигурант 6)"):
            check.equal(parsed_data["data"][5]["userID"], 4082)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 7)"
        ):
            check.equal(parsed_data["data"][6]["incidentID"], 73)
        with check.check, allure.step("Идентификатор пользователя (фигурант 7)"):
            check.equal(parsed_data["data"][6]["userID"], 4271)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 8)"
        ):
            check.equal(parsed_data["data"][7]["incidentID"], 73)
        with check.check, allure.step("Идентификатор пользователя (фигурант 8)"):
            check.equal(parsed_data["data"][7]["userID"], 4346)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 9)"
        ):
            check.equal(parsed_data["data"][8]["incidentID"], 73)
        with check.check, allure.step("Идентификатор пользователя (фигурант 9)"):
            check.equal(parsed_data["data"][8]["userID"], 7068)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 10)"
        ):
            check.equal(parsed_data["data"][9]["incidentID"], 73)
        with check.check, allure.step("Идентификатор пользователя (фигурант 10)"):
            check.equal(parsed_data["data"][9]["userID"], 7463)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 11)"
        ):
            check.equal(parsed_data["data"][10]["incidentID"], 165)
        with check.check, allure.step("Идентификатор пользователя (фигурант 11)"):
            check.equal(parsed_data["data"][10]["userID"], 7886)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 12)"
        ):
            check.equal(parsed_data["data"][11]["incidentID"], 73)
        with check.check, allure.step("Идентификатор пользователя (фигурант 12)"):
            check.equal(parsed_data["data"][11]["userID"], 9543)

    @allure.title("Список фигурантов по задаче 7")
    def test_person_for_task_7(self, dc_api: DcApiWithToken):
        url_tail = "/api/v2/task_management/persons?taskID=7"
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 1)"
        ):
            check.equal(parsed_data["data"][0]["incidentID"], 129)
        with check.check, allure.step("Идентификатор пользователя (фигурант 1)"):
            check.equal(parsed_data["data"][0]["userID"], 3016)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 2)"
        ):
            check.equal(parsed_data["data"][1]["incidentID"], 129)
        with check.check, allure.step("Идентификатор пользователя (фигурант 2)"):
            check.equal(parsed_data["data"][1]["userID"], 7886)

    @allure.title("Список фигурантов по задаче 26")
    def test_person_for_task_26(self, dc_api: DcApiWithToken):
        url_tail = "/api/v2/task_management/persons?taskID=26"
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 1)"
        ):
            check.equal(parsed_data["data"][0]["incidentID"], 178)
        with check.check, allure.step("Идентификатор пользователя (фигурант 1)"):
            check.equal(parsed_data["data"][0]["userID"], 6305)

    @allure.title("Список фигурантов по задаче 28")
    def test_person_for_task_28(self, dc_api: DcApiWithToken):
        url_tail = "/api/v2/task_management/persons?taskID=28"
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 1)"
        ):
            check.equal(parsed_data["data"][0]["incidentID"], 187)
        with check.check, allure.step("Идентификатор пользователя (фигурант 1)"):
            check.equal(parsed_data["data"][0]["userID"], 6305)
        with check.check, allure.step(
            "Идентификатор инцидента (0 - фигурант добавлен в задачу вручную) (фигурант 2)"
        ):
            check.equal(parsed_data["data"][1]["incidentID"], 203)
        with check.check, allure.step("Идентификатор пользователя (фигурант 2)"):
            check.equal(parsed_data["data"][1]["userID"], 7886)

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
                schema_models.SchemaModelsDataServiceAPIv2.ListOfPersonsInvolvedInIncidentOrTask.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.ListOfPersonsInvolvedInIncidentOrTask.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
