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
def handle(start_test_page):
    send_keys("{VK_MENU down}Y4Y07{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def sql_server_connection_setting_window(start_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y07{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=TaskManagementPage.setup_connection_to_db[title_key]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Additionalfeatures
class TestTaskManagementPage:
    @allure.story("тест главного окна настройки TaskManagement")
    class TestTaskManagementMainPage:
        def test_cancel_button(self, handle, title_key):
            cancel_button = handle.by(name=TaskManagementPage.cancel_button[title_key]).find().window_text()
            check.equal(cancel_button, TaskManagementPage.cancel_button[title_key])

        def test_apply_button(self, handle, title_key):
            apply_button = handle.by(name=TaskManagementPage.apply_button[title_key]).find().window_text()
            check.equal(apply_button, TaskManagementPage.apply_button[title_key])

        def test_setup_connection_to_db(self, handle, title_key):
            setup_connection_to_db = (
                handle.by(name=TaskManagementPage.setup_connection_to_db[title_key]).find().window_text()
            )
            check.equal(setup_connection_to_db, TaskManagementPage.setup_connection_to_db[title_key])

        def test_frm_task_management(self, handle, title_key):
            frm_task_management = (
                handle.by(name=TaskManagementPage.frm_task_management[title_key]).find().window_text()
            )
            check.equal(frm_task_management, TaskManagementPage.frm_task_management[title_key])

        def test_connection_to_database(self, handle, title_key):
            connection_to_database = (
                handle.by(name=TaskManagementPage.connection_to_database[title_key]).find().window_text()
            )
            check.equal(connection_to_database, TaskManagementPage.connection_to_database[title_key])

    @allure.story("тест окна настройки подключения к БД TaskManagement")
    class TestSQLServerConnectionSettingWindow:
        def test_sql_server_connection_settings(self, sql_server_connection_setting_window, title_key):
            sql_server_connection_settings = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.sql_server_connection_settings[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(sql_server_connection_settings, TaskManagementPage.sql_server_connection_settings[title_key])

        def test_create_button(self, sql_server_connection_setting_window, title_key):
            create_button = (
                sql_server_connection_setting_window.by(name=TaskManagementPage.create_button[title_key])
                .find()
                .window_text()
            )
            check.equal(create_button, TaskManagementPage.create_button[title_key])

        def test_database_name(self, sql_server_connection_setting_window, title_key):
            database_name = (
                sql_server_connection_setting_window.by(name=TaskManagementPage.database_name[title_key])
                .find()
                .window_text()
            )
            check.equal(database_name, TaskManagementPage.database_name[title_key])

        def test_password(self, sql_server_connection_setting_window, title_key):
            password = (
                sql_server_connection_setting_window.by(name=TaskManagementPage.password[title_key])
                .find()
                .window_text()
            )
            check.equal(password, TaskManagementPage.password[title_key])

        def test_username(self, sql_server_connection_setting_window, title_key):
            username = (
                sql_server_connection_setting_window.by(name=TaskManagementPage.username[title_key])
                .find()
                .window_text()
            )
            check.equal(username, TaskManagementPage.username[title_key])

        def test_sql_server_authentication_mode(self, sql_server_connection_setting_window, title_key):
            sql_server_authentication_mode = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.sql_server_authentication_mode[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(sql_server_authentication_mode, TaskManagementPage.sql_server_authentication_mode[title_key])

        def test_windows_authentication_mode(self, sql_server_connection_setting_window, title_key):
            windows_authentication_mode = (
                sql_server_connection_setting_window.by(name=TaskManagementPage.windows_authentication_mode[title_key])
                .find()
                .window_text()
            )
            check.equal(windows_authentication_mode, TaskManagementPage.windows_authentication_mode[title_key])

        def test_read_from_dc(self, sql_server_connection_setting_window, title_key):
            read_from_dc = (
                sql_server_connection_setting_window.by(name=TaskManagementPage.read_from_dc[title_key])
                .find()
                .window_text()
            )
            check.equal(read_from_dc, TaskManagementPage.read_from_dc[title_key])

        def test_server_name(self, sql_server_connection_setting_window, title_key):
            server_name = (
                sql_server_connection_setting_window.by(name=TaskManagementPage.server_name[title_key])
                .find()
                .window_text()
            )
            check.equal(server_name, TaskManagementPage.server_name[title_key])

        def test_server_type(self, sql_server_connection_setting_window, title_key):
            server_type = (
                sql_server_connection_setting_window.by(name=TaskManagementPage.server_type[title_key])
                .find()
                .window_text()
            )
            check.equal(server_type, TaskManagementPage.server_type[title_key])

        def test_cancel_button2(self, sql_server_connection_setting_window, title_key):
            cancel_button2 = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.cancel_button2[title_key],
                    found_index=TaskManagementPage.cancel_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button2, TaskManagementPage.cancel_button2[title_key])

        def test_ok_button(self, sql_server_connection_setting_window, title_key):
            ok_button = (
                sql_server_connection_setting_window.by(name=TaskManagementPage.ok_button[title_key])
                .find()
                .window_text()
            )
            check.equal(ok_button, TaskManagementPage.ok_button[title_key])

        def test_check_connection(self, sql_server_connection_setting_window, title_key):
            check_connection = (
                sql_server_connection_setting_window.by(name=TaskManagementPage.check_connection[title_key])
                .find()
                .window_text()
            )
            check.equal(check_connection, TaskManagementPage.check_connection[title_key])
