# Standart libraries
import datetime
import logging
import time

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
from DataCenter.buttons import ProfileCenterSettingsPage, CommonElements
from pytest_DataCenter_functional.test_SQL.sql_tools import Docker, delete_mssql_DB
from pytest_DataCenter_functional.test_SQL.tables_templates import profile_mssql

testdata = [
    (
        "192.168.1.12,1422",
        "sa",
        "Passw0rd",
        "ProfileCenter",
        "Тест проходил на MSSQL 2022",
        [],
    ),
    (
        "192.168.1.12,1419",
        "sa",
        "Passw0rd",
        "ProfileCenter",
        "Тест проходил на MSSQL 2019",
        [],
    ),
    (
        "192.168.1.12,1417",
        "sa",
        "Passw0rd",
        "ProfileCenter",
        "Тест проходил на MSSQL 2017",
        [],
    ),
]
testdata_spec_symbol = [
    (
        "192.168.1.12,14222",
        "sa",
        r'saSA123#$%^&_+|"' + r"%:\./''''~-`<>",
        "ProfileCenter",
        "Тест проходил на MSSQL 2022",
        [],
    ),
    (
        "192.168.1.12,14199",
        "sa",
        r'saSA123#$%^&_+|"' + r"%:\./''''~-`<>",
        "ProfileCenter",
        "Тест проходил на MSSQL 2019",
        [],
    ),
    (
        "192.168.1.12,14177",
        "sa",
        r'saSA123#$%^&_+|"' + r"%:\./''''~-`<>",
        "ProfileCenter",
        "Тест проходил на MSSQL 2017",
        [],
    ),
]

test_ids = ["{}, {}, {}".format(t[0], t[1], t[3]) for t in testdata]
test_ids_spec = ["{}, {}, {}".format(t[0], t[1], t[3]) for t in testdata_spec_symbol]


@pytest.fixture(scope="class")
def handle(sql_test_page_ru):
    # Docker().start_mssql()
    time.sleep(5)
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = sql_test_page_ru
    handle = app.window(name_re="DataCenter*")
    time.sleep(2)
    yield handle
    # Docker().stop_mssql()


@pytest.fixture(scope="class")
def handle_with_spec_symbol(sql_test_page_ru):
    # Docker().start_mssql_spec()
    time.sleep(5)
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = sql_test_page_ru
    handle = app.window(name_re="DataCenter*")
    time.sleep(2)
    yield handle
    # Docker().stop_mssql_spec()


@pytest.mark.order(100)
@allure.epic("SQL test")
@allure.feature("Profile create DB on MSSQL")
@pytest.mark.testSQLAll
@pytest.mark.testSQL_MSSQL
@allure.story("тест создания бд с паролем 'Passw0rd'")
class TestCreateMSSQLProfileDB:
    @pytest.mark.parametrize(argnames="db_data", argvalues=testdata, ids=test_ids)
    def test_create_profile_db(self, handle, db_data):
        with allure.step(
            "Время начала теста "
            + "("
            + str(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S") + ")")
        ):
            pass
        allure.dynamic.description(db_data[4])
        [allure.dynamic.issue(i) for i in db_data[5]]
        sql_serv_addr, username, password, db_name = db_data[0:4]
        delete_mssql_DB(sql_serv_addr, username, password, db_name)
        app_win32 = Application(backend="win32").connect(
            path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
        )
        handle_win32 = app_win32.window(name_re="Параметры подключения к SQL*")
        handle.by(
            name=ProfileCenterSettingsPage.setup_connection_to_db["title_ru"]
        ).click()
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox3").type_keys("m")
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox2").type_keys("^a{BACKSPACE}")
        time.sleep(2)
        handle.by(name=ProfileCenterSettingsPage.read_from_dc["title_ru"]).click()
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox2").type_keys(sql_serv_addr)
        time.sleep(2)
        handle.by(name=ProfileCenterSettingsPage.create_button["title_ru"]).click()
        time.sleep(5)
        handle.by(name=CommonElements.ok_button["title_ru"]).__getattribute__(
            CommonElements.ok_button["attribute_ru"]
        ).click()
        time.sleep(1)
        handle.by(name=ProfileCenterSettingsPage.ok_button["title_ru"]).click()
        time.sleep(2)
        try:
            handle_win32.close()
            print("Не закрылось окно настройки SQL")
        except Exception:
            print("Создание настройки подключения прошло успешно")
        time.sleep(2)
        handle.by(name=ProfileCenterSettingsPage.apply_button["title_ru"]).click()
        start_time = time.time()
        while time.time() - start_time < 120:
            try:
                connectionStr = (
                    "DRIVER={ODBC Driver 17 for SQL Server};"
                    + f"SERVER={sql_serv_addr};DATABASE=master;UID={username};PWD={password}"
                )
                with pyodbc.connect(connectionStr, autocommit=True) as cursor:
                    sqlMask = (
                        f"SELECT NAME FROM sys.sysdatabases WHERE name LIKE '{db_name}'"
                    )
                    rows = [row.NAME for row in cursor.execute(sqlMask).fetchall()]
                    logging.debug(f"Row {rows}")
                    if not rows:
                        time.sleep(10)
                        continue
                    else:
                        logging.info("БД Profile создана")
                        break
            except Exception as ex:
                logging.debug(ex)
        with check.check:
            assert_that(rows).described_as("Нет БД").contains(db_name)
        start_time = time.time()
        while time.time() - start_time < 120:
            try:
                engine = create_engine(
                    f"mssql+pyodbc://{username}:{password}@{sql_serv_addr}/{db_name}?driver=ODBC+Driver+17+for+SQL+Server"
                )
                list_of_tables = inspect(engine).get_table_names()
                if not list_of_tables:
                    time.sleep(10)
                    continue
                if len(list_of_tables) < 10:
                    time.sleep(10)
                else:
                    logging.info("Корректное кол-во таблиц в БД Profile")
                    break
            except Exception as ex:
                logging.debug(ex)
        with check.check:
            assert_that(list_of_tables).described_as(
                "Нет таблиц по умолчанию"
            ).is_equal_to(profile_mssql)
        delete_mssql_DB(sql_serv_addr, username, password, db_name)


