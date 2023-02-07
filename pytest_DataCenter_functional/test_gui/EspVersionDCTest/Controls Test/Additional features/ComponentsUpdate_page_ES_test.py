# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import ComponentsUpdatePage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y02{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("ESP Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsES
@pytest.mark.testGUI_EspVersionDCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки обновления компонентов")
class TestComponentsUpdatePage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=ComponentsUpdatePage.cancel_button["title_es"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Cancelar")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=ComponentsUpdatePage.apply_button["title_es"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Aplicar")

    def test_analyticconsole(self, handle):
        analyticconsole = (
            handle.by(name=ComponentsUpdatePage.analyticconsole["title_es"])
            .find()
            .window_text()
        )
        check.equal(analyticconsole, "AnalyticConsole")

    def test_automatic_update_of_versions3(self, handle):
        automatic_update_of_versions3 = (
            handle.by(
                name=ComponentsUpdatePage.automatic_update_of_versions3["title_es"],
                found_index=ComponentsUpdatePage.automatic_update_of_versions3[
                    "found_index"
                ],
            )
            .find()
            .window_text()
        )
        check.equal(
            automatic_update_of_versions3, "Actualización automática de versiones"
        )

    def test_installation_in_silent_mode(self, handle):
        installation_in_silent_mode = (
            handle.by(name=ComponentsUpdatePage.installation_in_silent_mode["title_es"])
            .find()
            .window_text()
        )
        check.equal(installation_in_silent_mode, "Instalación en modo silencioso")

    def test_api_installation(self, handle):
        api_installation = (
            handle.by(name=ComponentsUpdatePage.api_installation["title_es"])
            .find()
            .window_text()
        )
        check.equal(api_installation, "Instalación de API")

    def test_version3(self, handle):
        version3 = (
            handle.by(
                name=ComponentsUpdatePage.version3["title_es"],
                found_index=ComponentsUpdatePage.version3["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(version3, "Versión:")

    def test_reportcenter(self, handle):
        reportcenter = (
            handle.by(name=ComponentsUpdatePage.reportcenter["title_es"])
            .find()
            .window_text()
        )
        check.equal(reportcenter, "ReportCenter")

    def test_automatic_update_of_versions2(self, handle):
        automatic_update_of_versions2 = (
            handle.by(
                name=ComponentsUpdatePage.automatic_update_of_versions2["title_es"],
                found_index=ComponentsUpdatePage.automatic_update_of_versions3[
                    "found_index"
                ],
            )
            .find()
            .window_text()
        )
        check.equal(
            automatic_update_of_versions2, "Actualización automática de versiones"
        )

    def test_version2(self, handle):
        version2 = (
            handle.by(
                name=ComponentsUpdatePage.version2["title_es"],
                found_index=ComponentsUpdatePage.version2["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(version2, "Versión:")

    def test_searchapi(self, handle):
        searchapi = (
            handle.by(name=ComponentsUpdatePage.searchapi["title_es"])
            .find()
            .window_text()
        )
        check.equal(searchapi, "SearchAPI")

    def test_automatic_update_of_versions(self, handle):
        automatic_update_of_versions = (
            handle.by(
                name=ComponentsUpdatePage.automatic_update_of_versions["title_es"],
                found_index=ComponentsUpdatePage.automatic_update_of_versions[
                    "found_index"
                ],
            )
            .find()
            .window_text()
        )
        check.equal(
            automatic_update_of_versions, "Actualización automática de versiones"
        )

    def test_version(self, handle):
        version = (
            handle.by(
                name=ComponentsUpdatePage.version["title_es"],
                found_index=ComponentsUpdatePage.version["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(version, "Versión:")

    def test_webanalytic(self, handle):
        webanalytic = (
            handle.by(name=ComponentsUpdatePage.webanalytic["title_es"])
            .find()
            .window_text()
        )
        check.equal(webanalytic, "WebAnalytic")

    def test_automatic_update_of_versions4(self, handle):
        automatic_update_of_versions4 = (
            handle.by(
                name=ComponentsUpdatePage.automatic_update_of_versions4["title_es"],
                found_index=ComponentsUpdatePage.automatic_update_of_versions[
                    "found_index"
                ],
            )
            .find()
            .window_text()
        )
        check.equal(
            automatic_update_of_versions4, "Actualización automática de versiones"
        )

    def test_version4(self, handle):
        version4 = (
            handle.by(
                name=ComponentsUpdatePage.version4["title_es"],
                found_index=ComponentsUpdatePage.version4["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(version4, "Versión:")
