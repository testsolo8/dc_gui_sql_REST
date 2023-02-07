# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import AttributesStoragePage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y08{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("ESP Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsES
@pytest.mark.testGUI_EspVersionDCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки хранилища атрибутов")
class TestAttributesStoragePage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=AttributesStoragePage.cancel_button["title_es"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Cancelar")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=AttributesStoragePage.apply_button["title_es"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Aplicar")

    def test_clear_database(self, handle):
        clear_database = (
            handle.by(name=AttributesStoragePage.clear_database["title_es"])
            .find()
            .window_text()
        )
        check.equal(clear_database, "Borrar base de datos")

    def test_setup_connection_to_db(self, handle):
        setup_connection_to_db = (
            handle.by(name=AttributesStoragePage.setup_connection_to_db["title_es"])
            .find()
            .window_text()
        )
        check.equal(setup_connection_to_db, "Configurar conexión a base de datos")

    def test_months(self, handle):
        months = (
            handle.by(name=AttributesStoragePage.months["title_es"])
            .find()
            .window_text()
        )
        check.equal(months, "meses")

    def test_read_data_for_the_last(self, handle):
        read_data_for_the_last = (
            handle.by(name=AttributesStoragePage.read_data_for_the_last["title_es"])
            .find()
            .window_text()
        )
        check.equal(read_data_for_the_last, "Leer datos para los últimos")

    def test_use_storage_of_attributes(self, handle):
        use_storage_of_attributes = (
            handle.by(name=AttributesStoragePage.use_storage_of_attributes["title_es"])
            .find()
            .window_text()
        )
        check.equal(use_storage_of_attributes, "Usar almacenaje de atributos ")

    def test_log_level(self, handle):
        log_level = (
            handle.by(name=AttributesStoragePage.log_level["title_es"])
            .find()
            .window_text()
        )
        check.equal(log_level, "Nivel de registro ")

    def test_connection_to_db(self, handle):
        connection_to_db = (
            handle.by(name=AttributesStoragePage.connection_to_db["title_es"])
            .find()
            .window_text()
        )
        check.equal(connection_to_db, "Conexión a base de datos")

    def test_sql_server(self, handle):
        sql_server = (
            handle.by(name=AttributesStoragePage.sql_server["title_es"])
            .find()
            .window_text()
        )
        check.equal(sql_server, "Servidor SQL ")

    def test_database(self, handle):
        database = (
            handle.by(name=AttributesStoragePage.database["title_es"])
            .find()
            .window_text()
        )
        check.equal(database, "Base de datos")
