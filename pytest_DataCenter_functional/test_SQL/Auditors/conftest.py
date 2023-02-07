# Standart libraries
import time

# Third party packages
import pytest
from pywinauto import Application
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.services import Services
from DataCenter.settingsXML import SettingsXML
from pytest_DataCenter_functional.test_SQL.Auditors.auditors_tools import (
    change_regkey_to_win_auth, start_dc,
)
from pytest_DataCenter_functional.test_SQL.sql_tools import save_start_db_name, return_start_db_data


@pytest.fixture(scope="function")
def start_test_page_for_auditor():
    app, app_win32 = start_dc()
    yield app, app_win32
    # Закрытие клиента DC
    app_win32 = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    app_win32.kill()
    Services().DC_stop()
    change_regkey_to_win_auth()
    with SettingsXML(
            "C:\\ProgramData\\Searchinform\\Searchinform DataCenter\\Settings.xml"
    ) as S1:
        S1.active_state(False)
    Services().DC_start()
    time.sleep(10)


@pytest.fixture(scope="session")
def save_and_repair_main_db_name():
    app, app_win32 = start_dc()
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    handle = app.window(name_re="DataCenter*")
    time.sleep(2)
    # сохраняем текущее имя бд
    handle_win32, start_db_name = save_start_db_name(handle)
    yield app, app_win32
    app, app_win32 = start_dc()
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    time.sleep(2)
    handle = app.window(name_re="DataCenter*")
    handle_win32 = app_win32.window(name_re="Параметры подключения к SQL*")
    return_start_db_data(handle, handle_win32, start_db_name)
    time.sleep(20)
    app.kill()





