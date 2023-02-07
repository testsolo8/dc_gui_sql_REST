# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import TelegramlNotificationsPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y3Y8{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("ESP Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControlsES
@pytest.mark.testGUI_EspVersionDCTest_ControlsTest_Settings
@allure.story("тест главного окна настройки Telegram уведомлений")
class TestTelegramlNotificationsPage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=TelegramlNotificationsPage.cancel_button["title_es"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Cancelar")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=TelegramlNotificationsPage.apply_button["title_es"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Aplicar")

    def test_main_dcagent_for_sending_notifications_telegram(self, handle):
        main_dcagent_for_sending_notifications_telegram = (
            handle.by(
                name=TelegramlNotificationsPage.main_dcagent_for_sending_notifications_telegram[
                    "title_es"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            main_dcagent_for_sending_notifications_telegram,
            "DCAgent principal para enviar notificaciones a Telegram:",
        )

    def test_telegram_bot_token(self, handle):
        telegram_bot_token = (
            handle.by(name=TelegramlNotificationsPage.telegram_bot_token["title_es"])
            .find()
            .window_text()
        )
        check.equal(telegram_bot_token, "Token de bot te Telegram:")

    def test_settings_socks5proxy(self, handle):
        settings_socks5proxy = (
            handle.by(name=TelegramlNotificationsPage.settings_socks5proxy["title_es"])
            .find()
            .window_text()
        )
        check.equal(settings_socks5proxy, "Ajustes SOCKS5Proxy")

    def test_password(self, handle):
        password = (
            handle.by(name=TelegramlNotificationsPage.password["title_es"])
            .find()
            .window_text()
        )
        check.equal(password, "Contraseña:")

    def test_username(self, handle):
        username = (
            handle.by(name=TelegramlNotificationsPage.username["title_es"])
            .find()
            .window_text()
        )
        check.equal(username, "Nombre de usuario:")

    def test_server_port(self, handle):
        server_port = (
            handle.by(name=TelegramlNotificationsPage.server_port["title_es"])
            .find()
            .window_text()
        )
        check.equal(server_port, "Puerto de servidor:")

    def test_server(self, handle):
        server = (
            handle.by(name=TelegramlNotificationsPage.server["title_es"])
            .find()
            .window_text()
        )
        check.equal(server, "Servidor:")

    def test_use_proxy(self, handle):
        use_proxy = (
            handle.by(name=TelegramlNotificationsPage.use_proxy["title_es"])
            .find()
            .window_text()
        )
        check.equal(use_proxy, "Usar proxy")

    def test_list_of_telegram_users_authorized(self, handle):
        list_of_telegram_users_authorized = (
            handle.by(
                name=TelegramlNotificationsPage.list_of_telegram_users_authorized[
                    "title_es"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            list_of_telegram_users_authorized,
            r"La lista de usuarios de Telegram autorizados para habilitar/deshabilitar notificaciones:",
        )

    def test_each_user_must_be_specified_in_new_line(self, handle):
        each_user_must_be_specified_in_new_line = (
            handle.by(
                name=TelegramlNotificationsPage.each_user_must_be_specified_in_new_line[
                    "title_es"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            each_user_must_be_specified_in_new_line,
            r"* Cada usuario se debe especificar en línea nueva",
        )

    def test_send_notifications_to_telegram(self, handle):
        send_notifications_to_telegram = (
            handle.by(
                name=TelegramlNotificationsPage.send_notifications_to_telegram[
                    "title_es"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(send_notifications_to_telegram, r"Enviar notificaciones a Telegram")

    def test_check_connection(self, handle):
        check_connection = (
            handle.__getattribute__(
                TelegramlNotificationsPage.check_connection["title_es"]
            )
            .find()
            .window_text()
        )
        check.equal(check_connection, "Probar conexión")
