# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import ActiveDirectoryPage


@pytest.fixture(scope="class")
def handle(start_test_page):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def handle_sql_connection_settings(start_test_page, title_key):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=ActiveDirectoryPage.setup_connection_db[title_key]).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_add_domain(start_test_page, title_key):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=ActiveDirectoryPage.synchronization_with_active_directory[title_key]).__getattribute__(
        "Button3"
    ).click()
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_add_workgroup_user(start_test_page, title_key):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(
        name=ActiveDirectoryPage.add_button2[title_key],
        found_index=ActiveDirectoryPage.add_button2["found_index"],
    ).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_add_internal_user(start_test_page, title_key):
    send_keys("{VK_MENU down}Y3Y5{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(
        name=ActiveDirectoryPage.add_button[title_key],
        found_index=ActiveDirectoryPage.add_button["found_index"],
    ).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Settings
class TestActiveDirectoryPage:
    @allure.story("тест главного окна настройки AD")
    class TestActiveDirectoryMainPage:
        def test_cancel_button(self, handle, title_key):
            cancel_button = handle.by(name=ActiveDirectoryPage.cancel_button[title_key]).find().window_text()
            check.equal(cancel_button, ActiveDirectoryPage.cancel_button[title_key])

        def test_apply_button(self, handle, title_key):
            apply_button = handle.by(name=ActiveDirectoryPage.apply_button[title_key]).find().window_text()
            check.equal(apply_button, ActiveDirectoryPage.apply_button[title_key])

        def test_internal_users(self, handle, title_key):
            internal_users = handle.by(name=ActiveDirectoryPage.internal_users[title_key]).find().window_text()
            check.equal(internal_users, ActiveDirectoryPage.internal_users[title_key])

        def test_delete_button(self, handle, title_key):
            delete_button = (
                handle.by(
                    name=ActiveDirectoryPage.delete_button[title_key],
                    found_index=ActiveDirectoryPage.delete_button["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(delete_button, ActiveDirectoryPage.delete_button[title_key])

        def test_change_button(self, handle, title_key):
            change_button = (
                handle.by(
                    name=ActiveDirectoryPage.change_button[title_key],
                    found_index=ActiveDirectoryPage.change_button["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(change_button, ActiveDirectoryPage.change_button[title_key])

        def test_add_button(self, handle, title_key):
            add_button = (
                handle.by(
                    name=ActiveDirectoryPage.add_button[title_key],
                    found_index=ActiveDirectoryPage.add_button["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(add_button, ActiveDirectoryPage.add_button[title_key])

        def test_users_work_groups(self, handle, title_key):
            users_work_groups = handle.by(name=ActiveDirectoryPage.users_work_groups[title_key]).find().window_text()
            check.equal(users_work_groups, ActiveDirectoryPage.users_work_groups[title_key])

        def test_delete_button2(self, handle, title_key):
            delete_button2 = (
                handle.by(
                    name=ActiveDirectoryPage.delete_button2[title_key],
                    found_index=ActiveDirectoryPage.delete_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(delete_button2, ActiveDirectoryPage.delete_button2[title_key])

        def test_change_button2(self, handle, title_key):
            change_button2 = (
                handle.by(
                    name=ActiveDirectoryPage.change_button2[title_key],
                    found_index=ActiveDirectoryPage.change_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(change_button2, ActiveDirectoryPage.change_button2[title_key])

        def test_add_button2(self, handle, title_key):
            add_button2 = (
                handle.by(
                    name=ActiveDirectoryPage.add_button2[title_key],
                    found_index=ActiveDirectoryPage.add_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(add_button2, ActiveDirectoryPage.add_button2[title_key])

        def test_list_of_attributes(self, handle, title_key):
            list_of_attributes = handle.by(name=ActiveDirectoryPage.list_of_attributes[title_key]).find().window_text()
            check.equal(list_of_attributes, ActiveDirectoryPage.list_of_attributes[title_key])

        def test_synchronization_with_active_directory(self, handle, title_key):
            synchronization_with_active_directory = (
                handle.by(name=ActiveDirectoryPage.synchronization_with_active_directory[title_key])
                .find()
                .window_text()
            )
            check.equal(
                synchronization_with_active_directory,
                ActiveDirectoryPage.synchronization_with_active_directory[title_key],
            )

        def test_setup_connection_db(self, handle, title_key):
            setup_connection_db = (
                handle.by(name=ActiveDirectoryPage.setup_connection_db[title_key]).find().window_text()
            )
            check.equal(setup_connection_db, ActiveDirectoryPage.setup_connection_db[title_key])

    @allure.story("тест окна настройки подключения к бд ДЦ закладки AD")
    class TestSQLConnectionSettingsWindow:
        def test_sql_server_connection_settings(self, handle_sql_connection_settings, title_key):
            sql_server_connection_settings = (
                handle_sql_connection_settings.by(name=ActiveDirectoryPage.sql_server_connection_settings[title_key])
                .find()
                .window_text()
            )
            check.equal(sql_server_connection_settings, ActiveDirectoryPage.sql_server_connection_settings[title_key])

        def test_create(self, handle_sql_connection_settings, title_key):
            create = handle_sql_connection_settings.by(name=ActiveDirectoryPage.create[title_key]).find().window_text()
            check.equal(create, ActiveDirectoryPage.create[title_key])

        def test_database_name(self, handle_sql_connection_settings, title_key):
            database_name = (
                handle_sql_connection_settings.by(name=ActiveDirectoryPage.database_name[title_key])
                .find()
                .window_text()
            )
            check.equal(database_name, ActiveDirectoryPage.database_name[title_key])

        def test_password(self, handle_sql_connection_settings, title_key):
            password = (
                handle_sql_connection_settings.by(name=ActiveDirectoryPage.password[title_key]).find().window_text()
            )
            check.equal(password, ActiveDirectoryPage.password[title_key])

        def test_username(self, handle_sql_connection_settings, title_key):
            username = (
                handle_sql_connection_settings.by(name=ActiveDirectoryPage.username[title_key]).find().window_text()
            )
            check.equal(username, ActiveDirectoryPage.username[title_key])

        def test_sql_server_authentication_mode(self, handle_sql_connection_settings, title_key):
            sql_server_authentication_mode = (
                handle_sql_connection_settings.by(name=ActiveDirectoryPage.sql_server_authentication_mode[title_key])
                .find()
                .window_text()
            )
            check.equal(sql_server_authentication_mode, ActiveDirectoryPage.sql_server_authentication_mode[title_key])

        def test_windows_authentication_mode(self, handle_sql_connection_settings, title_key):
            windows_authentication_mode = (
                handle_sql_connection_settings.by(name=ActiveDirectoryPage.windows_authentication_mode[title_key])
                .find()
                .window_text()
            )
            check.equal(windows_authentication_mode, ActiveDirectoryPage.windows_authentication_mode[title_key])

        def test_read_from_dc(self, handle_sql_connection_settings, title_key):
            read_from_dc = (
                handle_sql_connection_settings.by(name=ActiveDirectoryPage.read_from_dc[title_key])
                .find()
                .window_text()
            )
            check.equal(read_from_dc, ActiveDirectoryPage.read_from_dc[title_key])

        def test_server_name(self, handle_sql_connection_settings, title_key):
            server_name = (
                handle_sql_connection_settings.by(name=ActiveDirectoryPage.server_name[title_key]).find().window_text()
            )
            check.equal(server_name, ActiveDirectoryPage.server_name[title_key])

        def test_server_type(self, handle_sql_connection_settings, title_key):
            server_type = (
                handle_sql_connection_settings.by(name=ActiveDirectoryPage.server_type[title_key]).find().window_text()
            )
            check.equal(server_type, ActiveDirectoryPage.server_type[title_key])

        def test_cancel_button2(self, handle_sql_connection_settings, title_key):
            cancel_button2 = (
                handle_sql_connection_settings.by(
                    name=ActiveDirectoryPage.cancel_button2[title_key],
                    found_index=ActiveDirectoryPage.cancel_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button2, ActiveDirectoryPage.cancel_button2[title_key])

        def test_ok_button(self, handle_sql_connection_settings, title_key):
            ok_button = (
                handle_sql_connection_settings.by(name=ActiveDirectoryPage.ok_button[title_key]).find().window_text()
            )
            check.equal(ok_button, ActiveDirectoryPage.ok_button[title_key])

        def test_check_connection(self, handle_sql_connection_settings, title_key):
            check_connection = (
                handle_sql_connection_settings.by(name=ActiveDirectoryPage.check_connection[title_key])
                .find()
                .window_text()
            )
            check.equal(check_connection, ActiveDirectoryPage.check_connection[title_key])

    @allure.story("тест окна добавления домена закладки AD")
    class TestAddDomainWindow:
        def test_add_domain(self, handle_add_domain, title_key):
            add_domain = handle_add_domain.by(name=ActiveDirectoryPage.add_domain[title_key]).find().window_text()
            check.equal(add_domain, ActiveDirectoryPage.add_domain[title_key])

        def test_synchronize(self, handle_add_domain, title_key):
            synchronize = handle_add_domain.by(name=ActiveDirectoryPage.synchronize[title_key]).find().window_text()
            check.equal(synchronize, ActiveDirectoryPage.synchronize[title_key])

        def test_check_connection2(self, handle_add_domain, title_key):
            check_connection2 = (
                handle_add_domain.by(name=ActiveDirectoryPage.check_connection2[title_key]).find().window_text()
            )
            check.equal(check_connection2, ActiveDirectoryPage.check_connection2[title_key])

        def test_ok_button2(self, handle_add_domain, title_key):
            ok_button2 = handle_add_domain.by(name=ActiveDirectoryPage.ok_button2[title_key]).find().window_text()
            check.equal(ok_button2, ActiveDirectoryPage.ok_button2[title_key])

        def test_cancel_button3(self, handle_add_domain, title_key):
            cancel_button3 = (
                handle_add_domain.by(
                    name=ActiveDirectoryPage.cancel_button3[title_key],
                    found_index=ActiveDirectoryPage.cancel_button3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button3, ActiveDirectoryPage.cancel_button3[title_key])

        def test_active_directory(self, handle_add_domain, title_key):
            active_directory = (
                handle_add_domain.by(name=ActiveDirectoryPage.active_directory[title_key]).find().window_text()
            )
            check.equal(active_directory, ActiveDirectoryPage.active_directory[title_key])

        def test_azure_ad(self, handle_add_domain, title_key):
            azure_ad = handle_add_domain.by(name=ActiveDirectoryPage.azure_ad[title_key]).find().window_text()
            check.equal(azure_ad, ActiveDirectoryPage.azure_ad[title_key])

        def test_connect_only_domain_controller(self, handle_add_domain, title_key):
            connect_only_domain_controller = (
                handle_add_domain.by(name=ActiveDirectoryPage.connect_only_domain_controller[title_key])
                .find()
                .window_text()
            )
            check.equal(connect_only_domain_controller, ActiveDirectoryPage.connect_only_domain_controller[title_key])

        def test_do_not_cache_data(self, handle_add_domain, title_key):
            do_not_cache_data = (
                handle_add_domain.by(name=ActiveDirectoryPage.do_not_cache_data[title_key]).find().window_text()
            )
            check.equal(do_not_cache_data, ActiveDirectoryPage.do_not_cache_data[title_key])

        def test_do_not_read_displayname_attribute(self, handle_add_domain, title_key):
            do_not_read_displayname_attribute = (
                handle_add_domain.by(name=ActiveDirectoryPage.do_not_read_displayname_attribute[title_key])
                .find()
                .window_text()
            )
            check.equal(do_not_read_displayname_attribute, ActiveDirectoryPage.do_not_read_displayname_attribute[title_key])

    @allure.story("тест окна добавления пользователя рабочей группы закладки AD")
    class TestAddWorkgroupUserWindow:
        def test_add_user(self, handle_add_workgroup_user, title_key):
            add_user = handle_add_workgroup_user.by(name=ActiveDirectoryPage.add_user[title_key]).find().window_text()
            check.equal(add_user, ActiveDirectoryPage.add_user[title_key])

        def test_username2(self, handle_add_workgroup_user, title_key):
            username2 = (
                handle_add_workgroup_user.by(name=ActiveDirectoryPage.username2[title_key]).find().window_text()
            )
            check.equal(username2, ActiveDirectoryPage.username2[title_key])

        def test_user(self, handle_add_workgroup_user, title_key):
            user = handle_add_workgroup_user.by(name=ActiveDirectoryPage.user[title_key]).find().window_text()
            check.equal(user, ActiveDirectoryPage.user[title_key])

        def test_computer(self, handle_add_workgroup_user, title_key):
            computer = handle_add_workgroup_user.by(name=ActiveDirectoryPage.computer[title_key]).find().window_text()
            check.equal(computer, ActiveDirectoryPage.computer[title_key])

        def test_cancel_button4(self, handle_add_workgroup_user, title_key):
            cancel_button4 = (
                handle_add_workgroup_user.by(
                    name=ActiveDirectoryPage.cancel_button4[title_key],
                    found_index=ActiveDirectoryPage.cancel_button3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button4, ActiveDirectoryPage.cancel_button4[title_key])

        def test_ok_button3(self, handle_add_workgroup_user, title_key):
            ok_button3 = (
                handle_add_workgroup_user.by(name=ActiveDirectoryPage.ok_button3[title_key]).find().window_text()
            )
            check.equal(ok_button3, ActiveDirectoryPage.ok_button3[title_key])

    @allure.story("тест окна добавления внутренних пользователей КИБ закладки AD")
    class TestAddInternalUserWindow:
        def test_add_user2(self, handle_add_internal_user, title_key):
            add_user2 = handle_add_internal_user.by(name=ActiveDirectoryPage.add_user2[title_key]).find().window_text()
            check.equal(add_user2, ActiveDirectoryPage.add_user2[title_key])

        def test_confirm_password(self, handle_add_internal_user, title_key):
            confirm_password = (
                handle_add_internal_user.by(name=ActiveDirectoryPage.confirm_password[title_key]).find().window_text()
            )
            check.equal(confirm_password, ActiveDirectoryPage.confirm_password[title_key])

        def test_password2(self, handle_add_internal_user, title_key):
            password2 = handle_add_internal_user.by(name=ActiveDirectoryPage.password2[title_key]).find().window_text()
            check.equal(password2, ActiveDirectoryPage.password2[title_key])

        def test_user2(self, handle_add_internal_user, title_key):
            user2 = handle_add_internal_user.by(name=ActiveDirectoryPage.user2[title_key]).find().window_text()
            check.equal(user2, ActiveDirectoryPage.user2[title_key])

        def test_username3(self, handle_add_internal_user, title_key):
            username3 = handle_add_internal_user.by(name=ActiveDirectoryPage.username3[title_key]).find().window_text()
            check.equal(username3, ActiveDirectoryPage.username3[title_key])

        def test_password_validity_days(self, handle_add_internal_user, title_key):
            password_validity_days = (
                handle_add_internal_user.by(name=ActiveDirectoryPage.password_validity_days[title_key])
                .find()
                .window_text()
            )
            check.equal(password_validity_days, ActiveDirectoryPage.password_validity_days[title_key])

        def test_cancel_button5(self, handle_add_internal_user, title_key):
            cancel_button5 = (
                handle_add_internal_user.by(
                    name=ActiveDirectoryPage.cancel_button5[title_key],
                    found_index=ActiveDirectoryPage.cancel_button3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button5, ActiveDirectoryPage.cancel_button5[title_key])

        def test_ok_button4s(self, handle_add_internal_user, title_key):
            ok_button4 = (
                handle_add_internal_user.by(name=ActiveDirectoryPage.ok_button4[title_key]).find().window_text()
            )
            check.equal(ok_button4, ActiveDirectoryPage.ok_button4[title_key])
