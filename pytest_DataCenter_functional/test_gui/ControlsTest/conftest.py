# Standart libraries
import logging
import time

# Third party packages
import psutil
import pytest
from pywinauto import Application


@pytest.fixture(scope="session", params=["eng", "es", "rus"], ids=["english version", "spanish version", "russian version"])
def lang_parametrize(request):
    return request.param


@pytest.fixture(scope="session")
def title_key(lang_parametrize):
    return f"title_{lang_parametrize}"


@pytest.fixture(scope="session")
def attribute_key(lang_parametrize):
    return f"attribute_{lang_parametrize}"


@pytest.fixture(scope="module")
def start_test_page(lang_parametrize):
    # Check if DCClient.exe is open
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            if proc.name() == "DCClient.exe":
                proc.kill()
        except Exception as ex:
            logging.debug(ex)
    # Start DCClient.exe
    app = Application().start(
        cmd_line=f"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe -L={lang_parametrize}",
        timeout=5,
    )
    app = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    main_dlg = app.window(name_re=".*Dcclient.*", found_index=0)
    main_dlg.find(timeout=120, retry_interval=2).wait_visible(timeout=120, retry_interval=2)
    time.sleep(2)
    main_dlg.OK.click()
    main_win = app.window(name_re="DataCenter*")
    main_win.find(timeout=120, retry_interval=2).wait_visible(timeout=120, retry_interval=2)
    # # Максимизация окна (занимает время)
    main_win.maximize()
    time.sleep(2)
    app = Application(backend="uia").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    yield app
    # Закрытие клиента DC
    app.kill()
