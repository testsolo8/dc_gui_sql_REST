# Standart libraries
import time

# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import OutlookCalendarsPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y10{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("ESP Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsES
@pytest.mark.testGUI_EspVersionDCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки Outlook calendars")
class TestOutlookCalendarsPage:
    def test_cancel(self, handle):
        cancel = (
            handle.by(name=OutlookCalendarsPage.cancel["title_es"]).find().window_text()
        )
        check.equal(cancel, "Cancelar")

    def test_apply(self, handle):
        apply = (
            handle.by(name=OutlookCalendarsPage.apply["title_es"]).find().window_text()
        )
        check.equal(apply, "Aplicar")

    def test_min_1(self, handle):
        min_1 = (
            handle.__getattribute__(OutlookCalendarsPage.min_1["attribute_es"])
            .find()
            .window_text()
        )
        check.equal(min_1, "min.")

    def test_min_2(self, handle):
        min_2 = (
            handle.__getattribute__(OutlookCalendarsPage.min_2["attribute_es"])
            .find()
            .window_text()
        )
        check.equal(min_2, "min.")

    def test_connection_to_exchange_server(self, handle):
        connection_to_exchange_server = (
            handle.by(
                name=OutlookCalendarsPage.connection_to_exchange_server["title_es"]
            )
            .find()
            .window_text()
        )
        check.equal(connection_to_exchange_server, "Conexión con el servidor Exchange")

    def test_server_address(self, handle):
        server_address = (
            handle.by(name=OutlookCalendarsPage.server_address["title_es"])
            .find()
            .window_text()
        )
        check.equal(server_address, "Dirección del servidor")

    def test_username(self, handle):
        username = (
            handle.by(name=OutlookCalendarsPage.username["title_es"])
            .find()
            .window_text()
        )
        check.equal(username, "Nombre del usuario")

    def test_password(self, handle):
        password = (
            handle.by(name=OutlookCalendarsPage.password["title_es"])
            .find()
            .window_text()
        )
        check.equal(password, "Contraseña")

    def test_maximum_time_of_script_execution(self, handle):
        maximum_time_of_script_execution = (
            handle.by(
                name=OutlookCalendarsPage.maximum_time_of_script_execution["title_es"]
            )
            .find()
            .window_text()
        )
        check.equal(
            maximum_time_of_script_execution, "Tiempo máximo de ejecución del script "
        )

    def test_read_calendars_every(self, handle):
        read_calendars_every = (
            handle.by(name=OutlookCalendarsPage.read_calendars_every["title_es"])
            .find()
            .window_text()
        )
        check.equal(read_calendars_every, "Leer calendarios cada ")

    def test_externalAPI_address(self, handle):
        externalAPI_address = (
            handle.by(name=OutlookCalendarsPage.externalAPI_address["title_es"])
            .find()
            .window_text()
        )
        check.equal(externalAPI_address, "Dirección de ExternalAPI")

    def test_disabled(self, handle):
        disabled = (
            handle.by(name=OutlookCalendarsPage.disabled["title_es"])
            .find()
            .window_text()
        )
        check.equal(disabled, "Deshabilitado")

    def test_log_level(self, handle):
        log_level = (
            handle.by(name=OutlookCalendarsPage.log_level["title_es"])
            .find()
            .window_text()
        )
        check.equal(log_level, "Nivel de registro ")

    def test_start_service_of_reading_outlook_calendars(self, handle):
        start_service_of_reading_outlook_calendars = (
            handle.by(
                name=OutlookCalendarsPage.start_service_of_reading_outlook_calendars[
                    "title_es"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            start_service_of_reading_outlook_calendars,
            "Iniciar el servicio de lectura de los calendarios de Outlook",
        )
