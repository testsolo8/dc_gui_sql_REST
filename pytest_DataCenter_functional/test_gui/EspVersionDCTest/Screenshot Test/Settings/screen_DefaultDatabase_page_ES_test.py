# Standart libraries
import time

# Third party packages
import allure
import pyautogui
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import DefaultDatabasePage
from DataCenter.locators.confidence import LevelOfConfidence
from DataCenter.locators.path_to_screenshots import PathToScreenshotsES
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.fixture(scope="class")
def handle_add_server(start_screen_test_page_es):
    send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
    app = start_screen_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DefaultDatabasePage.add_button["title_es"]).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_edit_server(start_screen_test_page_es):
    send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
    app = start_screen_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DefaultDatabasePage.edit_button["title_es"]).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_delete_server(start_screen_test_page_es):
    send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
    app = start_screen_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DefaultDatabasePage.delete_button["title_es"]).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("ESP Screenshot Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestScreensES
@pytest.mark.testGUI_EspVersionDCTest_ScreensTest_Settings
class TestDefaultDatabasePage:
    @allure.story("тест главного окна настройки БД по умолчанию")
    class TestDefaultDatabaseMainPage:
        def test_default_database_screen(self, start_screen_test_page_es):
            send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
            time.sleep(2)
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsES.default_database["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна добавления сервера на закладке настройки БД по умолчанию")
    class TestDefaultDatabaseAddServerWindow:
        def test_default_database_add_server_window(self, handle_add_server):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsES.default_database_add_server_window["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story(
        "тест окна редактирования сервера на закладке настройки БД по умолчанию"
    )
    class TestDefaultDatabaseEditServerWindow:
        def test_default_database_edit_server_window(self, handle_edit_server):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsES.default_database_edit_server_window["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна удаления сервера на закладке настройки БД по умолчанию")
    class TestDefaultDatabaseDeleteServerWindow:
        def test_handle_delete_server(self, handle_delete_server):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsES.default_database_delete_server_window["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))
