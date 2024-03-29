# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import DefaultDatabasePage


@pytest.fixture(scope="class")
def handle(start_test_page):
    send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def handle_add_server(start_test_page, title_key):
    send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DefaultDatabasePage.add_button[title_key]).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_edit_server(start_test_page, title_key):
    send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DefaultDatabasePage.edit_button[title_key]).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_delete_server(start_test_page, title_key):
    send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DefaultDatabasePage.delete_button[title_key]).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Settings
class TestDefaultDatabasePage:
    @allure.story("тест главного окна настройки БД по умолчанию")
    class TestDefaultDatabaseMainPage:
        def test_cancel_button(self, handle, title_key):
            cancel_button = handle.by(name=DefaultDatabasePage.cancel_button[title_key]).find().window_text()
            check.equal(cancel_button, DefaultDatabasePage.cancel_button[title_key])

        def test_apply_button(self, handle, title_key):
            apply_button = handle.by(name=DefaultDatabasePage.apply_button[title_key]).find().window_text()
            check.equal(apply_button, DefaultDatabasePage.apply_button[title_key])

        def test_edit_button(self, handle, title_key):
            edit_button = handle.by(name=DefaultDatabasePage.edit_button[title_key]).find().window_text()
            check.equal(edit_button, DefaultDatabasePage.edit_button[title_key])

        def test_delete_button(self, handle, title_key):
            delete_button = handle.by(name=DefaultDatabasePage.delete_button[title_key]).find().window_text()
            check.equal(delete_button, DefaultDatabasePage.delete_button[title_key])

        def test_add_button(self, handle, title_key):
            add_button = handle.by(name=DefaultDatabasePage.add_button[title_key]).find().window_text()
            check.equal(add_button, DefaultDatabasePage.add_button[title_key])

        def test_connection_settings(self, handle, title_key):
            connection_settings = (
                handle.by(name=DefaultDatabasePage.connection_settings[title_key]).find().window_text()
            )
            check.equal(
                connection_settings,
                DefaultDatabasePage.connection_settings[title_key],
            )

        def test_servers(self, handle, title_key):
            servers = handle.by(name=DefaultDatabasePage.servers[title_key]).find().window_text()
            check.equal(servers, DefaultDatabasePage.servers[title_key])

        def test_create_database(self, handle, title_key):
            create_database = handle.by(name=DefaultDatabasePage.create_database[title_key]).find().window_text()
            check.equal(
                create_database,
                DefaultDatabasePage.create_database[title_key],
            )

        def test_smtp_servers_integration(self, handle, title_key):
            smtp_servers_integration = (
                handle.by(name=DefaultDatabasePage.smtp_servers_integration[title_key]).find().window_text()
            )
            check.equal(smtp_servers_integration, DefaultDatabasePage.smtp_servers_integration[title_key])

        def test_datacenter(self, handle, title_key):
            datacenter = handle.by(name=DefaultDatabasePage.datacenter[title_key]).find().window_text()
            check.equal(datacenter, DefaultDatabasePage.datacenter[title_key])

        def test_mail_servers_integration(self, handle, title_key):
            mail_servers_integration = (
                handle.by(name=DefaultDatabasePage.mail_servers_integration[title_key]).find().window_text()
            )
            check.equal(mail_servers_integration, DefaultDatabasePage.mail_servers_integration[title_key])

        def test_reportcenter(self, handle, title_key):
            reportcenter = handle.by(name=DefaultDatabasePage.reportcenter[title_key]).find().window_text()
            check.equal(reportcenter, DefaultDatabasePage.reportcenter[title_key])

        def test_alertcenter(self, handle, title_key):
            alertcenter = handle.by(name=DefaultDatabasePage.alertcenter[title_key]).find().window_text()
            check.equal(alertcenter, DefaultDatabasePage.alertcenter[title_key])

        def test_endpointcontroller(self, handle, title_key):
            endpointcontroller = handle.by(name=DefaultDatabasePage.endpointcontroller[title_key]).find().window_text()
            check.equal(endpointcontroller, DefaultDatabasePage.endpointcontroller[title_key])

        def test_networkcontroller(self, handle, title_key):
            networkcontroller = handle.by(name=DefaultDatabasePage.networkcontroller[title_key]).find().window_text()
            check.equal(networkcontroller, DefaultDatabasePage.networkcontroller[title_key])

        def test_component_parameter(self, handle, title_key):
            component_parameter = (
                handle.by(name=DefaultDatabasePage.component_parameter[title_key]).find().window_text()
            )
            check.equal(component_parameter, DefaultDatabasePage.component_parameter[title_key])

        def test_db_suffix_center_components(self, handle, title_key):
            db_suffix_center_components = (
                handle.by(name=DefaultDatabasePage.db_suffix_center_components[title_key]).find().window_text()
            )
            check.equal(db_suffix_center_components, DefaultDatabasePage.db_suffix_center_components[title_key])

        def test_db_suffix_controller_components(self, handle, title_key):
            db_suffix_controller_components = (
                handle.by(name=DefaultDatabasePage.db_suffix_controller_components[title_key]).find().window_text()
            )
            check.equal(
                db_suffix_controller_components,
                DefaultDatabasePage.db_suffix_controller_components[title_key],
            )

        def test_component_id(self, handle, title_key):
            component_id = handle.by(name=DefaultDatabasePage.component_id[title_key]).find().window_text()
            check.equal(component_id, DefaultDatabasePage.component_id[title_key])

        def test_prefix(self, handle, title_key):
            prefix = handle.by(name=DefaultDatabasePage.prefix[title_key]).find().window_text()
            check.equal(prefix, DefaultDatabasePage.prefix[title_key])

        def test_server_with_installed_component(self, handle, title_key):
            server_with_installed_component = (
                handle.by(name=DefaultDatabasePage.server_with_installed_component[title_key]).find().window_text()
            )
            check.equal(server_with_installed_component, DefaultDatabasePage.server_with_installed_component[title_key])

    @allure.story("тест окна добавления сервера на закладке настройки БД по умолчанию")
    class TestDefaultDatabaseAddServerWindow:
        # Начало теста окна добавления сервера
        def test_add_server_window(self, handle_add_server, title_key):
            add_server = handle_add_server.by(name=DefaultDatabasePage.add_server[title_key]).find().window_text()
            check.equal(add_server, DefaultDatabasePage.add_server[title_key])

        def test_connection_settings2(self, handle_add_server, title_key):
            connection_settings2 = (
                handle_add_server.by(name=DefaultDatabasePage.connection_settings2[title_key]).find().window_text()
            )
            check.equal(connection_settings2, DefaultDatabasePage.connection_settings2[title_key])

        def test_check_connection(self, handle_add_server, title_key):
            check_connection = (
                handle_add_server.by(name=DefaultDatabasePage.check_connection[title_key]).find().window_text()
            )
            check.equal(check_connection, DefaultDatabasePage.check_connection[title_key])

        def test_sql_server_authentication_mode(self, handle_add_server, title_key):
            sql_server_authentication_mode = (
                handle_add_server.by(name=DefaultDatabasePage.sql_server_authentication_mode[title_key])
                .find()
                .window_text()
            )
            check.equal(sql_server_authentication_mode, DefaultDatabasePage.sql_server_authentication_mode[title_key])

        def test_windows_authentication_mode(self, handle_add_server, title_key):
            windows_authentication_mode = (
                handle_add_server.by(name=DefaultDatabasePage.windows_authentication_mode[title_key])
                .find()
                .window_text()
            )
            check.equal(windows_authentication_mode, DefaultDatabasePage.windows_authentication_mode[title_key])

        def test_password(self, handle_add_server, title_key):
            password = handle_add_server.by(name=DefaultDatabasePage.password[title_key]).find().window_text()
            check.equal(password, DefaultDatabasePage.password[title_key])

        def test_username(self, handle_add_server, title_key):
            username = handle_add_server.by(name=DefaultDatabasePage.username[title_key]).find().window_text()
            check.equal(username, DefaultDatabasePage.username[title_key])

        def test_cancel(self, handle_add_server, title_key):
            cancel = (
                handle_add_server.by(
                    name=DefaultDatabasePage.cancel[title_key],
                    found_index=DefaultDatabasePage.cancel["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel, DefaultDatabasePage.cancel[title_key])

        def test_add(self, handle_add_server, title_key):
            add = (
                handle_add_server.by(
                    name=DefaultDatabasePage.add[title_key],
                    found_index=DefaultDatabasePage.cancel["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(add, DefaultDatabasePage.add[title_key])

        def test_server_name(self, handle_add_server, title_key):
            server_name = handle_add_server.by(name=DefaultDatabasePage.server_name[title_key]).find().window_text()
            check.equal(server_name, DefaultDatabasePage.server_name[title_key])

        def test_server_type(self, handle_add_server, title_key):
            server_type = handle_add_server.by(name=DefaultDatabasePage.server_type[title_key]).find().window_text()
            check.equal(server_type, DefaultDatabasePage.server_type[title_key])

        # Конец теста окна добавления сервера

    @allure.story("тест окна редактирования сервера на закладке настройки БД по умолчанию")
    class TestDefaultDatabaseEditServerWindow:
        # Начало теста окна редактирования сервера
        def test_connection_settings3(self, handle_edit_server, title_key):
            connection_settings3 = (
                handle_edit_server.by(name=DefaultDatabasePage.connection_settings3[title_key]).find().window_text()
            )
            check.equal(connection_settings3, DefaultDatabasePage.connection_settings3[title_key])

        def test_check_connection2(self, handle_edit_server, title_key):
            check_connection2 = (
                handle_edit_server.by(name=DefaultDatabasePage.check_connection2[title_key]).find().window_text()
            )
            check.equal(check_connection2, DefaultDatabasePage.check_connection2[title_key])

        def test_sql_server_authentication_mode2(self, handle_edit_server, title_key):
            sql_server_authentication_mode2 = (
                handle_edit_server.by(name=DefaultDatabasePage.sql_server_authentication_mode2[title_key])
                .find()
                .window_text()
            )
            check.equal(sql_server_authentication_mode2, DefaultDatabasePage.sql_server_authentication_mode2[title_key])

        def test_windows_authentication_mode2(self, handle_edit_server, title_key):
            windows_authentication_mode2 = (
                handle_edit_server.by(name=DefaultDatabasePage.windows_authentication_mode2[title_key])
                .find()
                .window_text()
            )
            check.equal(windows_authentication_mode2, DefaultDatabasePage.windows_authentication_mode2[title_key])

        def test_password2(self, handle_edit_server, title_key):
            password2 = handle_edit_server.by(name=DefaultDatabasePage.password2[title_key]).find().window_text()
            check.equal(password2, DefaultDatabasePage.password2[title_key])

        def test_username2(self, handle_edit_server, title_key):
            username2 = handle_edit_server.by(name=DefaultDatabasePage.username2[title_key]).find().window_text()
            check.equal(username2, DefaultDatabasePage.username2[title_key])

        def test_cancel2(self, handle_edit_server, title_key):
            cancel2 = (
                handle_edit_server.by(
                    name=DefaultDatabasePage.cancel2[title_key],
                    found_index=DefaultDatabasePage.cancel["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel2, DefaultDatabasePage.cancel2[title_key])

        def test_ok_button(self, handle_edit_server, title_key):
            ok_button = (
                handle_edit_server.by(
                    name=DefaultDatabasePage.ok_button[title_key],
                    found_index=DefaultDatabasePage.cancel["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(ok_button, DefaultDatabasePage.ok_button[title_key])

        def test_server_name2(self, handle_edit_server, title_key):
            server_name2 = handle_edit_server.by(name=DefaultDatabasePage.server_name2[title_key]).find().window_text()
            check.equal(server_name2, DefaultDatabasePage.server_name2[title_key])

        def test_server_type2(self, handle_edit_server, title_key):
            server_type2 = handle_edit_server.by(name=DefaultDatabasePage.server_type2[title_key]).find().window_text()
            check.equal(server_type2, DefaultDatabasePage.server_type2[title_key])

        # Конец теста окна редактирования сервера

    @allure.story("тест окна удаления сервера на закладке настройки БД по умолчанию")
    class TestDefaultDatabaseDeleteServerWindow:
        # Начало теста окна удаления сервера
        def test_confirm(self, handle_delete_server, title_key):
            confirm = handle_delete_server.by(name=DefaultDatabasePage.confirm[title_key]).find().window_text()
            check.equal(confirm, DefaultDatabasePage.confirm[title_key])

        def test_no_button(self, handle_delete_server, title_key):
            no_button = handle_delete_server.by(name=DefaultDatabasePage.no_button[title_key]).find().window_text()
            check.equal(no_button, DefaultDatabasePage.no_button[title_key])

        def test_yes_button(self, handle_delete_server, title_key):
            yes_button = handle_delete_server.by(name=DefaultDatabasePage.yes_button[title_key]).find().window_text()
            check.equal(yes_button, DefaultDatabasePage.yes_button[title_key])

        # Конец теста окна удаления сервера
