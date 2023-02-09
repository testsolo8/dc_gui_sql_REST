# Standart libraries
import datetime
import logging
import time
from pathlib import Path

# Third party packages
import allure
import pyodbc
import pytest
import pytest_check as check
import sqlalchemy_utils
from assertpy import assert_that
from pywinauto import Application
from pywinauto.keyboard import send_keys
from sqlalchemy import create_engine, inspect

# My packages
from DataCenter.buttons import OperationsLoggingPage, CommonElements
from DataCenter.tools.get_project_root import get_project_root
from DataCenter.tools.take_image_difference import get_difference_between_checkbox_image
from pytest_DataCenter_functional.test_SQL.sql_tools import Docker, delete_postgres_DB
from pytest_DataCenter_functional.test_SQL.tables_templates import (
    operations_logging_postgresql,
)

testdata = [
    (
        "192.168.1.12",
        "5411",
        "postgres",
        "Passw0rd",
        "actionslog",
        "Тест проходил на PostgreSQL ver.11",
        [],
    ),
    (
        "192.168.1.12",
        "5412",
        "postgres",
        "Passw0rd",
        "actionslog",
        "Тест проходил на PostgreSQL ver.12",
        [],
    ),
    (
        "192.168.1.12",
        "5413",
        "postgres",
        "Passw0rd",
        "actionslog",
        "Тест проходил на PostgreSQL ver.13",
        [],
    ),
    (
        "192.168.1.12",
        "5414",
        "postgres",
        "Passw0rd",
        "actionslog",
        "Тест проходил на PostgreSQL ver.14",
        [],
    ),
    (
        "192.168.1.12",
        "5415",
        "postgres",
        "Passw0rd",
        "actionslog",
        "Тест проходил на PostgreSQL ver.15",
        [],
    ),
]
testdata_spec_symbol = [
    (
        "192.168.1.12",
        "54111",
        "postgres",
        r'saSA123#$%^&_+|"' + r"%:\./''''~-`<>",
        "actionslog",
        "Тест проходил на PostgreSQL ver.11",
        [],
    ),
    (
        "192.168.1.12",
        "54122",
        "postgres",
        r'saSA123#$%^&_+|"' + r"%:\./''''~-`<>",
        "actionslog",
        "Тест проходил на PostgreSQL ver.12",
        [],
    ),
    (
        "192.168.1.12",
        "54133",
        "postgres",
        r'saSA123#$%^&_+|"' + r"%:\./''''~-`<>",
        "actionslog",
        "Тест проходил на PostgreSQL ver.13",
        [],
    ),
    (
        "192.168.1.12",
        "54144",
        "postgres",
        r'saSA123#$%^&_+|"' + r"%:\./''''~-`<>",
        "actionslog",
        "Тест проходил на PostgreSQL ver.14",
        [],
    ),
    (
        "192.168.1.12",
        "54155",
        "postgres",
        r'saSA123#$%^&_+|"' + r"%:\./''''~-`<>",
        "actionslog",
        "Тест проходил на PostgreSQL ver.15",
        [],
    ),
]

test_ids = ["{}, {}, {}, {}".format(t[0], t[1], t[2], t[4]) for t in testdata]
test_ids_spec = [
    "{}, {}, {}, {}".format(t[0], t[1], t[2], t[4]) for t in testdata_spec_symbol
]


@pytest.fixture(scope="class")
def handle(sql_test_page_ru):
    # Docker().start_postgresql()
    time.sleep(5)
    send_keys("{VK_MENU down}Y4Y01{VK_MENU up}")
    app = sql_test_page_ru
    handle = app.window(name_re="DataCenter*")
    time.sleep(2)
    yield handle
    # Docker().stop_postgresql()


@pytest.fixture(scope="class")
def handle_with_spec_symbol(sql_test_page_ru):
    # Docker().start_postgresql_spec()
    time.sleep(5)
    send_keys("{VK_MENU down}Y4Y01{VK_MENU up}")
    app = sql_test_page_ru
    handle = app.window(name_re="DataCenter*")
    time.sleep(2)
    yield handle
    # Docker().stop_postgresql_spec()


