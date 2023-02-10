# Standart libraries
import json
from typing import List

# Third party packages
import allure
import pytest
import pytest_check as check
import requests
from jsonschema import validate
from pydantic import ValidationError, parse_obj_as

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc


@allure.epic("DCArchiving REST API")
@allure.feature("Getting information of specific tasks")
@pytest.mark.testRESTAPI
@allure.story("Получение задач с конкретным ID")
class TestGettingInformationOfSpecificTasks:
    class TestGettingInformationOfArchiveDevice:
        path = (
            "https://"
            + base_url_dc()
            + ":9082/archiving/api/v1/tasks/47093c3e3cdde9ab40e0e9db102fba61"
        )
        r = requests.get(path, verify=False)

        @allure.title("Успешность запроса")
        def test_status_code_200(self):
            assert (
                TestGettingInformationOfSpecificTasks.TestGettingInformationOfArchiveDevice.r.status_code
                == 200
            )

        @allure.title("Headers 'content-type'")
        def test_content_type(self):
            con_type = TestGettingInformationOfSpecificTasks.TestGettingInformationOfArchiveDevice.r.headers[
                "content-type"
            ]
            assert con_type == "application/json; charset=utf-8"

        @allure.title("Время ответа запроса")
        def test_response_time(self):
            resp_time = (
                TestGettingInformationOfSpecificTasks.TestGettingInformationOfArchiveDevice.r.elapsed.total_seconds()
            )
            assert resp_time <= 30

        @allure.title("Задача архивации индекса Device")
        def test_archive_device(self):
            data_dict = (
                TestGettingInformationOfSpecificTasks.TestGettingInformationOfArchiveDevice.r.json()
            )
            with allure.step("ID задачи"):
                check.equal(data_dict["ID"], "47093c3e3cdde9ab40e0e9db102fba61")
            with allure.step("ID хранилища из списка"):
                check.equal(data_dict["ShareID"], "9331fb7825581e8e724a4dac3f489ee4")
            with allure.step(
                "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
            ):
                check.equal(data_dict["TypeID"], 1)
            with allure.step(
                "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
            ):
                check.equal(data_dict["ActionID"], 0)
            with allure.step(
                "Количество поочередных ошибок произошедших с этим заданием"
            ):
                check.equal(data_dict["ErrorCount"], 2)
            with allure.step("Максимальное количество поочередных ошибок"):
                check.equal(data_dict["MaxErrorCount"], 2)
            with allure.step("Имя сервера"):
                check.equal(data_dict["Server"], "win-734hjf247we")
            with allure.step("Имя базы данных или путь до индекса"):
                check.equal(
                    data_dict["Source"], "{db14ec03-637c-449f-acfe-54b2ab27d0ba}"
                )
            with allure.step("Полное имя папки для резервной копии"):
                check.equal(data_dict["Backup"], r"e:\archive index")
            with allure.step("Размер резервной копии в мегабайтах"):
                check.equal(data_dict["BackupSize"], 955)
            with allure.step("Время последнего шага задачи в формате Unix"):
                check.equal(data_dict["Date"], 1662366851)
            with allure.step("ID протокола содержащегося в базе или индексе"):
                check.equal(data_dict["Protocol"], 16)
            with allure.step("Минимальная дата документа в БД или индексе"):
                check.equal(data_dict["MinDocDate"], 0)
            with allure.step("Максимальная дата документа в Бд или индексе"):
                check.equal(data_dict["MaxDocDate"], 0)
            with allure.step("BackupFile"):
                check.equal(
                    data_dict["BackupFile"],
                    r"e:\archive index\Device~28_04_2022_16_29.lbx.zbk",
                )
            with allure.step("StiPath"):
                check.equal(data_dict["StiPath"], "")
            with allure.step("IndexName"):
                check.equal(data_dict["IndexName"], "")
            with allure.step("IndexPath"):
                check.equal(
                    data_dict["IndexPath"],
                    "C:\Indexes\Device\Device~28_04_2022_16_29.lbx",
                )
            with allure.step("Идентификатор прогресса задачи"):
                check.equal(data_dict["Progress"]["ProgressID"], 0)
            with allure.step("Коды состояния прогресса"):
                check.equal(data_dict["Progress"]["Status"], 1)
            with allure.step("BackupSizeMB"):
                check.equal(data_dict["Progress"]["Messages"][0], "BackupSizeMB:955")
            with allure.step("StorageSizeMB"):
                check.equal(data_dict["Progress"]["Messages"][1], "IndexSizeMB:1820")
            with allure.step("Прогресс выполнения задачи"):
                check.equal(data_dict["Progress"]["CompletedPercent"], 100)

        @allure.title("Проверка возвращаемой схемы JSON")
        def test_schema(self):
            schema = {
                "type": "object",
                "required": ["ID", "Server", "Source", "Date"],
            }
            resp = (
                TestGettingInformationOfSpecificTasks.TestGettingInformationOfArchiveDevice.r.json()
            )
            validate(resp, schema=schema)

        @allure.title("Проверка возвращаемой схемы JSON")
        def test_schema2(self):
            data_dict = requests.get(
                TestGettingInformationOfSpecificTasks.TestGettingInformationOfArchiveDevice.path,
                verify=False,
            ).json()
            error_list = []
            for row in data_dict:
                try:
                    parse_obj_as(
                        List[
                            schema_models.SchemaModelsDCArchivingRESTAPI.GettingListOfAllTasks
                        ],
                        data_dict,
                    )
                except ValidationError as e:
                    error_list.append(f"Error found in object: {row}\n{e.json()}\n")
            try:
                schema_models.SchemaModelsDCArchivingRESTAPI.GettingListOfAllTasks.parse_obj(
                    data_dict
                )
            except Exception as e:
                if error_list:
                    raise Exception(f"{''.join(error_list)}\n{e}")
                else:
                    raise Exception(e)

    class TestGettingInformationOfMoveSkype:
        path = (
            "https://"
            + base_url_dc()
            + ":9082/archiving/api/v1/tasks/d012d198d5cfb925f85b6ae0b9cd78c4"
        )
        r = requests.get(path, verify=False)

        @allure.title("Успешность запроса")
        def test_status_code_200(self):
            assert (
                TestGettingInformationOfSpecificTasks.TestGettingInformationOfMoveSkype.r.status_code
                == 200
            )

        @allure.title("Headers 'content-type'")
        def test_content_type(self):
            con_type = TestGettingInformationOfSpecificTasks.TestGettingInformationOfMoveSkype.r.headers[
                "content-type"
            ]
            assert con_type == "application/json; charset=utf-8"

        @allure.title("Время ответа запроса")
        def test_response_time(self):
            resp_time = (
                TestGettingInformationOfSpecificTasks.TestGettingInformationOfMoveSkype.r.elapsed.total_seconds()
            )
            assert resp_time <= 30

        @allure.title("Задача архивации индекса Device")
        def test_move_skype(self):
            data_dict = (
                TestGettingInformationOfSpecificTasks.TestGettingInformationOfMoveSkype.r.json()
            )
            with allure.step("ID задачи"):
                check.equal(data_dict["ID"], "d012d198d5cfb925f85b6ae0b9cd78c4")
            with allure.step("ID хранилища из списка"):
                check.equal(data_dict["ShareID"], "e53d3141f741080c73aa78f1678b3611")
            with allure.step(
                "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
            ):
                check.equal(data_dict["TypeID"], 1)
            with allure.step(
                "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
            ):
                check.equal(data_dict["ActionID"], 3)
            with allure.step(
                "Количество поочередных ошибок произошедших с этим заданием"
            ):
                check.equal(data_dict["ErrorCount"], 0)
            with allure.step("Максимальное количество поочередных ошибок"):
                check.equal(data_dict["MaxErrorCount"], 3)
            with allure.step("Имя сервера"):
                check.equal(data_dict["Server"], "win-734hjf247we")
            with allure.step("Имя базы данных или путь до индекса"):
                check.equal(
                    data_dict["Source"], "{8aa0f634-5a36-42f1-83f3-356c8b3670c0}"
                )
            with allure.step("Полное имя папки для резервной копии"):
                check.equal(data_dict["Backup"], r"f:\move index")
            with allure.step("Размер резервной копии в мегабайтах"):
                check.equal(data_dict["BackupSize"], 4)
            with allure.step("Время последнего шага задачи в формате Unix"):
                check.equal(data_dict["Date"], 1662360203)
            with allure.step("ID протокола содержащегося в базе или индексе"):
                check.equal(data_dict["Protocol"], 15)
            with allure.step("Минимальная дата документа в БД или индексе"):
                check.equal(data_dict["MinDocDate"], 0)
            with allure.step("Максимальная дата документа в Бд или индексе"):
                check.equal(data_dict["MaxDocDate"], 0)
            with allure.step("BackupFile"):
                check.equal(
                    data_dict["BackupFile"],
                    r"f:\move index\skype~28_04_2022_13_21.lbx",
                )
            with allure.step("StiPath"):
                check.equal(data_dict["StiPath"], "")
            with allure.step("IndexName"):
                check.equal(data_dict["IndexName"], "")
            with allure.step("IndexPath"):
                check.equal(
                    data_dict["IndexPath"],
                    "C:\Indexes\skype\skype~28_04_2022_13_21.lbx",
                )
            with allure.step("Идентификатор прогресса задачи"):
                check.equal(data_dict["Progress"]["ProgressID"], 0)
            with allure.step("Коды состояния прогресса"):
                check.equal(data_dict["Progress"]["Status"], 1)
            with allure.step("Move files for"):
                check.equal(
                    data_dict["Progress"]["Messages"][0],
                    "Move files for {8aa0f634-5a36-42f1-83f3-356c8b3670c0}",
                )
            with allure.step("Move completed"):
                check.equal(data_dict["Progress"]["Messages"][1], "Move completed")
            with allure.step("Прогресс выполнения задачи"):
                check.equal(data_dict["Progress"]["CompletedPercent"], 100)

        @allure.title("Проверка возвращаемой схемы JSON")
        def test_schema(self):
            schema = {
                "type": "object",
                "required": ["ID", "Server", "Source", "Date"],
            }
            resp = (
                TestGettingInformationOfSpecificTasks.TestGettingInformationOfMoveSkype.r.json()
            )
            validate(resp, schema=schema)

        @allure.title("Проверка возвращаемой схемы JSON")
        def test_schema2(self):
            data_dict = requests.get(
                TestGettingInformationOfSpecificTasks.TestGettingInformationOfMoveSkype.path,
                verify=False,
            ).json()
            error_list = []
            for row in data_dict:
                try:
                    parse_obj_as(
                        List[
                            schema_models.SchemaModelsDCArchivingRESTAPI.GettingListOfAllTasks
                        ],
                        data_dict,
                    )
                except ValidationError as e:
                    error_list.append(f"Error found in object: {row}\n{e.json()}\n")
            try:
                schema_models.SchemaModelsDCArchivingRESTAPI.GettingListOfAllTasks.parse_obj(
                    data_dict
                )
            except Exception as e:
                if error_list:
                    raise Exception(f"{''.join(error_list)}\n{e}")
                else:
                    raise Exception(e)

    class TestGettingInformationOfArchiveMonitor:
        path = (
            "https://"
            + base_url_dc()
            + ":9082/archiving/api/v1/tasks/b511dbd0b9e1b40d537b0f2b92583145"
        )
        r = requests.get(path, verify=False)

        @allure.title("Успешность запроса")
        def test_status_code_200(self):
            assert (
                TestGettingInformationOfSpecificTasks.TestGettingInformationOfArchiveMonitor.r.status_code
                == 200
            )

        @allure.title("Headers 'content-type'")
        def test_content_type(self):
            con_type = TestGettingInformationOfSpecificTasks.TestGettingInformationOfArchiveMonitor.r.headers[
                "content-type"
            ]
            assert con_type == "application/json; charset=utf-8"

        @allure.title("Время ответа запроса")
        def test_response_time(self):
            resp_time = (
                TestGettingInformationOfSpecificTasks.TestGettingInformationOfArchiveMonitor.r.elapsed.total_seconds()
            )
            assert resp_time <= 30

        @allure.title("Задача архивации индекса Device")
        def test_archive_monitor(self):
            data_dict = (
                TestGettingInformationOfSpecificTasks.TestGettingInformationOfArchiveMonitor.r.json()
            )
            with allure.step("ID задачи"):
                check.equal(data_dict["ID"], "b511dbd0b9e1b40d537b0f2b92583145")
            with allure.step("ID хранилища из списка"):
                check.equal(data_dict["ShareID"], "0308b7f4b59902e3ff155187651d897d")
            with allure.step(
                "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
            ):
                check.equal(data_dict["TypeID"], 0)
            with allure.step(
                "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
            ):
                check.equal(data_dict["ActionID"], 4)
            with allure.step(
                "Количество поочередных ошибок произошедших с этим заданием"
            ):
                check.equal(data_dict["ErrorCount"], 0)
            with allure.step("Максимальное количество поочередных ошибок"):
                check.equal(data_dict["MaxErrorCount"], 3)
            with allure.step("Имя сервера"):
                check.equal(data_dict["Server"], "take-sql")
            with allure.step("Имя базы данных или путь до индекса"):
                check.equal(
                    data_dict["Source"],
                    "nsa2_minsk_searchinform_net_ec_monitor~01_07_2022_15_30",
                )
            with allure.step("Полное имя папки для резервной копии"):
                check.equal(
                    data_dict["Backup"], r"\\msq-nsa-sql\dataolde$\backup\monitor"
                )
            with allure.step("Размер резервной копии в мегабайтах"):
                check.equal(data_dict["BackupSize"], 51228)
            with allure.step("Время последнего шага задачи в формате Unix"):
                check.equal(data_dict["Date"], 1659822615)
            with allure.step("ID протокола содержащегося в базе или индексе"):
                check.equal(data_dict["Protocol"], 10)
            with allure.step("Минимальная дата документа в БД или индексе"):
                check.equal(data_dict["MinDocDate"], 0)
            with allure.step("Максимальная дата документа в Бд или индексе"):
                check.equal(data_dict["MaxDocDate"], 0)
            with allure.step("BackupFile"):
                check.equal(
                    data_dict["BackupFile"],
                    r"\\msq-nsa-sql\dataolde$\backup\monitor\nsa2_minsk_searchinform_net_ec_monitor~01_07_2022_15_30.bak",
                )
            with allure.step("StiPath"):
                check.equal(data_dict["StiPath"], "")
            with allure.step("IndexName"):
                check.equal(data_dict["IndexName"], "")
            with allure.step("IndexPath"):
                check.equal(data_dict["IndexPath"], "")
            with allure.step("Идентификатор прогресса задачи"):
                check.equal(data_dict["Progress"]["ProgressID"], 0)
            with allure.step("Коды состояния прогресса"):
                check.equal(data_dict["Progress"]["Status"], 1)
            with allure.step("LogsSizeMB"):
                check.equal(data_dict["Progress"]["Messages"][0], "LogsSizeMB:20")
            with allure.step("RowsSizeMB"):
                check.equal(data_dict["Progress"]["Messages"][1], "RowsSizeMB:51208")
            with allure.step("TotalSizeMB"):
                check.equal(data_dict["Progress"]["Messages"][2], "TotalSizeMB:51228")
            with allure.step("Прогресс выполнения задачи"):
                check.equal(data_dict["Progress"]["CompletedPercent"], 100)

        @allure.title("Проверка возвращаемой схемы JSON")
        def test_schema(self):
            schema = {
                "type": "object",
                "required": ["ID", "Server", "Source", "Date"],
            }
            resp = (
                TestGettingInformationOfSpecificTasks.TestGettingInformationOfArchiveMonitor.r.json()
            )
            validate(resp, schema=schema)

        @allure.title("Проверка возвращаемой схемы JSON")
        def test_schema2(self):
            data_dict = requests.get(
                TestGettingInformationOfSpecificTasks.TestGettingInformationOfArchiveMonitor.path,
                verify=False,
            ).json()
            error_list = []
            for row in data_dict:
                try:
                    parse_obj_as(
                        List[
                            schema_models.SchemaModelsDCArchivingRESTAPI.GettingListOfAllTasks
                        ],
                        data_dict,
                    )
                except ValidationError as e:
                    error_list.append(f"Error found in object: {row}\n{e.json()}\n")
            try:
                schema_models.SchemaModelsDCArchivingRESTAPI.GettingListOfAllTasks.parse_obj(
                    data_dict
                )
            except Exception as e:
                if error_list:
                    raise Exception(f"{''.join(error_list)}\n{e}")
                else:
                    raise Exception(e)
