# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import ActiveDirectoryPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def handle_sql_connection_settings(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=ActiveDirectoryPage.setup_connection_db["title_ru"]).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_add_domain(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(
        name=ActiveDirectoryPage.synchronization_with_active_directory["title_ru"]
    ).__getattribute__("Button3").click()
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_add_workgroup_user(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(
        name=ActiveDirectoryPage.add_button2["title_ru"],
        found_index=ActiveDirectoryPage.add_button2["found_index"],
    ).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_add_internal_user(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(
        name=ActiveDirectoryPage.add_button["title_ru"],
        found_index=ActiveDirectoryPage.add_button["found_index"],
    ).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("RUS Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControlsRU
@pytest.mark.testGUI_RusVersionDCTest_ControlsTest_Settings
class TestActiveDirectoryPage:
    @allure.story("тест главного окна настройки AD")
    class TestActiveDirectoryMainPage:
        def test_cancel_button(self, handle):
            cancel_button = (
                handle.by(name=ActiveDirectoryPage.cancel_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Отменить")

        def test_apply_button(self, handle):
            apply_button = (
                handle.by(name=ActiveDirectoryPage.apply_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(apply_button, "Применить")

        def test_internal_users(self, handle):
            internal_users = (
                handle.by(name=ActiveDirectoryPage.internal_users["title_ru"])
                .find()
                .window_text()
            )
            check.equal(internal_users, "Внутренние пользователи")

        def test_delete_button(self, handle):
            delete_button = (
                handle.by(
                    name=ActiveDirectoryPage.delete_button["title_ru"],
                    found_index=ActiveDirectoryPage.delete_button["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(delete_button, "Удалить")

        def test_change_button(self, handle):
            change_button = (
                handle.by(
                    name=ActiveDirectoryPage.change_button["title_ru"],
                    found_index=ActiveDirectoryPage.change_button["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(change_button, "Изменить")

        def test_add_button(self, handle):
            add_button = (
                handle.by(
                    name=ActiveDirectoryPage.add_button["title_ru"],
                    found_index=ActiveDirectoryPage.add_button["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(add_button, "Добавить")

        def test_users_work_groups(self, handle):
            users_work_groups = (
                handle.by(name=ActiveDirectoryPage.users_work_groups["title_ru"])
                .find()
                .window_text()
            )
            check.equal(users_work_groups, "Пользователи рабочих групп")

        def test_delete_button2(self, handle):
            delete_button2 = (
                handle.by(
                    name=ActiveDirectoryPage.delete_button2["title_ru"],
                    found_index=ActiveDirectoryPage.delete_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(delete_button2, "Удалить")

        def test_change_button2(self, handle):
            change_button2 = (
                handle.by(
                    name=ActiveDirectoryPage.change_button2["title_ru"],
                    found_index=ActiveDirectoryPage.change_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(change_button2, "Изменить")

        def test_add_button2(self, handle):
            add_button2 = (
                handle.by(
                    name=ActiveDirectoryPage.add_button2["title_ru"],
                    found_index=ActiveDirectoryPage.add_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(add_button2, "Добавить")

        def test_list_of_attributes(self, handle):
            list_of_attributes = (
                handle.by(name=ActiveDirectoryPage.list_of_attributes["title_ru"])
                .find()
                .window_text()
            )
            check.equal(list_of_attributes, "Список атрибутов")

        def test_synchronization_with_active_directory(self, handle):
            synchronization_with_active_directory = (
                handle.by(
                    name=ActiveDirectoryPage.synchronization_with_active_directory[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                synchronization_with_active_directory,
                "Синхронизация с Active Directory",
            )

        def test_setup_connection_db(self, handle):
            setup_connection_db = (
                handle.by(name=ActiveDirectoryPage.setup_connection_db["title_ru"])
                .find()
                .window_text()
            )
            check.equal(setup_connection_db, "Настроить подключение к БД")

    @allure.story("тест окна настройки подключения к бд ДЦ закладки AD")
    class TestSQLConnectionSettingsWindow:
        def test_sql_server_connection_settings(self, handle_sql_connection_settings):
            sql_server_connection_settings = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.sql_server_connection_settings["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_connection_settings, "Параметры подключения к SQL Server"
            )

        def test_create(self, handle_sql_connection_settings):
            create = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.create["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(create, "Создать")

        def test_database_name(self, handle_sql_connection_settings):
            database_name = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.database_name["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(database_name, "Имя базы данных:")

        def test_password(self, handle_sql_connection_settings):
            password = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.password["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(password, "Пароль:")

        def test_username(self, handle_sql_connection_settings):
            username = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.username["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(username, "Имя пользователя:")

        def test_sql_server_authentication_mode(self, handle_sql_connection_settings):
            sql_server_authentication_mode = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.sql_server_authentication_mode["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_authentication_mode,
                "Использовать внутреннюю аутентификацию SQL Server",
            )

        def test_windows_authentication_mode(self, handle_sql_connection_settings):
            windows_authentication_mode = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.windows_authentication_mode["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                windows_authentication_mode, "Использовать аутентификацию Windows"
            )

        def test_read_from_dc(self, handle_sql_connection_settings):
            read_from_dc = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.read_from_dc["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(read_from_dc, "Считать из DC")

        def test_server_name(self, handle_sql_connection_settings):
            server_name = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.server_name["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(server_name, "Имя сервера:")

        def test_server_type(self, handle_sql_connection_settings):
            server_type = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.server_type["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(server_type, "Тип сервера:")

        def test_cancel_button2(self, handle_sql_connection_settings):
            cancel_button2 = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.cancel_button2["title_ru"],
                    found_index=ActiveDirectoryPage.cancel_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button2, "Отменить")

        def test_ok_button(self, handle_sql_connection_settings):
            ok_button = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.ok_button["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(ok_button, "OK")

        def test_check_connection(self, handle_sql_connection_settings):
            check_connection = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.check_connection["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection, "Проверка подключения")

    @allure.story("тест окна добавления домена закладки AD")
    class TestAddDomainWindow:
        def test_add_domain(self, handle_add_domain):
            add_domain = (
                handle_add_domain.by(name=ActiveDirectoryPage.add_domain["title_ru"])
                .find()
                .window_text()
            )
            check.equal(add_domain, "Добавить домен")

        def test_synchronize(self, handle_add_domain):
            synchronize = (
                handle_add_domain.by(name=ActiveDirectoryPage.synchronize["title_ru"])
                .find()
                .window_text()
            )
            check.equal(synchronize, "Синхронизировать")

        def test_check_connection2(self, handle_add_domain):
            check_connection2 = (
                handle_add_domain.by(
                    name=ActiveDirectoryPage.check_connection2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection2, "Проверка подключения")

        def test_ok_button2(self, handle_add_domain):
            ok_button2 = (
                handle_add_domain.by(name=ActiveDirectoryPage.ok_button2["title_ru"])
                .find()
                .window_text()
            )
            check.equal(ok_button2, "OK")

        def test_cancel_button3(self, handle_add_domain):
            cancel_button3 = (
                handle_add_domain.by(
                    name=ActiveDirectoryPage.cancel_button3["title_ru"],
                    found_index=ActiveDirectoryPage.cancel_button3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button3, "Отменить")

        def test_active_directory(self, handle_add_domain):
            active_directory = (
                handle_add_domain.by(
                    name=ActiveDirectoryPage.active_directory["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(active_directory, "Active Directory")

        def test_azure_ad(self, handle_add_domain):
            azure_ad = (
                handle_add_domain.by(name=ActiveDirectoryPage.azure_ad["title_ru"])
                .find()
                .window_text()
            )
            check.equal(azure_ad, "Azure AD")

        def test_connect_only_domain_controller(self, handle_add_domain):
            connect_only_domain_controller = (
                handle_add_domain.by(
                    name=ActiveDirectoryPage.connect_only_domain_controller["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                connect_only_domain_controller,
                "Подключаться только к контроллеру домена",
            )

        def test_do_not_cache_data(self, handle_add_domain):
            do_not_cache_data = (
                handle_add_domain.by(
                    name=ActiveDirectoryPage.do_not_cache_data["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(do_not_cache_data, "Не использовать кэширование данных")

        def test_do_not_read_displayname_attribute(self, handle_add_domain):
            do_not_read_displayname_attribute = (
                handle_add_domain.by(
                    name=ActiveDirectoryPage.do_not_read_displayname_attribute[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                do_not_read_displayname_attribute, "Не вычитывать атрибут DisplayName"
            )

    @allure.story("тест окна добавления пользователя рабочей группы закладки AD")
    class TestAddWorkgroupUserWindow:
        def test_add_user(self, handle_add_workgroup_user):
            add_user = (
                handle_add_workgroup_user.by(
                    name=ActiveDirectoryPage.add_user["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(add_user, "Добавить пользователя")

        def test_username2(self, handle_add_workgroup_user):
            username2 = (
                handle_add_workgroup_user.by(
                    name=ActiveDirectoryPage.username2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(username2, "Полное имя")

        def test_user(self, handle_add_workgroup_user):
            user = (
                handle_add_workgroup_user.by(name=ActiveDirectoryPage.user["title_ru"])
                .find()
                .window_text()
            )
            check.equal(user, "Пользователь")

        def test_computer(self, handle_add_workgroup_user):
            computer = (
                handle_add_workgroup_user.by(
                    name=ActiveDirectoryPage.computer["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(computer, "Компьютер")

        def test_cancel_button4(self, handle_add_workgroup_user):
            cancel_button4 = (
                handle_add_workgroup_user.by(
                    name=ActiveDirectoryPage.cancel_button4["title_ru"],
                    found_index=ActiveDirectoryPage.cancel_button3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button4, "Отменить")

        def test_ok_button3(self, handle_add_workgroup_user):
            ok_button3 = (
                handle_add_workgroup_user.by(
                    name=ActiveDirectoryPage.ok_button3["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(ok_button3, "OK")

    @allure.story("тест окна добавления внутренних пользователей КИБ закладки AD")
    class TestAddInternalUserWindow:
        def test_add_user2(self, handle_add_internal_user):
            add_user2 = (
                handle_add_internal_user.by(
                    name=ActiveDirectoryPage.add_user2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(add_user2, "Добавить пользователя")

        def test_confirm_password(self, handle_add_internal_user):
            confirm_password = (
                handle_add_internal_user.by(
                    name=ActiveDirectoryPage.confirm_password["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(confirm_password, "Подтверждение")

        def test_password2(self, handle_add_internal_user):
            password2 = (
                handle_add_internal_user.by(
                    name=ActiveDirectoryPage.password2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(password2, "Пароль")

        def test_user2(self, handle_add_internal_user):
            user2 = (
                handle_add_internal_user.by(name=ActiveDirectoryPage.user2["title_ru"])
                .find()
                .window_text()
            )
            check.equal(user2, "Пользователь")

        def test_username3(self, handle_add_internal_user):
            username3 = (
                handle_add_internal_user.by(
                    name=ActiveDirectoryPage.username3["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(username3, "Полное имя")

        def test_password_validity_days(self, handle_add_internal_user):
            password_validity_days = (
                handle_add_internal_user.by(
                    name=ActiveDirectoryPage.password_validity_days["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(password_validity_days, "Срок действия пароля, дней:")

        def test_cancel_button5(self, handle_add_internal_user):
            cancel_button5 = (
                handle_add_internal_user.by(
                    name=ActiveDirectoryPage.cancel_button5["title_ru"],
                    found_index=ActiveDirectoryPage.cancel_button3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button5, "Отменить")

        def test_ok_button4s(self, handle_add_internal_user):
            ok_button4 = (
                handle_add_internal_user.by(
                    name=ActiveDirectoryPage.ok_button4["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(ok_button4, "OK")
