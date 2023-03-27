# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import ComponentsSettingsPage


@pytest.fixture(scope="class")
def handle(start_test_page):
    send_keys("{VK_MENU down}Y4Y04{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки компонентов")
class TestComponentsSettingsPage:
    def test_cancel_button(self, handle, title_key):
        cancel_button = handle.by(name=ComponentsSettingsPage.cancel_button[title_key]).find().window_text()
        check.equal(cancel_button, ComponentsSettingsPage.cancel_button[title_key])

    def test_apply_button(self, handle, title_key):
        apply_button = handle.by(name=ComponentsSettingsPage.apply_button[title_key]).find().window_text()
        check.equal(apply_button, ComponentsSettingsPage.apply_button[title_key])

    def test_check_connection(self, handle, title_key):
        check_connection = handle.by(name=ComponentsSettingsPage.check_connection[title_key]).find().window_text()
        check.equal(check_connection, ComponentsSettingsPage.check_connection[title_key])

    def test_unified_storage_settings(self, handle, title_key):
        unified_storage_settings = (
            handle.by(name=ComponentsSettingsPage.unified_storage_settings[title_key]).find().window_text()
        )
        check.equal(unified_storage_settings, ComponentsSettingsPage.unified_storage_settings[title_key])

    def test_display_of_company_data(self, handle, title_key):
        display_of_company_data = (
            handle.by(name=ComponentsSettingsPage.display_of_company_data[title_key]).find().window_text()
        )
        check.equal(display_of_company_data, ComponentsSettingsPage.display_of_company_data[title_key])

    def test_proxy_server_settings(self, handle, title_key):
        proxy_server_settings = (
            handle.by(name=ComponentsSettingsPage.proxy_server_settings[title_key]).find().window_text()
        )
        check.equal(proxy_server_settings, ComponentsSettingsPage.proxy_server_settings[title_key])

    def test_display_logo(self, handle, title_key):
        display_logo = handle.by(name=ComponentsSettingsPage.display_logo[title_key]).find().window_text()
        check.equal(display_logo, ComponentsSettingsPage.display_logo[title_key])

    def test_display_icon(self, handle, title_key):
        display_icon = handle.by(name=ComponentsSettingsPage.display_icon[title_key]).find().window_text()
        check.equal(display_icon, ComponentsSettingsPage.display_icon[title_key])

    def test_use_proxy(self, handle, title_key):
        use_proxy = handle.by(name=ComponentsSettingsPage.use_proxy[title_key]).find().window_text()
        check.equal(use_proxy, ComponentsSettingsPage.use_proxy[title_key])
