# Standart libraries
import time

# Third party packages
import allure
import pyautogui
import pytest
import pytest_check as check
from pywinauto import Application
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import ProfileCenterSettingsPage
from DataCenter.locators.confidence import LevelOfConfidence
from DataCenter.locators.path_to_screenshots import PathToScreenshotsEN
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.fixture(scope="class")
def handle_sql_server_connection_setting(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_screen_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(name=ProfileCenterSettingsPage.setup_connection_to_db["title_en"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_reading_window(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_screen_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_reading_button
    ).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_reading_second_window(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = Application(backend="uia").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_reading_button
    ).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button["title_en"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_reading_third_window(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = Application(backend="uia").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_reading_button
    ).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button["title_en"]).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button2["title_en"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_profiling_window(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_screen_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_profiling_button
    ).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_profiling_second_window(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = Application(backend="uia").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_profiling_button
    ).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button3["title_en"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_profiling_third_window(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = Application(backend="uia").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_profiling_button
    ).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button3["title_en"]).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button4["title_en"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("ENG Screenshot Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestScreensEN
@pytest.mark.testGUI_EngVersionDCTest_ScreensTest_Additionalfeatures
class TestProfileCenterSettingsPage:
    @allure.story("тест главного окна ProfileCenter")
    class TestProfileCenterSettingsMainPage:
        def test_profile_center_settings_page_screen(self, start_screen_test_page_en):
            send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
            time.sleep(2)
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.profile_center_settings["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна настройки подключения к БД ProfileCenter")
    class TestSQLServerConnectionSettingWindow:
        def test_sql_server_connection_setting_screen(
            self, handle_sql_server_connection_setting
        ):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.profile_center_settings_sql_server_connection_setting_window[
                    "path"
                ],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна настройки расписания вычитки индексов ProfileCenter")
    class TestScheduleOfReadingWindow:
        def test_schedule_of_reading_window(self, schedule_of_reading_window):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.profile_schedule_of_reading_window["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story(
        "тест второго окна настройки расписания вычитки индексов ProfileCenter"
    )
    class TestScheduleOfReadingSecondWindow:
        def test_schedule_of_reading_second_window(
            self, schedule_of_reading_second_window
        ):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.profile_schedule_of_reading_second_window["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story(
        "тест третьего окна настройки расписания вычитки индексов ProfileCenter"
    )
    class TestScheduleOfReadingThirdWindow:
        def test_schedule_of_reading_third_window(
            self, schedule_of_reading_third_window
        ):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.profile_schedule_of_reading_third_window["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна настройки расписания профилирования ProfileCenter")
    class TestScheduleOfProfilingWindow:
        def test_schedule_of_profiling_window(self, schedule_of_profiling_window):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.profile_schedule_of_profiling_window["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест второго окна настройки расписания профилирования ProfileCenter")
    class TestScheduleOfProfilingSecondWindow:
        def test_schedule_of_profiling_second_window(
            self, schedule_of_profiling_second_window
        ):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.profile_schedule_of_profiling_second_window["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story(
        "тест третьего окна настройки расписания профилирования ProfileCenter"
    )
    class TestScheduleOfProfilingThirdWindow:
        def test_schedule_of_profiling_third_window(
            self, schedule_of_profiling_third_window
        ):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.profile_schedule_of_profiling_third_window["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))
