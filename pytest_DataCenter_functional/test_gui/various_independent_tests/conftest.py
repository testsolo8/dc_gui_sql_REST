# Standart libraries
import logging
import time

# Third party packages
import psutil
import pytest
from pywinauto import Application


@pytest.fixture(scope="module")
def start_test_page_en():
    # Check if DCClient.exe is open
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            if proc.name() == "DCClient.exe":
                proc.kill()
        except Exception as ex:
            logging.debug(ex)
    # Start DCClient.exe
    app = Application().start(
        cmd_line=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe -L=ENG",
        timeout=5,
    )
    app = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    main_dlg = app.window(name_re=".*Dcclient.*", found_index=0)
    main_dlg.find(timeout=120, retry_interval=2).wait_visible(
        timeout=120, retry_interval=2
    )
    time.sleep(2)
    main_dlg.OK.click()
    main_win = app.window(name_re="DataCenter*")
    main_win.find(timeout=120, retry_interval=2).wait_visible(
        timeout=120, retry_interval=2
    )
    # # Максимизация окна (занимает время)
    main_win.maximize()
    time.sleep(2)
    app = Application(backend="uia").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    yield app
    # Закрытие клиента DC
    app.kill()

@pytest.fixture(scope="module")
def start_test_page_ru():
    # Check if DCClient.exe is open
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            if proc.name() == "DCClient.exe":
                proc.kill()
        except Exception as ex:
            logging.debug(ex)
    # Start DCClient.exe
    app = Application().start(
        cmd_line=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe -L=RUS",
        timeout=5,
    )
    app = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    main_dlg = app.window(name_re=".*Dcclient.*", found_index=0)
    main_dlg.find(timeout=120, retry_interval=2).wait_visible(
        timeout=120, retry_interval=2
    )
    time.sleep(2)
    main_dlg.OK.click()
    main_win = app.window(name_re="DataCenter*")
    main_win.find(timeout=120, retry_interval=2).wait_visible(
        timeout=120, retry_interval=2
    )
    # # Максимизация окна (занимает время)
    main_win.maximize()
    time.sleep(2)
    app = Application(backend="uia").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    yield app
    # Закрытие клиента DC
    app.kill()
