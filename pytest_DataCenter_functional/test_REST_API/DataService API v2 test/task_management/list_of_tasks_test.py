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

url_tail = (
    "/api/v2/task_management/tasks?selectFields=TaskID, CreateDateTime, ChangeDateTime, CompleteDateTime, "
    "ChangeStateDateTime, TaskName, Description, TaskTypeID, TypeIconID,  TypeName, TaskNumber, TaskStateID, "
    "PriorityID, TagID, TagName, TagColor, CreateUserID, ExecUserID, ParentTaskID, Notes, CntChildTasks, "
    "CntEndChildTasks, Prefix, ParentTaskNumber, RvisionID, GossopkaID, _RowsCount, RowNum"
)


@allure.epic("DataService API v2 (task_management)")
@allure.feature("List of tasks")
@pytest.mark.testRESTAPI
@allure.story("Получение списка задач")
class TestListOfTasks:
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

    @allure.title("Задача 0")
    def test_task_0(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with check.check, allure.step("Дата изменения"):
            check.equal(data_dict["data"][0]["changeDateTime"], 1662713423)
        with check.check, allure.step("Дата изменения статуса"):
            check.equal(data_dict["data"][0]["changeStateDateTime"], 1662713423)
        with check.check, allure.step("Общее количество подзадач"):
            check.equal(data_dict["data"][0]["cntChildTasks"], 0)
        with check.check, allure.step(
            "Количествое выполненных подзадач (статус выполнено, отклонено)"
        ):
            check.equal(data_dict["data"][0]["cntEndChildTasks"], 0)
        with check.check, allure.step("Срок завершения"):
            check.is_none(data_dict["data"][0]["completeDateTime"])
        with check.check, allure.step("Дата создания"):
            check.equal(data_dict["data"][0]["createDateTime"], 1636611309)
        with check.check, allure.step("Идентификатор пользователя (Автор задачи)"):
            check.equal(data_dict["data"][0]["createUserID"], 7886)
        with check.check, allure.step("Описание задачи"):
            check.equal(data_dict["data"][0]["description"], "taskID : 1")
        with check.check, allure.step(
            "Идентификатор пользователя (Исполнитель задачи)"
        ):
            check.equal(data_dict["data"][0]["execUserID"], 15)
        with check.check, allure.step("Идентификатор задачи ГосСОПКА"):
            check.is_none(data_dict["data"][0]["gossopkaID"])
        with check.check, allure.step("Пользовательские заметки"):
            check.is_none(data_dict["data"][0]["notes"])
        with check.check, allure.step("ID Родителя, если это подзадача"):
            check.equal(data_dict["data"][0]["parentTaskID"], 0)
        with check.check, allure.step("Сквозной номер задачи родителя"):
            check.is_none(data_dict["data"][0]["parentTaskNumber"])
        with check.check, allure.step("Префикс нумерации задач"):
            check.equal(data_dict["data"][0]["prefix"], "GEN")
        with check.check, allure.step("Приоритет: срочный, высокий, средний, низкий"):
            check.equal(data_dict["data"][0]["priorityID"], 3)
        with check.check, allure.step("Номер строки"):
            check.equal(data_dict["data"][0]["rowNum"], 1)
        with check.check, allure.step("Идентификатор задачи R-Vision"):
            check.is_none(data_dict["data"][0]["rvisionID"])
        with check.check, allure.step("Цвет метки"):
            check.equal(data_dict["data"][0]["tagColor"], 2)
        with check.check, allure.step("Метка: Важно, Проверить, Обратить внимание"):
            check.equal(data_dict["data"][0]["tagID"], 2)
        with check.check, allure.step("Название метки"):
            check.equal(data_dict["data"][0]["tagName"], "Verify")
        with check.check, allure.step("Идентификатор задачи"):
            check.equal(data_dict["data"][0]["taskID"], 1)
        with check.check, allure.step("Название задачи"):
            check.equal(data_dict["data"][0]["taskName"], "New task")
        with check.check, allure.step("Сквозной номер задачи"):
            check.equal(data_dict["data"][0]["taskNumber"], "GEN-1")
        with check.check, allure.step(
            "Статус: открыта, в работе, выполнено, отклонено"
        ):
            check.equal(data_dict["data"][0]["taskStateID"], 1)
        with check.check, allure.step(
            "Тип задачи: идентификатор из таблицы TM_TasksTypes"
        ):
            check.equal(data_dict["data"][0]["taskTypeID"], 1)
        with check.check, allure.step("Идентификатор иконки типа задачи"):
            check.equal(data_dict["data"][0]["typeIconID"], 1)
        with check.check, allure.step("Название типа задачи"):
            check.equal(data_dict["data"][0]["typeName"], "Common task")

    @allure.title("Задача 4")
    def test_task_4(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with check.check, allure.step("Дата изменения"):
            check.equal(data_dict["data"][4]["changeDateTime"], 1646226061)
        with check.check, allure.step("Дата изменения статуса"):
            check.equal(data_dict["data"][4]["changeStateDateTime"], 1646226061)
        with check.check, allure.step("Общее количество подзадач"):
            check.equal(data_dict["data"][4]["cntChildTasks"], 0)
        with check.check, allure.step(
            "Количествое выполненных подзадач (статус выполнено, отклонено)"
        ):
            check.equal(data_dict["data"][4]["cntEndChildTasks"], 0)
        with check.check, allure.step("Срок завершения"):
            check.is_none(data_dict["data"][4]["completeDateTime"])
        with check.check, allure.step("Дата создания"):
            check.equal(data_dict["data"][4]["createDateTime"], 1637752856)
        with check.check, allure.step("Идентификатор пользователя (Автор задачи)"):
            check.equal(data_dict["data"][4]["createUserID"], 7886)
        with check.check, allure.step("Описание задачи"):
            check.equal(data_dict["data"][4]["description"], "")
        with check.check, allure.step(
            "Идентификатор пользователя (Исполнитель задачи)"
        ):
            check.equal(data_dict["data"][4]["execUserID"], 7886)
        with check.check, allure.step("Идентификатор задачи ГосСОПКА"):
            check.is_none(data_dict["data"][4]["gossopkaID"])
        with check.check, allure.step("Пользовательские заметки"):
            check.is_none(data_dict["data"][4]["notes"])
        with check.check, allure.step("ID Родителя, если это подзадача"):
            check.equal(data_dict["data"][4]["parentTaskID"], 0)
        with check.check, allure.step("Сквозной номер задачи родителя"):
            check.is_none(data_dict["data"][4]["parentTaskNumber"])
        with check.check, allure.step("Префикс нумерации задач"):
            check.equal(data_dict["data"][4]["prefix"], "GEN")
        with check.check, allure.step("Приоритет: срочный, высокий, средний, низкий"):
            check.equal(data_dict["data"][4]["priorityID"], 1)
        with check.check, allure.step("Номер строки"):
            check.equal(data_dict["data"][4]["rowNum"], 5)
        with check.check, allure.step("Идентификатор задачи R-Vision"):
            check.is_none(data_dict["data"][4]["rvisionID"])
        with check.check, allure.step("Цвет метки"):
            check.equal(data_dict["data"][4]["tagColor"], 1)
        with check.check, allure.step("Метка: Важно, Проверить, Обратить внимание"):
            check.equal(data_dict["data"][4]["tagID"], 1)
        with check.check, allure.step("Название метки"):
            check.equal(data_dict["data"][4]["tagName"], "Important")
        with check.check, allure.step("Идентификатор задачи"):
            check.equal(data_dict["data"][4]["taskID"], 5)
        with check.check, allure.step("Название задачи"):
            check.equal(data_dict["data"][4]["taskName"], "Новая задача")
        with check.check, allure.step("Сквозной номер задачи"):
            check.equal(data_dict["data"][4]["taskNumber"], "GEN-5")
        with check.check, allure.step(
            "Статус: открыта, в работе, выполнено, отклонено"
        ):
            check.equal(data_dict["data"][4]["taskStateID"], 1)
        with check.check, allure.step(
            "Тип задачи: идентификатор из таблицы TM_TasksTypes"
        ):
            check.equal(data_dict["data"][4]["taskTypeID"], 1)
        with check.check, allure.step("Идентификатор иконки типа задачи"):
            check.equal(data_dict["data"][4]["typeIconID"], 1)
        with check.check, allure.step("Название типа задачи"):
            check.equal(data_dict["data"][4]["typeName"], "Common task")

    @allure.title("Задача 27")
    def test_task_27(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with check.check, allure.step("Дата изменения"):
            check.equal(data_dict["data"][27]["changeDateTime"], 1660572015)
        with check.check, allure.step("Дата изменения статуса"):
            check.equal(data_dict["data"][27]["changeStateDateTime"], 1660572015)
        with check.check, allure.step("Общее количество подзадач"):
            check.equal(data_dict["data"][27]["cntChildTasks"], 0)
        with check.check, allure.step(
            "Количествое выполненных подзадач (статус выполнено, отклонено)"
        ):
            check.equal(data_dict["data"][27]["cntEndChildTasks"], 0)
        with check.check, allure.step("Срок завершения"):
            check.is_none(data_dict["data"][27]["completeDateTime"])
        with check.check, allure.step("Дата создания"):
            check.equal(data_dict["data"][27]["createDateTime"], 1650529942)
        with check.check, allure.step("Идентификатор пользователя (Автор задачи)"):
            check.equal(data_dict["data"][27]["createUserID"], 60705)
        with check.check, allure.step("Описание задачи"):
            check.equal(
                data_dict["data"][27]["description"],
                "бьиб<div><br></div><div>олдьл</div><div><br></div>",
            )
        with check.check, allure.step(
            "Идентификатор пользователя (Исполнитель задачи)"
        ):
            check.equal(data_dict["data"][27]["execUserID"], 60705)
        with check.check, allure.step("Идентификатор задачи ГосСОПКА"):
            check.is_none(data_dict["data"][27]["gossopkaID"])
        with check.check, allure.step("Пользовательские заметки"):
            check.is_none(data_dict["data"][27]["notes"])
        with check.check, allure.step("ID Родителя, если это подзадача"):
            check.equal(data_dict["data"][27]["parentTaskID"], 0)
        with check.check, allure.step("Сквозной номер задачи родителя"):
            check.is_none(data_dict["data"][27]["parentTaskNumber"])
        with check.check, allure.step("Префикс нумерации задач"):
            check.equal(data_dict["data"][27]["prefix"], "INC")
        with check.check, allure.step("Приоритет: срочный, высокий, средний, низкий"):
            check.equal(data_dict["data"][27]["priorityID"], 1)
        with check.check, allure.step("Номер строки"):
            check.equal(data_dict["data"][27]["rowNum"], 28)
        with check.check, allure.step("Идентификатор задачи R-Vision"):
            check.is_none(data_dict["data"][27]["rvisionID"])
        with check.check, allure.step("Цвет метки"):
            check.equal(data_dict["data"][27]["tagColor"], 2)
        with check.check, allure.step("Метка: Важно, Проверить, Обратить внимание"):
            check.equal(data_dict["data"][27]["tagID"], 2)
        with check.check, allure.step("Название метки"):
            check.equal(data_dict["data"][27]["tagName"], "Verify")
        with check.check, allure.step("Идентификатор задачи"):
            check.equal(data_dict["data"][27]["taskID"], 28)
        with check.check, allure.step("Название задачи"):
            check.equal(data_dict["data"][27]["taskName"], "Новая задача")
        with check.check, allure.step("Сквозной номер задачи"):
            check.equal(data_dict["data"][27]["taskNumber"], "INC-1")
        with check.check, allure.step(
            "Статус: открыта, в работе, выполнено, отклонено"
        ):
            check.equal(data_dict["data"][27]["taskStateID"], 2)
        with check.check, allure.step(
            "Тип задачи: идентификатор из таблицы TM_TasksTypes"
        ):
            check.equal(data_dict["data"][27]["taskTypeID"], 2)
        with check.check, allure.step("Идентификатор иконки типа задачи"):
            check.equal(data_dict["data"][27]["typeIconID"], 2)
        with check.check, allure.step("Название типа задачи"):
            check.equal(data_dict["data"][27]["typeName"], "Information Security")

    @allure.title("Задача 36")
    def test_task_36(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with check.check, allure.step("Дата изменения"):
            check.equal(data_dict["data"][36]["changeDateTime"], 1659015457)
        with check.check, allure.step("Дата изменения статуса"):
            check.equal(data_dict["data"][36]["changeStateDateTime"], 1659015457)
        with check.check, allure.step("Общее количество подзадач"):
            check.equal(data_dict["data"][36]["cntChildTasks"], 0)
        with check.check, allure.step(
            "Количествое выполненных подзадач (статус выполнено, отклонено)"
        ):
            check.equal(data_dict["data"][36]["cntEndChildTasks"], 0)
        with check.check, allure.step("Срок завершения"):
            check.is_none(data_dict["data"][36]["completeDateTime"])
        with check.check, allure.step("Дата создания"):
            check.equal(data_dict["data"][36]["createDateTime"], 1659015383)
        with check.check, allure.step("Идентификатор пользователя (Автор задачи)"):
            check.equal(data_dict["data"][36]["createUserID"], 6305)
        with check.check, allure.step("Описание задачи"):
            check.equal(
                data_dict["data"][36]["description"], "Операции над учетной записью"
            )
        with check.check, allure.step(
            "Идентификатор пользователя (Исполнитель задачи)"
        ):
            check.equal(data_dict["data"][36]["execUserID"], 6305)
        with check.check, allure.step("Идентификатор задачи ГосСОПКА"):
            check.is_none(data_dict["data"][36]["gossopkaID"])
        with check.check, allure.step("Пользовательские заметки"):
            check.is_none(data_dict["data"][36]["notes"])
        with check.check, allure.step("ID Родителя, если это подзадача"):
            check.equal(data_dict["data"][36]["parentTaskID"], 0)
        with check.check, allure.step("Сквозной номер задачи родителя"):
            check.is_none(data_dict["data"][36]["parentTaskNumber"])
        with check.check, allure.step("Префикс нумерации задач"):
            check.equal(data_dict["data"][36]["prefix"], "GEN")
        with check.check, allure.step("Приоритет: срочный, высокий, средний, низкий"):
            check.equal(data_dict["data"][36]["priorityID"], 1)
        with check.check, allure.step("Номер строки"):
            check.equal(data_dict["data"][36]["rowNum"], 37)
        with check.check, allure.step("Идентификатор задачи R-Vision"):
            check.equal(data_dict["data"][36]["rvisionID"], "22-07-98")
        with check.check, allure.step("Цвет метки"):
            check.is_none(data_dict["data"][36]["tagColor"])
        with check.check, allure.step("Метка: Важно, Проверить, Обратить внимание"):
            check.is_none(data_dict["data"][36]["tagID"])
        with check.check, allure.step("Название метки"):
            check.is_none(data_dict["data"][36]["tagName"])
        with check.check, allure.step("Идентификатор задачи"):
            check.equal(data_dict["data"][36]["taskID"], 37)
        with check.check, allure.step("Название задачи"):
            check.equal(
                data_dict["data"][36]["taskName"], "Операции над учетной записью"
            )
        with check.check, allure.step("Сквозной номер задачи"):
            check.equal(data_dict["data"][36]["taskNumber"], "GEN-33")
        with check.check, allure.step(
            "Статус: открыта, в работе, выполнено, отклонено"
        ):
            check.equal(data_dict["data"][36]["taskStateID"], 1)
        with check.check, allure.step(
            "Тип задачи: идентификатор из таблицы TM_TasksTypes"
        ):
            check.equal(data_dict["data"][36]["taskTypeID"], 1)
        with check.check, allure.step("Идентификатор иконки типа задачи"):
            check.equal(data_dict["data"][36]["typeIconID"], 1)
        with check.check, allure.step("Название типа задачи"):
            check.equal(data_dict["data"][36]["typeName"], "Common task")

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
                schema_models.SchemaModelsDataServiceAPIv2.ListOfTasks.parse_obj(row)
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.ListOfTasks.Data.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
