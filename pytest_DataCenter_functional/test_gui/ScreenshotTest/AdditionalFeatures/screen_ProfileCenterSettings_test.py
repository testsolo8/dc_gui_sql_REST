# Standart libraries
import io
import time

# Third party packages
import allure
import pytest
import pywinauto.mouse as mouse
from PIL import ImageGrab
from pywinauto import Application
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import ProfileCenterSettingsPage
from DataCenter.tools.take_screen import take_screenshot_with_elements


@pytest.fixture(scope="class")
def handle_sql_server_connection_setting(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=ProfileCenterSettingsPage.setup_connection_to_db[title_key]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_reading_window(start_screen_test_page):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(ProfileCenterSettingsPage.edit_schedule_of_reading_button).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_reading_second_window(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = Application(backend="uia").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(ProfileCenterSettingsPage.edit_schedule_of_reading_button).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button[title_key]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_reading_third_window(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = Application(backend="uia").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(ProfileCenterSettingsPage.edit_schedule_of_reading_button).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button[title_key]).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button2[title_key]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_profiling_window(start_screen_test_page):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(ProfileCenterSettingsPage.edit_schedule_of_profiling_button).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_profiling_second_window(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = Application(backend="uia").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(ProfileCenterSettingsPage.edit_schedule_of_profiling_button).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button3[title_key]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_profiling_third_window(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = Application(backend="uia").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(ProfileCenterSettingsPage.edit_schedule_of_profiling_button).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button3[title_key]).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button4[title_key]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("Screenshot Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestScreens
@pytest.mark.testGUI_DCTest_ScreensTest_Additionalfeatures
class TestProfileCenterSettingsPage:
    @allure.story("тест главного окна ProfileCenter")
    class TestProfileCenterSettingsMainPage:
        def test_profile_center_settings_screen(self, start_screen_test_page, assert_snapshot):
            send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
            time.sleep(2)
            mouse.move(coords=(0, 0))
            app = start_screen_test_page
            window = app.window(name_re="DataCenter*")
            time.sleep(1)
            elements = [
                {"name": "TitleBar", "element": window.TitleBar},
                {
                    "name": "TimePicker",
                    "element": window.Pane19.by(class_name="TDateTimePicker", control_type="Pane", found_index=0),
                },
            ]
            screenshot = take_screenshot_with_elements(window, elements=elements)
            assert_snapshot(screenshot)

    @allure.story("тест окна настройки подключения к БД ProfileCenter")
    class TestSQLServerConnectionSettingWindow:
        def test_sql_server_connection_setting_screen(self, handle_sql_server_connection_setting, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = handle_sql_server_connection_setting
            window = handle.by(name=ProfileCenterSettingsPage.sql_server_connection_settings[title_key])
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())

    @allure.story("тест окна настройки расписания вычитки индексов ProfileCenter")
    class TestScheduleOfReadingWindow:
        def test_schedule_of_reading_window(self, schedule_of_reading_window, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = schedule_of_reading_window
            window = handle.by(name=ProfileCenterSettingsPage.modifying_schedule[title_key])
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())

    @allure.story("тест второго окна настройки расписания вычитки индексов ProfileCenter")
    class TestScheduleOfReadingSecondWindow:
        def test_schedule_of_reading_second_window(self, schedule_of_reading_second_window, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = schedule_of_reading_second_window
            window = handle.by(name=ProfileCenterSettingsPage.modifying_schedule2[title_key])
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())

    @allure.story("тест третьего окна настройки расписания вычитки индексов ProfileCenter")
    class TestScheduleOfReadingThirdWindow:
        def test_schedule_of_reading_third_window(self, schedule_of_reading_third_window, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = schedule_of_reading_third_window
            window = handle.by(name=ProfileCenterSettingsPage.modifying_schedule3[title_key])
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())

    @allure.story("тест окна настройки расписания профилирования ProfileCenter")
    class TestScheduleOfProfilingWindow:
        def test_schedule_of_profiling_window(self, schedule_of_profiling_window, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = schedule_of_profiling_window
            window = handle.by(name=ProfileCenterSettingsPage.modifying_schedule4[title_key])
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())

    @allure.story("тест второго окна настройки расписания профилирования ProfileCenter")
    class TestScheduleOfProfilingSecondWindow:
        def test_schedule_of_profiling_second_window(self, schedule_of_profiling_second_window, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = schedule_of_profiling_second_window
            window = handle.by(name=ProfileCenterSettingsPage.modifying_schedule5[title_key])
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())

    @allure.story("тест третьего окна настройки расписания профилирования ProfileCenter")
    class TestScheduleOfProfilingThirdWindow:
        def test_schedule_of_profiling_third_window(self, schedule_of_profiling_third_window, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = schedule_of_profiling_third_window
            window = handle.by(name=ProfileCenterSettingsPage.modifying_schedule6[title_key])
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())
