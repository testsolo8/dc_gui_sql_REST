# Standart libraries
import time

# Third party packages
import allure
import pyautogui
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import ActiveDirectoryPage
from DataCenter.locators.confidence import LevelOfConfidence
from DataCenter.locators.path_to_screenshots import PathToScreenshotsRU
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.fixture(scope="class")
def handle_sql_connection_settings(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_screen_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=ActiveDirectoryPage.setup_connection_db["title_ru"]).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_add_domain(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_screen_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(
        name=ActiveDirectoryPage.synchronization_with_active_directory["title_ru"]
    ).__getattribute__("Button3").click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_add_workgroup_user(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_screen_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(
        name=ActiveDirectoryPage.add_button2["title_ru"],
        found_index=ActiveDirectoryPage.add_button2["found_index"],
    ).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_add_internal_user(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_screen_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(
        name=ActiveDirectoryPage.add_button["title_ru"],
        found_index=ActiveDirectoryPage.add_button["found_index"],
    ).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("RUS Screenshot Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestScreensRU
@pytest.mark.testGUI_RusVersionDCTest_ScreensTest_Settings
class TestActiveDirectoryPage:
    @allure.story("тест главного окна настройки AD")
    class TestActiveDirectoryMainPage:
        def test_active_directory_screen(self, start_screen_test_page_ru):
            send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
            time.sleep(2)
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.active_directory["path"],
                confidence=LevelOfConfidence.confidence["reduced_confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна настройки подключения к бд ДЦ закладки AD")
    class TestSQLConnectionSettingsWindow:
        def test_sql_connection_settings_screen(self, handle_sql_connection_settings):
            send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.active_directory_active_directory_sql_connection_settings[
                    "path"
                ],
                confidence=LevelOfConfidence.confidence["reduced_confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна добавления домена закладки AD")
    class TestAddDomainWindow:
        def test_add_domain_screen(self, handle_add_domain):
            send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.active_directory_active_directory_add_domain[
                    "path"
                ],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна добавления пользователя рабочей группы закладки AD")
    class TestAddWorkgroupUserWindow:
        def test_add_workgroup_user_screen(self, handle_add_workgroup_user):
            send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.active_directory_active_directory_add_workgroup_user[
                    "path"
                ],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна добавления внутренних пользователей КИБ закладки AD")
    class TestAddInternalUserWindow:
        def test_add_internal_user_screen(self, handle_add_internal_user):
            send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.active_directory_active_directory_add_internal_user[
                    "path"
                ],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))
