# Standart libraries
import time
from pathlib import Path

# Third party packages
import allure
import pyautogui
import pytest
import pytest_check as check
from pywinauto import Application
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.locators.confidence import LevelOfConfidence
from DataCenter.locators.path_to_screenshots import PathToScreenshotsES
from DataCenter.tools.get_project_root import get_project_root
from DataCenter.tools.take_image_difference import percent_image_difference
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.fixture(scope="class")
def handle_licence_key(start_screen_test_page_es):
    send_keys("{VK_MENU down}Y2Y1{VK_MENU up}")
    app = start_screen_test_page_es
    handle = app.window(name_re="DataCenter*")
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_auto_license(start_screen_test_page_es):
    send_keys("{VK_MENU down}Y2Y3{VK_MENU up}")
    app = start_screen_test_page_es
    handle = app.window(name_re="DataCenter*")
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_statistic_license(start_screen_test_page_es):
    send_keys("{VK_MENU down}Y2Y2{VK_MENU up}")
    app = start_screen_test_page_es
    handle = app.window(name_re="DataCenter*")
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("ESP Screenshot Test")
@allure.feature("Licenses")
@pytest.mark.testGUI_TestScreensES
@pytest.mark.testGUI_EspVersionDCTest_ScreensTest_Licenses
class TestLicensePage:
    @allure.story("тест главного окна работы с лицензиями")
    class TestLicenseMainPage:
        def test_license_page_screen(self, start_screen_test_page_es):
            send_keys("{VK_MENU down}Y2{VK_MENU up}%")
            time.sleep(2)
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsES.licenses_page["path"],
                confidence=LevelOfConfidence.confidence["reduced_confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна обновления лицензии")
    class TestLicenseUpdateLicenseWindow:
        def test_licence_key(self, handle_licence_key):
            time.sleep(2)
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsES.license_page_update_license_window["path"],
                confidence=LevelOfConfidence.confidence["reduced_confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна автораспределения лицензии")
    class TestLicenseDistributeAutomaticallyWindow:
        def test_auto_license(self, handle_auto_license):
            time.sleep(2)
            app_win32 = Application(backend="win32").connect(
                path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
            )
            handle = app_win32.window(name_re="Confirma*")
            handle.move_window(width=386, height=159)
            handle.capture_as_image().save(
                Path(
                    get_project_root(),
                    "pytest_DataCenter_functional",
                    "test_gui",
                    "EspVersionDCTest",
                    "Screenshot Test",
                    "Licenses",
                    "Screenshots",
                    "for_compare_LicensePage_DistributeAutomaticallyWindow.png",
                )
            )
            time.sleep(1)
            image1 = Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_gui",
                "EspVersionDCTest",
                "Screenshot Test",
                "Licenses",
                "Screenshots",
                "for_compare_LicensePage_DistributeAutomaticallyWindow.png",
            )
            image2 = Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_gui",
                "EspVersionDCTest",
                "Screenshot Test",
                "Licenses",
                "Screenshots",
                "LicensePage_DistributeAutomaticallyWindow.png",
            )
            dif = percent_image_difference(image1, image2)
            make_screenshot_if_error(check.less(dif, 1.5))

    @allure.story("тест окна статистики лицензирования")
    class TestLicenseStatisticsWindow:
        def test_handle_statistic_license(self, handle_statistic_license):
            time.sleep(6)
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsES.license_page_statistics_window["path"],
                confidence=LevelOfConfidence.confidence["reduced_confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))
