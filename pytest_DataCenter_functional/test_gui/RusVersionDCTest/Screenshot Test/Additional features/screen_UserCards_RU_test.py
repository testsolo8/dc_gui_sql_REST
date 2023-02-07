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
from DataCenter.buttons import UserCardsPage
from DataCenter.locators.confidence import LevelOfConfidence
from DataCenter.locators.path_to_screenshots import PathToScreenshotsRU
from DataCenter.tools.get_project_root import get_project_root
from DataCenter.tools.take_image_difference import percent_image_difference
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.fixture(scope="class")
def confirm_clear_db(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y4Y06{VK_MENU up}")
    app = start_screen_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=UserCardsPage.clear_database["title_ru"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("RUS Screenshot Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestScreensRU
@pytest.mark.testGUI_RusVersionDCTest_ScreensTest_Additionalfeatures
class TestUserCardsPage:
    @allure.story("тест главного окна UserCards")
    class TestUserCardsMainPage:
        def test_user_cards_page_screen(self, start_screen_test_page_ru):
            send_keys("{VK_MENU down}Y4Y06{VK_MENU up}")
            time.sleep(2)
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.user_cards["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест окна подтверждения очистки БД UserCards")
    class TestConfirmClearDBWindow:
        def test_confirm_clear_db(self, confirm_clear_db):
            app_win32 = Application(backend="win32").connect(
                path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
            )
            handle = app_win32.window(name_re="Подтвер*")
            handle.move_window(width=988, height=146)
            handle.capture_as_image().save(
                Path(
                    get_project_root(),
                    "pytest_DataCenter_functional",
                    "test_gui",
                    "RusVersionDCTest",
                    "Screenshot Test",
                    "Additional features",
                    "Screenshots",
                    "for_compare_UserCardsPage_ConfirmClearDB.png",
                )
            )
            time.sleep(1)
            image1 = Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_gui",
                "RusVersionDCTest",
                "Screenshot Test",
                "Additional features",
                "Screenshots",
                "for_compare_UserCardsPage_ConfirmClearDB.png",
            )
            image2 = Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_gui",
                "RusVersionDCTest",
                "Screenshot Test",
                "Additional features",
                "Screenshots",
                "UserCardsPage_ConfirmClearDB.png",
            )
            dif = percent_image_difference(image1, image2)
            make_screenshot_if_error(check.less(dif, 1.5))
