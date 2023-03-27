# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import ComponentsUpdatePage


@pytest.fixture(scope="class")
def handle(start_test_page):
    send_keys("{VK_MENU down}Y4Y02{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки обновления компонентов")
class TestComponentsUpdatePage:
    def test_cancel_button(self, handle, title_key):
        cancel_button = handle.by(name=ComponentsUpdatePage.cancel_button[title_key]).find().window_text()
        check.equal(cancel_button, ComponentsUpdatePage.cancel_button[title_key])

    def test_apply_button(self, handle, title_key):
        apply_button = handle.by(name=ComponentsUpdatePage.apply_button[title_key]).find().window_text()
        check.equal(apply_button, ComponentsUpdatePage.apply_button[title_key])

    def test_analyticconsole(self, handle, title_key):
        analyticconsole = handle.by(name=ComponentsUpdatePage.analyticconsole[title_key]).find().window_text()
        check.equal(analyticconsole, ComponentsUpdatePage.analyticconsole[title_key])

    def test_automatic_update_of_versions3(self, handle, title_key):
        automatic_update_of_versions3 = (
            handle.by(
                name=ComponentsUpdatePage.automatic_update_of_versions3[title_key],
                found_index=ComponentsUpdatePage.automatic_update_of_versions3["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(automatic_update_of_versions3, ComponentsUpdatePage.automatic_update_of_versions3[title_key])

    def test_installation_in_silent_mode(self, handle, title_key):
        installation_in_silent_mode = (
            handle.by(name=ComponentsUpdatePage.installation_in_silent_mode[title_key]).find().window_text()
        )
        check.equal(installation_in_silent_mode, ComponentsUpdatePage.installation_in_silent_mode[title_key])

    def test_api_installation(self, handle, title_key):
        api_installation = handle.by(name=ComponentsUpdatePage.api_installation[title_key]).find().window_text()
        check.equal(api_installation, ComponentsUpdatePage.api_installation[title_key])

    def test_version3(self, handle, title_key):
        version3 = (
            handle.by(
                name=ComponentsUpdatePage.version3[title_key],
                found_index=ComponentsUpdatePage.version3["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(version3, ComponentsUpdatePage.version3[title_key])

    def test_reportcenter(self, handle, title_key):
        reportcenter = handle.by(name=ComponentsUpdatePage.reportcenter[title_key]).find().window_text()
        check.equal(reportcenter, ComponentsUpdatePage.reportcenter[title_key])

    def test_automatic_update_of_versions2(self, handle, title_key):
        automatic_update_of_versions2 = (
            handle.by(
                name=ComponentsUpdatePage.automatic_update_of_versions2[title_key],
                found_index=ComponentsUpdatePage.automatic_update_of_versions3["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(automatic_update_of_versions2, ComponentsUpdatePage.automatic_update_of_versions2[title_key])

    def test_version2(self, handle, title_key):
        version2 = (
            handle.by(
                name=ComponentsUpdatePage.version2[title_key],
                found_index=ComponentsUpdatePage.version2["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(version2, ComponentsUpdatePage.version2[title_key])

    def test_searchapi(self, handle, title_key):
        searchapi = handle.by(name=ComponentsUpdatePage.searchapi[title_key]).find().window_text()
        check.equal(searchapi, ComponentsUpdatePage.searchapi[title_key])

    def test_automatic_update_of_versions(self, handle, title_key):
        automatic_update_of_versions = (
            handle.by(
                name=ComponentsUpdatePage.automatic_update_of_versions[title_key],
                found_index=ComponentsUpdatePage.automatic_update_of_versions["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(automatic_update_of_versions, ComponentsUpdatePage.automatic_update_of_versions[title_key])

    def test_version(self, handle, title_key):
        version = (
            handle.by(
                name=ComponentsUpdatePage.version[title_key],
                found_index=ComponentsUpdatePage.version["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(version, ComponentsUpdatePage.version[title_key])

    def test_webanalytic(self, handle, title_key):
        webanalytic = handle.by(name=ComponentsUpdatePage.webanalytic[title_key]).find().window_text()
        check.equal(webanalytic, ComponentsUpdatePage.webanalytic[title_key])

    def test_automatic_update_of_versions4(self, handle, title_key):
        automatic_update_of_versions4 = (
            handle.by(
                name=ComponentsUpdatePage.automatic_update_of_versions4[title_key],
                found_index=ComponentsUpdatePage.automatic_update_of_versions["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(automatic_update_of_versions4, ComponentsUpdatePage.automatic_update_of_versions4[title_key])

    def test_version4(self, handle, title_key):
        version4 = (
            handle.by(
                name=ComponentsUpdatePage.version4[title_key],
                found_index=ComponentsUpdatePage.version4["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(version4, ComponentsUpdatePage.version4[title_key])
