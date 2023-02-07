# Standart libraries
import logging
import time
import winreg
from pathlib import Path

import psutil
# Third party packages
import pyautogui
from pywinauto import Application

# My packages
from DataCenter.buttons import AccessRightsPage, ActiveDirectoryPage
from DataCenter.tools.get_project_root import get_project_root


def create_internal_user_admin():
    app = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle = app.window(name_re="Data*")
    handle.by(
        name=ActiveDirectoryPage.add_button["title_ru"],
        found_index=ActiveDirectoryPage.add_button["found_index"],
    ).click_input()
    handle = app.window(name_re="Добавить пользователя")
    time.sleep(2)
    handle.__getattribute__("Edit6").type_keys("admin")  # Username
    time.sleep(2)
    handle.__getattribute__("Edit5").type_keys("admin")  # User
    time.sleep(2)
    handle.__getattribute__("Edit4").type_keys(
        "{VK_SHIFT down}" "p" "{VK_SHIFT up}" "assw0rd"
    )  # Password
    time.sleep(2)
    handle.__getattribute__("Edit3").type_keys(
        "{VK_SHIFT down}" "p" "{VK_SHIFT up}" "assw0rd"
    )  # Confirm password
    time.sleep(2)
    handle.__getattribute__("OKButton").click()
    time.sleep(5)
    handle = app.window(name_re="Data*")
    handle.by(name=ActiveDirectoryPage.apply_button["title_ru"]).click()
    time.sleep(5)


def create_internal_cyrillic_user_admin():
    app = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle = app.window(name_re="Data*")
    handle.by(
        name=ActiveDirectoryPage.add_button["title_ru"],
        found_index=ActiveDirectoryPage.add_button["found_index"],
    ).click_input()
    handle = app.window(name_re="Добавить пользователя")
    time.sleep(2)
    handle.__getattribute__("Edit6").type_keys("админ")  # Username
    time.sleep(2)
    handle.__getattribute__("Edit5").type_keys("админ")  # User
    time.sleep(2)
    handle.__getattribute__("Edit4").type_keys("админ")  # Password
    time.sleep(2)
    handle.__getattribute__("Edit3").type_keys("админ")  # Confirm password
    time.sleep(2)
    handle.__getattribute__("OKButton").click()
    time.sleep(5)
    handle = app.window(name_re="Data*")
    handle.by(name=ActiveDirectoryPage.apply_button["title_ru"]).click()
    time.sleep(5)


def create_internal_user_spec():
    app = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle = app.window(name_re="Data*")
    handle.by(
        name=ActiveDirectoryPage.add_button["title_ru"],
        found_index=ActiveDirectoryPage.add_button["found_index"],
    ).click_input()
    handle = app.window(name_re="Добавить пользователя")
    time.sleep(2)
    handle.__getattribute__("Edit6").type_keys("spec")  # Username
    time.sleep(2)
    handle.__getattribute__("Edit5").type_keys("spec")  # User
    time.sleep(2)
    handle.__getattribute__("Edit4").type_keys(
        r'saSA123#${%}{^}{&}_{+}|"' + r"{%}{:}\./''''{~}-`<>"
    )  # Password
    time.sleep(2)
    handle.__getattribute__("Edit3").type_keys(
        r'saSA123#${%}{^}{&}_{+}|"' + r"{%}{:}\./''''{~}-`<>"
    )  # Confirm password
    time.sleep(2)
    handle.__getattribute__("OKButton").click()
    time.sleep(5)
    handle = app.window(name_re="Data*")
    handle.by(name=ActiveDirectoryPage.apply_button["title_ru"]).click()
    time.sleep(5)


def add_admin_auditor():
    app = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle = app.window(name_re="Data*")
    handle.by(
        name=AccessRightsPage.enable_access_restrictions["title_ru"]
    ).click_input()
    add_button = pyautogui.locateOnScreen(
        str(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "Auditors",
                "ScreensForTest",
                "Add_button.png",
            )
        )
    )
    add_button_center = pyautogui.center(add_button)
    time.sleep(2)
    pyautogui.click(add_button_center)
    time.sleep(10)
    handle = app.window(name_re="Список*")
    handle.__getattribute__("Edit2").type_keys("ad")
    admin_button = pyautogui.locateOnScreen(
        str(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "Auditors",
                "ScreensForTest",
                "admin.png",
            )
        )
    )
    admin_button_center = pyautogui.center(admin_button)
    pyautogui.click(admin_button_center)
    pyautogui.move(0, 100)
    time.sleep(2)
    handle.__getattribute__("Button6").click()
    time.sleep(2)
    handle.__getattribute__("ПрименитьButton").click_input()
    time.sleep(2)
    shild_button = pyautogui.locateOnScreen(
        str(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "Auditors",
                "ScreensForTest",
                "shild.png",
            )
        )
    )
    shild_button_center = pyautogui.center(shild_button)
    pyautogui.click(shild_button_center)
    time.sleep(2)
    admin_list_button = pyautogui.locateOnScreen(
        str(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "Auditors",
                "ScreensForTest",
                "admin_list.png",
            )
        )
    )
    admin_list_button_center = pyautogui.center(admin_list_button)
    pyautogui.click(admin_list_button_center)
    time.sleep(2)
    handle = app.window(name_re="Data*")
    handle.by(name=AccessRightsPage.apply_button["title_ru"]).click_input()
    time.sleep(2)
    handle = app.window(name_re="Подтверд*")
    handle.__getattribute__("Да").click()
    time.sleep(5)


