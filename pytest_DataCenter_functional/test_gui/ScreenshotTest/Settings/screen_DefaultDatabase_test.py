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
from DataCenter.buttons import DefaultDatabasePage
from DataCenter.locators.confidence import LevelOfConfidence
from DataCenter.locators.path_to_screenshots import PathToScreenshotsEN
from DataCenter.tools.take_screen import (
    make_screenshot_if_error,
    take_screenshot_with_elements,
)


@pytest.fixture(scope="class")
def handle_add_server(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DefaultDatabasePage.add_button[title_key]).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_edit_server(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DefaultDatabasePage.edit_button[title_key]).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_delete_server(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DefaultDatabasePage.delete_button[title_key]).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("Screenshot Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestScreens
@pytest.mark.testGUI_DCTest_ScreensTest_Settings
class TestDefaultDatabasePage:
    @allure.story("тест главного окна настройки БД по умолчанию")
    class TestDefaultDatabaseMainPage:
        def test_default_database_screen(self, start_screen_test_page, assert_snapshot):
            send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
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

    @allure.story("тест окна добавления сервера на закладке настройки БД по умолчанию")
    class TestDefaultDatabaseAddServerWindow:
        def test_default_database_add_server_window(self, handle_add_server, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = handle_add_server
            window = handle.by(name=DefaultDatabasePage.add_server[title_key])
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())

    @allure.story("тест окна редактирования сервера на закладке настройки БД по умолчанию")
    class TestDefaultDatabaseEditServerWindow:
        def test_default_database_edit_server_window(self, handle_edit_server, assert_snapshot):
            mouse.move(coords=(0, 0))
            handle = handle_edit_server
            window = handle.by(name_re="MS SQL*", found_index=0)
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())

    @allure.story("тест окна удаления сервера на закладке настройки БД по умолчанию")
    class TestDefaultDatabaseDeleteServerWindow:
        def test_handle_delete_server(self, handle_delete_server, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = handle_delete_server
            window = handle.by(name=DefaultDatabasePage.confirm[title_key])
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())
