# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import DefaultDatabasePage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def handle_add_server(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DefaultDatabasePage.add_button["title_ru"]).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_edit_server(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DefaultDatabasePage.edit_button["title_ru"]).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_delete_server(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y3Y2{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DefaultDatabasePage.delete_button["title_ru"]).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("RUS Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControlsRU
@pytest.mark.testGUI_RusVersionDCTest_ControlsTest_Settings
class TestDefaultDatabasePage:
    @allure.story("тест главного окна настройки БД по умолчанию")
    class TestDefaultDatabaseMainPage:
        def test_cancel_button(self, handle):
            cancel_button = (
                handle.by(name=DefaultDatabasePage.cancel_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Отменить")

        def test_apply_button(self, handle):
            apply_button = (
                handle.by(name=DefaultDatabasePage.apply_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(apply_button, "Применить")

        def test_edit_button(self, handle):
            edit_button = (
                handle.by(name=DefaultDatabasePage.edit_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(edit_button, "Редактировать")

        def test_delete_button(self, handle):
            delete_button = (
                handle.by(name=DefaultDatabasePage.delete_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(delete_button, "Удалить")

        def test_add_button(self, handle):
            add_button = (
                handle.by(name=DefaultDatabasePage.add_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(add_button, "Добавить")

        def test_connection_settings(self, handle):
            connection_settings = (
                handle.by(name=DefaultDatabasePage.connection_settings["title_ru"])
                .find()
                .window_text()
            )
            check.equal(
                connection_settings,
                "Создайте список серверов, укажите настройки подключения и параметры формирования имени базы данных.",
            )

        def test_servers(self, handle):
            servers = (
                handle.by(name=DefaultDatabasePage.servers["title_ru"])
                .find()
                .window_text()
            )
            check.equal(servers, "Серверы")

        def test_create_database(self, handle):
            create_database = (
                handle.by(name=DefaultDatabasePage.create_database["title_ru"])
                .find()
                .window_text()
            )
            check.equal(
                create_database, "Формировать имя базы данных из следующих параметров:"
            )

        def test_smtp_servers_integration(self, handle):
            smtp_servers_integration = (
                handle.by(name=DefaultDatabasePage.smtp_servers_integration["title_ru"])
                .find()
                .window_text()
            )
            check.equal(smtp_servers_integration, "SMTP servers integration")

        def test_datacenter(self, handle):
            datacenter = (
                handle.by(name=DefaultDatabasePage.datacenter["title_ru"])
                .find()
                .window_text()
            )
            check.equal(datacenter, "DataCenter")

        def test_mail_servers_integration(self, handle):
            mail_servers_integration = (
                handle.by(name=DefaultDatabasePage.mail_servers_integration["title_ru"])
                .find()
                .window_text()
            )
            check.equal(mail_servers_integration, "Mail servers integration")

        def test_reportcenter(self, handle):
            reportcenter = (
                handle.by(name=DefaultDatabasePage.reportcenter["title_ru"])
                .find()
                .window_text()
            )
            check.equal(reportcenter, "ReportCenter")

        def test_alertcenter(self, handle):
            alertcenter = (
                handle.by(name=DefaultDatabasePage.alertcenter["title_ru"])
                .find()
                .window_text()
            )
            check.equal(alertcenter, "AlertCenter")

        def test_endpointcontroller(self, handle):
            endpointcontroller = (
                handle.by(name=DefaultDatabasePage.endpointcontroller["title_ru"])
                .find()
                .window_text()
            )
            check.equal(endpointcontroller, "EndpointController")

        def test_networkcontroller(self, handle):
            networkcontroller = (
                handle.by(name=DefaultDatabasePage.networkcontroller["title_ru"])
                .find()
                .window_text()
            )
            check.equal(networkcontroller, "NetworkController")

        def test_component_parameter(self, handle):
            component_parameter = (
                handle.by(name=DefaultDatabasePage.component_parameter["title_ru"])
                .find()
                .window_text()
            )
            check.equal(component_parameter, "Параметр компонента (продукт, протокол)")

        def test_db_suffix_center_components(self, handle):
            db_suffix_center_components = (
                handle.by(
                    name=DefaultDatabasePage.db_suffix_center_components["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                db_suffix_center_components, "Суффикс имени БД для компонентов Center"
            )

        def test_db_suffix_controller_components(self, handle):
            db_suffix_controller_components = (
                handle.by(
                    name=DefaultDatabasePage.db_suffix_controller_components["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                db_suffix_controller_components,
                "Суффикс имени БД для компонентов Controller",
            )

        def test_component_id(self, handle):
            component_id = (
                handle.by(name=DefaultDatabasePage.component_id["title_ru"])
                .find()
                .window_text()
            )
            check.equal(component_id, "Идентификатор компонента")

        def test_prefix(self, handle):
            prefix = (
                handle.by(name=DefaultDatabasePage.prefix["title_ru"])
                .find()
                .window_text()
            )
            check.equal(prefix, "Префикс")

        def test_server_with_installed_component(self, handle):
            server_with_installed_component = (
                handle.by(
                    name=DefaultDatabasePage.server_with_installed_component["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                server_with_installed_component,
                "Имя сервера, на котором установлен компонент",
            )

    @allure.story("тест окна добавления сервера на закладке настройки БД по умолчанию")
    class TestDefaultDatabaseAddServerWindow:

        # Начало теста окна добавления сервера
        def test_add_server_window(self, handle_add_server):
            add_server = (
                handle_add_server.by(name=DefaultDatabasePage.add_server["title_ru"])
                .find()
                .window_text()
            )
            check.equal(add_server, "Добавление сервера")

        def test_connection_settings2(self, handle_add_server):
            connection_settings2 = (
                handle_add_server.by(
                    name=DefaultDatabasePage.connection_settings2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(connection_settings2, "Настройки подключения")

        def test_check_connection(self, handle_add_server):
            check_connection = (
                handle_add_server.by(
                    name=DefaultDatabasePage.check_connection["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection, "Проверка подключения")

        def test_sql_server_authentication_mode(self, handle_add_server):
            sql_server_authentication_mode = (
                handle_add_server.by(
                    name=DefaultDatabasePage.sql_server_authentication_mode["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_authentication_mode,
                "Использовать внутреннюю аутентификацию SQL Server",
            )

        def test_windows_authentication_mode(self, handle_add_server):
            windows_authentication_mode = (
                handle_add_server.by(
                    name=DefaultDatabasePage.windows_authentication_mode["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                windows_authentication_mode, "Использовать аутентификацию Windows"
            )

        def test_password(self, handle_add_server):
            password = (
                handle_add_server.by(name=DefaultDatabasePage.password["title_ru"])
                .find()
                .window_text()
            )
            check.equal(password, "Пароль:")

        def test_username(self, handle_add_server):
            username = (
                handle_add_server.by(name=DefaultDatabasePage.username["title_ru"])
                .find()
                .window_text()
            )
            check.equal(username, "Имя пользователя:")

        def test_cancel(self, handle_add_server):
            cancel = (
                handle_add_server.by(
                    name=DefaultDatabasePage.cancel["title_ru"],
                    found_index=DefaultDatabasePage.cancel["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel, "Отменить")

        def test_add(self, handle_add_server):
            add = (
                handle_add_server.by(
                    name=DefaultDatabasePage.add["title_ru"],
                    found_index=DefaultDatabasePage.cancel["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(add, "Добавить")

        def test_server_name(self, handle_add_server):
            server_name = (
                handle_add_server.by(name=DefaultDatabasePage.server_name["title_ru"])
                .find()
                .window_text()
            )
            check.equal(server_name, "Имя сервера:")

        def test_server_type(self, handle_add_server):
            server_type = (
                handle_add_server.by(name=DefaultDatabasePage.server_type["title_ru"])
                .find()
                .window_text()
            )
            check.equal(server_type, "Тип сервера:")

        # Конец теста окна добавления сервера

    @allure.story(
        "тест окна редактирования сервера на закладке настройки БД по умолчанию"
    )
    class TestDefaultDatabaseEditServerWindow:
        # Начало теста окна редактирования сервера
        def test_connection_settings3(self, handle_edit_server):
            connection_settings3 = (
                handle_edit_server.by(
                    name=DefaultDatabasePage.connection_settings3["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(connection_settings3, "Настройки подключения")

        def test_check_connection2(self, handle_edit_server):
            check_connection2 = (
                handle_edit_server.by(
                    name=DefaultDatabasePage.check_connection2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection2, "Проверка подключения")

        def test_sql_server_authentication_mode2(self, handle_edit_server):
            sql_server_authentication_mode2 = (
                handle_edit_server.by(
                    name=DefaultDatabasePage.sql_server_authentication_mode2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_authentication_mode2,
                "Использовать внутреннюю аутентификацию SQL Server",
            )

        def test_windows_authentication_mode2(self, handle_edit_server):
            windows_authentication_mode2 = (
                handle_edit_server.by(
                    name=DefaultDatabasePage.windows_authentication_mode2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                windows_authentication_mode2, "Использовать аутентификацию Windows"
            )

        def test_password2(self, handle_edit_server):
            password2 = (
                handle_edit_server.by(name=DefaultDatabasePage.password2["title_ru"])
                .find()
                .window_text()
            )
            check.equal(password2, "Пароль:")

        def test_username2(self, handle_edit_server):
            username2 = (
                handle_edit_server.by(name=DefaultDatabasePage.username2["title_ru"])
                .find()
                .window_text()
            )
            check.equal(username2, "Имя пользователя:")

        def test_cancel2(self, handle_edit_server):
            cancel2 = (
                handle_edit_server.by(
                    name=DefaultDatabasePage.cancel2["title_ru"],
                    found_index=DefaultDatabasePage.cancel["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel2, "Отменить")

        def test_ok_button(self, handle_edit_server):
            ok_button = (
                handle_edit_server.by(
                    name=DefaultDatabasePage.ok_button["title_ru"],
                    found_index=DefaultDatabasePage.cancel["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(ok_button, "OK")

        def test_server_name2(self, handle_edit_server):
            server_name2 = (
                handle_edit_server.by(name=DefaultDatabasePage.server_name2["title_ru"])
                .find()
                .window_text()
            )
            check.equal(server_name2, "Имя сервера:")

        def test_server_type2(self, handle_edit_server):
            server_type2 = (
                handle_edit_server.by(name=DefaultDatabasePage.server_type2["title_ru"])
                .find()
                .window_text()
            )
            check.equal(server_type2, "Тип сервера:")

        # Конец теста окна редактирования сервера

    @allure.story("тест окна удаления сервера на закладке настройки БД по умолчанию")
    class TestDefaultDatabaseDeleteServerWindow:
        # Начало теста окна удаления сервера
        def test_confirm(self, handle_delete_server):
            confirm = (
                handle_delete_server.by(name=DefaultDatabasePage.confirm["title_ru"])
                .find()
                .window_text()
            )
            check.equal(confirm, "Подтверждение")

        def test_no_button(self, handle_delete_server):
            no_button = (
                handle_delete_server.by(name=DefaultDatabasePage.no_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(no_button, "Нет")

        def test_yes_button(self, handle_delete_server):
            yes_button = (
                handle_delete_server.by(name=DefaultDatabasePage.yes_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(yes_button, "Да")

        # Конец теста окна удаления сервера
