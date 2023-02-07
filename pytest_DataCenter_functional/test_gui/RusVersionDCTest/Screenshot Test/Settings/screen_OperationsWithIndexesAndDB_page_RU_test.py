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
@allure.story("тест главного окна настройки операций над индексами и БД")
class TestOperationsWithIndexesAndDBPage:
    def test_operations_with_indexes_and_db_screen(self, start_screen_test_page_ru):
        send_keys("{VK_MENU down}Y3Y4{VK_MENU up}")
        time.sleep(2)
        screenshot = pyautogui.locateOnScreen(
            PathToScreenshotsRU.operations_with_indexes_and_db["path"],
            confidence=LevelOfConfidence.confidence["confidence"],
        )
        make_screenshot_if_error(check.is_not_none(screenshot))
