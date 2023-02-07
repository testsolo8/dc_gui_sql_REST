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
def handle(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y07{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def sql_server_connection_setting_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y07{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=TaskManagementPage.setup_connection_to_db["title_ru"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("RUS Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsRU
@pytest.mark.testGUI_RusVersionDCTest_ControlsTest_Additionalfeatures
class TestTaskManagementPage:
    @allure.story("тест главного окна настройки TaskManagement")
    class TestTaskManagementMainPage:
        def test_cancel_button(self, handle):
            cancel_button = (
                handle.by(name=TaskManagementPage.cancel_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Отменить")

        def test_apply_button(self, handle):
            apply_button = (
                handle.by(name=TaskManagementPage.apply_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(apply_button, "Применить")

        def test_setup_connection_to_db(self, handle):
            setup_connection_to_db = (
                handle.by(name=TaskManagementPage.setup_connection_to_db["title_ru"])
                .find()
                .window_text()
            )
            check.equal(setup_connection_to_db, "Настроить подключение к БД")

        def test_frm_task_management(self, handle):
            frm_task_management = (
                handle.by(name=TaskManagementPage.frm_task_management["title_ru"])
                .find()
                .window_text()
            )
            check.equal(frm_task_management, "frmTaskManagement")

        def test_connection_to_database(self, handle):
            connection_to_database = (
                handle.by(name=TaskManagementPage.connection_to_database["title_ru"])
                .find()
                .window_text()
            )
            check.equal(connection_to_database, "Подключение к БД")

    @allure.story("тест окна настройки подключения к БД TaskManagement")
    class TestSQLServerConnectionSettingWindow:
        def test_sql_server_connection_settings(
            self, sql_server_connection_setting_window
        ):
            sql_server_connection_settings = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.sql_server_connection_settings["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_connection_settings, "Параметры подключения к SQL Server"
            )

        def test_create_button(self, sql_server_connection_setting_window):
            create_button = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.create_button["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(create_button, "Создать")

        def test_database_name(self, sql_server_connection_setting_window):
            database_name = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.database_name["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(database_name, "Имя базы данных:")

        def test_password(self, sql_server_connection_setting_window):
            password = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.password["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(password, "Пароль:")

        def test_username(self, sql_server_connection_setting_window):
            username = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.username["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(username, "Имя пользователя:")

        def test_sql_server_authentication_mode(
            self, sql_server_connection_setting_window
        ):
            sql_server_authentication_mode = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.sql_server_authentication_mode["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_authentication_mode,
                "Использовать внутреннюю аутентификацию SQL Server",
            )

        def test_windows_authentication_mode(
            self, sql_server_connection_setting_window
        ):
            windows_authentication_mode = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.windows_authentication_mode["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                windows_authentication_mode, "Использовать аутентификацию Windows"
            )

        def test_read_from_dc(self, sql_server_connection_setting_window):
            read_from_dc = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.read_from_dc["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(read_from_dc, "Считать из DC")

        def test_server_name(self, sql_server_connection_setting_window):
            server_name = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.server_name["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(server_name, "Имя сервера:")

        def test_server_type(self, sql_server_connection_setting_window):
            server_type = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.server_type["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(server_type, "Тип сервера:")

        def test_cancel_button2(self, sql_server_connection_setting_window):
            cancel_button2 = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.cancel_button2["title_ru"],
                    found_index=TaskManagementPage.cancel_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button2, "Отменить")

        def test_ok_button(self, sql_server_connection_setting_window):
            ok_button = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.ok_button["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(ok_button, "OK")

        def test_check_connection(self, sql_server_connection_setting_window):
            check_connection = (
                sql_server_connection_setting_window.by(
                    name=TaskManagementPage.check_connection["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection, "Проверка подключения")
