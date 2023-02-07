# Standart libraries
import time

# Third party packages
import allure
import pyautogui
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import TaskManagementPage
from DataCenter.locators.confidence import LevelOfConfidence
from DataCenter.locators.path_to_screenshots import PathToScreenshotsEN
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.fixture(scope="class")
def handle_sql_server_connection_setting(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y07{VK_MENU up}")
    app = start_screen_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(name=TaskManagementPage.setup_connection_to_db["title_en"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("ENG Screenshot Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestScreensEN
@pytest.mark.testGUI_EngVersionDCTest_ScreensTest_Additionalfeatures
class TestTaskManagementPage:
    @allure.story("тест главного окна настройки TaskManagement")
    class TestTaskManagementMainPage:
        def test_task_management_page_screen(self, start_screen_test_page_en):
            send_keys("{VK_MENU down}Y4Y07{VK_MENU up}")
            time.sleep(2)
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.task_management["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна настройки подключения к БД TaskManagement")
    class TestSQLServerConnectionSettingWindow:
        def test_sql_server_connection_setting_screen(
            self, handle_sql_server_connection_setting
        ):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.task_management_sql_server_connection_setting_window[
                    "path"
                ],
                # confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))
