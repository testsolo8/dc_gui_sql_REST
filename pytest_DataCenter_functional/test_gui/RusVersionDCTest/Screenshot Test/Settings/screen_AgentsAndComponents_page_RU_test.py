# Standart libraries
import time

# Third party packages
import allure
import pyautogui
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import AgentsAndComponentsPage
from DataCenter.locators.confidence import LevelOfConfidence
from DataCenter.locators.path_to_screenshots import PathToScreenshotsRU
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.fixture(scope="class")
def handle_free_disk_space_monitoring_window(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y3Y3{VK_MENU up}")
    app = start_screen_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        AgentsAndComponentsPage.free_space_monitor_button
    ).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_change_mail_button(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y3Y3{VK_MENU up}")
    app = start_screen_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(AgentsAndComponentsPage.change_mail_button).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("RUS Screenshot Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestScreensRU
@pytest.mark.testGUI_RusVersionDCTest_ScreensTest_Settings
class TestAgentsAndComponentsPage:
    @allure.story("тест главного окна Agents and Components")
    class TestAgentsAndComponentsMainPage:
        def test_agents_and_components_screen(self, start_screen_test_page_ru):
            send_keys("{VK_MENU down}Y3Y3{VK_MENU up}")
            time.sleep(2)
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.agents_and_components["path"],
                confidence=LevelOfConfidence.confidence["reduced_confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story(
        "тест окна настройки мониторинга свободного места на дисках закладки Agents and Components"
    )
    class TestAgentsAndComponentsFreeDiskSpaceMonitoringWindow:
        def test_free_disk_space_monitoring_window(
            self, handle_free_disk_space_monitoring_window
        ):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.agents_and_components_free_disk_space_monitoring_window[
                    "path"
                ],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story(
        "тест окна индивидуальных настроек почты закладки Agents and Components"
    )
    class TestAgentsAndComponentsChangeMailWindow:
        def test_change_mail_button(self, handle_change_mail_button):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.agents_and_components_change_mail_window["path"],
                confidence=0.98,
            )
            make_screenshot_if_error(check.is_not_none(screenshot))
