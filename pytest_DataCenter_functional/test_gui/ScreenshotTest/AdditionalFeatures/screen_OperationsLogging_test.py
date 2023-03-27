# Standart libraries
import time

# Third party packages
import allure
import pytest
import pywinauto.mouse as mouse
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.tools.take_screen import take_screenshot_with_elements


@pytest.mark.order(2)
@allure.epic("Screenshot Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestScreens
@pytest.mark.testGUI_DCTest_ScreensTest_Additionalfeatures
@allure.story("тест главного окна настройки журналирования операций")
class TestOperationsLoggingPage:
    def test_operations_logging_screen(self, start_screen_test_page, assert_snapshot):
        send_keys("{VK_MENU down}Y4Y01{VK_MENU up}")
        time.sleep(2)
        mouse.move(coords=(0, 0))
        app = start_screen_test_page
        window = app.window(name_re="DataCenter*")
        time.sleep(1)
        elements = [
            {"name": "TitleBar", "element": window.TitleBar},
        ]
        screenshot = take_screenshot_with_elements(window, elements=elements)
        assert_snapshot(screenshot)
