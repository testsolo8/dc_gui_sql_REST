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
from DataCenter.buttons import ManagementPage


@pytest.fixture(scope="class")
def synchronization_with_active_directory_window(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y1{VK_MENU up}%")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=ManagementPage.synchronization_with_active_directory[title_key]).by(
        class_name="TcxButton", control_type="Button"
    ).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(2)
@allure.epic("Screenshot Test")
@allure.feature("Management")
@pytest.mark.testGUI_TestScreens
@pytest.mark.testGUI_DCTest_ScreensTest_Management
class TestManagementPage:
    @allure.story("тест окна синхронизации с AD закладки управления")
    class TestSynchronizationWithActiveDirectoryWindow:
        def test_synchronization_with_active_directory_window(
            self, synchronization_with_active_directory_window, assert_snapshot, title_key
        ):
            time.sleep(2)
            mouse.move(coords=(0, 0))
            handle = synchronization_with_active_directory_window
            window = handle.by(name=ManagementPage.window_header[title_key])
            time.sleep(1)
            screenshot_image = ImageGrab.grab(window.rectangle())
            with io.BytesIO() as output:
                screenshot_image.save(output, format="PNG")
                assert_snapshot(output.getvalue())
