# Standart libraries
import datetime
import time

# Third party packages
import allure
import pytest
import pytest_check as check
import sqlalchemy_utils
from assertpy import assert_that, fail
from pywinauto import Application
from pywinauto.keyboard import send_keys
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

# My packages
from DataCenter.buttons import ActiveDirectoryPage, CommonElements
from DataCenter.DB_models.datacenter_db_models import AD_ObjectAttributes, ADObjectsList
from pytest_DataCenter_functional.test_SQL.sql_tools import (
    Docker,
    add_domain,
    delete_domain,
    delete_postgres_DB,
    return_start_db_data,
    save_start_db_name,
)

testdata = [
    (
        "192.168.1.12",
        "5412",
        "postgres",
        "Passw0rd",
        "datacenter",
        "Тест проходил на PostgreSQL ver.12",
        [],
    ),
    (
        "192.168.1.12",
        "5413",
        "postgres",
        "Passw0rd",
        "datacenter",
        "Тест проходил на PostgreSQL ver.13",
        [],
    ),
    (
        "192.168.1.12",
        "5414",
        "postgres",
        "Passw0rd",
        "datacenter",
        "Тест проходил на PostgreSQL ver.14",
        [],
    ),
    (
        "192.168.1.12",
        "5415",
        "postgres",
        "Passw0rd",
        "datacenter",
        "Тест проходил на PostgreSQL ver.15",
        [],
    ),
]

test_ids = ["{}, {}, {}, {}, {}".format(t[0], t[1], t[2], t[3], t[4]) for t in testdata]


@pytest.fixture(scope="class")
def handle(sql_test_page_ru):
    # Docker().start_postgresql()
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = sql_test_page_ru
    handle = app.window(name_re="DataCenter*")
    app_win32 = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    try:
        if handle.by(name="autotest.lan", control_type="ListItem"):
            delete_domain(app_win32, handle)
            print("Домен удален")
    except Exception:
        print("Домена не было")
    time.sleep(2)
    # сохраняем текущее имя бд
    handle_win32, start_db_name = save_start_db_name(handle)
    # добавляем домен
    app_win32 = add_domain(handle)
    yield handle
    # восстанавливаем первоначальные настройки бд дц
    return_start_db_data(handle, handle_win32, start_db_name)
    time.sleep(20)
    # удаляем домен
    delete_domain(app_win32, handle)
    time.sleep(5)
    # Docker().stop_postgresql()


