# Standart libraries
import time

# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import ManagementPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y1{VK_MENU up}%")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def synchronization_with_active_directory_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y1{VK_MENU up}%")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=ManagementPage.synchronization_with_active_directory["title_ru"]).by(
        class_name="TcxButton", control_type="Button"
    ).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("RUS Controls Test")
@allure.feature("Management")
@pytest.mark.testGUI_TestControlsRU
@pytest.mark.testGUI_RusVersionDCTest_ControlsTest_Management
class TestManagementPage:
    @allure.story("тест главного окна управления")
    class TestManagementMainPage:
        def test_synchronization_with_active_directory(self, handle):
            synchronization_with_active_directory = (
                handle.by(
                    name=ManagementPage.synchronization_with_active_directory[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                synchronization_with_active_directory,
                "Синхронизация с Active Directory",
            )

        def test_logs_size(self, handle):
            logs_size = (
                handle.__getattribute__(ManagementPage.logs_size["title_ru"])
                .find()
                .window_text()
            )
            check.equal(logs_size, "Размер логов")

        def test_free_space_on_drives(self, handle):
            logs_size = (
                handle.by(name=ManagementPage.free_space_on_drives["title_ru"])
                .find()
                .window_text()
            )
            check.equal(logs_size, "Свободное место на дисках")

    @allure.story("тест окна синхронизации с AD закладки управления")
    class TestSynchronizationWithActiveDirectoryWindow:
        def test_stop_synchronization(
            self, synchronization_with_active_directory_window
        ):
            stop_synchronization = (
                synchronization_with_active_directory_window.by(
                    name=ManagementPage.stop_synchronization["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(stop_synchronization, "Прервать синхронизацию")

        def test_start_synchronization(
            self, synchronization_with_active_directory_window
        ):
            start_synchronization = (
                synchronization_with_active_directory_window.by(
                    name=ManagementPage.start_synchronization["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(start_synchronization, "Начать синхронизацию")

        def test_close_button(self, synchronization_with_active_directory_window):
            close_button = (
                synchronization_with_active_directory_window.by(
                    name=ManagementPage.close_button["title_ru"],
                    found_index=ManagementPage.close_button["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(close_button, "Закрыть")
