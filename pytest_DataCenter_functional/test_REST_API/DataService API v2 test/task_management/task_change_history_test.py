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

url_tail = "/api/v2/task_management/task_history?taskID=2"


@allure.epic("DataService API v2 (task_management)")
@allure.feature("Task change history")
@pytest.mark.testRESTAPI
@allure.story("История изменений задачи")
class TestTaskChangeHistory:
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

    @allure.title("История изменений задачи 2")
    def test_change_history_task_2(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with check.check, allure.step("Дата изменения"):
            check.equal(parsed_data["data"][0]["changeDateTime"], 1637740630)
        with check.check, allure.step("Дата изменения статуса"):
            check.is_none(parsed_data["data"][0]["changeStateDateTime"])
        with check.check, allure.step("Срок завершения"):
            check.is_none(parsed_data["data"][0]["completeDateTime"])
        with check.check, allure.step("Дата создания"):
            check.equal(parsed_data["data"][0]["createDateTime"], 1637740630)
        with check.check, allure.step("Идентификатор пользователя (Автор задачи)"):
            check.equal(parsed_data["data"][0]["createUserID"], 7886)
        with check.check, allure.step("deleted"):
            check.is_false(parsed_data["data"][0]["deleted"])
        with check.check, allure.step("Описание задачи"):
            check.equal(parsed_data["data"][0]["description"], "")
        with check.check, allure.step("Идентификатор пользователя (Исполнитель задачи)"):
            check.equal(parsed_data["data"][0]["execUserID"], 7886)
        with check.check, allure.step("Пользовательские заметки"):
            check.is_none(parsed_data["data"][0]["notes"])
        with check.check, allure.step("ID Родителя, если это подзадача"):
            check.equal(parsed_data["data"][0]["parentTaskID"], 0)
        with check.check, allure.step("Приоритет: срочный, высокий, средний, низкий"):
            check.equal(parsed_data["data"][0]["priorityID"], 1)
        with check.check, allure.step("processDate"):
            check.equal(parsed_data["data"][0]["processDate"], 1637740620)
        with check.check, allure.step("Метка: Важно, Проверить, Обратить внимание"):
            check.is_none(parsed_data["data"][0]["tagID"])
        with check.check, allure.step("Название задачи"):
            check.equal(parsed_data["data"][0]["taskName"], "Новая задача")
        with check.check, allure.step("taskNumber"):
            check.equal(parsed_data["data"][0]["taskNumber"], 2)
        with check.check, allure.step("Статус: открыта, в работе, выполнено, отклонено"):
            check.equal(parsed_data["data"][0]["taskStateID"], 1)
        with check.check, allure.step("Тип задачи: идентификатор из таблицы TM_TasksTypes"):
            check.equal(parsed_data["data"][0]["taskTypeID"], 1)

    @allure.title("История изменений задачи 37")
    def test_change_history_task_37(self, dc_api: DcApiWithToken):
        url_tail = "/api/v2/task_management/task_history?taskID=37"
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with check.check, allure.step("Дата изменения (изменение 1)"):
            check.equal(parsed_data["data"][0]["changeDateTime"], 1659015383)
        with check.check, allure.step("Дата изменения статуса (изменение 1)"):
            check.is_none(parsed_data["data"][0]["changeStateDateTime"])
        with check.check, allure.step("Срок завершения (изменение 1)"):
            check.is_none(parsed_data["data"][0]["completeDateTime"])
        with check.check, allure.step("Дата создания (изменение 1)"):
            check.equal(parsed_data["data"][0]["createDateTime"], 1659015383)
        with check.check, allure.step("Идентификатор пользователя (Автор задачи) (изменение 1)"):
            check.equal(parsed_data["data"][0]["createUserID"], 6305)
        with check.check, allure.step("deleted (изменение 1)"):
            check.is_false(parsed_data["data"][0]["deleted"])
        with check.check, allure.step("Описание задачи (изменение 1)"):
            check.equal(
                parsed_data["data"][0]["description"], "Операции над учетной записью"
            )
        with check.check, allure.step(
            "Идентификатор пользователя (Исполнитель задачи) (изменение 1)"
        ):
            check.equal(parsed_data["data"][0]["execUserID"], 6305)
        with check.check, allure.step("Пользовательские заметки (изменение 1)"):
            check.is_none(parsed_data["data"][0]["notes"])
        with check.check, allure.step("ID Родителя, если это подзадача (изменение 1)"):
            check.equal(parsed_data["data"][0]["parentTaskID"], 0)
        with check.check, allure.step("Приоритет: срочный, высокий, средний, низкий (изменение 1)"):
            check.equal(parsed_data["data"][0]["priorityID"], 1)
        with check.check, allure.step("processDate (изменение 1)"):
            check.equal(parsed_data["data"][0]["processDate"], 1659015360)
        with check.check, allure.step("Метка: Важно, Проверить, Обратить внимание (изменение 1)"):
            check.is_none(parsed_data["data"][0]["tagID"])
        with check.check, allure.step("Название задачи (изменение 1)"):
            check.equal(
                parsed_data["data"][0]["taskName"], "Операции над учетной записью"
            )
        with check.check, allure.step("taskNumber (изменение 1)"):
            check.equal(parsed_data["data"][0]["taskNumber"], 33)
        with check.check, allure.step(
            "Статус: открыта, в работе, выполнено, отклонено (изменение 1)"
        ):
            check.equal(parsed_data["data"][0]["taskStateID"], 1)
        with check.check, allure.step(
            "Тип задачи: идентификатор из таблицы TM_TasksTypes (изменение 1)"
        ):
            check.equal(parsed_data["data"][0]["taskTypeID"], 1)

        with check.check, allure.step("Дата изменения (изменение 2)"):
            check.equal(parsed_data["data"][1]["changeDateTime"], 1659015457)
        with check.check, allure.step("Дата изменения статуса (изменение 2)"):
            check.equal(parsed_data["data"][1]["changeStateDateTime"], 1659015457)
        with check.check, allure.step("Срок завершения (изменение 2)"):
            check.is_none(parsed_data["data"][1]["completeDateTime"])
        with check.check, allure.step("Дата создания (изменение 2)"):
            check.equal(parsed_data["data"][1]["createDateTime"], 1659015383)
        with check.check, allure.step("Идентификатор пользователя (Автор задачи) (изменение 2)"):
            check.equal(parsed_data["data"][1]["createUserID"], 6305)
        with check.check, allure.step("deleted (изменение 2)"):
            check.is_false(parsed_data["data"][1]["deleted"])
        with check.check, allure.step("Описание задачи (изменение 2)"):
            check.equal(
                parsed_data["data"][1]["description"], "Операции над учетной записью"
            )
        with check.check, allure.step(
            "Идентификатор пользователя (Исполнитель задачи) (изменение 2)"
        ):
            check.equal(parsed_data["data"][1]["execUserID"], 6305)
        with check.check, allure.step("Пользовательские заметки (изменение 2)"):
            check.is_none(parsed_data["data"][1]["notes"])
        with check.check, allure.step("ID Родителя, если это подзадача (изменение 2)"):
            check.equal(parsed_data["data"][1]["parentTaskID"], 0)
        with check.check, allure.step("Приоритет: срочный, высокий, средний, низкий (изменение 2)"):
            check.equal(parsed_data["data"][1]["priorityID"], 1)
        with check.check, allure.step("processDate (изменение 2)"):
            check.equal(parsed_data["data"][1]["processDate"], 1659015480)
        with check.check, allure.step("Метка: Важно, Проверить, Обратить внимание (изменение 2)"):
            check.is_none(parsed_data["data"][1]["tagID"])
        with check.check, allure.step("Название задачи (изменение 2)"):
            check.equal(
                parsed_data["data"][1]["taskName"], "Операции над учетной записью"
            )
        with check.check, allure.step("taskNumber (изменение 2)"):
            check.equal(parsed_data["data"][1]["taskNumber"], 33)
        with check.check, allure.step(
            "Статус: открыта, в работе, выполнено, отклонено (изменение 2)"
        ):
            check.equal(parsed_data["data"][1]["taskStateID"], 1)
        with check.check, allure.step(
            "Тип задачи: идентификатор из таблицы TM_TasksTypes (изменение 2)"
        ):
            check.equal(parsed_data["data"][1]["taskTypeID"], 1)

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
                schema_models.SchemaModelsDataServiceAPIv2.TaskChangeHistory.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.TaskChangeHistory.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
