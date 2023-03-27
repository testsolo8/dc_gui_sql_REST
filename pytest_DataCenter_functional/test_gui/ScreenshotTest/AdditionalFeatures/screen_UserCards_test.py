# Standart libraries
import io
import time

# Third party packages
import allure
import pytest
import pywinauto.mouse as mouse
from PIL import ImageGrab
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import UserCardsPage
from DataCenter.tools.take_screen import take_screenshot_with_elements


@pytest.fixture(scope="class")
def confirm_clear_db(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y06{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=UserCardsPage.clear_database[title_key]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("Screenshot Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestScreens
@pytest.mark.testGUI_DCTest_ScreensTest_Additionalfeatures
class TestUserCardsPage:
    @allure.story("тест главного окна UserCards")
    class TestUserCardsMainPage:
        def test_user_cards_screen(self, start_screen_test_page, assert_snapshot):
            send_keys("{VK_MENU down}Y4Y06{VK_MENU up}")
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

    @allure.story("тест окна подтверждения очистки БД UserCards")
    class TestConfirmClearDBWindow:
        def test_confirm_clear_db(self, confirm_clear_db, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = confirm_clear_db
            window = handle.by(name=UserCardsPage.confirm[title_key])
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())
