# Standart libraries
import time

# Third party packages
import allure
import pyautogui
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import UserCardsPage
from DataCenter.locators.confidence import LevelOfConfidence
from DataCenter.locators.path_to_screenshots import PathToScreenshotsEN
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.fixture(scope="class")
def confirm_clear_db(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y06{VK_MENU up}")
    app = start_screen_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(name=UserCardsPage.clear_database["title_en"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("ENG Screenshot Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestScreensEN
@pytest.mark.testGUI_EngVersionDCTest_ScreensTest_Additionalfeatures
class TestUserCardsPage:
    @allure.story("тест главного окна UserCards")
    class TestUserCardsMainPage:
        def test_user_cards_page_screen(self, start_screen_test_page_en):
            send_keys("{VK_MENU down}Y4Y06{VK_MENU up}")
            time.sleep(2)
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.user_cards["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна подтверждения очистки БД UserCards")
    class TestConfirmClearDBWindow:
        def test_confirm_clear_db(self, confirm_clear_db):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.user_cards_confirm_clear_db["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))
