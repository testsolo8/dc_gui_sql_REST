# Standart libraries
import io
import time

# Third party packages
import allure
import pytest
import pywinauto.mouse as mouse
from PIL import ImageDraw, ImageGrab
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import LicensePage
from DataCenter.tools.take_screen import take_screenshot_with_elements

COORDINATES = {
    "eng": {
        "license_page_screen": [
            {"element": {"left": 189, "top": 201, "right": 253, "bottom": 215}},
            {"element": {"left": 100, "top": 216, "right": 175, "bottom": 233}},
        ],
        "licence_key": [
            {"element": {"left": 84, "top": 56, "right": 147, "bottom": 76}},
        ],
    },
    "es": {
        "license_page_screen": [
            {"element": {"left": 122, "top": 199, "right": 197, "bottom": 234}},
        ],
        "licence_key": [
            {"element": {"left": 101, "top": 55, "right": 166, "bottom": 76}},
        ],
    },
    "rus": {
        "license_page_screen": [
            {"element": {"left": 164, "top": 201, "right": 228, "bottom": 215}},
            {"element": {"left": 218, "top": 216, "right": 291, "bottom": 233}},
        ],
        "licence_key": [
            {"element": {"left": 180, "top": 56, "right": 241, "bottom": 76}},
        ],
    },
    "general": [
        {"element": {"left": 1061, "top": 136, "right": 1182, "bottom": 209}},
        {"element": {"left": 752, "top": 136, "right": 873, "bottom": 209}},
        {"element": {"left": 704, "top": 525, "right": 802, "bottom": 549}},
        {"element": {"left": 312, "top": 229, "right": 424, "bottom": 247}},
            ]
    }



@pytest.fixture(scope="class")
def handle_licence_key(start_screen_test_page):
    send_keys("{VK_MENU down}Y2Y1{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_auto_license(start_screen_test_page):
    send_keys("{VK_MENU down}Y2Y3{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_statistic_license(start_screen_test_page):
    send_keys("{VK_MENU down}Y2Y2{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("Screenshot Test")
@allure.feature("Licenses")
@pytest.mark.testGUI_TestScreens
@pytest.mark.testGUI_DCTest_ScreensTest_Licenses
class TestLicensePage:
    @allure.story("тест главного окна работы с лицензиями")
    class TestLicenseMainPage:
        def test_license_page_screen(self, start_screen_test_page, assert_snapshot, lang_parametrize):
            send_keys("{VK_MENU down}Y2{VK_MENU up}%")
            time.sleep(2)
            mouse.move(coords=(0, 0))
            app = start_screen_test_page
            window = app.window(name_re="DataCenter*")
            time.sleep(1)
            elements = [
                {"name": "TitleBar", "element": window.TitleBar},
            ]
            coordinates = COORDINATES.get(lang_parametrize).get("license_page_screen")
            screenshot = take_screenshot_with_elements(window, elements=elements, coordinates=coordinates)
            assert_snapshot(screenshot)

    @allure.story("тест окна обновления лицензии")
    class TestLicenseUpdateLicenseWindow:
        def test_licence_key(self, handle_licence_key, assert_snapshot, lang_parametrize):
            time.sleep(2)
            mouse.move(coords=(0, 0))
            handle = handle_licence_key
            window = handle.Dialog2
            time.sleep(1)
            coordinates = COORDINATES.get(lang_parametrize).get("licence_key")
            screenshot = take_screenshot_with_elements(window, coordinates=coordinates)
            assert_snapshot(screenshot)

    @allure.story("тест окна автораспределения лицензии")
    class TestLicenseDistributeAutomaticallyWindow:
        def test_auto_license(self, handle_auto_license, assert_snapshot, title_key):
            time.sleep(2)
            mouse.move(coords=(0, 0))
            handle = handle_auto_license
            window = handle.by(name=LicensePage.DistributeAutomaticallyWindow.window_header[title_key])
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())

    @allure.story("тест окна статистики лицензирования")
    class TestLicenseStatisticsWindow:
        def test_handle_statistic_license(self, handle_statistic_license, assert_snapshot, title_key):
            time.sleep(6)
            mouse.move(coords=(0, 0))
            handle = handle_statistic_license
            window = handle.by(name=LicensePage.StatisticsWindow.window_header[title_key])
            window.move_window(x=50, y=20, width=1200, height=600)
            time.sleep(1)
            elements = [
                {"element": window.Pane14.Edit2},
                {"element": window.Pane12.Edit},
            ]
            coordinates = COORDINATES.get("general")
            screenshot = take_screenshot_with_elements(window, elements=elements, coordinates=coordinates)
            assert_snapshot(screenshot)
