# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import AgentsAndComponentsPage


@pytest.fixture(scope="class")
def handle(start_test_page_en):
    send_keys("{VK_MENU down}Y3Y3{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def handle_free_disk_space_monitoring_window(start_test_page_en):
    send_keys("{VK_MENU down}Y3Y3{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        AgentsAndComponentsPage.free_space_monitor_button
    ).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_change_mail_button(start_test_page_en):
    send_keys("{VK_MENU down}Y3Y3{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(AgentsAndComponentsPage.change_mail_button).click_input()
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("ENG Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControlsEN
@pytest.mark.testGUI_EngVersionDCTest_ControlsTest_Settings
class TestAgentsAndComponentsPage:
    @allure.story("тест главного окна Agents and Components")
    class TestAgentsAndComponentsMainPage:
        def test_cancel_button(self, handle):
            cancel_button = (
                handle.by(name=AgentsAndComponentsPage.cancel_button["title_en"])
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Cancel")

        def test_apply_button(self, handle):
            apply_button = (
                handle.by(name=AgentsAndComponentsPage.apply_button["title_en"])
                .find()
                .window_text()
            )
            check.equal(apply_button, "Apply")

    @allure.story(
        "тест окна настройки мониторинга свободного места на дисках закладки Agents and Components"
    )
    class TestAgentsAndComponentsFreeDiskSpaceMonitoringWindow:
        def test_handle_free_disk_space_monitoring_window(
            self, handle_free_disk_space_monitoring_window
        ):
            free_disk_space_monitoring = (
                handle_free_disk_space_monitoring_window.__getattribute__(
                    AgentsAndComponentsPage.free_disk_space_monitoring
                )
                .find()
                .window_text()
            )
            check.is_in("Free disk space monitoring", free_disk_space_monitoring)

        def test_enable_monitoring(self, handle_free_disk_space_monitoring_window):
            enable_monitoring = (
                handle_free_disk_space_monitoring_window.by(
                    name=AgentsAndComponentsPage.enable_monitoring["title_en"],
                    found_index=AgentsAndComponentsPage.enable_monitoring[
                        "found_index"
                    ],
                )
                .find()
                .window_text()
            )
            check.equal(enable_monitoring, "Enable monitoring")

        def test_cancel2(self, handle_free_disk_space_monitoring_window):
            cancel2 = (
                handle_free_disk_space_monitoring_window.by(
                    name=AgentsAndComponentsPage.cancel2["title_en"],
                    found_index=AgentsAndComponentsPage.enable_monitoring[
                        "found_index"
                    ],
                )
                .find()
                .window_text()
            )
            check.equal(cancel2, "Cancel")

        def test_ok_button(self, handle_free_disk_space_monitoring_window):
            ok_button = (
                handle_free_disk_space_monitoring_window.by(
                    name=AgentsAndComponentsPage.ok_button["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(ok_button, "OK")

    @allure.story(
        "тест окна индивидуальных настроек почты закладки Agents and Components"
    )
    class TestAgentsAndComponentsChangeMailWindow:
        def test_each_user_mustbe_specified_in_new_line(
            self, handle_change_mail_button
        ):
            each_user_mustbe_specified_in_new_line = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.each_user_mustbe_specified_in_new_line[
                        "title_en"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                each_user_mustbe_specified_in_new_line,
                "* Each user must be specified in a new line",
            )

        def test_list_of_telegram_users_authorized_enabledisable_notifications(
            self, handle_change_mail_button
        ):
            list_of_telegram_users_authorized_enabledisable_notifications = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.list_of_telegram_users_authorized_enabledisable_notifications[
                        "title_en"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                list_of_telegram_users_authorized_enabledisable_notifications,
                "The list of Telegram users authorized to enable/disable notifications:",
            )

        def test_settings_socks5proxy(self, handle_change_mail_button):
            settings_socks5proxy = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.settings_socks5proxy["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(settings_socks5proxy, "Settings SOCKS5Proxy")

        def test_password(self, handle_change_mail_button):
            password = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.password["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(password, "Password:")

        def test_username(self, handle_change_mail_button):
            username = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.username["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(username, "Username:")

        def test_server_port(self, handle_change_mail_button):
            server_port = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.server_port["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(server_port, "Server port:")

        def test_server(self, handle_change_mail_button):
            server = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.server["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(server, "Server:")

        def test_use_proxy(self, handle_change_mail_button):
            use_proxy = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.use_proxy["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(use_proxy, "Use proxy")

        def test_telegram_bot_token(self, handle_change_mail_button):
            telegram_bot_token = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.telegram_bot_token["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(telegram_bot_token, "Telegram bot token:")

        def test_redirect_to_another_dcagent(self, handle_change_mail_button):
            redirect_to_another_dcagent = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.redirect_to_another_dcagent["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(redirect_to_another_dcagent, "Redirect to another DCAgent")

        def test_customize_bot(self, handle_change_mail_button):
            customize_bot = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.customize_bot["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(customize_bot, "Customize Bot ")

        def test_use_following_settings_send_notifications_telegram(
            self, handle_change_mail_button
        ):
            use_following_settings_send_notifications_telegram = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.use_following_settings_send_notifications_telegram[
                        "title_en"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                use_following_settings_send_notifications_telegram,
                "Use the following settings to send notifications to Telegram:",
            )

        def test_close(self, handle_change_mail_button):
            close = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.close["title_en"],
                    found_index=AgentsAndComponentsPage.close["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(close, "Close")

        def test_save(self, handle_change_mail_button):
            save = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.save["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(save, "Save")

        def test_check_connection(self, handle_change_mail_button):
            check_connection = (
                handle_change_mail_button.__getattribute__(
                    AgentsAndComponentsPage.check_connection["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection, "Check connection")

        def test_check_connection2(self, handle_change_mail_button):
            check_connection = (
                handle_change_mail_button.__getattribute__(
                    AgentsAndComponentsPage.check_connection2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection, "Check connection")

        def test_authentication(self, handle_change_mail_button):
            authentication = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.authentication["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(authentication, "Authentication")

        def test_use_following_settings_send_email_notifications(
            self, handle_change_mail_button
        ):
            use_following_settings_send_email_notifications = (
                handle_change_mail_button.by(
                    name=AgentsAndComponentsPage.use_following_settings_send_email_notifications[
                        "title_en"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                use_following_settings_send_email_notifications,
                "Use the following settings to send e-mail notifications:",
            )
