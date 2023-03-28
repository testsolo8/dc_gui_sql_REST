# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import AgentsAndComponentsPage


@pytest.fixture(scope="class")
def handle(start_test_page):
    send_keys("{VK_MENU down}Y3Y3{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def handle_free_disk_space_monitoring_window(start_test_page):
    send_keys("{VK_MENU down}Y3Y3{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(AgentsAndComponentsPage.free_space_monitor_button).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_change_mail_button(start_test_page):
    send_keys("{VK_MENU down}Y3Y3{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(AgentsAndComponentsPage.change_mail_button).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Settings
class TestAgentsAndComponentsPage:
    @allure.story("тест главного окна Agents and Components")
    class TestAgentsAndComponentsMainPage:
        def test_cancel_button(self, handle, title_key):
            cancel_button = handle.by(name=AgentsAndComponentsPage.cancel_button[title_key]).find().window_text()
            check.equal(cancel_button, AgentsAndComponentsPage.cancel_button[title_key])

        def test_apply_button(self, handle, title_key):
            apply_button = handle.by(name=AgentsAndComponentsPage.apply_button[title_key]).find().window_text()
            check.equal(apply_button, AgentsAndComponentsPage.apply_button[title_key])

    @allure.story("тест окна настройки мониторинга свободного места на дисках закладки Agents and Components")
    class TestAgentsAndComponentsFreeDiskSpaceMonitoringWindow:
        def test_handle_free_disk_space_monitoring_window(self, handle_free_disk_space_monitoring_window, title_key):
            free_disk_space_monitoring = (
                handle_free_disk_space_monitoring_window.__getattribute__(
                    AgentsAndComponentsPage.free_disk_space_monitoring["control_type"]
                )
                .find()
                .window_text()
            )
            check.is_in(AgentsAndComponentsPage.free_disk_space_monitoring[title_key], free_disk_space_monitoring)

        def test_enable_monitoring(self, handle_free_disk_space_monitoring_window, title_key):
            enable_monitoring = (
                handle_free_disk_space_monitoring_window.by(
                    name=AgentsAndComponentsPage.enable_monitoring[title_key],
                    found_index=AgentsAndComponentsPage.enable_monitoring["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(enable_monitoring, AgentsAndComponentsPage.enable_monitoring[title_key])

        def test_cancel2(self, handle_free_disk_space_monitoring_window, title_key):
            cancel2 = (
                handle_free_disk_space_monitoring_window.by(
                    name=AgentsAndComponentsPage.cancel2[title_key],
                    found_index=AgentsAndComponentsPage.enable_monitoring["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel2, AgentsAndComponentsPage.cancel2[title_key])

        def test_ok_button(self, handle_free_disk_space_monitoring_window, title_key):
            ok_button = (
                handle_free_disk_space_monitoring_window.by(name=AgentsAndComponentsPage.ok_button[title_key])
                .find()
                .window_text()
            )
            check.equal(ok_button, AgentsAndComponentsPage.ok_button[title_key])

    @allure.story("тест окна индивидуальных настроек почты закладки Agents and Components")
    class TestAgentsAndComponentsChangeMailWindow:
        def test_each_user_mustbe_specified_in_new_line(self, handle_change_mail_button, title_key):
            each_user_mustbe_specified_in_new_line = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.each_user_mustbe_specified_in_new_line[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(
                each_user_mustbe_specified_in_new_line,
                AgentsAndComponentsPage.each_user_mustbe_specified_in_new_line[title_key],
            )

        def test_list_of_telegram_users_authorized_enabledisable_notifications(self, handle_change_mail_button, title_key):
            list_of_telegram_users_authorized_enabledisable_notifications = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.list_of_telegram_users_authorized_enabledisable_notifications[
                        title_key
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                list_of_telegram_users_authorized_enabledisable_notifications,
                AgentsAndComponentsPage.list_of_telegram_users_authorized_enabledisable_notifications[title_key]
            )

        def test_settings_socks5proxy(self, handle_change_mail_button, title_key):
            settings_socks5proxy = (
                handle_change_mail_button.by(name=AgentsAndComponentsPage.settings_socks5proxy[title_key])
                .find()
                .window_text()
            )
            check.equal(settings_socks5proxy, AgentsAndComponentsPage.settings_socks5proxy[title_key])

        def test_password(self, handle_change_mail_button, title_key):
            password = (
                handle_change_mail_button.by(name=AgentsAndComponentsPage.password[title_key]).find().window_text()
            )
            check.equal(password, AgentsAndComponentsPage.password[title_key])

        def test_username(self, handle_change_mail_button, title_key):
            username = (
                handle_change_mail_button.by(name=AgentsAndComponentsPage.username[title_key]).find().window_text()
            )
            check.equal(username, AgentsAndComponentsPage.username[title_key])

        def test_server_port(self, handle_change_mail_button, title_key):
            server_port = (
                handle_change_mail_button.by(name=AgentsAndComponentsPage.server_port[title_key]).find().window_text()
            )
            check.equal(server_port, AgentsAndComponentsPage.server_port[title_key])

        def test_server(self, handle_change_mail_button, title_key):
            server = handle_change_mail_button.by(name=AgentsAndComponentsPage.server[title_key]).find().window_text()
            check.equal(server, AgentsAndComponentsPage.server[title_key])

        def test_use_proxy(self, handle_change_mail_button, title_key):
            use_proxy = (
                handle_change_mail_button.by(name=AgentsAndComponentsPage.use_proxy[title_key]).find().window_text()
            )
            check.equal(use_proxy, AgentsAndComponentsPage.use_proxy[title_key])

        def test_telegram_bot_token(self, handle_change_mail_button, title_key):
            telegram_bot_token = (
                handle_change_mail_button.by(name=AgentsAndComponentsPage.telegram_bot_token[title_key])
                .find()
                .window_text()
            )
            check.equal(telegram_bot_token, AgentsAndComponentsPage.telegram_bot_token[title_key])

        def test_redirect_to_another_dcagent(self, handle_change_mail_button, title_key):
            redirect_to_another_dcagent = (
                handle_change_mail_button.by(name=AgentsAndComponentsPage.redirect_to_another_dcagent[title_key])
                .find()
                .window_text()
            )
            check.equal(redirect_to_another_dcagent, AgentsAndComponentsPage.redirect_to_another_dcagent[title_key])

        def test_customize_bot(self, handle_change_mail_button, title_key):
            customize_bot = (
                handle_change_mail_button.by(name=AgentsAndComponentsPage.customize_bot[title_key])
                .find()
                .window_text()
            )
            check.equal(customize_bot, AgentsAndComponentsPage.customize_bot[title_key])

        def test_use_following_settings_send_notifications_telegram(self, handle_change_mail_button, title_key):
            use_following_settings_send_notifications_telegram = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.use_following_settings_send_notifications_telegram[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(
                use_following_settings_send_notifications_telegram,
                AgentsAndComponentsPage.use_following_settings_send_notifications_telegram[title_key],
            )

        def test_close(self, handle_change_mail_button, title_key):
            close = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.close[title_key],
                    found_index=AgentsAndComponentsPage.close["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(close, AgentsAndComponentsPage.close[title_key])

        def test_save(self, handle_change_mail_button, title_key):
            save = handle_change_mail_button.by(name=AgentsAndComponentsPage.save[title_key]).find().window_text()
            check.equal(save, AgentsAndComponentsPage.save[title_key])

        def test_check_connection(self, handle_change_mail_button, title_key, attribute_key):
            check_connection = (
                handle_change_mail_button.__getattribute__(AgentsAndComponentsPage.check_connection[attribute_key])
                .find()
                .window_text()
            )
            check.equal(check_connection, AgentsAndComponentsPage.check_connection[title_key])

        def test_check_connection2(self, handle_change_mail_button, title_key, attribute_key):
            check_connection = (
                handle_change_mail_button.__getattribute__(AgentsAndComponentsPage.check_connection2[attribute_key])
                .find()
                .window_text()
            )
            check.equal(check_connection, AgentsAndComponentsPage.check_connection2[title_key])

        def test_authentication(self, handle_change_mail_button, title_key):
            authentication = (
                handle_change_mail_button.by(name=AgentsAndComponentsPage.authentication[title_key])
                .find()
                .window_text()
            )
            check.equal(authentication, AgentsAndComponentsPage.authentication[title_key])

        def test_use_following_settings_send_email_notifications(self, handle_change_mail_button, title_key):
            use_following_settings_send_email_notifications = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.use_following_settings_send_email_notifications[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(
                use_following_settings_send_email_notifications,
                AgentsAndComponentsPage.use_following_settings_send_email_notifications[title_key],
            )
