# Standart libraries
import io
import time

# Third party packages
import allure
import pyautogui
import pytest
import pytest_check as check
import pywinauto.mouse as mouse
from PIL import ImageGrab
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import ActiveDirectoryPage
from DataCenter.locators.confidence import LevelOfConfidence
from DataCenter.locators.path_to_screenshots import PathToScreenshotsEN
from DataCenter.tools.take_screen import (
    make_screenshot_if_error,
    take_screenshot_with_elements,
)


@pytest.fixture(scope="class")
def handle_sql_connection_settings(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=ActiveDirectoryPage.setup_connection_db[title_key]).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_add_domain(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=ActiveDirectoryPage.synchronization_with_active_directory[title_key]).__getattribute__(
        "Button3"
    ).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_add_workgroup_user(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(
        name=ActiveDirectoryPage.add_button2[title_key],
        found_index=ActiveDirectoryPage.add_button2["found_index"],
    ).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_add_internal_user(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(
        name=ActiveDirectoryPage.add_button[title_key],
        found_index=ActiveDirectoryPage.add_button["found_index"],
    ).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("Screenshot Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestScreens
@pytest.mark.testGUI_DCTest_ScreensTest_Settings
class TestActiveDirectoryPage:
    @allure.story("тест главного окна настройки AD")
    class TestActiveDirectoryMainPage:
        def test_active_directory_screen(self, start_screen_test_page, assert_snapshot, title_key):
            send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
            time.sleep(2)
            mouse.move(coords=(0, 0))
            app = start_screen_test_page
            window = app.window(name_re="DataCenter*")
            time.sleep(1)
            elements = [
                {"name": "TitleBar", "element": window.TitleBar},
                {
                    "name": "GroupBoxSynchronizationwithActiveDirectory",
                    "element": window.by(name=ActiveDirectoryPage.synchronization_with_active_directory[title_key]),
                },
            ]
            screenshot = take_screenshot_with_elements(window, elements=elements)
            assert_snapshot(screenshot)

    @allure.story("тест окна настройки подключения к бд ДЦ закладки AD")
    class TestSQLConnectionSettingsWindow:
        def test_sql_connection_settings_screen(self, handle_sql_connection_settings, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = handle_sql_connection_settings
            window = handle.by(name=ActiveDirectoryPage.sql_server_connection_settings[title_key])
            time.sleep(1)
            elements = [
                {
                    "name": "ComboBox",
                    "element": window.ComboBox.by(class_name="Edit", control_type="Edit", found_index=0),
                }
            ]
            screenshot = take_screenshot_with_elements(window, elements=elements)
            assert_snapshot(screenshot)

    @allure.story("тест окна добавления домена закладки AD")
    class TestAddDomainWindow:
        def test_add_domain_screen(self, handle_add_domain, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = handle_add_domain
            window = handle.by(name=ActiveDirectoryPage.add_domain[title_key])
            send_keys("+{TAB}")
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())

    @allure.story("тест окна добавления пользователя рабочей группы закладки AD")
    class TestAddWorkgroupUserWindow:
        def test_add_workgroup_user_screen(self, handle_add_workgroup_user, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = handle_add_workgroup_user
            window = handle.by(name=ActiveDirectoryPage.window_header_add_user[title_key])
            send_keys("+{TAB}")
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())

    @allure.story("тест окна добавления внутренних пользователей КИБ закладки AD")
    class TestAddInternalUserWindow:
        def test_add_internal_user_screen(self, handle_add_internal_user, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = handle_add_internal_user
            window = handle.by(name=ActiveDirectoryPage.window_header_add_user[title_key])
            send_keys("+{TAB}")
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())
