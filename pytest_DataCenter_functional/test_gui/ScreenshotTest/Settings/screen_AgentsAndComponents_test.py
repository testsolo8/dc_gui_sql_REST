# Standart libraries
import time

# Third party packages
import allure
import pytest
import pywinauto.mouse as mouse
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import AgentsAndComponentsPage
from DataCenter.tools.take_screen import take_screenshot_with_elements

COORDINATES = {
    "eng": {
        "free_disk_space_monitoring_window": [
            {"element": {"left": 53, "top": 61, "right": 128, "bottom": 79}}
        ],
    },
    "es": {
        "free_disk_space_monitoring_window": [
            {"element": {"left": 53, "top": 61, "right": 128, "bottom": 79}},
        ],
    },
    "rus": {
        "free_disk_space_monitoring_window": [
            {"element": {"left": 52, "top": 61, "right": 145, "bottom": 79}},
        ],
    },
    "general": [
        {"element": {"left": 430, "top": 180, "right": 539, "bottom": 209}},
        {"element": {"left": 105, "top": 188, "right": 156, "bottom": 202}},
        {"element": {"left": 53, "top": 220, "right": 155, "bottom": 235}},
        {"element": {"left": 320, "top": 220, "right": 369, "bottom": 235}},
            ]
    }



@pytest.fixture(scope="class")
def handle_free_disk_space_monitoring_window(start_screen_test_page):
    send_keys("{VK_MENU down}Y3Y3{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(AgentsAndComponentsPage.free_space_monitor_button).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_change_mail_button(start_screen_test_page):
    send_keys("{VK_MENU down}Y3Y3{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(AgentsAndComponentsPage.change_mail_button).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("Screenshot Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestScreens
@pytest.mark.testGUI_DCTest_ScreensTest_Settings
class TestAgentsAndComponentsPage:
    @allure.story("тест главного окна Agents and Components")
    class TestAgentsAndComponentsMainPage:
        def test_agents_and_components_screen(self, start_screen_test_page, assert_snapshot):
            send_keys("{VK_MENU down}Y3Y3{VK_MENU up}")
            time.sleep(2)
            mouse.move(coords=(0, 0))
            app = start_screen_test_page
            window = app.window(name_re="DataCenter*")
            time.sleep(1)
            elements = [
                {"name": "TitleBar", "element": window.TitleBar},
            ]
            coordinates = COORDINATES.get("general")
            screenshot = take_screenshot_with_elements(window, elements=elements, coordinates=coordinates)
            assert_snapshot(screenshot)

    @allure.story("тест окна настройки мониторинга свободного места на дисках закладки Agents and Components")
    class TestAgentsAndComponentsFreeDiskSpaceMonitoringWindow:
        def test_free_disk_space_monitoring_window(self, handle_free_disk_space_monitoring_window, assert_snapshot, lang_parametrize):
            mouse.move(coords=(0, 0))
            handle = handle_free_disk_space_monitoring_window
            window = handle.Dialog2
            time.sleep(1)
            elements = [
                {"name": "TitleBar", "element": window.TitleBar},
            ]
            coordinates = COORDINATES.get(lang_parametrize).get("free_disk_space_monitoring_window")
            screenshot = take_screenshot_with_elements(window, elements=elements, coordinates=coordinates)
            assert_snapshot(screenshot)

    @allure.story("тест окна индивидуальных настроек почты закладки Agents and Components")
    class TestAgentsAndComponentsChangeMailWindow:
        def test_change_mail_button(self, handle_change_mail_button, assert_snapshot):
            mouse.move(coords=(0, 0))
            handle = handle_change_mail_button
            window = handle.Dialog2
            time.sleep(1)
            elements = [
                {"name": "TitleBar", "element": window.TitleBar},
            ]
            screenshot = take_screenshot_with_elements(window, elements=elements)
            assert_snapshot(screenshot)