@pytest.mark.order(100)
@allure.epic("SQL test")
@allure.feature("Operations Logging create DB on PostgreSQL")
@pytest.mark.testSQLAll
@pytest.mark.testSQL_PostgreSQL
@allure.story("тест создания бд с паролем 'Passw0rd'")
class TestCreatePostgreSQLOperationsLoggingDB:
    @pytest.mark.parametrize(argnames="db_data", argvalues=testdata, ids=test_ids)
    def test_create_operations_logging_postgresql_db(self, handle, db_data):
        with allure.step(
            "Время начала теста "
            + "("
            + str(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S") + ")")
        ):
            pass
        allure.dynamic.description(db_data[5])
        [allure.dynamic.issue(i) for i in db_data[6]]
        sql_serv_addr, port, username, password, db_name = db_data[0:5]
        delete_postgres_DB(sql_serv_addr, port, username, password, db_name)
        app_win32 = Application(backend="win32").connect(
            path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
        )
        handle.by(
            name="Включить журналирование действий аудиторов в консолях продуктов"
        ).set_focus()
        time.sleep(1)
        handle.by(
            name="Включить журналирование действий аудиторов в консолях продуктов"
        ).capture_as_image().save(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "MSSQL",
                "screen_for_OperationsLogging.png",
            )
        )
        image1 = Path(
            get_project_root(),
            "pytest_DataCenter_functional",
            "test_SQL",
            "MSSQL",
            "screen_for_OperationsLogging.png",
        )
        image2 = Path(
            get_project_root(),
            "pytest_DataCenter_functional",
            "test_SQL",
            "example_OperationsLogging_checkbox.png",
        )
        time.sleep(3)
        if get_difference_between_checkbox_image(image1, image2) < 2:
            handle.by(
                name=OperationsLoggingPage.enable_logging_of_auditors["title_ru"]
            ).click_input()
        else:
            handle.by(
                name=OperationsLoggingPage.setup_connection_to_db["title_ru"]
            ).click()
        handle_win32 = app_win32.window(name_re="Параметры подключения к SQL*")
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox3").type_keys("p")
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox2").type_keys("^a{BACKSPACE}")
        time.sleep(2)
        handle.by(name=OperationsLoggingPage.read_from_dc["title_ru"]).click()
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox2").type_keys(f"{sql_serv_addr},{port}")
        time.sleep(2)
        handle_win32.__getattribute__(
            "Использовать внутреннюю аутентификацию SQL ServerComboBox2"
        ).type_keys("^a{BACKSPACE}")
        time.sleep(2)
        handle_win32.__getattribute__(
            "Использовать внутреннюю аутентификацию SQL ServerComboBox2"
        ).type_keys(r"actionslog")
        time.sleep(2)
        handle.by(name=OperationsLoggingPage.create_button["title_ru"]).click()
        time.sleep(5)
        handle.by(name=CommonElements.ok_button["title_ru"]).__getattribute__(
            CommonElements.ok_button["attribute_ru"]
        ).click()
        time.sleep(1)
        handle.by(name=OperationsLoggingPage.ok_button["title_ru"]).click()
        time.sleep(2)
        try:
            handle_win32.close()
            print("Не закрылось окно настройки SQL")
        except Exception:
            print("Создание настройки подключения прошло успешно")
        time.sleep(2)
        handle.by(name=OperationsLoggingPage.apply_button["title_ru"]).click()
        start_time = time.time()
        while time.time() - start_time < 120:
            try:
                exist_db = sqlalchemy_utils.functions.database_exists(
                    f"postgresql://{username}:{password}@{sql_serv_addr}:{port}/{db_name}"
                )
                if not exist_db:
                    time.sleep(10)
                    continue
                else:
                    logging.info("БД Operations Logging создана")
                    break
            except Exception as ex:
                logging.debug(ex)
        with check.check:
            assert_that(exist_db).described_as("Нет БД").is_true()
        if exist_db is True:
            start_time = time.time()
            while time.time() - start_time < 120:
                try:
                    engine = create_engine(
                        f"postgresql://{username}:{password}@{sql_serv_addr}:{port}/{db_name}"
                    )
                    list_of_tables = inspect(engine).get_table_names()
                    if not list_of_tables:
                        time.sleep(10)
                        continue
                    if len(list_of_tables) < 8:
                        time.sleep(10)
                    else:
                        logging.info("Корректное кол-во таблиц в БД Operations Logging")
                        break
                except Exception as ex:
                    logging.debug(ex)
            with check.check:
                assert_that(list_of_tables).described_as(
                    "Нет таблиц по умолчанию"
                ).is_equal_to(operations_logging_postgresql)
        delete_postgres_DB(sql_serv_addr, port, username, password, db_name)


