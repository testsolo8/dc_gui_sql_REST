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
from DataCenter.locators.path_to_screenshots import PathToScreenshotsRU
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.fixture(scope="class")
def handle_licence_key(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y2Y1{VK_MENU up}")
    app = start_screen_test_page_ru
    handle = app.window(name_re="DataCenter*")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_auto_license(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y2Y3{VK_MENU up}")
    app = start_screen_test_page_ru
    handle = app.window(name_re="DataCenter*")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_statistic_license(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y2Y2{VK_MENU up}")
    app = start_screen_test_page_ru
    handle = app.window(name_re="DataCenter*")
    time.sleep(6)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("RUS Screenshot Test")
@allure.feature("Licenses")
@pytest.mark.testGUI_TestScreensRU
@pytest.mark.testGUI_RusVersionDCTest_ScreensTest_Licenses
class TestLicensePage:
    @allure.story("тест главного окна работы с лицензиями")
    class TestLicenseMainPage:
        def test_license_page_screen(self, start_screen_test_page_ru):
            send_keys("{VK_MENU down}Y2{VK_MENU up}%")
            time.sleep(2)
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.licenses_page["path"],
                confidence=LevelOfConfidence.confidence["reduced_confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна обновления лицензии")
    class TestLicenseUpdateLicenseWindow:
        def test_licence_key(self, handle_licence_key):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.license_page_update_license_window["path"],
                confidence=LevelOfConfidence.confidence["reduced_confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна автораспределения лицензии")
    class TestLicenseDistributeAutomaticallyWindow:
        def test_auto_license(self, handle_auto_license):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.license_page_distribute_automatically_window[
                    "path"
                ],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна статистики лицензирования")
    class TestLicenseStatisticsWindow:
        def test_handle_statistic_license(self, handle_statistic_license):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.license_page_statistics_window["path"],
                confidence=LevelOfConfidence.confidence["reduced_confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))
