# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import ComponentsSettingsPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y04{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("RUS Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsRU
@pytest.mark.testGUI_RusVersionDCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки компонентов")
class TestComponentsSettingsPage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=ComponentsSettingsPage.cancel_button["title_ru"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Отменить")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=ComponentsSettingsPage.apply_button["title_ru"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Применить")

    def test_check_connection(self, handle):
        check_connection = (
            handle.by(name=ComponentsSettingsPage.check_connection["title_ru"])
            .find()
            .window_text()
        )
        check.equal(check_connection, "Проверить соединение")

    def test_unified_storage_settings(self, handle):
        unified_storage_settings = (
            handle.by(name=ComponentsSettingsPage.unified_storage_settings["title_ru"])
            .find()
            .window_text()
        )
        check.equal(unified_storage_settings, "Настройки Unified Storage")

    def test_display_of_company_data(self, handle):
        display_of_company_data = (
            handle.by(name=ComponentsSettingsPage.display_of_company_data["title_ru"])
            .find()
            .window_text()
        )
        check.equal(display_of_company_data, "Отображение данных компании")

    def test_proxy_server_settings(self, handle):
        proxy_server_settings = (
            handle.by(name=ComponentsSettingsPage.proxy_server_settings["title_ru"])
            .find()
            .window_text()
        )
        check.equal(proxy_server_settings, "Настройки прокси сервера")

    def test_display_logo(self, handle):
        display_logo = (
            handle.by(name=ComponentsSettingsPage.display_logo["title_ru"])
            .find()
            .window_text()
        )
        check.equal(display_logo, "Отображать логотип")

    def test_display_icon(self, handle):
        display_icon = (
            handle.by(name=ComponentsSettingsPage.display_icon["title_ru"])
            .find()
            .window_text()
        )
        check.equal(display_icon, "Отображать иконку")

    def test_use_proxy(self, handle):
        use_proxy = (
            handle.by(name=ComponentsSettingsPage.use_proxy["title_ru"])
            .find()
            .window_text()
        )
        check.equal(use_proxy, "Использовать прокси")
