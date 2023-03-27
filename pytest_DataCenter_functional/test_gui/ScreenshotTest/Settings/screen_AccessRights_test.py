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
@allure.feature("Settings")
@pytest.mark.testGUI_TestScreens
@pytest.mark.testGUI_DCTest_ScreensTest_Settings
@allure.story("тест главного окна настройки прав доступа")
class TestAccessRightsPage:
    def test_access_rights_screen(self, start_screen_test_page, assert_snapshot):
        send_keys("{VK_MENU down}Y3Y6{VK_MENU up}")
        time.sleep(7)
        mouse.move(coords=(0, 0))
        app = start_screen_test_page
        window = app.window(name_re="DataCenter*")
        time.sleep(1)
        elements = [
            {"name": "TitleBar", "element": window.TitleBar},
        ]
        screenshot = take_screenshot_with_elements(window, elements=elements)
        assert_snapshot(screenshot)
