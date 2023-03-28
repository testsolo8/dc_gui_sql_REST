# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import TelegramlNotificationsPage


@pytest.fixture(scope="class")
def handle(start_test_page):
    send_keys("{VK_MENU down}Y3Y8{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Settings
@allure.story("тест главного окна настройки Telegram уведомлений")
class TestTelegramlNotificationsPage:
    def test_cancel_button(self, handle, title_key):
        cancel_button = handle.by(name=TelegramlNotificationsPage.cancel_button[title_key]).find().window_text()
        check.equal(cancel_button, TelegramlNotificationsPage.cancel_button[title_key])

    def test_apply_button(self, handle, title_key):
        apply_button = handle.by(name=TelegramlNotificationsPage.apply_button[title_key]).find().window_text()
        check.equal(apply_button, TelegramlNotificationsPage.apply_button[title_key])

    def test_main_dcagent_for_sending_notifications_telegram(self, handle, title_key):
        main_dcagent_for_sending_notifications_telegram = (
            handle.by(name=TelegramlNotificationsPage.main_dcagent_for_sending_notifications_telegram[title_key])
            .find()
            .window_text()
        )
        check.equal(
            main_dcagent_for_sending_notifications_telegram,
            TelegramlNotificationsPage.main_dcagent_for_sending_notifications_telegram[title_key],
        )

    def test_telegram_bot_token(self, handle, title_key):
        telegram_bot_token = (
            handle.by(name=TelegramlNotificationsPage.telegram_bot_token[title_key]).find().window_text()
        )
        check.equal(telegram_bot_token, TelegramlNotificationsPage.telegram_bot_token[title_key])

    def test_settings_socks5proxy(self, handle, title_key):
        settings_socks5proxy = (
            handle.by(name=TelegramlNotificationsPage.settings_socks5proxy[title_key]).find().window_text()
        )
        check.equal(settings_socks5proxy, TelegramlNotificationsPage.settings_socks5proxy[title_key])

    def test_password(self, handle, title_key):
        password = handle.by(name=TelegramlNotificationsPage.password[title_key]).find().window_text()
        check.equal(password, TelegramlNotificationsPage.password[title_key])

    def test_username(self, handle, title_key):
        username = handle.by(name=TelegramlNotificationsPage.username[title_key]).find().window_text()
        check.equal(username, TelegramlNotificationsPage.username[title_key])

    def test_server_port(self, handle, title_key):
        server_port = handle.by(name=TelegramlNotificationsPage.server_port[title_key]).find().window_text()
        check.equal(server_port, TelegramlNotificationsPage.server_port[title_key])

    def test_server(self, handle, title_key):
        server = handle.by(name=TelegramlNotificationsPage.server[title_key]).find().window_text()
        check.equal(server, TelegramlNotificationsPage.server[title_key])

    def test_use_proxy(self, handle, title_key):
        use_proxy = handle.by(name=TelegramlNotificationsPage.use_proxy[title_key]).find().window_text()
        check.equal(use_proxy, TelegramlNotificationsPage.use_proxy[title_key])

    def test_list_of_telegram_users_authorized(self, handle, title_key):
        list_of_telegram_users_authorized = (
            handle.by(name=TelegramlNotificationsPage.list_of_telegram_users_authorized[title_key])
            .find()
            .window_text()
        )
        check.equal(
            list_of_telegram_users_authorized,
            TelegramlNotificationsPage.list_of_telegram_users_authorized[title_key],
        )

    def test_each_user_must_be_specified_in_new_line(self, handle, title_key):
        each_user_must_be_specified_in_new_line = (
            handle.by(name=TelegramlNotificationsPage.each_user_must_be_specified_in_new_line[title_key])
            .find()
            .window_text()
        )
        check.equal(
            each_user_must_be_specified_in_new_line,
            TelegramlNotificationsPage.each_user_must_be_specified_in_new_line[title_key],
        )

    def test_send_notifications_to_telegram(self, handle, title_key):
        send_notifications_to_telegram = (
            handle.by(name=TelegramlNotificationsPage.send_notifications_to_telegram[title_key]).find().window_text()
        )
        check.equal(send_notifications_to_telegram, TelegramlNotificationsPage.send_notifications_to_telegram[title_key])

    def test_check_connection(self, handle, title_key, attribute_key):
        check_connection = (
            handle.__getattribute__(TelegramlNotificationsPage.check_connection[attribute_key]).find().window_text()
        )
        check.equal(check_connection, TelegramlNotificationsPage.check_connection[title_key])
