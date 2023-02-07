# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import ActiveDirectoryPage


@pytest.fixture(scope="class")
def handle(start_test_page_en):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def handle_sql_connection_settings(start_test_page_en):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(name=ActiveDirectoryPage.setup_connection_db["title_en"]).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_add_domain(start_test_page_en):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(
        name=ActiveDirectoryPage.synchronization_with_active_directory["title_en"]
    ).__getattribute__("Button3").click()
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_add_workgroup_user(start_test_page_en):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(
        name=ActiveDirectoryPage.add_button2["title_en"],
        found_index=ActiveDirectoryPage.add_button2["found_index"],
    ).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_add_internal_user(start_test_page_en):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(
        name=ActiveDirectoryPage.add_button["title_en"],
        found_index=ActiveDirectoryPage.add_button["found_index"],
    ).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("ENG Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControlsEN
@pytest.mark.testGUI_EngVersionDCTest_ControlsTest_Settings
class TestActiveDirectoryPage:
    @allure.story("тест главного окна настройки AD")
    class TestActiveDirectoryMainPage:
        def test_cancel_button(self, handle):
            cancel_button = (
                handle.by(name=ActiveDirectoryPage.cancel_button["title_en"])
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Cancel")

        def test_apply_button(self, handle):
            apply_button = (
                handle.by(name=ActiveDirectoryPage.apply_button["title_en"])
                .find()
                .window_text()
            )
            check.equal(apply_button, "Apply")

        def test_internal_users(self, handle):
            internal_users = (
                handle.by(name=ActiveDirectoryPage.internal_users["title_en"])
                .find()
                .window_text()
            )
            check.equal(internal_users, "Internal users")

        def test_delete_button(self, handle):
            delete_button = (
                handle.by(
                    name=ActiveDirectoryPage.delete_button["title_en"],
                    found_index=ActiveDirectoryPage.delete_button["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(delete_button, "Delete")

        def test_change_button(self, handle):
            change_button = (
                handle.by(
                    name=ActiveDirectoryPage.change_button["title_en"],
                    found_index=ActiveDirectoryPage.change_button["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(change_button, "Change")

        def test_add_button(self, handle):
            add_button = (
                handle.by(
                    name=ActiveDirectoryPage.add_button["title_en"],
                    found_index=ActiveDirectoryPage.add_button["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(add_button, "Add")

        def test_users_work_groups(self, handle):
            users_work_groups = (
                handle.by(name=ActiveDirectoryPage.users_work_groups["title_en"])
                .find()
                .window_text()
            )
            check.equal(users_work_groups, "Users of work groups")

        def test_delete_button2(self, handle):
            delete_button2 = (
                handle.by(
                    name=ActiveDirectoryPage.delete_button2["title_en"],
                    found_index=ActiveDirectoryPage.delete_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(delete_button2, "Delete")

        def test_change_button2(self, handle):
            change_button2 = (
                handle.by(
                    name=ActiveDirectoryPage.change_button2["title_en"],
                    found_index=ActiveDirectoryPage.change_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(change_button2, "Change")

        def test_add_button2(self, handle):
            add_button2 = (
                handle.by(
                    name=ActiveDirectoryPage.add_button2["title_en"],
                    found_index=ActiveDirectoryPage.add_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(add_button2, "Add")

        def test_list_of_attributes(self, handle):
            list_of_attributes = (
                handle.by(name=ActiveDirectoryPage.list_of_attributes["title_en"])
                .find()
                .window_text()
            )
            check.equal(list_of_attributes, "List of attributes")

        def test_synchronization_with_active_directory(self, handle):
            synchronization_with_active_directory = (
                handle.by(
                    name=ActiveDirectoryPage.synchronization_with_active_directory[
                        "title_en"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                synchronization_with_active_directory,
                "Synchronization with Active Directory",
            )

        def test_setup_connection_db(self, handle):
            setup_connection_db = (
                handle.by(name=ActiveDirectoryPage.setup_connection_db["title_en"])
                .find()
                .window_text()
            )
            check.equal(setup_connection_db, "Set up connection to DB ")

    @allure.story("тест окна настройки подключения к бд ДЦ закладки AD")
    class TestSQLConnectionSettingsWindow:
        def test_sql_server_connection_settings(self, handle_sql_connection_settings):
            sql_server_connection_settings = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.sql_server_connection_settings["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_connection_settings, "SQL Server connection settings"
            )

        def test_create(self, handle_sql_connection_settings):
            create = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.create["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(create, "Create")

        def test_database_name(self, handle_sql_connection_settings):
            database_name = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.database_name["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(database_name, "Database name:")

        def test_password(self, handle_sql_connection_settings):
            password = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.password["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(password, "Password:")

        def test_username(self, handle_sql_connection_settings):
            username = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.username["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(username, "Username:")

        def test_sql_server_authentication_mode(self, handle_sql_connection_settings):
            sql_server_authentication_mode = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.sql_server_authentication_mode["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_authentication_mode, "SQL Server Authentication mode"
            )

        def test_windows_authentication_mode(self, handle_sql_connection_settings):
            windows_authentication_mode = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.windows_authentication_mode["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(windows_authentication_mode, "Windows Authentication mode")

        def test_read_from_dc(self, handle_sql_connection_settings):
            read_from_dc = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.read_from_dc["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(read_from_dc, "Read from DC")

        def test_server_name(self, handle_sql_connection_settings):
            server_name = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.server_name["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(server_name, "Server name:")

        def test_server_type(self, handle_sql_connection_settings):
            server_type = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.server_type["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(server_type, "Server type:")

        def test_cancel_button2(self, handle_sql_connection_settings):
            cancel_button2 = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.cancel_button2["title_en"],
                    found_index=ActiveDirectoryPage.cancel_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button2, "Cancel")

        def test_ok_button(self, handle_sql_connection_settings):
            ok_button = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.ok_button["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(ok_button, "OK")

        def test_check_connection(self, handle_sql_connection_settings):
            check_connection = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.check_connection["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection, "Check connection")

    @allure.story("тест окна добавления домена закладки AD")
    class TestAddDomainWindow:
        def test_add_domain(self, handle_add_domain):
            add_domain = (
                handle_add_domain.by(name=ActiveDirectoryPage.add_domain["title_en"])
                .find()
                .window_text()
            )
            check.equal(add_domain, "Add domain")

        def test_synchronize(self, handle_add_domain):
            synchronize = (
                handle_add_domain.by(name=ActiveDirectoryPage.synchronize["title_en"])
                .find()
                .window_text()
            )
            check.equal(synchronize, "Synchronize")

        def test_check_connection2(self, handle_add_domain):
            check_connection2 = (
                handle_add_domain.by(
                    name=ActiveDirectoryPage.check_connection2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection2, "Check connection")

        def test_ok_button2(self, handle_add_domain):
            ok_button2 = (
                handle_add_domain.by(name=ActiveDirectoryPage.ok_button2["title_en"])
                .find()
                .window_text()
            )
            check.equal(ok_button2, "OK")

        def test_cancel_button3(self, handle_add_domain):
            cancel_button3 = (
                handle_add_domain.by(
                    name=ActiveDirectoryPage.cancel_button3["title_en"],
                    found_index=ActiveDirectoryPage.cancel_button3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button3, "Cancel")

        def test_active_directory(self, handle_add_domain):
            active_directory = (
                handle_add_domain.by(
                    name=ActiveDirectoryPage.active_directory["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(active_directory, "Active Directory")

        def test_azure_ad(self, handle_add_domain):
            azure_ad = (
                handle_add_domain.by(name=ActiveDirectoryPage.azure_ad["title_en"])
                .find()
                .window_text()
            )
            check.equal(azure_ad, "Azure AD")

        def test_connect_only_domain_controller(self, handle_add_domain):
            connect_only_domain_controller = (
                handle_add_domain.by(
                    name=ActiveDirectoryPage.connect_only_domain_controller["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(
                connect_only_domain_controller, "Connect only to domain controller"
            )

        def test_do_not_cache_data(self, handle_add_domain):
            do_not_cache_data = (
                handle_add_domain.by(
                    name=ActiveDirectoryPage.do_not_cache_data["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(do_not_cache_data, "Do not cache data ")

        def test_do_not_read_displayname_attribute(self, handle_add_domain):
            do_not_read_displayname_attribute = (
                handle_add_domain.by(
                    name=ActiveDirectoryPage.do_not_read_displayname_attribute[
                        "title_en"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                do_not_read_displayname_attribute, "Do not read DisplayName attribute"
            )

    @allure.story("тест окна добавления пользователя рабочей группы закладки AD")
    class TestAddWorkgroupUserWindow:
        def test_add_user(self, handle_add_workgroup_user):
            add_user = (
                handle_add_workgroup_user.by(
                    name=ActiveDirectoryPage.add_user["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(add_user, "Add user")

        def test_username2(self, handle_add_workgroup_user):
            username2 = (
                handle_add_workgroup_user.by(
                    name=ActiveDirectoryPage.username2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(username2, "Username")

        def test_user(self, handle_add_workgroup_user):
            user = (
                handle_add_workgroup_user.by(name=ActiveDirectoryPage.user["title_en"])
                .find()
                .window_text()
            )
            check.equal(user, "User")

        def test_computer(self, handle_add_workgroup_user):
            computer = (
                handle_add_workgroup_user.by(
                    name=ActiveDirectoryPage.computer["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(computer, "Computer")

        def test_cancel_button4(self, handle_add_workgroup_user):
            cancel_button4 = (
                handle_add_workgroup_user.by(
                    name=ActiveDirectoryPage.cancel_button4["title_en"],
                    found_index=ActiveDirectoryPage.cancel_button3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button4, "Cancel")

        def test_ok_button3(self, handle_add_workgroup_user):
            ok_button3 = (
                handle_add_workgroup_user.by(
                    name=ActiveDirectoryPage.ok_button3["title_en"]
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
                    name=ActiveDirectoryPage.add_user2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(add_user2, "Add user")

        def test_confirm_password(self, handle_add_internal_user):
            confirm_password = (
                handle_add_internal_user.by(
                    name=ActiveDirectoryPage.confirm_password["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(confirm_password, "Confirm password")

        def test_password2(self, handle_add_internal_user):
            password2 = (
                handle_add_internal_user.by(
                    name=ActiveDirectoryPage.password2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(password2, "Password")

        def test_user2(self, handle_add_internal_user):
            user2 = (
                handle_add_internal_user.by(name=ActiveDirectoryPage.user2["title_en"])
                .find()
                .window_text()
            )
            check.equal(user2, "User")

        def test_username3(self, handle_add_internal_user):
            username3 = (
                handle_add_internal_user.by(
                    name=ActiveDirectoryPage.username3["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(username3, "Username")

        def test_password_validity_days(self, handle_add_internal_user):
            password_validity_days = (
                handle_add_internal_user.by(
                    name=ActiveDirectoryPage.password_validity_days["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(password_validity_days, "Password validity, days:")

        def test_cancel_button5(self, handle_add_internal_user):
            cancel_button5 = (
                handle_add_internal_user.by(
                    name=ActiveDirectoryPage.cancel_button5["title_en"],
                    found_index=ActiveDirectoryPage.cancel_button3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button5, "Cancel")

        def test_ok_button4s(self, handle_add_internal_user):
            ok_button4 = (
                handle_add_internal_user.by(
                    name=ActiveDirectoryPage.ok_button4["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(ok_button4, "OK")
