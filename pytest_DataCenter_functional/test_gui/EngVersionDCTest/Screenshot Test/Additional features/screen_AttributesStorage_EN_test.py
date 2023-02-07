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
from DataCenter.locators.path_to_screenshots import PathToScreenshotsEN
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.mark.order(2)
@allure.epic("ENG Screenshot Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestScreensEN
@pytest.mark.testGUI_EngVersionDCTest_ScreensTest_Additionalfeatures
@allure.story("тест главного окна настройки хранилища атрибутов")
class TestAttributesStoragePage:
    def test_attributes_storage_page_screen(self, start_screen_test_page_en):
        send_keys("{VK_MENU down}Y4Y08{VK_MENU up}")
        time.sleep(2)
        screenshot = pyautogui.locateOnScreen(
            PathToScreenshotsEN.attributes_storage["path"],
            confidence=LevelOfConfidence.confidence["confidence"],
        )
        make_screenshot_if_error(check.is_not_none(screenshot))