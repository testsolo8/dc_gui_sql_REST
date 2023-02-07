# Standart libraries
import time

# Third party packages
import allure
import pyautogui
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import ManagementPage
from DataCenter.locators.confidence import LevelOfConfidence
from DataCenter.locators.path_to_screenshots import PathToScreenshotsRU
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.fixture(scope="class")
def synchronization_with_active_directory_window(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y1{VK_MENU up}%")
    app = start_screen_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=ManagementPage.synchronization_with_active_directory["title_ru"]).by(
        class_name="TcxButton", control_type="Button"
    ).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("RUS Screenshot Test")
@allure.feature("Management")
@pytest.mark.testGUI_TestScreensRU
@pytest.mark.testGUI_RusVersionDCTest_ScreensTest_Management
class TestManagementPage:
    # @allure.story("тест главного окна управления")
    # class TestManagementMainPage:
    #     def test_license_page_screen(self, start_screen_test_page_en):
    #         send_keys("{VK_MENU down}Y2{VK_MENU up}%")
    #         time.sleep(2)
    #         screenshot = pyautogui.locateOnScreen(
    #             PathToScreenshotsRU.licenses_page["path"],
    #             confidence=LevelOfConfidence.confidence["confidence"],
    #         )
    #         make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна синхронизации с AD")
    class TestSynchronizationWithActiveDirectoryWindow:
        def test_synchronization_with_active_directory_window(
            self, synchronization_with_active_directory_window
        ):
            time.sleep(2)
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.management_page_synchronization_with_active_directory_window[
                    "path"
                ],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))
