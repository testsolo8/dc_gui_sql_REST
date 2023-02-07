# Standart libraries
import json
from typing import List

# Third party packages
import allure
import pytest
import pytest_check as check
from  assertpy import assert_that, soft_assertions
import requests
from jsonschema import validate
from pydantic import ValidationError, parse_obj_as

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc

path = "https://" + base_url_dc() + ":9082/archiving/api/v1/shares"
r = requests.get(path, verify=False)


@allure.epic("DCArchiving REST API")
@allure.feature("Getting list of storages for backups")
@pytest.mark.testRESTAPI
@allure.story("Получение списка хранилищ для бэкапов")
class TestGettingListOfStoragesForBackups:
    @allure.title("Успешность запроса")
    def test_status_code_200(self):
        assert r.status_code == 200

    @allure.title("Headers 'content-type'")
    def test_content_type(self):
        con_type = r.headers["content-type"]
        assert con_type == "application/json; charset=utf-8"

    @allure.title("Время ответа запроса")
    def test_response_time(self):
        resp_time = r.elapsed.total_seconds()
        assert resp_time <= 30

    @allure.title("Хранилище переноса БД")
    def test_db_migration_storage(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step(
            "Поле для хранения произвольных настроек. Байты в кодировке base64"
        ):
            check.equal(
                parsed_data[0]["Settings"],
                "ewAiAFIAdQBsAGUAVAB5AHAAZQAiADoAMAAsACIARABlAGwAZQB0AGUARABCACIAOgB0AHIAdQBlACwAIgBFAG4AZABUAGkAbQBlACIAOgAwAC4AMgA1ACwAIgBEAG8AYwBBAGcAZQBUAHkAcABlACIAOgAxACwAIgBFAG4AYQBiAGwAZQBGAHIAZQBlAFMAcABhAGMAZQAiADoAdAByAHUAZQAsACIAUwBjAGgAZQBkAHUAbABlACIAOgAiACIALAAiAE0AXAB1ADAANAAzADAAXAB1ADAANAA0ADUARQByAHIAbwByAEMAbwB1AG4AdAAiADoAMgAsACIAZgBGAHIAZQBlAFMAcABhAGMAZQBTAGkAegBlAFAAZQByAGMAZQBuAHQAIgA6ADEANQAsACIARQBuAGEAYgBsAGUAZAAiADoAZgBhAGwAcwBlACwAIgBTAHQAbwByAGUAQwBvAHUAbgB0ACIAOgAwACwAIgBVAHMAZQBEAGkAcwBrACIAOgBmAGEAbABzAGUALAAiAGYARgByAGUAZQBTAHAAYQBjAGUAUwBpAHoAZQBUAHkAcABlACIAOgAwACwAIgBCAGUAZwBpAG4AVABpAG0AZQAiADoAMAAuADEAMgA1ACwAIgBDAHIAZQBhAHQAaQBvAG4ARABhAHQAZQAiADoALQA3ADAAMAAwADAAMAAsACIAUAByAG8AZAB1AGMAdABzACIAOgAxADYAOQA3ADcANwA5ADIALAAiAEQAbwBjAEEAZwBlACIAOgAxADIALAAiAFMAdABvAHIAZQBUAHkAcABlACIAOgAwACwAIgBmAEYAcgBlAGUAUwBwAGEAYwBlAFMAaQB6AGUARwBCACIAOgAyADAAMAAsACIAUwBlAHIAdgBpAGMAZQBEAEIAUAByAG8AZAB1AGMAdABzACIAOgAwACwAIgBVAHMAZQBDAHIAZQBhAHQAaQBvAG4ARABhAHQAZQAiADoAZgBhAGwAcwBlACwAIgBEAG8AQgBhAGMAawB1AHAAVABpAG0AZQAiADoAMAAsACIASQBuAGQAZQB4AEQAQgBQAHIAbwBkAHUAYwB0AHMAIgA6ADYAMwA3ADQAMQA4ADIANAAsACIARQBuAGEAYgBsAGUARABvAGMAQQBnAGUAIgA6AGYAYQBsAHMAZQAsACIARABpAHMAawBMAGUAdAB0AGUAcgAiADoAIgAiACwAIgBPAGIAagBlAGMAdABUAHkAcABlACIAOgAwAH0A",
            )
        with allure.step("ID хранилища"):
            check.equal(parsed_data[0]["ID"], "25569d92abd5a091bf41a5b5b5532ad4")
        with allure.step("Путь до целевой папки на шаре"):
            check.equal(parsed_data[0]["Path"], "d:\db")
        with allure.step(
            "Имя пользователя для авторизации (если отсутствует - имперсонация выполняться не будет)"
        ):
            check.equal(parsed_data[0]["User"], "")
        with allure.step(
            "Пароль для пользователя заданного в ShareUser. Шифрование стандартное для наших строк"
        ):
            check.equal(parsed_data[0]["Password"], "")
        with allure.step("Имя сервера SQL"):
            check.equal(parsed_data[0]["Server"], "TAKE-SQL.minsk.searchinform.net")
        with allure.step("Версия агента БД. Если не опознано - вернется Unknown"):
            agent_version = list(parsed_data[0]["AgentVersion"].split('.'))
            with soft_assertions():
                assert_that(agent_version).is_not_empty()
                assert_that(agent_version).is_length(4)
                assert_that(agent_version[0]).is_equal_to('2')
        with allure.step("Версия API агента БД. Если не опознано - вернется 0"):
            check.equal(parsed_data[0]["AgentAPIVersion"], 2)
        with allure.step("Порт службы агента БД."):
            check.equal(parsed_data[0]["AgentAPIPort"], 9085)
        with allure.step("Флаг необходимости обновить агент"):
            check.is_false(parsed_data[0]["AgentNeedsUpdate"])
        with allure.step("Mode"):
            check.equal(parsed_data[0]["Mode"], 0)
        with allure.step("Лимит на шару в мегабайтах"):
            check.equal(parsed_data[0]["Limit"], 0)

    @allure.title("Хранилище переноса индекса")
    def test_index_migration_storage(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step(
            "Поле для хранения произвольных настроек. Байты в кодировке base64"
        ):
            check.equal(
                parsed_data[1]["Settings"],
                "ewAiAFIAdQBsAGUAVAB5AHAAZQAiADoAMAAsACIARABlAGwAZQB0AGUARABCACIAOgB0AHIAdQBlACwAIgBFAG4AZABUAGkAbQBlACIAOgAwAC4AMgAwADgAMwAzADMAMwAzADMAMwAzADMAMwAzADMALAAiAEQAbwBjAEEAZwBlAFQAeQBwAGUAIgA6ADEALAAiAEUAbgBhAGIAbABlAEYAcgBlAGUAUwBwAGEAYwBlACIAOgBmAGEAbABzAGUALAAiAFMAYwBoAGUAZAB1AGwAZQAiADoAIgB7AH0AIgAsACIATQBcAHUAMAA0ADMAMABcAHUAMAA0ADQANQBFAHIAcgBvAHIAQwBvAHUAbgB0ACIAOgA1ACwAIgBmAEYAcgBlAGUAUwBwAGEAYwBlAFMAaQB6AGUAUABlAHIAYwBlAG4AdAAiADoAMQA1ACwAIgBFAG4AYQBiAGwAZQBkACIAOgBmAGEAbABzAGUALAAiAFMAdABvAHIAZQBDAG8AdQBuAHQAIgA6ADQALAAiAFUAcwBlAEQAaQBzAGsAIgA6AGYAYQBsAHMAZQAsACIAZgBGAHIAZQBlAFMAcABhAGMAZQBTAGkAegBlAFQAeQBwAGUAIgA6ADAALAAiAEIAZQBnAGkAbgBUAGkAbQBlACIAOgAwAC4AMAA0ADEANgA2ADYANgA2ADYANgA2ADYANgA2ADYANwAsACIAQwByAGUAYQB0AGkAbwBuAEQAYQB0AGUAIgA6ADQANAA4ADAANgAsACIAUAByAG8AZAB1AGMAdABzACIAOgAwACwAIgBEAG8AYwBBAGcAZQAiADoAMQAyACwAIgBTAHQAbwByAGUAVAB5AHAAZQAiADoAMAAsACIAZgBGAHIAZQBlAFMAcABhAGMAZQBTAGkAegBlAEcAQgAiADoANQAwACwAIgBTAGUAcgB2AGkAYwBlAEQAQgBQAHIAbwBkAHUAYwB0AHMAIgA6ADAALAAiAFUAcwBlAEMAcgBlAGEAdABpAG8AbgBEAGEAdABlACIAOgB0AHIAdQBlACwAIgBEAG8AQgBhAGMAawB1AHAAVABpAG0AZQAiADoAMAAsACIASQBuAGQAZQB4AEQAQgBQAHIAbwBkAHUAYwB0AHMAIgA6ADEAMwAyADAAOQA1ADgANwAyACwAIgBFAG4AYQBiAGwAZQBEAG8AYwBBAGcAZQAiADoAdAByAHUAZQAsACIARABpAHMAawBMAGUAdAB0AGUAcgAiADoAIgAiACwAIgBPAGIAagBlAGMAdABUAHkAcABlACIAOgAxAH0A",
            )
        with allure.step("ID хранилища"):
            check.equal(parsed_data[1]["ID"], "6b6c02ecb70a888ba5ea5dd81e6b41bc")
        with allure.step("Путь до целевой папки на шаре"):
            check.equal(parsed_data[1]["Path"], "d:\index")
        with allure.step(
            "Имя пользователя для авторизации (если отсутствует - имперсонация выполняться не будет)"
        ):
            check.equal(parsed_data[1]["User"], "")
        with allure.step(
            "Пароль для пользователя заданного в ShareUser. Шифрование стандартное для наших строк"
        ):
            check.equal(parsed_data[1]["Password"], "")
        with allure.step("Имя сервера SQL"):
            check.equal(parsed_data[1]["Server"], "nsa2.minsk.searchinform.net")
        with allure.step("Версия агента БД. Если не опознано - вернется Unknown"):
            agent_version = list(parsed_data[1]["AgentVersion"].split('.'))
            with soft_assertions():
                assert_that(agent_version).is_not_empty()
                assert_that(agent_version).is_length(4)
                assert_that(agent_version[0]).is_equal_to('2')
        with allure.step("Версия API агента БД. Если не опознано - вернется 0"):
            check.equal(parsed_data[1]["AgentAPIVersion"], 2)
        with allure.step("Порт службы агента БД."):
            check.equal(parsed_data[1]["AgentAPIPort"], 9085)
        with allure.step("Флаг необходимости обновить агент"):
            check.is_false(parsed_data[1]["AgentNeedsUpdate"])
        with allure.step("Mode"):
            check.equal(parsed_data[1]["Mode"], 0)
        with allure.step("Лимит на шару в мегабайтах"):
            check.equal(parsed_data[1]["Limit"], 0)

    @allure.title("Хранилище архивации индекса")
    def test_index_backup_storage(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step(
            "Поле для хранения произвольных настроек. Байты в кодировке base64"
        ):
            check.equal(
                parsed_data[2]["Settings"],
                "ewAiAFIAdQBsAGUAVAB5AHAAZQAiADoAMQAsACIARABlAGwAZQB0AGUARABCACIAOgB0AHIAdQBlACwAIgBFAG4AZABUAGkAbQBlACIAOgAwAC4AMgAwADgAMwAzADMAMwAzADMAMwAzADMAMwAzADMALAAiAEQAbwBjAEEAZwBlAFQAeQBwAGUAIgA6ADEALAAiAEUAbgBhAGIAbABlAEYAcgBlAGUAUwBwAGEAYwBlACIAOgBmAGEAbABzAGUALAAiAFMAYwBoAGUAZAB1AGwAZQAiADoAIgB7AH0AIgAsACIATQBcAHUAMAA0ADMAMABcAHUAMAA0ADQANQBFAHIAcgBvAHIAQwBvAHUAbgB0ACIAOgAyACwAIgBmAEYAcgBlAGUAUwBwAGEAYwBlAFMAaQB6AGUAUABlAHIAYwBlAG4AdAAiADoAMQA1ACwAIgBFAG4AYQBiAGwAZQBkACIAOgBmAGEAbABzAGUALAAiAFMAdABvAHIAZQBDAG8AdQBuAHQAIgA6ADQALAAiAFUAcwBlAEQAaQBzAGsAIgA6AGYAYQBsAHMAZQAsACIAZgBGAHIAZQBlAFMAcABhAGMAZQBTAGkAegBlAFQAeQBwAGUAIgA6ADAALAAiAEIAZQBnAGkAbgBUAGkAbQBlACIAOgAwAC4AMgAwADgAMwAzADMAMwAzADMAMwAzADMAMwAzADMALAAiAEMAcgBlAGEAdABpAG8AbgBEAGEAdABlACIAOgA0ADQANwAzADYALAAiAFAAcgBvAGQAdQBjAHQAcwAiADoAMAAsACIARABvAGMAQQBnAGUAIgA6ADYALAAiAFMAdABvAHIAZQBUAHkAcABlACIAOgAwACwAIgBmAEYAcgBlAGUAUwBwAGEAYwBlAFMAaQB6AGUARwBCACIAOgA1ADAALAAiAFMAZQByAHYAaQBjAGUARABCAFAAcgBvAGQAdQBjAHQAcwAiADoAMAAsACIAVQBzAGUAQwByAGUAYQB0AGkAbwBuAEQAYQB0AGUAIgA6AGYAYQBsAHMAZQAsACIARABvAEIAYQBjAGsAdQBwAFQAaQBtAGUAIgA6ADAALAAiAEkAbgBkAGUAeABEAEIAUAByAG8AZAB1AGMAdABzACIAOgAxADMAMgAwADkANQA4ADcAMgAsACIARQBuAGEAYgBsAGUARABvAGMAQQBnAGUAIgA6AHQAcgB1AGUALAAiAEQAaQBzAGsATABlAHQAdABlAHIAIgA6ACIAIgAsACIATwBiAGoAZQBjAHQAVAB5AHAAZQAiADoAMQB9AA==",
            )
        with allure.step("ID хранилища"):
            check.equal(parsed_data[2]["ID"], "8ea14f593b39fcccb1c67df20db9220a")
        with allure.step("Путь до целевой папки на шаре"):
            check.equal(parsed_data[2]["Path"], r"\\msq-nsa-sql\dataoldf$\backup\index")
        with allure.step(
            "Имя пользователя для авторизации (если отсутствует - имперсонация выполняться не будет)"
        ):
            check.equal(parsed_data[2]["User"], "")
        with allure.step(
            "Пароль для пользователя заданного в ShareUser. Шифрование стандартное для наших строк"
        ):
            check.equal(parsed_data[2]["Password"], "")
        with allure.step("Имя сервера SQL"):
            check.equal(parsed_data[2]["Server"], "nsa2.minsk.searchinform.net")
        with allure.step("Версия агента БД. Если не опознано - вернется Unknown"):
            agent_version = list(parsed_data[2]["AgentVersion"].split('.'))
            with soft_assertions():
                assert_that(agent_version).is_not_empty()
                assert_that(agent_version).is_length(4)
                assert_that(agent_version[0]).is_equal_to('2')
        with allure.step("Версия API агента БД. Если не опознано - вернется 0"):
            check.equal(parsed_data[2]["AgentAPIVersion"], 2)
        with allure.step("Порт службы агента БД."):
            check.equal(parsed_data[2]["AgentAPIPort"], 9085)
        with allure.step("Флаг необходимости обновить агент"):
            check.is_false(parsed_data[2]["AgentNeedsUpdate"])
        with allure.step("Mode"):
            check.equal(parsed_data[2]["Mode"], 0)
        with allure.step("Лимит на шару в мегабайтах"):
            check.equal(parsed_data[2]["Limit"], 0)

    @allure.title("Хранилище архивации STI")
    def test_sti_backup_storage(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step(
            "Поле для хранения произвольных настроек. Байты в кодировке base64"
        ):
            check.equal(
                parsed_data[3]["Settings"],
                "ewAiAFIAdQBsAGUAVAB5AHAAZQAiADoAMQAsACIARABlAGwAZQB0AGUARABCACIAOgB0AHIAdQBlACwAIgBFAG4AZABUAGkAbQBlACIAOgAwAC4AMgAwADgAMwAzADMAMwAzADMAMwAzADMAMwAzADMALAAiAEQAbwBjAEEAZwBlAFQAeQBwAGUAIgA6ADEALAAiAEUAbgBhAGIAbABlAEYAcgBlAGUAUwBwAGEAYwBlACIAOgB0AHIAdQBlACwAIgBTAGMAaABlAGQAdQBsAGUAIgA6ACIAewB9ACIALAAiAE0AXAB1ADAANAAzADAAXAB1ADAANAA0ADUARQByAHIAbwByAEMAbwB1AG4AdAAiADoANQAsACIAZgBGAHIAZQBlAFMAcABhAGMAZQBTAGkAegBlAFAAZQByAGMAZQBuAHQAIgA6ADEANQAsACIARQBuAGEAYgBsAGUAZAAiADoAZgBhAGwAcwBlACwAIgBTAHQAbwByAGUAQwBvAHUAbgB0ACIAOgA0ACwAIgBVAHMAZQBEAGkAcwBrACIAOgB0AHIAdQBlACwAIgBmAEYAcgBlAGUAUwBwAGEAYwBlAFMAaQB6AGUAVAB5AHAAZQAiADoAMAAsACIAQgBlAGcAaQBuAFQAaQBtAGUAIgA6ADAALgAwADQAMQA2ADYANgA2ADYANgA2ADYANgA2ADYANgA3ACwAIgBDAHIAZQBhAHQAaQBvAG4ARABhAHQAZQAiADoANAA0ADcANQA0ACwAIgBQAHIAbwBkAHUAYwB0AHMAIgA6ADAALAAiAEQAbwBjAEEAZwBlACIAOgAxADIALAAiAFMAdABvAHIAZQBUAHkAcABlACIAOgAwACwAIgBmAEYAcgBlAGUAUwBwAGEAYwBlAFMAaQB6AGUARwBCACIAOgA1ADAALAAiAFMAZQByAHYAaQBjAGUARABCAFAAcgBvAGQAdQBjAHQAcwAiADoAMAAsACIAVQBzAGUAQwByAGUAYQB0AGkAbwBuAEQAYQB0AGUAIgA6AHQAcgB1AGUALAAiAEQAbwBCAGEAYwBrAHUAcABUAGkAbQBlACIAOgAwACwAIgBJAG4AZABlAHgARABCAFAAcgBvAGQAdQBjAHQAcwAiADoAMQA5ADYANgAwADgALAAiAEUAbgBhAGIAbABlAEQAbwBjAEEAZwBlACIAOgB0AHIAdQBlACwAIgBEAGkAcwBrAEwAZQB0AHQAZQByACIAOgAiAEUAOgBcAFwAIgAsACIATwBiAGoAZQBjAHQAVAB5AHAAZQAiADoAMgB9AA==",
            )
        with allure.step("ID хранилища"):
            check.equal(parsed_data[3]["ID"], "a0c980e71a704281f392ac2f3df9978b")
        with allure.step("Путь до целевой папки на шаре"):
            check.equal(parsed_data[3]["Path"], r"\\msq-nsa-sql\dataoldf$\backup\sti")
        with allure.step(
            "Имя пользователя для авторизации (если отсутствует - имперсонация выполняться не будет)"
        ):
            check.equal(parsed_data[3]["User"], "")
        with allure.step(
            "Пароль для пользователя заданного в ShareUser. Шифрование стандартное для наших строк"
        ):
            check.equal(parsed_data[3]["Password"], "")
        with allure.step("Имя сервера SQL"):
            check.equal(parsed_data[3]["Server"], "nsa2.minsk.searchinform.net")
        with allure.step("Версия агента БД. Если не опознано - вернется Unknown"):
            agent_version = list(parsed_data[3]["AgentVersion"].split('.'))
            with soft_assertions():
                assert_that(agent_version).is_not_empty()
                assert_that(agent_version).is_length(4)
                assert_that(agent_version[0]).is_equal_to('2')
        with allure.step("Версия API агента БД. Если не опознано - вернется 0"):
            check.equal(parsed_data[3]["AgentAPIVersion"], 2)
        with allure.step("Порт службы агента БД."):
            check.equal(parsed_data[3]["AgentAPIPort"], 9085)
        with allure.step("Флаг необходимости обновить агент"):
            check.is_false(parsed_data[3]["AgentNeedsUpdate"])
        with allure.step("Mode"):
            check.equal(parsed_data[3]["Mode"], 0)
        with allure.step("Лимит на шару в мегабайтах"):
            check.equal(parsed_data[3]["Limit"], 0)

    @allure.title("Хранилище архивации БД")
    def test_db_backup_storage(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step(
            "Поле для хранения произвольных настроек. Байты в кодировке base64"
        ):
            check.equal(
                parsed_data[4]["Settings"],
                "ewAiAFIAdQBsAGUAVAB5AHAAZQAiADoAMQAsACIARABlAGwAZQB0AGUARABCACIAOgB0AHIAdQBlACwAIgBFAG4AZABUAGkAbQBlACIAOgAwAC4AMQAyADUALAAiAEQAbwBjAEEAZwBlAFQAeQBwAGUAIgA6ADEALAAiAEUAbgBhAGIAbABlAEYAcgBlAGUAUwBwAGEAYwBlACIAOgBmAGEAbABzAGUALAAiAFMAYwBoAGUAZAB1AGwAZQAiADoAIgAiACwAIgBNAFwAdQAwADQAMwAwAFwAdQAwADQANAA1AEUAcgByAG8AcgBDAG8AdQBuAHQAIgA6ADIALAAiAGYARgByAGUAZQBTAHAAYQBjAGUAUwBpAHoAZQBQAGUAcgBjAGUAbgB0ACIAOgAxADUALAAiAEUAbgBhAGIAbABlAGQAIgA6AGYAYQBsAHMAZQAsACIAUwB0AG8AcgBlAEMAbwB1AG4AdAAiADoAMAAsACIAVQBzAGUARABpAHMAawAiADoAZgBhAGwAcwBlACwAIgBmAEYAcgBlAGUAUwBwAGEAYwBlAFMAaQB6AGUAVAB5AHAAZQAiADoAMAAsACIAQgBlAGcAaQBuAFQAaQBtAGUAIgA6ADAALAAiAEMAcgBlAGEAdABpAG8AbgBEAGEAdABlACIAOgAtADcAMAAwADAAMAAwACwAIgBQAHIAbwBkAHUAYwB0AHMAIgA6ADEANgA5ADcANwA3ADkAMgAsACIARABvAGMAQQBnAGUAIgA6ADQALAAiAFMAdABvAHIAZQBUAHkAcABlACIAOgAwACwAIgBmAEYAcgBlAGUAUwBwAGEAYwBlAFMAaQB6AGUARwBCACIAOgA1ADAALAAiAFMAZQByAHYAaQBjAGUARABCAFAAcgBvAGQAdQBjAHQAcwAiADoAMAAsACIAVQBzAGUAQwByAGUAYQB0AGkAbwBuAEQAYQB0AGUAIgA6AGYAYQBsAHMAZQAsACIARABvAEIAYQBjAGsAdQBwAFQAaQBtAGUAIgA6ADAALAAiAEkAbgBkAGUAeABEAEIAUAByAG8AZAB1AGMAdABzACIAOgA2ADMANwA0ADEAOAAyADQALAAiAEUAbgBhAGIAbABlAEQAbwBjAEEAZwBlACIAOgB0AHIAdQBlACwAIgBEAGkAcwBrAEwAZQB0AHQAZQByACIAOgAiACIALAAiAE8AYgBqAGUAYwB0AFQAeQBwAGUAIgA6ADAAfQA=",
            )
        with allure.step("ID хранилища"):
            check.equal(parsed_data[4]["ID"], "bb8271d84f55d989a044d206411f706a")
        with allure.step("Путь до целевой папки на шаре"):
            check.equal(parsed_data[4]["Path"], r"\\msq-nsa-sql\dataoldf$\backup\db")
        with allure.step(
            "Имя пользователя для авторизации (если отсутствует - имперсонация выполняться не будет)"
        ):
            check.equal(parsed_data[4]["User"], "")
        with allure.step(
            "Пароль для пользователя заданного в ShareUser. Шифрование стандартное для наших строк"
        ):
            check.equal(parsed_data[4]["Password"], "")
        with allure.step("Имя сервера SQL"):
            check.equal(parsed_data[4]["Server"], "TAKE-SQL.minsk.searchinform.net")
        with allure.step("Версия агента БД. Если не опознано - вернется Unknown"):
            agent_version = list(parsed_data[4]["AgentVersion"].split('.'))
            with soft_assertions():
                assert_that(agent_version).is_not_empty()
                assert_that(agent_version).is_length(4)
                assert_that(agent_version[0]).is_equal_to('2')
        with allure.step("Версия API агента БД. Если не опознано - вернется 0"):
            check.equal(parsed_data[4]["AgentAPIVersion"], 2)
        with allure.step("Порт службы агента БД."):
            check.equal(parsed_data[4]["AgentAPIPort"], 9085)
        with allure.step("Флаг необходимости обновить агент"):
            check.is_false(parsed_data[4]["AgentNeedsUpdate"])
        with allure.step("Mode"):
            check.equal(parsed_data[4]["Mode"], 0)
        with allure.step("Лимит на шару в мегабайтах"):
            check.equal(parsed_data[4]["Limit"], 0)

    @allure.title("Хранилище переноса STI")
    def test_sti_migration_storage(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step(
            "Поле для хранения произвольных настроек. Байты в кодировке base64"
        ):
            check.equal(
                parsed_data[5]["Settings"],
                "ewAiAFIAdQBsAGUAVAB5AHAAZQAiADoAMAAsACIARABlAGwAZQB0AGUARABCACIAOgB0AHIAdQBlACwAIgBFAG4AZABUAGkAbQBlACIAOgAwAC4AMgAwADgAMwAzADMAMwAzADMAMwAzADMAMwAzADMALAAiAEQAbwBjAEEAZwBlAFQAeQBwAGUAIgA6ADEALAAiAEUAbgBhAGIAbABlAEYAcgBlAGUAUwBwAGEAYwBlACIAOgB0AHIAdQBlACwAIgBTAGMAaABlAGQAdQBsAGUAIgA6ACIAewB9ACIALAAiAE0AXAB1ADAANAAzADAAXAB1ADAANAA0ADUARQByAHIAbwByAEMAbwB1AG4AdAAiADoANQAsACIAZgBGAHIAZQBlAFMAcABhAGMAZQBTAGkAegBlAFAAZQByAGMAZQBuAHQAIgA6ADEANQAsACIARQBuAGEAYgBsAGUAZAAiADoAZgBhAGwAcwBlACwAIgBTAHQAbwByAGUAQwBvAHUAbgB0ACIAOgA0ACwAIgBVAHMAZQBEAGkAcwBrACIAOgB0AHIAdQBlACwAIgBmAEYAcgBlAGUAUwBwAGEAYwBlAFMAaQB6AGUAVAB5AHAAZQAiADoAMAAsACIAQgBlAGcAaQBuAFQAaQBtAGUAIgA6ADAALgAwADQAMQA2ADYANgA2ADYANgA2ADYANgA2ADYANgA3ACwAIgBDAHIAZQBhAHQAaQBvAG4ARABhAHQAZQAiADoANAA0ADgAMAAzACwAIgBQAHIAbwBkAHUAYwB0AHMAIgA6ADAALAAiAEQAbwBjAEEAZwBlACIAOgA2ACwAIgBTAHQAbwByAGUAVAB5AHAAZQAiADoAMAAsACIAZgBGAHIAZQBlAFMAcABhAGMAZQBTAGkAegBlAEcAQgAiADoANQAwACwAIgBTAGUAcgB2AGkAYwBlAEQAQgBQAHIAbwBkAHUAYwB0AHMAIgA6ADAALAAiAFUAcwBlAEMAcgBlAGEAdABpAG8AbgBEAGEAdABlACIAOgB0AHIAdQBlACwAIgBEAG8AQgBhAGMAawB1AHAAVABpAG0AZQAiADoAMAAsACIASQBuAGQAZQB4AEQAQgBQAHIAbwBkAHUAYwB0AHMAIgA6ADEAOQA2ADYAMAA4ACwAIgBFAG4AYQBiAGwAZQBEAG8AYwBBAGcAZQAiADoAdAByAHUAZQAsACIARABpAHMAawBMAGUAdAB0AGUAcgAiADoAIgBGADoAXABcACIALAAiAE8AYgBqAGUAYwB0AFQAeQBwAGUAIgA6ADIAfQA=",
            )
        with allure.step("ID хранилища"):
            check.equal(parsed_data[5]["ID"], "bda31da73f1f454e2f5305aaba9015b3")
        with allure.step("Путь до целевой папки на шаре"):
            check.equal(parsed_data[5]["Path"], r"d:\sti")
        with allure.step(
            "Имя пользователя для авторизации (если отсутствует - имперсонация выполняться не будет)"
        ):
            check.equal(parsed_data[5]["User"], "")
        with allure.step(
            "Пароль для пользователя заданного в ShareUser. Шифрование стандартное для наших строк"
        ):
            check.equal(parsed_data[5]["Password"], "")
        with allure.step("Имя сервера SQL"):
            check.equal(parsed_data[5]["Server"], "nsa2.minsk.searchinform.net")
        with allure.step("Версия агента БД. Если не опознано - вернется Unknown"):
            agent_version = list(parsed_data[5]["AgentVersion"].split('.'))
            with soft_assertions():
                assert_that(agent_version).is_not_empty()
                assert_that(agent_version).is_length(4)
                assert_that(agent_version[0]).is_equal_to('2')
        with allure.step("Версия API агента БД. Если не опознано - вернется 0"):
            check.equal(parsed_data[5]["AgentAPIVersion"], 2)
        with allure.step("Порт службы агента БД."):
            check.equal(parsed_data[5]["AgentAPIPort"], 9085)
        with allure.step("Флаг необходимости обновить агент"):
            check.is_false(parsed_data[5]["AgentNeedsUpdate"])
        with allure.step("Mode"):
            check.equal(parsed_data[5]["Mode"], 0)
        with allure.step("Лимит на шару в мегабайтах"):
            check.equal(parsed_data[5]["Limit"], 0)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["Settings", "ID", "Path", "Server"],
            },
        }
        resp = r.json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self):
        data_dict = requests.get(path, verify=False).json()
        error_list = []
        for row in data_dict:
            try:
                parse_obj_as(
                    List[
                        schema_models.SchemaModelsDCArchivingRESTAPI.GettingListOfStoragesForBackups
                    ],
                    data_dict,
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDCArchivingRESTAPI.GettingListOfStoragesForBackups.parse_obj(
                data_dict[0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
