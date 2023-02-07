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
@allure.feature("Additional features")
@pytest.mark.testGUI_TestScreensES
@pytest.mark.testGUI_EspVersionDCTest_ScreensTest_Additionalfeatures
@allure.story("тест главного окна настройки цифровых отпечатков")
class TestDigitalFingerprintsPage:
    def test_digital_fingerprints_page_screen(self, start_screen_test_page_es):
        send_keys("{VK_MENU down}Y4Y03{VK_MENU up}")
        time.sleep(2)
        screenshot = pyautogui.locateOnScreen(
            PathToScreenshotsES.digital_fingerprints["path"],
            confidence=LevelOfConfidence.confidence["confidence"],
        )
        make_screenshot_if_error(check.is_not_none(screenshot))
