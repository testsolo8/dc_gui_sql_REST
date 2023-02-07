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
def handle(start_test_page_en):
    send_keys("{VK_MENU down}Y4Y07{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def sql_server_connection_setting_window(start_test_page_en):
    send_keys("{VK_MENU down}Y4Y07{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(name=TaskManagementPage.setup_connection_to_db["title_en"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("ENG Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsEN
@pytest.mark.testGUI_EngVersionDCTest_ControlsTest_Additionalfeatures
class TestTaskManagementPage:
    @allure.story("тест главного окна настройки TaskManagement")
    class TestTaskManagementMainPage:
        def test_cancel_button(self, handle):
            cancel_button = (
                handle.by(name=TaskManagementPage.cancel_button["title_en"])
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Cancel")

        def test_apply_button(self, handle):
            apply_button = (
                handle.by(name=TaskManagementPage.apply_button["title_en"])
                .find()
                .window_text()
            )
            check.equal(apply_button, "Apply")

        def test_setup_connection_to_db(self, handle):
            setup_connection_to_db = (
                handle.by(name=TaskManagementPage.setup_connection_to_db["title_en"])
                .find()
                .window_text()
            )
            check.equal(setup_connection_to_db, "Set up connection to DB ")

        def test_frm_task_management(self, handle):
            frm_task_management = (
                handle.by(name=TaskManagementPage.frm_task_management["title_en"])
                .find()
                .window_text()
            )
            check.equal(frm_task_management, "frmTaskManagement")

        def test_connection_to_database(self, handle):
            connection_to_database = (
                handle.by(name=TaskManagementPage.connection_to_database["title_en"])
                .find()
                .window_text()
            )
            check.equal(connection_to_database, "Connection to database")

    @allure.story("тест окна настройки подключения к БД TaskManagement")
    class TestSQLServerConnectionSettingWindow:
        def test_sql_server_connection_settings(
            self, sql_server_connection_setting_window
        ):
            sql_server_connection_settings = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.sql_server_connection_settings["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_connection_settings, "SQL Server connection settings"
            )

        def test_create_button(self, sql_server_connection_setting_window):
            create_button = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.create_button["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(create_button, "Create")

        def test_database_name(self, sql_server_connection_setting_window):
            database_name = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.database_name["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(database_name, "Database name:")

        def test_password(self, sql_server_connection_setting_window):
            password = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.password["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(password, "Password:")

        def test_username(self, sql_server_connection_setting_window):
            username = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.username["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(username, "Username:")

        def test_sql_server_authentication_mode(
            self, sql_server_connection_setting_window
        ):
            sql_server_authentication_mode = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.sql_server_authentication_mode["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_authentication_mode, "SQL Server Authentication mode"
            )

        def test_windows_authentication_mode(
            self, sql_server_connection_setting_window
        ):
            windows_authentication_mode = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.windows_authentication_mode["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(windows_authentication_mode, "Windows Authentication mode")

        def test_read_from_dc(self, sql_server_connection_setting_window):
            read_from_dc = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.read_from_dc["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(read_from_dc, "Read from DC")

        def test_server_name(self, sql_server_connection_setting_window):
            server_name = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.server_name["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(server_name, "Server name:")

        def test_server_type(self, sql_server_connection_setting_window):
            server_type = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.server_type["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(server_type, "Server type:")

        def test_cancel_button2(self, sql_server_connection_setting_window):
            cancel_button2 = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.cancel_button2["title_en"],
                    found_index=TaskManagementPage.cancel_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button2, "Cancel")

        def test_ok_button(self, sql_server_connection_setting_window):
            ok_button = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.ok_button["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(ok_button, "OK")

        def test_check_connection(self, sql_server_connection_setting_window):
            check_connection = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.check_connection["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection, "Check connection")