@pytest.mark.order(100)
@allure.epic("SQL test")
@allure.feature("Operations Logging create DB on PostgreSQL")
@pytest.mark.testSQLAll
@pytest.mark.testSQL_PostgreSQL
@allure.story("тест создания бд с паролем 'saSA123#$%^&_+|" + "%:\./''''~-`<>'")
class TestCreatePostgreSQLOperationsLoggingDBWithSpecSymbol:
    @pytest.mark.parametrize(
        argnames="db_data_spec", argvalues=testdata_spec_symbol, ids=test_ids_spec
    )
    def test_create_operations_logging_postgresql_db_with_spec_symbols(
        self, handle_with_spec_symbol, db_data_spec
    ):
        with allure.step(
            "Время начала теста "
            + "("
            + str(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S") + ")")
        ):
            pass
        allure.dynamic.description(db_data_spec[5])
        [allure.dynamic.issue(i) for i in db_data_spec[6]]
        sql_serv_addr, port, username, password, db_name = db_data_spec[0:5]
        delete_postgres_DB(sql_serv_addr, port, username, password, db_name)
        app_win32 = Application(backend="win32").connect(
            path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
        )
        handle_with_spec_symbol.by(
            name="Включить журналирование действий аудиторов в консолях продуктов"
        ).set_focus()
        time.sleep(1)
        handle_with_spec_symbol.by(
            name="Включить журналирование действий аудиторов в консолях продуктов"
        ).capture_as_image().save(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "MSSQL",
                "screen_for_OperationsLogging.png",
            )
        )
        image1 = Path(
            get_project_root(),
            "pytest_DataCenter_functional",
            "test_SQL",
            "MSSQL",
            "screen_for_OperationsLogging.png",
        )
        image2 = Path(
            get_project_root(),
            "pytest_DataCenter_functional",
            "test_SQL",
            "example_OperationsLogging_checkbox.png",
        )
        time.sleep(3)
        if get_difference_between_checkbox_image(image1, image2) < 2:
            handle_with_spec_symbol.by(
                name=OperationsLoggingPage.enable_logging_of_auditors["title_ru"]
            ).click_input()
        else:
            handle_with_spec_symbol.by(
                name=OperationsLoggingPage.setup_connection_to_db["title_ru"]
            ).click()
        handle_win32 = app_win32.window(name_re="Параметры подключения к SQL*")
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox3").type_keys("p")
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox2").type_keys("^a{BACKSPACE}")
        time.sleep(2)
        handle_with_spec_symbol.by(
            name=OperationsLoggingPage.read_from_dc["title_ru"]
        ).click()
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox2").type_keys(f"{sql_serv_addr},{port}")
        time.sleep(2)
        handle_win32.__getattribute__("Edit0").type_keys("^a{BACKSPACE}")
        time.sleep(2)
        handle_win32.__getattribute__("Edit0").type_keys(
            r'saSA123#${%}{^}{&}_{+}|"' + r"{%}{:}\./''''{~}-`<>"
        )
        time.sleep(2)
        handle_win32.__getattribute__(
            "Использовать внутреннюю аутентификацию SQL ServerComboBox2"
        ).type_keys("^a{BACKSPACE}")
        time.sleep(2)
        handle_win32.__getattribute__(
            "Использовать внутреннюю аутентификацию SQL ServerComboBox2"
        ).type_keys(r"actionslog")
        time.sleep(2)
        handle_with_spec_symbol.by(
            name=OperationsLoggingPage.create_button["title_ru"]
        ).click()
        time.sleep(5)
        handle_with_spec_symbol.by(
            name=CommonElements.ok_button["title_ru"]
        ).__getattribute__(CommonElements.ok_button["attribute_ru"]).click()
        time.sleep(1)
        handle_with_spec_symbol.by(
            name=OperationsLoggingPage.ok_button["title_ru"]
        ).click()
        time.sleep(2)
        try:
            handle_win32.close()
            print("Не закрылось окно настройки SQL")
        except Exception:
            print("Создание настройки подключения прошло успешно")
        time.sleep(2)
        handle_with_spec_symbol.by(
            name=OperationsLoggingPage.apply_button["title_ru"]
        ).click()
        start_time = time.time()
        while time.time() - start_time < 120:
            try:
                exist_db = sqlalchemy_utils.functions.database_exists(
                    f"postgresql://{username}:{password}@{sql_serv_addr}:{port}/{db_name}"
                )
                if not exist_db:
                    time.sleep(10)
                    continue
                else:
                    logging.info("БД Operations Logging создана")
                    break
            except Exception as ex:
                logging.debug(ex)
        with check.check:
            assert_that(exist_db).described_as("Нет БД").is_true()
        if exist_db is True:
            start_time = time.time()
            while time.time() - start_time < 120:
                try:
                    engine = create_engine(
                        f"postgresql://{username}:{password}@{sql_serv_addr}:{port}/{db_name}"
                    )
                    list_of_tables = inspect(engine).get_table_names()
                    if not list_of_tables:
                        time.sleep(10)
                        continue
                    if len(list_of_tables) < 8:
                        time.sleep(10)
                    else:
                        logging.info("Корректное кол-во таблиц в БД Operations Logging")
                        break
                except Exception as ex:
                    logging.debug(ex)
            with check.check:
                assert_that(list_of_tables).described_as(
                    "Нет таблиц по умолчанию"
                ).is_equal_to(operations_logging_postgresql)
        delete_postgres_DB(sql_serv_addr, port, username, password, db_name)