@pytest.mark.order(100)
@allure.epic("SQL test")
@allure.feature("Profile create DB on MSSQL")
@pytest.mark.testSQLAll
@pytest.mark.testSQL_MSSQL
@allure.story("тест создания бд с паролем 'saSA123#$%^&_+|" + "%:\./''''~-`<>'")
class TestCreateMSSQLProfileDBWithSpecSymbol:
    @pytest.mark.parametrize(
        argnames="db_data_spec", argvalues=testdata_spec_symbol, ids=test_ids_spec
    )
    def test_create_profile_db_with_spec_symbols(
        self, handle_with_spec_symbol, db_data_spec
    ):
        with allure.step(
            "Время начала теста "
            + "("
            + str(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S") + ")")
        ):
            pass
        allure.dynamic.description(db_data_spec[4])
        [allure.dynamic.issue(i) for i in db_data_spec[5]]
        sql_serv_addr, username, password, db_name = db_data_spec[0:4]
        delete_mssql_DB(sql_serv_addr, username, password, db_name)
        app_win32 = Application(backend="win32").connect(
            path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
        )
        handle_win32 = app_win32.window(name_re="Параметры подключения к SQL*")
        handle_with_spec_symbol.by(
            name=ProfileCenterSettingsPage.setup_connection_to_db["title_ru"]
        ).click()
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox3").type_keys("m")
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox2").type_keys("^a{BACKSPACE}")
        time.sleep(2)
        handle_with_spec_symbol.by(
            name=ProfileCenterSettingsPage.read_from_dc["title_ru"]
        ).click()
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox2").type_keys(sql_serv_addr)
        time.sleep(2)
        handle_win32.__getattribute__("Edit0").type_keys("^a{BACKSPACE}")
        time.sleep(2)
        handle_win32.__getattribute__("Edit0").type_keys(
            r'saSA123#${%}{^}{&}_{+}|"' + r"{%}{:}\./''''{~}-`<>"
        )
        time.sleep(2)
        handle_with_spec_symbol.by(
            name=ProfileCenterSettingsPage.create_button["title_ru"]
        ).click()
        time.sleep(5)
        handle_with_spec_symbol.by(
            name=CommonElements.ok_button["title_ru"]
        ).__getattribute__(CommonElements.ok_button["attribute_ru"]).click()
        time.sleep(1)
        handle_with_spec_symbol.by(
            name=ProfileCenterSettingsPage.ok_button["title_ru"]
        ).click()
        time.sleep(2)
        try:
            handle_win32.close()
            print("Не закрылось окно настройки SQL")
        except Exception:
            print("Создание настройки подключения прошло успешно")
        time.sleep(2)
        handle_with_spec_symbol.by(
            name=ProfileCenterSettingsPage.apply_button["title_ru"]
        ).click()
        start_time = time.time()
        while time.time() - start_time < 120:
            try:
                connectionStr = (
                    "DRIVER={ODBC Driver 17 for SQL Server};"
                    + f"SERVER={sql_serv_addr};DATABASE=master;UID={username};PWD={password}"
                )
                with pyodbc.connect(connectionStr, autocommit=True) as cursor:
                    sqlMask = (
                        f"SELECT NAME FROM sys.sysdatabases WHERE name LIKE '{db_name}'"
                    )
                    rows = [row.NAME for row in cursor.execute(sqlMask).fetchall()]
                    logging.debug(f"Row {rows}")
                    if not rows:
                        time.sleep(10)
                        continue
                    else:
                        logging.info("БД Profile создана")
                        break
            except Exception as ex:
                logging.debug(ex)
        with check.check:
            assert_that(rows).described_as("Нет БД").contains(db_name)
        start_time = time.time()
        while time.time() - start_time < 120:
            try:
                engine = create_engine(
                    f"mssql+pyodbc://{username}:{password}@{sql_serv_addr}/{db_name}?driver=ODBC+Driver+17+for+SQL+Server"
                )
                list_of_tables = inspect(engine).get_table_names()
                if not list_of_tables:
                    time.sleep(10)
                    continue
                if len(list_of_tables) < 10:
                    time.sleep(10)
                else:
                    logging.info("Корректное кол-во таблиц в БД Profile")
                    break
            except Exception as ex:
                logging.debug(ex)
        with check.check:
            assert_that(list_of_tables).described_as(
                "Нет таблиц по умолчанию"
            ).is_equal_to(profile_mssql)
        delete_mssql_DB(sql_serv_addr, username, password, db_name)
