# Standart libraries
import datetime
import logging
import time
from pathlib import Path

# Third party packages
import allure
import pytest
import pytest_check as check
import sqlalchemy_utils
from assertpy import assert_that
from pywinauto import Application
from pywinauto.keyboard import send_keys
from sqlalchemy import create_engine, inspect

# My packages
from DataCenter.buttons import AttributesStoragePage, CommonElements
from DataCenter.tools.get_project_root import get_project_root
from DataCenter.tools.take_image_difference import get_difference_between_checkbox_image
from pytest_DataCenter_functional.test_SQL.sql_tools import Docker, delete_postgres_DB
from pytest_DataCenter_functional.test_SQL.tables_templates import (
    attributes_storage_postgresql,
)

testdata = [
    (
        "192.168.1.12",
        "5411",
        "postgres",
        "Passw0rd",
        "digestattribute",
        "Тест проходил на PostgreSQL ver.11",
        [],
    ),
    (
        "192.168.1.12",
        "5412",
        "postgres",
        "Passw0rd",
        "digestattribute",
        "Тест проходил на PostgreSQL ver.12",
        [],
    ),
    (
        "192.168.1.12",
        "5413",
        "postgres",
        "Passw0rd",
        "digestattribute",
        "Тест проходил на PostgreSQL ver.13",
        [],
    ),
    (
        "192.168.1.12",
        "5414",
        "postgres",
        "Passw0rd",
        "digestattribute",
        "Тест проходил на PostgreSQL ver.14",
        [],
    ),
    (
        "192.168.1.12",
        "5415",
        "postgres",
        "Passw0rd",
        "digestattribute",
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
        "digestattribute",
        "Тест проходил на PostgreSQL ver.11",
        [],
    ),
    (
        "192.168.1.12",
        "54122",
        "postgres",
        r'saSA123#$%^&_+|"' + r"%:\./''''~-`<>",
        "digestattribute",
        "Тест проходил на PostgreSQL ver.12",
        [],
    ),
    (
        "192.168.1.12",
        "54133",
        "postgres",
        r'saSA123#$%^&_+|"' + r"%:\./''''~-`<>",
        "digestattribute",
        "Тест проходил на PostgreSQL ver.13",
        [],
    ),
    (
        "192.168.1.12",
        "54144",
        "postgres",
        r'saSA123#$%^&_+|"' + r"%:\./''''~-`<>",
        "digestattribute",
        "Тест проходил на PostgreSQL ver.14",
        ["https://jira.searchinform.ru/browse/DC-5582"],
    ),
    (
        "192.168.1.12",
        "54155",
        "postgres",
        r'saSA123#$%^&_+|"' + r"%:\./''''~-`<>",
        "digestattribute",
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
    send_keys("{VK_MENU down}Y4Y08{VK_MENU up}")
    app = sql_test_page_ru
    handle = app.window(name_re="DataCenter*")
    time.sleep(2)
    yield handle
    # Docker().stop_postgresql()


@pytest.fixture(scope="class")
def handle_with_spec_symbol(sql_test_page_ru):
    # Docker().start_postgresql_spec()
    time.sleep(5)
    send_keys("{VK_MENU down}Y4Y08{VK_MENU up}")
    app = sql_test_page_ru
    handle = app.window(name_re="DataCenter*")
    time.sleep(2)
    yield handle
    # Docker().stop_postgresql_spec()


@pytest.mark.order(100)
@allure.epic("SQL test")
@allure.feature("Attribute Storage create DB on PostgreSQL")
@pytest.mark.testSQLAll
@pytest.mark.testSQL_PostgreSQL
@allure.story("тест создания бд с паролем 'Passw0rd'")
class TestCreatePostgreSQLAttributeStorageDB:
    @pytest.mark.parametrize(argnames="db_data", argvalues=testdata, ids=test_ids)
    def test_create_attributes_storage_postgresql_db(self, handle, db_data):
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
        handle.by(name="Использовать хранилище атрибутов").set_focus()
        time.sleep(1)
        handle.by(name="Использовать хранилище атрибутов").capture_as_image().save(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "PostgreSQL",
                "screen_for_AttributesStorage.png",
            )
        )
        image1 = Path(
            get_project_root(),
            "pytest_DataCenter_functional",
            "test_SQL",
            "PostgreSQL",
            "screen_for_AttributesStorage.png",
        )
        image2 = Path(
            get_project_root(),
            "pytest_DataCenter_functional",
            "test_SQL",
            "example_AttributesStorage_checkbox.png",
        )
        time.sleep(3)
        if get_difference_between_checkbox_image(image1, image2) < 2:
            handle.by(
                name=AttributesStoragePage.use_storage_of_attributes["title_ru"]
            ).click_input()
        handle.by(name=AttributesStoragePage.setup_connection_to_db["title_ru"]).click()
        handle_win32 = app_win32.window(name_re="Параметры подключения к SQL*")
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox3").type_keys("p")
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox2").type_keys("^a{BACKSPACE}")
        time.sleep(2)
        handle.by(name=AttributesStoragePage.read_from_dc["title_ru"]).click()
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox2").type_keys(f"{sql_serv_addr},{port}")
        time.sleep(2)
        handle.by(name=AttributesStoragePage.create_button["title_ru"]).click()
        time.sleep(5)
        handle.by(name=CommonElements.ok_button["title_ru"]).__getattribute__(
            CommonElements.ok_button["attribute_ru"]
        ).click()
        time.sleep(1)
        handle.by(name=AttributesStoragePage.ok_button["title_ru"]).click()
        time.sleep(2)
        try:
            handle_win32.close()
            print("Не закрылось окно настройки SQL")
        except Exception:
            print("Создание настройки подключения прошло успешно")
        time.sleep(2)
        handle.by(name=AttributesStoragePage.apply_button["title_ru"]).click()
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
                    logging.info("БД Attribute Storage создана")
                    break
            except Exception as ex:
                logging.debug(ex)
        with check.check:
            assert_that(exist_db).described_as("Нет БД").is_true()
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
                    logging.info("Корректное кол-во таблиц в БД Attribute Storage")
                    break
            except Exception as ex:
                logging.debug(ex)
        with check.check:
            assert_that(list_of_tables).described_as(
                "Нет таблиц по умолчанию"
            ).is_equal_to(attributes_storage_postgresql)
        delete_postgres_DB(sql_serv_addr, port, username, password, db_name)


@pytest.mark.order(100)
@allure.epic("SQL test")
@allure.feature("Attribute Storage create DB on PostgreSQL")
@pytest.mark.testSQLAll
@pytest.mark.testSQL_PostgreSQL
@allure.story("тест создания бд с паролем 'saSA123#$%^&_+|" + "%:\./''''~-`<>'")
class TestCreatePostgreSQLAttributeStorageDBWithSpecSymbol:
    @pytest.mark.parametrize(
        argnames="db_data_spec", argvalues=testdata_spec_symbol, ids=test_ids_spec
    )
    def test_create_attributes_storage_postgresql_db_with_spec_symbols(
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
        handle_with_spec_symbol.by(name="Использовать хранилище атрибутов").set_focus()
        time.sleep(1)
        handle_with_spec_symbol.by(
            name="Использовать хранилище атрибутов"
        ).capture_as_image().save(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "PostgreSQL",
                "screen_for_AttStor.png",
            )
        )
        image1 = Path(
            get_project_root(),
            "pytest_DataCenter_functional",
            "test_SQL",
            "PostgreSQL",
            "screen_for_AttStor.png",
        )
        image2 = Path(
            get_project_root(),
            "pytest_DataCenter_functional",
            "test_SQL",
            "example_AttributesStorage_checkbox.png",
        )
        time.sleep(3)
        if get_difference_between_checkbox_image(image1, image2) < 2:
            handle_with_spec_symbol.by(
                name=AttributesStoragePage.use_storage_of_attributes["title_ru"]
            ).click_input()
        handle_with_spec_symbol.by(
            name=AttributesStoragePage.setup_connection_to_db["title_ru"]
        ).click()
        handle_win32 = app_win32.window(name_re="Параметры подключения к SQL*")
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox3").type_keys("p")
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox2").type_keys("^a{BACKSPACE}")
        time.sleep(2)
        handle_with_spec_symbol.by(
            name=AttributesStoragePage.read_from_dc["title_ru"]
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
        handle_with_spec_symbol.by(
            name=AttributesStoragePage.create_button["title_ru"]
        ).click()
        time.sleep(5)
        handle_with_spec_symbol.by(
            name=CommonElements.ok_button["title_ru"]
        ).__getattribute__(CommonElements.ok_button["attribute_ru"]).click()
        time.sleep(1)
        handle_with_spec_symbol.by(
            name=AttributesStoragePage.ok_button["title_ru"]
        ).click()
        time.sleep(2)
        try:
            handle_win32.close()
            print("Не закрылось окно настройки SQL")
        except Exception:
            print("Создание настройки подключения прошло успешно")
        time.sleep(2)
        handle_with_spec_symbol.by(
            name=AttributesStoragePage.apply_button["title_ru"]
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
                    logging.info("БД Attribute Storage создана")
                    break
            except Exception as ex:
                logging.debug(ex)
        with check.check:
            assert_that(exist_db).described_as("Нет БД").is_true()
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
                    logging.info("Корректное кол-во таблиц в БД Attribute Storage")
                    break
            except Exception as ex:
                logging.debug(ex)
        with check.check:
            assert_that(list_of_tables).described_as(
                "Нет таблиц по умолчанию"
            ).is_equal_to(attributes_storage_postgresql)
        delete_postgres_DB(sql_serv_addr, port, username, password, db_name)
