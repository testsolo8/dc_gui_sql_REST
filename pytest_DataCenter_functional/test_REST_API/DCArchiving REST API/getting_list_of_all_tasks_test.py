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

path = "https://" + base_url_dc() + ":9082/archiving/api/v1/tasks"
r = requests.get(path, verify=False)


@allure.epic("DCArchiving REST API")
@allure.feature("Getting list of all tasks")
@pytest.mark.testRESTAPI
@allure.story("Получение списка всех задач")
class TestGettingListOfAllTasks:
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

    @allure.title("Задача переноса БД монитора")
    def test_task1(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[0]["ID"], "e69b154e1a3dcf0c7880666d2e8773cc")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[0]["ShareID"], "e201cfae8103847217916225dd49da55")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[0]["TypeID"], 0)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[0]["ActionID"], 3)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[0]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[0]["MaxErrorCount"], 5)
        with allure.step("Имя сервера"):
            check.equal(data_dict[0]["Server"], "msq-si-sql")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[0]["Source"], "monitor")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[0]["Backup"], "d:\monitor")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[0]["BackupSize"], 52255)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[0]["Date"], 1588111918)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[0]["Protocol"], 10)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[0]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[0]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[0]["BackupFile"], "")
        with allure.step("StiPath"):
            check.equal(data_dict[0]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[0]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[0]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[0]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[0]["Progress"]["Status"], 1)
        with allure.step("LogsSizeMB"):
            check.equal(data_dict[0]["Progress"]["Messages"][0], "LogsSizeMB:555")
        with allure.step("RowsSizeMB"):
            check.equal(data_dict[0]["Progress"]["Messages"][1], "RowsSizeMB:51700")
        with allure.step("TotalSizeMB"):
            check.equal(data_dict[0]["Progress"]["Messages"][2], "TotalSizeMB:52255")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[0]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача переноса БД вэбкамеры")
    def test_task2(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[1]["ID"], "8504a610d02c7f26c3bdbea35759347e")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[1]["ShareID"], "8d96f69fd657044b8e143e115f4ebff4")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[1]["TypeID"], 0)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[1]["ActionID"], 3)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[1]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[1]["MaxErrorCount"], 5)
        with allure.step("Имя сервера"):
            check.equal(data_dict[1]["Server"], "msq-si-sql")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[1]["Source"], "camera~01_04_2020_07_48")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[1]["Backup"], "d:\webcam")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[1]["BackupSize"], 51297)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[1]["Date"], 1597961873)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[1]["Protocol"], 11)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[1]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[1]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[1]["BackupFile"], "")
        with allure.step("StiPath"):
            check.equal(data_dict[1]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[1]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[1]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[1]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[1]["Progress"]["Status"], 1)
        with allure.step("LogsSizeMB"):
            check.equal(data_dict[1]["Progress"]["Messages"][0], "LogsSizeMB:189")
        with allure.step("RowsSizeMB"):
            check.equal(data_dict[1]["Progress"]["Messages"][1], "RowsSizeMB:51108")
        with allure.step("TotalSizeMB"):
            check.equal(data_dict[1]["Progress"]["Messages"][2], "TotalSizeMB:51297")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[1]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача архивирования БД вэбкамеры")
    def test_task3(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[2]["ID"], "74925acf35c0ab2de3317bcca196191c")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[2]["ShareID"], "602ff3b7cb1b2d1e172767be3f098a9b")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[2]["TypeID"], 0)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[2]["ActionID"], 4)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[2]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[2]["MaxErrorCount"], 5)
        with allure.step("Имя сервера"):
            check.equal(data_dict[2]["Server"], "msq-si-sql")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[2]["Source"], "camera")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(
                data_dict[2]["Backup"], r"\\msq-nsa-sql\dataoldf$\backup\webcam"
            )
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[2]["BackupSize"], 51213)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[2]["Date"], 1605616503)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[2]["Protocol"], 11)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[2]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[2]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[2]["BackupFile"], "")
        with allure.step("StiPath"):
            check.equal(data_dict[2]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[2]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[2]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[2]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[2]["Progress"]["Status"], 1)
        with allure.step("LogsSizeMB"):
            check.equal(data_dict[2]["Progress"]["Messages"][0], "LogsSizeMB:313")
        with allure.step("RowsSizeMB"):
            check.equal(data_dict[2]["Progress"]["Messages"][1], "RowsSizeMB:50900")
        with allure.step("TotalSizeMB"):
            check.equal(data_dict[2]["Progress"]["Messages"][2], "TotalSizeMB:51213")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[2]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача архивирования БД http post")
    def test_task4(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[3]["ID"], "b0f52481baaf039681a6843f7e9e2180")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[3]["ShareID"], "b24e718537982e5995ee89f80ce1aa0e")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[3]["TypeID"], 0)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[3]["ActionID"], 4)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[3]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[3]["MaxErrorCount"], 5)
        with allure.step("Имя сервера"):
            check.equal(data_dict[3]["Server"], "msq-si-sql")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[3]["Source"], "http_post~04_02_2019_03_31")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(
                data_dict[3]["Backup"], r"\\msq-nsa-sql\dataoldf$\backup\post"
            )
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[3]["BackupSize"], 2243)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[3]["Date"], 1605634269)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[3]["Protocol"], 65559)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[3]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[3]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[3]["BackupFile"], "")
        with allure.step("StiPath"):
            check.equal(data_dict[3]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[3]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[3]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[3]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[3]["Progress"]["Status"], 1)
        with allure.step("LogsSizeMB"):
            check.equal(data_dict[3]["Progress"]["Messages"][0], "LogsSizeMB:47")
        with allure.step("RowsSizeMB"):
            check.equal(data_dict[3]["Progress"]["Messages"][1], "RowsSizeMB:2196")
        with allure.step("TotalSizeMB"):
            check.equal(data_dict[3]["Progress"]["Messages"][2], "TotalSizeMB:2243")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[3]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача архивирования БД микрофона")
    def test_task5(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[4]["ID"], "cf37382e7428a514f9bfc207f04143b0")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[4]["ShareID"], "243653db230ae8b36ff36702a08e92cb")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[4]["TypeID"], 0)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[4]["ActionID"], 4)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[4]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[4]["MaxErrorCount"], 1)
        with allure.step("Имя сервера"):
            check.equal(data_dict[4]["Server"], "msq-si-sql")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(
                data_dict[4]["Source"],
                "nsa2_minsk_searchinform_net_ec_microphone~01_03_2021_11_36",
            )
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(
                data_dict[4]["Backup"], r"\\msq-nsa-sql\dataoldf$\backup\microphone"
            )
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[4]["BackupSize"], 51225)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[4]["Date"], 1629243166)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[4]["Protocol"], 65560)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[4]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[4]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[4]["BackupFile"], "")
        with allure.step("StiPath"):
            check.equal(data_dict[4]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[4]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[4]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[4]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[4]["Progress"]["Status"], 1)
        with allure.step("LogsSizeMB"):
            check.equal(data_dict[4]["Progress"]["Messages"][0], "LogsSizeMB:17")
        with allure.step("RowsSizeMB"):
            check.equal(data_dict[4]["Progress"]["Messages"][1], "RowsSizeMB:51208")
        with allure.step("TotalSizeMB"):
            check.equal(data_dict[4]["Progress"]["Messages"][2], "TotalSizeMB:51225")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[4]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача архивирования БД почты smtpint")
    def test_task6(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[5]["ID"], "b48fdbe4bef834a097f97fb15ceb05b9")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[5]["ShareID"], "7b6831785495ef3ab86d68714425485b")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[5]["TypeID"], 0)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[5]["ActionID"], 4)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[5]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[5]["MaxErrorCount"], 2)
        with allure.step("Имя сервера"):
            check.equal(data_dict[5]["Server"], "take-sql")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[5]["Source"], "nc_smtpint")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(
                data_dict[5]["Backup"], r"\\msq-nsa-sql\dataoldf$\backup\mail"
            )
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[5]["BackupSize"], 942)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[5]["Date"], 1645047582)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[5]["Protocol"], 65543)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[5]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[5]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[5]["BackupFile"], "")
        with allure.step("StiPath"):
            check.equal(data_dict[5]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[5]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[5]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[5]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[5]["Progress"]["Status"], 1)
        with allure.step("LogsSizeMB"):
            check.equal(data_dict[5]["Progress"]["Messages"][0], "LogsSizeMB:42")
        with allure.step("RowsSizeMB"):
            check.equal(data_dict[5]["Progress"]["Messages"][1], "RowsSizeMB:900")
        with allure.step("TotalSizeMB"):
            check.equal(data_dict[5]["Progress"]["Messages"][2], "TotalSizeMB:942")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[5]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача архивирования БД почты mailint")
    def test_task7(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[6]["ID"], "1ac9f1dc2bd736e6d60d5abbf038c4a9")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[6]["ShareID"], "7b6831785495ef3ab86d68714425485b")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[6]["TypeID"], 0)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[6]["ActionID"], 4)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[6]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[6]["MaxErrorCount"], 2)
        with allure.step("Имя сервера"):
            check.equal(data_dict[6]["Server"], "take-sql")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[6]["Source"], "nc_mailint")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(
                data_dict[6]["Backup"], r"\\msq-nsa-sql\dataoldf$\backup\mail"
            )
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[6]["BackupSize"], 3074)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[6]["Date"], 1645047956)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[6]["Protocol"], 65543)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[6]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[6]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[6]["BackupFile"], "")
        with allure.step("StiPath"):
            check.equal(data_dict[6]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[6]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[6]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[6]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[6]["Progress"]["Status"], 1)
        with allure.step("LogsSizeMB"):
            check.equal(data_dict[6]["Progress"]["Messages"][0], "LogsSizeMB:74")
        with allure.step("RowsSizeMB"):
            check.equal(data_dict[6]["Progress"]["Messages"][1], "RowsSizeMB:3000")
        with allure.step("TotalSizeMB"):
            check.equal(data_dict[6]["Progress"]["Messages"][2], "TotalSizeMB:3074")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[6]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача переноса БД почты")
    def test_task8(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[7]["ID"], "70dd98d65f3363117c6b2b84ee275a3f")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[7]["ShareID"], "dc235a38d19509ab6a08d66f8885bd7a")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[7]["TypeID"], 0)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[7]["ActionID"], 3)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[7]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[7]["MaxErrorCount"], 2)
        with allure.step("Имя сервера"):
            check.equal(data_dict[7]["Server"], "take-sql")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[7]["Source"], "nc_mail")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[7]["Backup"], r"d:\mail")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[7]["BackupSize"], 101)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[7]["Date"], 1645142645)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[7]["Protocol"], 65543)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[7]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[7]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[7]["BackupFile"], "")
        with allure.step("StiPath"):
            check.equal(data_dict[7]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[7]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[7]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[7]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[7]["Progress"]["Status"], 1)
        with allure.step("LogsSizeMB"):
            check.equal(data_dict[7]["Progress"]["Messages"][0], "LogsSizeMB:1")
        with allure.step("RowsSizeMB"):
            check.equal(data_dict[7]["Progress"]["Messages"][1], "RowsSizeMB:100")
        with allure.step("TotalSizeMB"):
            check.equal(data_dict[7]["Progress"]["Messages"][2], "TotalSizeMB:101")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[7]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача переноса БД почты smtpint")
    def test_task9(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[8]["ID"], "b320f07a4838562ebaaeb09f4e7071d0")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[8]["ShareID"], "dc235a38d19509ab6a08d66f8885bd7a")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[8]["TypeID"], 0)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[8]["ActionID"], 3)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[8]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[8]["MaxErrorCount"], 2)
        with allure.step("Имя сервера"):
            check.equal(data_dict[8]["Server"], "take-sql")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[8]["Source"], "nc_smtpint~01_03_2022_03_00")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[8]["Backup"], r"d:\mail")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[8]["BackupSize"], 3544)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[8]["Date"], 1647475706)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[8]["Protocol"], 65543)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[8]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[8]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[8]["BackupFile"], "")
        with allure.step("StiPath"):
            check.equal(data_dict[8]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[8]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[8]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[8]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[8]["Progress"]["Status"], 1)
        with allure.step("LogsSizeMB"):
            check.equal(data_dict[8]["Progress"]["Messages"][0], "LogsSizeMB:136")
        with allure.step("RowsSizeMB"):
            check.equal(data_dict[8]["Progress"]["Messages"][1], "RowsSizeMB:3408")
        with allure.step("TotalSizeMB"):
            check.equal(data_dict[8]["Progress"]["Messages"][2], "TotalSizeMB:3544")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[8]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача архивации БД Skype")
    def test_task10(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[9]["ID"], "f6b634af32bfdb71e87327b6ad91afbe")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[9]["ShareID"], "bb8271d84f55d989a044d206411f706a")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[9]["TypeID"], 0)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[9]["ActionID"], 4)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[9]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[9]["MaxErrorCount"], 2)
        with allure.step("Имя сервера"):
            check.equal(data_dict[9]["Server"], "take-sql")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(
                data_dict[9]["Source"],
                "nsa2_minsk_searchinform_net_ec_skype~03_11_2021_10_21",
            )
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(
                data_dict[9]["Backup"], r"\\msq-nsa-sql\dataoldf$\backup\skype"
            )
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[9]["BackupSize"], 10249)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[9]["Date"], 1648156225)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[9]["Protocol"], 65551)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[9]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[9]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[9]["BackupFile"], "")
        with allure.step("StiPath"):
            check.equal(data_dict[9]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[9]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[9]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[9]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[9]["Progress"]["Status"], 1)
        with allure.step("LogsSizeMB"):
            check.equal(data_dict[9]["Progress"]["Messages"][0], "LogsSizeMB:41")
        with allure.step("RowsSizeMB"):
            check.equal(data_dict[9]["Progress"]["Messages"][1], "RowsSizeMB:10208")
        with allure.step("TotalSizeMB"):
            check.equal(data_dict[9]["Progress"]["Messages"][2], "TotalSizeMB:10249")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[9]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача переноса БД Skype")
    def test_task11(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[10]["ID"], "2c28d3ccda6835dfd3bd3e0bc733134b")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[10]["ShareID"], "25569d92abd5a091bf41a5b5b5532ad4")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[10]["TypeID"], 0)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[10]["ActionID"], 3)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[10]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[10]["MaxErrorCount"], 2)
        with allure.step("Имя сервера"):
            check.equal(data_dict[10]["Server"], "take-sql")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(
                data_dict[10]["Source"],
                "nsa2_minsk_searchinform_net_ec_skype~04_04_2022_12_00",
            )
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[10]["Backup"], r"d:\skype")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[10]["BackupSize"], 10253)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[10]["Date"], 1650326878)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[10]["Protocol"], 65551)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[10]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[10]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[10]["BackupFile"], "")
        with allure.step("StiPath"):
            check.equal(data_dict[10]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[10]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[10]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[10]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[10]["Progress"]["Status"], 1)
        with allure.step("LogsSizeMB"):
            check.equal(data_dict[10]["Progress"]["Messages"][0], "LogsSizeMB:45")
        with allure.step("RowsSizeMB"):
            check.equal(data_dict[10]["Progress"]["Messages"][1], "RowsSizeMB:10208")
        with allure.step("TotalSizeMB"):
            check.equal(data_dict[10]["Progress"]["Messages"][2], "TotalSizeMB:10253")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[10]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача архивации БД принт")
    def test_task12(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[11]["ID"], "6a45ccf0a0be9e4802ba5a7bb95a912b")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[11]["ShareID"], "652611fbab258e6e4e4b5602b18d72a5")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[11]["TypeID"], 0)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[11]["ActionID"], 4)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[11]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[11]["MaxErrorCount"], 3)
        with allure.step("Имя сервера"):
            check.equal(data_dict[11]["Server"], "take-sql")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(
                data_dict[11]["Source"],
                "nsa2_minsk_searchinform_net_ec_print~01_01_2022_00_02",
            )
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(
                data_dict[11]["Backup"], r"\\msq-nsa-sql\dataoldf$\backup\print"
            )
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[11]["BackupSize"], 219)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[11]["Date"], 1654203852)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[11]["Protocol"], 65554)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[11]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[11]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[11]["BackupFile"], "")
        with allure.step("StiPath"):
            check.equal(data_dict[11]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[11]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[11]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[11]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[11]["Progress"]["Status"], 1)
        with allure.step("LogsSizeMB"):
            check.equal(data_dict[11]["Progress"]["Messages"][0], "LogsSizeMB:11")
        with allure.step("RowsSizeMB"):
            check.equal(data_dict[11]["Progress"]["Messages"][1], "RowsSizeMB:208")
        with allure.step("TotalSizeMB"):
            check.equal(data_dict[11]["Progress"]["Messages"][2], "TotalSizeMB:219")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[11]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача переноса БД микрофона")
    def test_task13(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[12]["ID"], "827370df2810c39af5f57f7da89d101a")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[12]["ShareID"], "c09ad55dcc0d4a1155963e08d34ff264")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[12]["TypeID"], 0)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[12]["ActionID"], 3)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[12]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[12]["MaxErrorCount"], 2)
        with allure.step("Имя сервера"):
            check.equal(data_dict[12]["Server"], "take-sql")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(
                data_dict[12]["Source"],
                "nsa2_minsk_searchinform_net_ec_microphone~01_06_2022_14_11",
            )
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[12]["Backup"], r"d:\microphone")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[12]["BackupSize"], 51327)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[12]["Date"], 1654820798)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[12]["Protocol"], 65560)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[12]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[12]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[12]["BackupFile"], "")
        with allure.step("StiPath"):
            check.equal(data_dict[12]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[12]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[12]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[12]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[12]["Progress"]["Status"], 1)
        with allure.step("LogsSizeMB"):
            check.equal(data_dict[12]["Progress"]["Messages"][0], "LogsSizeMB:19")
        with allure.step("RowsSizeMB"):
            check.equal(data_dict[12]["Progress"]["Messages"][1], "RowsSizeMB:51308")
        with allure.step("TotalSizeMB"):
            check.equal(data_dict[12]["Progress"]["Messages"][2], "TotalSizeMB:51327")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[12]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача архивации индекса микрофона")
    def test_task14(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[13]["ID"], "758d7c4c3f4339ab9a1f208e1729c206")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[13]["ShareID"], "8ea14f593b39fcccb1c67df20db9220a")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[13]["TypeID"], 1)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[13]["ActionID"], 0)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[13]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[13]["MaxErrorCount"], 2)
        with allure.step("Имя сервера"):
            check.equal(data_dict[13]["Server"], "nsa2.minsk.searchinform.net")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(
                data_dict[13]["Source"],
                "nsa2_minsk_searchinform_net_EC_Microphone~23_07_2021_11_13",
            )
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(
                data_dict[13]["Backup"],
                r"\\msq-nsa-sql\dataoldf$\backup\microphone\index\nsa2_minsk_searchinform_net_EC_Microphone~18_12_2020_11_50",
            )
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[13]["BackupSize"], 9)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[13]["Date"], 1656089169)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[13]["Protocol"], 24)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[13]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[13]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(
                data_dict[13]["BackupFile"],
                r"\\msq-nsa-sql\dataoldf$\backup\microphone\index\nsa2_minsk_searchinform_net_EC_Microphone~18_12_2020_11_50\nsa2_minsk_searchinform_net_EC_Microphone~23_07_2021_11_13.lbx.zbk",
            )
        with allure.step("StiPath"):
            check.equal(data_dict[13]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(
                data_dict[13]["IndexName"],
                "nsa2_minsk_searchinform_net_EC_Microphone~23_07_2021_11_13",
            )
        with allure.step("IndexPath"):
            check.equal(
                data_dict[13]["IndexPath"],
                r"D:\Indexes2\nsa2_minsk_searchinform_net_EC_Microphone~18_12_2020_11_50\nsa2_minsk_searchinform_net_EC_Microphone~23_07_2021_11_13.lbx",
            )
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[13]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[13]["Progress"]["Status"], 1)
        with allure.step("BackupSizeMB"):
            check.equal(data_dict[13]["Progress"]["Messages"][0], "BackupSizeMB:9")
        with allure.step("IndexSizeMB"):
            check.equal(data_dict[13]["Progress"]["Messages"][1], "IndexSizeMB:17")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[13]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача переноса БД http post")
    def test_task15(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[14]["ID"], "015971ab880c427511c2ae682b30c26d")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[14]["ShareID"], "17c21567259274fd3d2db58482439f63")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[14]["TypeID"], 0)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[14]["ActionID"], 3)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[14]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[14]["MaxErrorCount"], 2)
        with allure.step("Имя сервера"):
            check.equal(data_dict[14]["Server"], "take-sql")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(
                data_dict[14]["Source"],
                "nsa2_minsk_searchinform_net_ec_http~04_07_2022_15_20",
            )
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[14]["Backup"], r"d:\http post")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[14]["BackupSize"], 2627)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[14]["Date"], 1657585401)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[14]["Protocol"], 65559)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[14]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[14]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[14]["BackupFile"], "")
        with allure.step("StiPath"):
            check.equal(data_dict[14]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[14]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[14]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[14]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[14]["Progress"]["Status"], 1)
        with allure.step("LogsSizeMB"):
            check.equal(data_dict[14]["Progress"]["Messages"][0], "LogsSizeMB:19")
        with allure.step("RowsSizeMB"):
            check.equal(data_dict[14]["Progress"]["Messages"][1], "RowsSizeMB:2608")
        with allure.step("TotalSizeMB"):
            check.equal(data_dict[14]["Progress"]["Messages"][2], "TotalSizeMB:2627")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[14]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача архивации БД монитора")
    def test_task16(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[15]["ID"], "b511dbd0b9e1b40d537b0f2b92583145")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[15]["ShareID"], "0308b7f4b59902e3ff155187651d897d")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[15]["TypeID"], 0)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[15]["ActionID"], 4)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[15]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[15]["MaxErrorCount"], 3)
        with allure.step("Имя сервера"):
            check.equal(data_dict[15]["Server"], "take-sql")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(
                data_dict[15]["Source"],
                "nsa2_minsk_searchinform_net_ec_monitor~01_07_2022_15_30",
            )
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(
                data_dict[15]["Backup"], r"\\msq-nsa-sql\dataolde$\backup\monitor"
            )
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[15]["BackupSize"], 51228)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[15]["Date"], 1659822615)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[15]["Protocol"], 10)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[15]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[15]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(
                data_dict[15]["BackupFile"],
                r"\\msq-nsa-sql\dataolde$\backup\monitor\nsa2_minsk_searchinform_net_ec_monitor~01_07_2022_15_30.bak",
            )
        with allure.step("StiPath"):
            check.equal(data_dict[15]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[15]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[15]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[15]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[15]["Progress"]["Status"], 1)
        with allure.step("LogsSizeMB"):
            check.equal(data_dict[15]["Progress"]["Messages"][0], "LogsSizeMB:20")
        with allure.step("RowsSizeMB"):
            check.equal(data_dict[15]["Progress"]["Messages"][1], "RowsSizeMB:51208")
        with allure.step("TotalSizeMB"):
            check.equal(data_dict[15]["Progress"]["Messages"][2], "TotalSizeMB:51228")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[15]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача переноса индекса skype")
    def test_task17(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[16]["ID"], "ae0499ae5cad9d42d3aebef6fa312faa")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[16]["ShareID"], "")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[16]["TypeID"], 1)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[16]["ActionID"], 3)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[16]["ErrorCount"], 1)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[16]["MaxErrorCount"], 5)
        with allure.step("Имя сервера"):
            check.equal(data_dict[16]["Server"], "win-734hjf247we")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[16]["Source"], "skype")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[16]["Backup"], r"f:\move index")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[16]["BackupSize"], 5)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[16]["Date"], 1662355459)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[16]["Protocol"], 65551)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[16]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[16]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[16]["BackupFile"], r"f:\move index\skype.lbx")
        with allure.step("StiPath"):
            check.equal(data_dict[16]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[16]["IndexName"], "skype")
        with allure.step("IndexPath"):
            check.equal(data_dict[16]["IndexPath"], "C:\Indexes\skype\skype.lbx")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[16]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[16]["Progress"]["Status"], 1)
        with allure.step("Move files for"):
            check.equal(
                data_dict[16]["Progress"]["Messages"][0],
                "Move files for {b7060600-a148-4fb3-a00e-6735c27aad14}",
            )
        with allure.step("Move completed"):
            check.equal(data_dict[16]["Progress"]["Messages"][1], "Move completed")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[16]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача переноса STI device")
    def test_task18(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[17]["ID"], "5b00aa4ebeea9477645c8606a2cf16e7")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[17]["ShareID"], "c064115a3aa347f2c1bdf37a5f02d27d")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[17]["TypeID"], 2)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[17]["ActionID"], 3)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[17]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[17]["MaxErrorCount"], 5)
        with allure.step("Имя сервера"):
            check.equal(data_dict[17]["Server"], "win-734hjf247we")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[17]["Source"], "C:\Device\device.sti")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[17]["Backup"], r"f:\move sti")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[17]["BackupSize"], 1352)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[17]["Date"], 1662356924)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[17]["Protocol"], 16)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[17]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[17]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[17]["BackupFile"], r"f:\move sti\device.sti")
        with allure.step("StiPath"):
            check.equal(data_dict[17]["StiPath"], "C:\Device\device.sti")
        with allure.step("IndexName"):
            check.equal(data_dict[17]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[17]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[17]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[17]["Progress"]["Status"], 1)
        with allure.step("File"):
            check.equal(
                data_dict[17]["Progress"]["Messages"][0],
                "File C:\Device\device.sti moved to f:\move sti",
            )
        with allure.step("Index"):
            check.equal(
                data_dict[17]["Progress"]["Messages"][1],
                "Index: {eb4786d1-6f0d-4a06-8c2b-a4ad33e5ee03}, Storage(sti) changed to f:\move sti\device.sti",
            )
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[17]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача переноса STI FTP")
    def test_task19(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[18]["ID"], "f19be2b87184a723f3e51ddaadda4852")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[18]["ShareID"], "c064115a3aa347f2c1bdf37a5f02d27d")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[18]["TypeID"], 2)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[18]["ActionID"], 3)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[18]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[18]["MaxErrorCount"], 5)
        with allure.step("Имя сервера"):
            check.equal(data_dict[18]["Server"], "win-734hjf247we")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[18]["Source"], "C:\FTP\FTP.sti")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[18]["Backup"], r"f:\move sti")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[18]["BackupSize"], 738)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[18]["Date"], 1662357515)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[18]["Protocol"], 17)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[18]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[18]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[18]["BackupFile"], r"f:\move sti\FTP.sti")
        with allure.step("StiPath"):
            check.equal(data_dict[18]["StiPath"], "C:\FTP\FTP.sti")
        with allure.step("IndexName"):
            check.equal(data_dict[18]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[18]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[18]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[18]["Progress"]["Status"], 1)
        with allure.step("File"):
            check.equal(
                data_dict[18]["Progress"]["Messages"][0],
                "File C:\FTP\FTP.sti moved to f:\move sti",
            )
        with allure.step("Index"):
            check.equal(
                data_dict[18]["Progress"]["Messages"][1],
                "Index: {5551babe-9b94-4af7-90b8-8c67c23f6a40}, Storage(sti) changed to f:\move sti\FTP.sti",
            )
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[18]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача переноса индекса Device")
    def test_task20(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[19]["ID"], "87ef8b5381df3dd0f3ebf72768dda658")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[19]["ShareID"], "e53d3141f741080c73aa78f1678b3611")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[19]["TypeID"], 1)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[19]["ActionID"], 3)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[19]["ErrorCount"], 2)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[19]["MaxErrorCount"], 3)
        with allure.step("Имя сервера"):
            check.equal(data_dict[19]["Server"], "win-734hjf247we")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[19]["Source"], "Device")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[19]["Backup"], r"f:\move index")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[19]["BackupSize"], 4062)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[19]["Date"], 1662358478)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[19]["Protocol"], 16)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[19]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[19]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[19]["BackupFile"], r"f:\move index\Device.lbx")
        with allure.step("StiPath"):
            check.equal(data_dict[19]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[19]["IndexName"], "Device")
        with allure.step("IndexPath"):
            check.equal(data_dict[19]["IndexPath"], "C:\Indexes\Device\Device.lbx")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[19]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[19]["Progress"]["Status"], 1)
        with allure.step("Move files for"):
            check.equal(
                data_dict[19]["Progress"]["Messages"][0],
                "Move files for {eb4786d1-6f0d-4a06-8c2b-a4ad33e5ee03}",
            )
        with allure.step("Move completed"):
            check.equal(data_dict[19]["Progress"]["Messages"][1], "Move completed")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[19]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача переноса индекса принт")
    def test_task21(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[20]["ID"], "ca2b551eafcb1f384461b0e7e4bd82f1")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[20]["ShareID"], "e53d3141f741080c73aa78f1678b3611")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[20]["TypeID"], 1)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[20]["ActionID"], 3)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[20]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[20]["MaxErrorCount"], 3)
        with allure.step("Имя сервера"):
            check.equal(data_dict[20]["Server"], "win-734hjf247we")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[20]["Source"], "Print")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[20]["Backup"], r"f:\move index")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[20]["BackupSize"], 6)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[20]["Date"], 1662359003)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[20]["Protocol"], 18)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[20]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[20]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[20]["BackupFile"], r"f:\move index\print.lbx")
        with allure.step("StiPath"):
            check.equal(data_dict[20]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[20]["IndexName"], "Print")
        with allure.step("IndexPath"):
            check.equal(data_dict[20]["IndexPath"], "C:\Indexes\print\print.lbx")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[20]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[20]["Progress"]["Status"], 1)
        with allure.step("Move files for"):
            check.equal(
                data_dict[20]["Progress"]["Messages"][0],
                "Move files for {59b3dd3a-3eac-498f-a317-1e19916dc9f8}",
            )
        with allure.step("Move completed"):
            check.equal(data_dict[20]["Progress"]["Messages"][1], "Move completed")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[20]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача переноса индекса FTP")
    def test_task22(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[21]["ID"], "3905a60791616f5679298cb1a15cfb24")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[21]["ShareID"], "e53d3141f741080c73aa78f1678b3611")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[21]["TypeID"], 1)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[21]["ActionID"], 3)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[21]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[21]["MaxErrorCount"], 3)
        with allure.step("Имя сервера"):
            check.equal(data_dict[21]["Server"], "win-734hjf247we")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[21]["Source"], "FTP")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[21]["Backup"], r"f:\move index")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[21]["BackupSize"], 1979)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[21]["Date"], 1662359642)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[21]["Protocol"], 17)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[21]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[21]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(data_dict[21]["BackupFile"], r"f:\move index\FTP.lbx")
        with allure.step("StiPath"):
            check.equal(data_dict[21]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[21]["IndexName"], "FTP")
        with allure.step("IndexPath"):
            check.equal(data_dict[21]["IndexPath"], "C:\Indexes\FTP\FTP.lbx")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[21]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[21]["Progress"]["Status"], 1)
        with allure.step("Move files for"):
            check.equal(
                data_dict[21]["Progress"]["Messages"][0],
                "Move files for {5551babe-9b94-4af7-90b8-8c67c23f6a40}",
            )
        with allure.step("Move completed"):
            check.equal(data_dict[21]["Progress"]["Messages"][1], "Move completed")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[21]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача переноса индекса Skype")
    def test_task23(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[22]["ID"], "d012d198d5cfb925f85b6ae0b9cd78c4")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[22]["ShareID"], "e53d3141f741080c73aa78f1678b3611")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[22]["TypeID"], 1)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[22]["ActionID"], 3)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[22]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[22]["MaxErrorCount"], 3)
        with allure.step("Имя сервера"):
            check.equal(data_dict[22]["Server"], "win-734hjf247we")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[22]["Source"], "skype~28_04_2022_13_21")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[22]["Backup"], r"f:\move index")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[22]["BackupSize"], 4)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[22]["Date"], 1662360203)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[22]["Protocol"], 15)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[22]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[22]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(
                data_dict[22]["BackupFile"],
                r"f:\move index\skype~28_04_2022_13_21.lbx",
            )
        with allure.step("StiPath"):
            check.equal(data_dict[22]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[22]["IndexName"], "skype~28_04_2022_13_21")
        with allure.step("IndexPath"):
            check.equal(
                data_dict[22]["IndexPath"],
                "C:\Indexes\skype\skype~28_04_2022_13_21.lbx",
            )
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[22]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[22]["Progress"]["Status"], 1)
        with allure.step("Move files for"):
            check.equal(
                data_dict[22]["Progress"]["Messages"][0],
                "Move files for {8aa0f634-5a36-42f1-83f3-356c8b3670c0}",
            )
        with allure.step("Move completed"):
            check.equal(data_dict[22]["Progress"]["Messages"][1], "Move completed")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[22]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача архивации STI device")
    def test_task24(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[23]["ID"], "c35eb6b556225dcd6c6378a98226c88b")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[23]["ShareID"], "cee3eca5e952d5159d234b4942ec7057")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[23]["TypeID"], 2)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[23]["ActionID"], 4)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[23]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[23]["MaxErrorCount"], 5)
        with allure.step("Имя сервера"):
            check.equal(data_dict[23]["Server"], "win-734hjf247we")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(
                data_dict[23]["Source"], "C:\Device\~28_04_2022_15_04\device.sti"
            )
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[23]["Backup"], r"e:\archive sti\~28_04_2022_15_04")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[23]["BackupSize"], 612)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[23]["Date"], 1662362342)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[23]["Protocol"], 16)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[23]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[23]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(
                data_dict[23]["BackupFile"],
                r"e:\archive sti\~28_04_2022_15_04\device.sti.zip",
            )
        with allure.step("StiPath"):
            check.equal(
                data_dict[23]["StiPath"], "C:\Device\~28_04_2022_15_04\device.sti"
            )
        with allure.step("IndexName"):
            check.equal(data_dict[23]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[23]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[23]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[23]["Progress"]["Status"], 1)
        with allure.step("BackupSizeMB"):
            check.equal(data_dict[23]["Progress"]["Messages"][0], "BackupSizeMB:612")
        with allure.step("StorageSizeMB"):
            check.equal(data_dict[23]["Progress"]["Messages"][1], "StorageSizeMB:613")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[23]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача архивации STI FTP")
    def test_task25(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[24]["ID"], "904e848adedd5ce9737c7250b17b7570")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[24]["ShareID"], "cee3eca5e952d5159d234b4942ec7057")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[24]["TypeID"], 2)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[24]["ActionID"], 4)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[24]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[24]["MaxErrorCount"], 5)
        with allure.step("Имя сервера"):
            check.equal(data_dict[24]["Server"], "win-734hjf247we")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[24]["Source"], "C:\FTP\~28_04_2022_13_21\FTP.sti")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[24]["Backup"], r"e:\archive sti\~28_04_2022_13_21")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[24]["BackupSize"], 613)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[24]["Date"], 1662362941)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[24]["Protocol"], 17)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[24]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[24]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(
                data_dict[24]["BackupFile"],
                r"e:\archive sti\~28_04_2022_13_21\FTP.sti.zip",
            )
        with allure.step("StiPath"):
            check.equal(data_dict[24]["StiPath"], "C:\FTP\~28_04_2022_13_21\FTP.sti")
        with allure.step("IndexName"):
            check.equal(data_dict[24]["IndexName"], "")
        with allure.step("IndexPath"):
            check.equal(data_dict[24]["IndexPath"], "")
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[24]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[24]["Progress"]["Status"], 1)
        with allure.step("BackupSizeMB"):
            check.equal(data_dict[24]["Progress"]["Messages"][0], "BackupSizeMB:613")
        with allure.step("StorageSizeMB"):
            check.equal(data_dict[24]["Progress"]["Messages"][1], "StorageSizeMB:614")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[24]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача архивации индекса принт")
    def test_task26(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[25]["ID"], "8d9ca902cf5796b3c71b848648a9c7c7")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[25]["ShareID"], "9331fb7825581e8e724a4dac3f489ee4")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[25]["TypeID"], 1)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[25]["ActionID"], 0)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[25]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[25]["MaxErrorCount"], 1)
        with allure.step("Имя сервера"):
            check.equal(data_dict[25]["Server"], "win-734hjf247we")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[25]["Source"], "print~28_04_2022_15_19")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[25]["Backup"], r"e:\archive index")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[25]["BackupSize"], 1)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[25]["Date"], 1662366202)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[25]["Protocol"], 18)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[25]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[25]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(
                data_dict[25]["BackupFile"],
                r"e:\archive index\print~28_04_2022_15_19.lbx.zbk",
            )
        with allure.step("StiPath"):
            check.equal(data_dict[25]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[25]["IndexName"], "print~28_04_2022_15_19")
        with allure.step("IndexPath"):
            check.equal(
                data_dict[25]["IndexPath"],
                "C:\Indexes\print\print~28_04_2022_15_19.lbx",
            )
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[25]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[25]["Progress"]["Status"], 1)
        with allure.step("BackupSizeMB"):
            check.equal(data_dict[25]["Progress"]["Messages"][0], "BackupSizeMB:1")
        with allure.step("StorageSizeMB"):
            check.equal(data_dict[25]["Progress"]["Messages"][1], "IndexSizeMB:6")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[25]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача архивации индекса Device")
    def test_task27(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[26]["ID"], "47093c3e3cdde9ab40e0e9db102fba61")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[26]["ShareID"], "9331fb7825581e8e724a4dac3f489ee4")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[26]["TypeID"], 1)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[26]["ActionID"], 0)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[26]["ErrorCount"], 2)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[26]["MaxErrorCount"], 2)
        with allure.step("Имя сервера"):
            check.equal(data_dict[26]["Server"], "win-734hjf247we")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[26]["Source"], "Device~28_04_2022_16_29")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[26]["Backup"], r"e:\archive index")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[26]["BackupSize"], 955)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[26]["Date"], 1662366851)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[26]["Protocol"], 16)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[26]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[26]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(
                data_dict[26]["BackupFile"],
                r"e:\archive index\Device~28_04_2022_16_29.lbx.zbk",
            )
        with allure.step("StiPath"):
            check.equal(data_dict[26]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[26]["IndexName"], "Device~28_04_2022_16_29")
        with allure.step("IndexPath"):
            check.equal(
                data_dict[26]["IndexPath"],
                "C:\Indexes\Device\Device~28_04_2022_16_29.lbx",
            )
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[26]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[26]["Progress"]["Status"], 1)
        with allure.step("BackupSizeMB"):
            check.equal(data_dict[26]["Progress"]["Messages"][0], "BackupSizeMB:955")
        with allure.step("StorageSizeMB"):
            check.equal(data_dict[26]["Progress"]["Messages"][1], "IndexSizeMB:1820")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[26]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача архивации индекса FTP")
    def test_task28(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[27]["ID"], "fdeb7349b8c78bd226385ce4889adec7")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[27]["ShareID"], "9331fb7825581e8e724a4dac3f489ee4")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[27]["TypeID"], 1)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[27]["ActionID"], 0)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[27]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[27]["MaxErrorCount"], 1)
        with allure.step("Имя сервера"):
            check.equal(data_dict[27]["Server"], "win-734hjf247we")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[27]["Source"], "FTP~28_04_2022_13_21")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[27]["Backup"], r"e:\archive index")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[27]["BackupSize"], 907)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[27]["Date"], 1662369249)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[27]["Protocol"], 17)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[27]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[27]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(
                data_dict[27]["BackupFile"],
                r"e:\archive index\FTP~28_04_2022_13_21.lbx.zbk",
            )
        with allure.step("StiPath"):
            check.equal(data_dict[27]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[27]["IndexName"], "FTP~28_04_2022_13_21")
        with allure.step("IndexPath"):
            check.equal(
                data_dict[27]["IndexPath"], "C:\Indexes\FTP\FTP~28_04_2022_13_21.lbx"
            )
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[27]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[27]["Progress"]["Status"], 1)
        with allure.step("BackupSizeMB"):
            check.equal(data_dict[27]["Progress"]["Messages"][0], "BackupSizeMB:907")
        with allure.step("StorageSizeMB"):
            check.equal(data_dict[27]["Progress"]["Messages"][1], "IndexSizeMB:1666")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[27]["Progress"]["CompletedPercent"], 100)

    @allure.title("Задача архивации индекса Skype")
    def test_task29(self):
        data_dict = r.json()
        with allure.step("ID задачи"):
            check.equal(data_dict[28]["ID"], "db9bdb5e170e85433a93e9faa5463945")
        with allure.step("ID хранилища из списка"):
            check.equal(data_dict[28]["ShareID"], "9331fb7825581e8e724a4dac3f489ee4")
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - База данных SQL, 1 - Индекс SearchServer"
        ):
            check.equal(data_dict[28]["TypeID"], 1)
        with allure.step(
            "Идентификатор типа задачи. Возможные типы: 0 - Резервное копирование базы данных, 1 - Восстановление из резервной копии, 2 - Удаление резервной копии из хранилища"
        ):
            check.equal(data_dict[28]["ActionID"], 0)
        with allure.step("Количество поочередных ошибок произошедших с этим заданием"):
            check.equal(data_dict[28]["ErrorCount"], 0)
        with allure.step("Максимальное количество поочередных ошибок"):
            check.equal(data_dict[28]["MaxErrorCount"], 1)
        with allure.step("Имя сервера"):
            check.equal(data_dict[28]["Server"], "win-734hjf247we")
        with allure.step("Имя базы данных или путь до индекса"):
            check.equal(data_dict[28]["Source"], "skype~28_04_2022_15_04")
        with allure.step("Полное имя папки для резервной копии"):
            check.equal(data_dict[28]["Backup"], r"e:\archive index")
        with allure.step("Размер резервной копии в мегабайтах"):
            check.equal(data_dict[28]["BackupSize"], 0)
        with allure.step("Время последнего шага задачи в формате Unix"):
            check.equal(data_dict[28]["Date"], 1662371001)
        with allure.step("ID протокола содержащегося в базе или индексе"):
            check.equal(data_dict[28]["Protocol"], 15)
        with allure.step("Минимальная дата документа в БД или индексе"):
            check.equal(data_dict[28]["MinDocDate"], 0)
        with allure.step("Максимальная дата документа в Бд или индексе"):
            check.equal(data_dict[28]["MaxDocDate"], 0)
        with allure.step("BackupFile"):
            check.equal(
                data_dict[28]["BackupFile"],
                r"e:\archive index\skype~28_04_2022_15_04.lbx.zbk",
            )
        with allure.step("StiPath"):
            check.equal(data_dict[28]["StiPath"], "")
        with allure.step("IndexName"):
            check.equal(data_dict[28]["IndexName"], "skype~28_04_2022_15_04")
        with allure.step("IndexPath"):
            check.equal(
                data_dict[28]["IndexPath"],
                "C:\Indexes\skype\skype~28_04_2022_15_04.lbx",
            )
        with allure.step("Идентификатор прогресса задачи"):
            check.equal(data_dict[28]["Progress"]["ProgressID"], 0)
        with allure.step("Коды состояния прогресса"):
            check.equal(data_dict[28]["Progress"]["Status"], 1)
        with allure.step("BackupSizeMB"):
            check.equal(data_dict[28]["Progress"]["Messages"][0], "BackupSizeMB:0")
        with allure.step("StorageSizeMB"):
            check.equal(data_dict[28]["Progress"]["Messages"][1], "IndexSizeMB:5")
        with allure.step("Прогресс выполнения задачи"):
            check.equal(data_dict[28]["Progress"]["CompletedPercent"], 100)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["ID", "Server", "Source", "Date"],
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
                        schema_models.SchemaModelsDCArchivingRESTAPI.GettingListOfAllTasks
                    ],
                    data_dict,
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDCArchivingRESTAPI.GettingListOfAllTasks.parse_obj(
                data_dict[0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
