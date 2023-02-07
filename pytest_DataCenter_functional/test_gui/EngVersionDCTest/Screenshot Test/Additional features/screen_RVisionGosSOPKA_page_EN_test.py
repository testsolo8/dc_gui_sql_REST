# Standart libraries
import time

# Third party packages
import allure
import pyautogui
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import RVisionGosSOPKAPage
from DataCenter.locators.confidence import LevelOfConfidence
from DataCenter.locators.path_to_screenshots import PathToScreenshotsEN
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.fixture(scope="class")
def handle_add_controlled_information_resources(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y09{VK_MENU up}")
    app = start_screen_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(name=RVisionGosSOPKAPage.add["title_en"]).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("ENG Screenshot Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestScreensEN
@pytest.mark.testGUI_EngVersionDCTest_ScreensTest_Additionalfeatures
class TestRVisionGosSOPKAPage:
    @allure.story("тест главного окна настройки ГосСОПКА")
    class TestRVisionGosSOPKAMainPage:
        def test_RVisionGosSOPKA_page_screen(self, start_screen_test_page_en):
            send_keys("{VK_MENU down}Y4Y09{VK_MENU up}")
            time.sleep(2)
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.RVisionGosSOPKA["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story(
        "тест скрина окна настройки добавления контролируемого информационного ресурса ГосСОПКА"
    )
    class TestAddControlledInformationResources:
        def test_add_controlled_information_resources(
            self, handle_add_controlled_information_resources
        ):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.RVisionGosSOPKAPage_add_controlled_information_resources[
                    "path"
                ],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))
