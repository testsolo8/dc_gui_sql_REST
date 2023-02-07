# Standart libraries
import time

# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import TaskManagementPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y07{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def sql_server_connection_setting_window(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y07{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.by(name=TaskManagementPage.setup_connection_to_db["title_es"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("ESP Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsES
@pytest.mark.testGUI_EspVersionDCTest_ControlsTest_Additionalfeatures
class TestTaskManagementPage:
    @allure.story("тест главного окна настройки TaskManagement")
    class TestTaskManagementMainPage:
        def test_cancel_button(self, handle):
            cancel_button = (
                handle.by(name=TaskManagementPage.cancel_button["title_es"])
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Cancelar")

        def test_apply_button(self, handle):
            apply_button = (
                handle.by(name=TaskManagementPage.apply_button["title_es"])
                .find()
                .window_text()
            )
            check.equal(apply_button, "Aplicar")

        def test_setup_connection_to_db(self, handle):
            setup_connection_to_db = (
                handle.by(name=TaskManagementPage.setup_connection_to_db["title_es"])
                .find()
                .window_text()
            )
            check.equal(setup_connection_to_db, "Configurar conexión a base de datos")

        def test_frm_task_management(self, handle):
            frm_task_management = (
                handle.by(name=TaskManagementPage.frm_task_management["title_es"])
                .find()
                .window_text()
            )
            check.equal(frm_task_management, "frmTaskManagement")

        def test_connection_to_database(self, handle):
            connection_to_database = (
                handle.by(name=TaskManagementPage.connection_to_database["title_es"])
                .find()
                .window_text()
            )
            check.equal(connection_to_database, "Conexión a la base de datos")

    @allure.story("тест окна настройки подключения к БД TaskManagement")
    class TestSQLServerConnectionSettingWindow:
        def test_sql_server_connection_settings(
            self, sql_server_connection_setting_window
        ):
            sql_server_connection_settings = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.sql_server_connection_settings["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_connection_settings, "Parámetros de conexión a SQL Server"
            )

        def test_create_button(self, sql_server_connection_setting_window):
            create_button = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.create_button["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(create_button, "Crear")

        def test_database_name(self, sql_server_connection_setting_window):
            database_name = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.database_name["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(database_name, "Nombre de base de datos:")

        def test_password(self, sql_server_connection_setting_window):
            password = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.password["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(password, "Contraseña:")

        def test_username(self, sql_server_connection_setting_window):
            username = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.username["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(username, "Nombre de usuario:")

        def test_sql_server_authentication_mode(
            self, sql_server_connection_setting_window
        ):
            sql_server_authentication_mode = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.sql_server_authentication_mode["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_authentication_mode,
                "Usar autenticación de SQL Server interna",
            )

        def test_windows_authentication_mode(
            self, sql_server_connection_setting_window
        ):
            windows_authentication_mode = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.windows_authentication_mode["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(windows_authentication_mode, "Usar autenticación Windows")

        def test_read_from_dc(self, sql_server_connection_setting_window):
            read_from_dc = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.read_from_dc["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(read_from_dc, "Leer de DC")

        def test_server_name(self, sql_server_connection_setting_window):
            server_name = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.server_name["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(server_name, "Nombre del servidor")

        def test_server_type(self, sql_server_connection_setting_window):
            server_type = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.server_type["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(server_type, "Tipo del servidor")

        def test_cancel_button2(self, sql_server_connection_setting_window):
            cancel_button2 = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.cancel_button2["title_es"],
                    found_index=TaskManagementPage.cancel_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button2, "Cancelar")

        def test_ok_button(self, sql_server_connection_setting_window):
            ok_button = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.ok_button["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(ok_button, "OK")

        def test_check_connection(self, sql_server_connection_setting_window):
            check_connection = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.check_connection["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection, "Probar conexión ")
