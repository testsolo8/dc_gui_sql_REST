# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import TelegramlNotificationsPage


@pytest.fixture(scope="class")
def handle(start_test_page_en):
    send_keys("{VK_MENU down}Y3Y8{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("ENG Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControlsEN
@pytest.mark.testGUI_EngVersionDCTest_ControlsTest_Settings
@allure.story("тест главного окна настройки Telegram уведомлений")
class TestTelegramlNotificationsPage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=TelegramlNotificationsPage.cancel_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Cancel")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=TelegramlNotificationsPage.apply_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Apply")

    def test_main_dcagent_for_sending_notifications_telegram(self, handle):
        main_dcagent_for_sending_notifications_telegram = (
            handle.by(
                name=TelegramlNotificationsPage.main_dcagent_for_sending_notifications_telegram[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            main_dcagent_for_sending_notifications_telegram,
            "Main DCAgent for sending notifications to Telegram:",
        )

    def test_telegram_bot_token(self, handle):
        telegram_bot_token = (
            handle.by(name=TelegramlNotificationsPage.telegram_bot_token["title_en"])
            .find()
            .window_text()
        )
        check.equal(telegram_bot_token, "Telegram bot token:")

    def test_settings_socks5proxy(self, handle):
        settings_socks5proxy = (
            handle.by(name=TelegramlNotificationsPage.settings_socks5proxy["title_en"])
            .find()
            .window_text()
        )
        check.equal(settings_socks5proxy, "Settings SOCKS5Proxy")

    def test_password(self, handle):
        password = (
            handle.by(name=TelegramlNotificationsPage.password["title_en"])
            .find()
            .window_text()
        )
        check.equal(password, "Password:")

    def test_username(self, handle):
        username = (
            handle.by(name=TelegramlNotificationsPage.username["title_en"])
            .find()
            .window_text()
        )
        check.equal(username, "Username:")

    def test_server_port(self, handle):
        server_port = (
            handle.by(name=TelegramlNotificationsPage.server_port["title_en"])
            .find()
            .window_text()
        )
        check.equal(server_port, "Server port:")

    def test_server(self, handle):
        server = (
            handle.by(name=TelegramlNotificationsPage.server["title_en"])
            .find()
            .window_text()
        )
        check.equal(server, "Server:")

    def test_use_proxy(self, handle):
        use_proxy = (
            handle.by(name=TelegramlNotificationsPage.use_proxy["title_en"])
            .find()
            .window_text()
        )
        check.equal(use_proxy, "Use proxy")

    def test_list_of_telegram_users_authorized(self, handle):
        list_of_telegram_users_authorized = (
            handle.by(
                name=TelegramlNotificationsPage.list_of_telegram_users_authorized[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            list_of_telegram_users_authorized,
            r"The list of Telegram users authorized to enable/disable notifications:",
        )

    def test_each_user_must_be_specified_in_new_line(self, handle):
        each_user_must_be_specified_in_new_line = (
            handle.by(
                name=TelegramlNotificationsPage.each_user_must_be_specified_in_new_line[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            each_user_must_be_specified_in_new_line,
            r"* Each user must be specified in a new line",
        )

    def test_send_notifications_to_telegram(self, handle):
        send_notifications_to_telegram = (
            handle.by(
                name=TelegramlNotificationsPage.send_notifications_to_telegram[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(send_notifications_to_telegram, r"Send notifications to Telegram ")

    def test_check_connection(self, handle):
        check_connection = (
            handle.__getattribute__(
                TelegramlNotificationsPage.check_connection["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(check_connection, "Check connection")