@pytest.mark.order(120)
@allure.epic("Various independent tests")
@allure.feature("Add domain on PostgreSQL")
@pytest.mark.VariousIndependentTests_AddDomain
@allure.story("добавление домена к бд с паролем 'Passw0rd'")
class TestAddDomainToPostgreSQLDB:
    @pytest.mark.parametrize(argnames="db_data", argvalues=testdata, ids=test_ids)
    def test_add_domain_to_postgresql_db(self, handle, db_data):
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
        handle_win32 = app_win32.window(name_re="Параметры подключения к SQL*")
        handle.by(name=ActiveDirectoryPage.setup_connection_db["title_ru"]).click()
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox3").type_keys("p")
        time.sleep(1)
        try:
            handle_for_ok_button = app_win32.window(name_re="Предупреж*")
            handle_for_ok_button.__getattribute__("OKButton").click()
            print("Во время выбора типа бд был тип MSSQL")
        except Exception:
            print("Во время выбора типа бд был тип PostgreSQL")
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox2").type_keys("^a{BACKSPACE}")
        time.sleep(2)
        handle.by(name=ActiveDirectoryPage.read_from_dc["title_ru"]).click()
        time.sleep(2)
        handle_win32.__getattribute__("ComboBox2").type_keys(f"{sql_serv_addr},{port}")
        time.sleep(2)
        handle.by(name=ActiveDirectoryPage.create["title_ru"]).click()
        time.sleep(5)
        handle.by(name=CommonElements.ok_button["title_ru"]).__getattribute__(
            CommonElements.ok_button["attribute_ru"]
        ).click()
        time.sleep(1)
        handle.by(name=ActiveDirectoryPage.ok_button["title_ru"]).click()
        time.sleep(2)
        try:
            handle_win32.close()
            print("Не закрылось окно настройки SQL")
        except Exception:
            print("Создание настройки подключения прошло успешно")
        time.sleep(8)
        handle.by(name=ActiveDirectoryPage.apply_button["title_ru"]).click()
        time.sleep(120)
        if (
            sqlalchemy_utils.functions.database_exists(
                f"postgresql://{username}:{password}@{sql_serv_addr}:{port}/{db_name}"
            )
            is True
        ):
            engine = create_engine(
                f"postgresql://{username}:{password}@{sql_serv_addr}:{port}/{db_name}"
            )
            Session = sessionmaker(bind=engine)
            session = Session()
            count_rows_AD_ObjectAttributes = session.query(AD_ObjectAttributes).count()
            count_rows_AD_ADObjectsList = session.query(ADObjectsList).count()
            with check.check, allure.step(
                "сравнение кол-ва записей в таблицах AD_ObjectAttributes и ADObjectsList"
            ):
                assert_that(count_rows_AD_ObjectAttributes).described_as(
                    "Разное кол-во записей в таблицах (должно быть одинаковое)"
                ).is_equal_to(count_rows_AD_ADObjectsList)
            count_rows_AD_ADObjectsList = (
                session.query(ADObjectsList)
                .filter_by(obj_guid="{0034226E-077C-40A0-A789-40B07EDD35E5}")
                .all()
            )
            result_dict = [rec.__dict__ for rec in count_rows_AD_ADObjectsList]
            obj_displayName_SQL = result_dict[0]["obj_displayname"]
            with check.check, allure.step(
                "получение Obj_DisplayName компьютера на основании Obj_GUID"
            ):
                assert_that(obj_displayName_SQL).described_as(
                    "Не совпадает DisplayName компьютера"
                ).is_equal_to("SQL")
            count_rows_AD_ADObjectsList = (
                session.query(ADObjectsList)
                .filter_by(obj_guid="{5C305EA9-78E0-4B34-AD81-4116DB593DD6}")
                .all()
            )
            result_dict = [rec.__dict__ for rec in count_rows_AD_ADObjectsList]
            obj_displayName_sa = result_dict[0]["obj_displayname"]
            with check.check, allure.step(
                "получение Obj_DisplayName пользователя на основании Obj_GUID"
            ):
                assert_that(obj_displayName_sa).described_as(
                    "Не совпадает DisplayName пользователя"
                ).is_equal_to("sa")
            count_rows_AD_ObjectAttributes = (
                session.query(AD_ObjectAttributes)
                .filter_by(objectsid="S-1-5-21-4141237049-2453287432-1636914503-1106")
                .all()
            )
            result_dict = [rec.__dict__ for rec in count_rows_AD_ObjectAttributes]
            obj_displayName_DATACENTER = result_dict[0]["cn"]
            with check.check, allure.step(
                "получение cn компьютера на основании objectSid"
            ):
                assert_that(obj_displayName_DATACENTER).described_as(
                    "Не совпадает DisplayName компьютера"
                ).is_equal_to("DATACENTER")
            count_rows_AD_ObjectAttributes = (
                session.query(AD_ObjectAttributes)
                .filter_by(objectsid="S-1-5-21-4141237049-2453287432-1636914503-2607")
                .all()
            )
            result_dict = [rec.__dict__ for rec in count_rows_AD_ObjectAttributes]
            obj_displayName_dc_sync = result_dict[0]["cn"]
            with check.check, allure.step(
                "получение cn пользователя на основании objectSid"
            ):
                assert_that(obj_displayName_dc_sync).described_as(
                    "Не совпадает DisplayName пользователя"
                ).is_equal_to("dc_sync")
            session.close()
        else:
            fail("Нет БД")
        time.sleep(10)
        delete_postgres_DB(sql_serv_addr, port, username, password, db_name)
