# Standart libraries
import time

# Third party packages
import allure
import pyautogui
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.locators.confidence import LevelOfConfidence
from DataCenter.locators.path_to_screenshots import PathToScreenshotsES
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.mark.order(2)
@allure.epic("ESP Screenshot Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestScreensES
@pytest.mark.testGUI_EspVersionDCTest_ScreensTest_Settings
@allure.story("тест главного окна настройки прав доступа")
class TestAccessRightsPage:
    def test_access_rights_screen(self, start_screen_test_page_es):
        send_keys("{VK_MENU down}Y3Y6{VK_MENU up}")
        time.sleep(7)
        screenshot = pyautogui.locateOnScreen(
            PathToScreenshotsES.access_rights["path"],
            confidence=LevelOfConfidence.confidence["confidence"],
        )
        make_screenshot_if_error(check.is_not_none(screenshot))