def add_cyrillic_admin_auditor():
    app = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle = app.window(name_re="Data*")
    handle.by(
        name=AccessRightsPage.enable_access_restrictions["title_ru"]
    ).click_input()
    add_button = pyautogui.locateOnScreen(
        str(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "Auditors",
                "ScreensForTest",
                "Add_button.png",
            )
        )
    )
    add_button_center = pyautogui.center(add_button)
    time.sleep(2)
    pyautogui.click(add_button_center)
    time.sleep(10)
    handle = app.window(name_re="Список*")
    handle.__getattribute__("Edit2").type_keys("ад")
    admin_cyrillic = pyautogui.locateOnScreen(
        str(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "Auditors",
                "ScreensForTest",
                "admin_cyrillic.png",
            )
        )
    )
    admin_cyrillic_center = pyautogui.center(admin_cyrillic)
    pyautogui.click(admin_cyrillic_center)
    pyautogui.move(0, 100)
    time.sleep(2)
    handle.__getattribute__("Button6").click()
    time.sleep(2)
    handle.__getattribute__("ПрименитьButton").click_input()
    time.sleep(2)
    shild_button = pyautogui.locateOnScreen(
        str(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "Auditors",
                "ScreensForTest",
                "shild.png",
            )
        ),
        confidence=0.9,
    )
    shild_button_center = pyautogui.center(shild_button)
    pyautogui.click(shild_button_center)
    time.sleep(2)
    admin_list_button = pyautogui.locateOnScreen(
        str(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "Auditors",
                "ScreensForTest",
                "admin_list.png",
            )
        )
    )
    admin_list_button_center = pyautogui.center(admin_list_button)
    pyautogui.click(admin_list_button_center)
    time.sleep(2)
    handle = app.window(name_re="Data*")
    handle.by(name=AccessRightsPage.apply_button["title_ru"]).click_input()
    time.sleep(2)
    handle = app.window(name_re="Подтверд*")
    handle.__getattribute__("Да").click()
    time.sleep(5)


def add_spec_auditor():
    app = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle = app.window(name_re="Data*")
    handle.by(
        name=AccessRightsPage.enable_access_restrictions["title_ru"]
    ).click_input()
    add_button = pyautogui.locateOnScreen(
        str(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "Auditors",
                "ScreensForTest",
                "Add_button.png",
            )
        )
    )
    add_button_center = pyautogui.center(add_button)
    time.sleep(2)
    pyautogui.click(add_button_center)
    time.sleep(10)
    handle = app.window(name_re="Список*")
    handle.__getattribute__("Edit2").type_keys("sp")
    spec_button = pyautogui.locateOnScreen(
        str(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "Auditors",
                "ScreensForTest",
                "spec.png",
            )
        )
    )
    spec_button_center = pyautogui.center(spec_button)
    pyautogui.click(spec_button_center)
    pyautogui.move(0, 100)
    time.sleep(2)
    handle.__getattribute__("Button6").click()
    time.sleep(2)
    handle.__getattribute__("ПрименитьButton").click_input()
    time.sleep(2)
    shild_button = pyautogui.locateOnScreen(
        str(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "Auditors",
                "ScreensForTest",
                "shild.png",
            )
        ),
        confidence=0.9,
    )
    shild_button_center = pyautogui.center(shild_button)
    pyautogui.click(shild_button_center)
    time.sleep(2)
    admin_list_button = pyautogui.locateOnScreen(
        str(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "Auditors",
                "ScreensForTest",
                "admin_list.png",
            )
        )
    )
    admin_list_button_center = pyautogui.center(admin_list_button)
    pyautogui.click(admin_list_button_center)
    time.sleep(2)
    handle = app.window(name_re="Data*")
    handle.by(name=AccessRightsPage.apply_button["title_ru"]).click_input()
    time.sleep(2)
    handle = app.window(name_re="Подтверд*")
    handle.__getattribute__("Да").click()
    time.sleep(5)


def change_regkey_to_win_auth():
    authWin = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"SOFTWARE\SearchInform",
        0,
        winreg.KEY_WOW64_64KEY | winreg.KEY_ALL_ACCESS,
    )
    winreg.SetValueEx(authWin, "Authentication", None, winreg.REG_DWORD, 0)


def start_dc():
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
    app_win32 = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    main_dlg = app_win32.window(name_re=".*Dcclient.*", found_index=0)
    main_dlg.find(timeout=240, retry_interval=5).wait_visible(
        timeout=240, retry_interval=5
    )
    time.sleep(2)
    main_dlg.OK.click()
    main_win = app_win32.window(name_re="DataCenter*")
    main_win.find(timeout=240, retry_interval=5).wait_visible(
        timeout=240, retry_interval=5
    )
    # # Максимизация окна
    main_win.maximize()
    time.sleep(2)
    app = Application(backend="uia").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    return app, app_win32
