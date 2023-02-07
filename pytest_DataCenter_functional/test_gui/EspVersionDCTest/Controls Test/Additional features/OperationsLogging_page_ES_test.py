# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import OperationsLoggingPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y01{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("ESP Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsES
@pytest.mark.testGUI_EspVersionDCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки журналирования операций")
class TestOperationsLoggingPage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=OperationsLoggingPage.cancel_button["title_es"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Cancelar")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=OperationsLoggingPage.apply_button["title_es"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Aplicar")

    def test_setup_connection_to_db(self, handle):
        setup_connection_to_db = (
            handle.by(name=OperationsLoggingPage.setup_connection_to_db["title_es"])
            .find()
            .window_text()
        )
        check.equal(setup_connection_to_db, "Configurar conexión a base de datos")

    def test_data_restriction_when_logging_operations(self, handle):
        data_restriction_when_logging_operations = (
            handle.by(
                name=OperationsLoggingPage.data_restriction_when_logging_operations[
                    "title_es"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            data_restriction_when_logging_operations,
            "Límite de datos registrando operaciones",
        )

    def test_list_of_products(self, handle):
        list_of_products = (
            handle.by(name=OperationsLoggingPage.list_of_products["title_es"])
            .find()
            .window_text()
        )
        check.equal(list_of_products, "Lista de productos")

    def test_connection_to_db(self, handle):
        connection_to_db = (
            handle.by(name=OperationsLoggingPage.connection_to_db["title_es"])
            .find()
            .window_text()
        )
        check.equal(connection_to_db, "Conexión a base de datos")

    def test_enable_logging_of_auditors(self, handle):
        enable_logging_of_auditors = (
            handle.by(name=OperationsLoggingPage.enable_logging_of_auditors["title_es"])
            .find()
            .window_text()
        )
        check.equal(
            enable_logging_of_auditors,
            "Habilitar registro de acciones de auditores en las consolas ",
        )
