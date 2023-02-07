# Standart libraries
import time

# Third party packages
import allure
import pyautogui
import pytest
import pytest_check as check
from pywinauto import Application
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.locators.confidence import LevelOfConfidence
from DataCenter.locators.path_to_screenshots import PathToScreenshotsRU
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.mark.order(2)
@allure.epic("RUS Screenshot Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestScreensRU
@pytest.mark.testGUI_RusVersionDCTest_ScreensTest_Settings
@allure.story("тест главного окна настройки сервера DataCenter")
class TestDataCenterServerPage:
    def test_data_center_server_screen(self, start_screen_test_page_ru):
        send_keys("{VK_MENU down}Y3Y1{VK_MENU up}")
        time.sleep(2)
        time.sleep(2)
        app = Application(backend="uia").connect(
            path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
        )
        handle = app.window(name_re="DataCenter*")
        handle.by(name="12").click_input()
        screenshot = pyautogui.locateOnScreen(
            PathToScreenshotsRU.data_center_server["path"],
            confidence=LevelOfConfidence.confidence["confidence"],
        )
        make_screenshot_if_error(check.is_not_none(screenshot))
