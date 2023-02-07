# Standart libraries
import datetime
import re
import time

# Third party packages
import allure
import pyodbc
import pytest
import pytest_check as check
from assertpy import assert_that
from pywinauto import Application
from pywinauto.keyboard import send_keys
from sqlalchemy import create_engine, inspect

# My packages
from DataCenter.buttons import ManagementPage, ActiveDirectoryPage, CommonElements
from pytest_DataCenter_functional.test_SQL.Auditors.auditors_tools import (
    add_admin_auditor,
    add_cyrillic_admin_auditor,
    add_spec_auditor,
    create_internal_cyrillic_user_admin,
    create_internal_user_admin,
    create_internal_user_spec,
)
from pytest_DataCenter_functional.test_SQL.sql_tools import save_start_db_name

testdata_cyrillic_auditor_admin = [
    (
        "192.168.1.12,1422",
        "sa",
        "Passw0rd",
        "datacenter_for_cyrillic_auditor_admin",
        "Тест проходил на MSSQL 2022",
        [],
    ),
    (
        "192.168.1.12,1419",
        "sa",
        "Passw0rd",
        "datacenter_for_cyrillic_auditor_admin",
        "Тест проходил на MSSQL 2019",
        [],
    ),
    (
        "192.168.1.12,1417",
        "sa",
        "Passw0rd",
        "datacenter_for_cyrillic_auditor_admin",
        "Тест проходил на MSSQL 2017",
        [],
    ),
]

test_ids = ["{}, {}, {}, {}".format(t[0], t[1], t[2], t[3]) for t in testdata_cyrillic_auditor_admin]

@pytest.mark.order(130)
@allure.epic("Auditor test")
@allure.feature("Create auditor 'админ' on MSSQL")
@pytest.mark.testAuditor
@pytest.mark.parametrize(argnames="db_data", argvalues=testdata_cyrillic_auditor_admin, ids=test_ids)
def test_add_cyrillic_auditor_admin_to_mssql_db(save_and_repair_main_db_name, start_test_page_for_auditor, db_data):
    with allure.step(
        "Время начала теста "
        + "("
        + str(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S") + ")")
    ):
        pass
    allure.dynamic.description(db_data[4])
    [allure.dynamic.issue(i) for i in db_data[5]]
    sql_serv_addr, username, password, db_name = db_data[0:4]
    app, app_win32 = start_test_page_for_auditor
    time.sleep(2)
    app_win32 = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle_win32 = app_win32.window(name_re="Параметры подключения к SQL*")
    handle = app.window(name_re="DataCenter*")
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    handle.by(name=ActiveDirectoryPage.setup_connection_db["title_ru"]).click()
    time.sleep(2)
    handle_win32.__getattribute__("ComboBox3").type_keys("m")
    time.sleep(2)
    handle_win32.__getattribute__("ComboBox2").type_keys("^a{BACKSPACE}")
    time.sleep(2)
    handle.by(name=ActiveDirectoryPage.read_from_dc["title_ru"]).click()
    time.sleep(2)
    handle_win32.__getattribute__("ComboBox2").type_keys(f"{sql_serv_addr}")
    time.sleep(2)
    handle_win32.__getattribute__(
        "Использовать внутреннюю аутентификацию SQL ServerComboBox2"
    ).type_keys(f"{db_name}")
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
    time.sleep(10)
    handle.by(name=ActiveDirectoryPage.apply_button["title_ru"]).click()
    time.sleep(5)
    handle.by(name=ActiveDirectoryPage.setup_connection_db["title_ru"]).click()
    time.sleep(2)
    handle.by(name=ActiveDirectoryPage.ok_button["title_ru"]).click()
    time.sleep(15)
    handle.by(name=ActiveDirectoryPage.apply_button["title_ru"]).click()
    time.sleep(3)
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    time.sleep(2)
    create_internal_cyrillic_user_admin()
    time.sleep(10)
    send_keys("{VK_MENU down}Y3Y6{VK_MENU up}")
    time.sleep(10)
    add_cyrillic_admin_auditor()
    app.kill()
    app = Application().start(
        cmd_line=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe -L=RUS",
        timeout=5,
    )
    app = Application(backend="uia").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    main_dlg = app["Dcclient"]
    main_dlg.find(timeout=240, retry_interval=5).wait_visible(
        timeout=240, retry_interval=5
    )
    time.sleep(1)
    main_dlg.__getattribute__("Edit2").type_keys("s")
    time.sleep(1)
    main_dlg.__getattribute__("Edit3").type_keys("админ")  # Login
    time.sleep(1)
    main_dlg.__getattribute__("Edit4").type_keys("админ")  # Password
    time.sleep(1)
    main_dlg.Button2.click()
    main_win = app.window(name_re="DataCenter*")
    main_win.find(timeout=240, retry_interval=5).wait_visible(
        timeout=240, retry_interval=5
    )
    main_win.maximize()
    time.sleep(2)
    synchronization_with_active_directory = (
        main_win.by(
            name=ManagementPage.synchronization_with_active_directory["title_ru"]
        )
        .find()
        .window_text()
    )
    assert_that(synchronization_with_active_directory).is_equal_to(
        "Синхронизация с Active Directory"
    )
    try:
        connectionStr = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            + f"SERVER={sql_serv_addr};DATABASE={db_name};UID={username};PWD={password}"
        )
        with pyodbc.connect(connectionStr, autocommit=True) as cursor:
            sqlMask = (
                f"DECLARE @id int = (SELECT TOP(1) obj_id FROM AD_ObjectAttributes WHERE userPrincipalName = 'admin@Internal.ISC');"
                f"EXEC DeleteExtraAgent @DeletedObjID = @id;"
            )
            cursor.execute(sqlMask)
    except(Exception):
        print("Было Exception")
        pass


