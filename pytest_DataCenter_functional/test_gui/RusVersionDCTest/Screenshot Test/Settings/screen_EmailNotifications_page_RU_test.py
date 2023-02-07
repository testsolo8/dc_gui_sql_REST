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
from DataCenter.locators.path_to_screenshots import PathToScreenshotsRU
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.mark.order(2)
@allure.epic("RUS Screenshot Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestScreensRU
@pytest.mark.testGUI_RusVersionDCTest_ScreensTest_Settings
@allure.story("тест главного окна настройки почтовых уведомлений")
class TestEmailNotificationsPage:
    def test_email_notifications_screen(self, start_screen_test_page_ru):
        send_keys("{VK_MENU down}Y3Y7{VK_MENU up}")
        time.sleep(2)
        screenshot = pyautogui.locateOnScreen(
            PathToScreenshotsRU.email_notifications["path"],
            confidence=LevelOfConfidence.confidence["confidence"],
        )
        make_screenshot_if_error(check.is_not_none(screenshot))
