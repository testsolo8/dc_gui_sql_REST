# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import DataCenterServerPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y3Y1{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("ESP Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControlsES
@pytest.mark.testGUI_EspVersionDCTest_ControlsTest_Settings
@allure.story("тест главного окна настройки сервера DataCenter")
class TestDataCenterServerPage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=DataCenterServerPage.cancel_button["title_es"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Cancelar")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=DataCenterServerPage.apply_button["title_es"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Aplicar")

    def test_block_account(self, handle):
        block_account = (
            handle.by(name=DataCenterServerPage.block_account["title_es"])
            .find()
            .window_text()
        )
        check.equal(block_account, "Bloquear la cuenta")

    def test_block_interface(self, handle):
        block_interface = (
            handle.by(name=DataCenterServerPage.block_interface["title_es"])
            .find()
            .window_text()
        )
        check.equal(block_interface, "Bloquear interfaz por un minuto")

    def test_setup_acc_pass(self, handle):
        setup_acc_pass = (
            handle.by(name=DataCenterServerPage.setup_acc_pass["title_es"])
            .find()
            .window_text()
        )
        check.equal(setup_acc_pass, "Configurar contraseñas para cuentas")

    def test_failed_attempts(self, handle):
        failed_attempts = (
            handle.by(name=DataCenterServerPage.failed_attempts["title_es"])
            .find()
            .window_text()
        )
        check.equal(
            failed_attempts, "Después de 3 intentos fracasados de entrar contraseña:"
        )

    def test_special_characters(self, handle):
        special_characters = (
            handle.by(name=DataCenterServerPage.special_characters["title_es"])
            .find()
            .window_text()
        )
        check.equal(special_characters, "Carácteres especiales")

    def test_lower_upper_cases(self, handle):
        lower_upper_cases = (
            handle.by(name=DataCenterServerPage.lower_upper_cases["title_es"])
            .find()
            .window_text()
        )
        check.equal(lower_upper_cases, "Minúsculas y mayúsculas")

    def test_letters_figures(self, handle):
        letters_figures = (
            handle.by(name=DataCenterServerPage.letters_figures["title_es"])
            .find()
            .window_text()
        )
        check.equal(letters_figures, "Letras y cifras")

    def test_password_contain(self, handle):
        password_contain = (
            handle.by(name=DataCenterServerPage.password_contain["title_es"])
            .find()
            .window_text()
        )
        check.equal(password_contain, "La contraseña debe contener:")

    def test_minimum_characters(self, handle):
        minimum_characters = (
            handle.by(name=DataCenterServerPage.minimum_characters["title_es"])
            .find()
            .window_text()
        )
        check.equal(minimum_characters, "Longitud mínima, carácteres")

    def test_notify_if(self, handle):
        notify_if = (
            handle.by(name=DataCenterServerPage.notify_if["title_es"])
            .find()
            .window_text()
        )
        check.equal(notify_if, "Notificar si:")

    def test_pcap(self, handle):
        pcap = (
            handle.by(name=DataCenterServerPage.pcap["title_es"]).find().window_text()
        )
        check.equal(pcap, "Archivos de tráfico guardado están más de")

    def test_free_space_on_local_drive(self, handle):
        free_space_on_local_drive = (
            handle.by(name=DataCenterServerPage.free_space_on_local_drive["title_es"])
            .find()
            .window_text()
        )
        check.equal(
            free_space_on_local_drive, "Espacio libre en el disco local está menos de"
        )

    def test_performance_logs(self, handle):
        performance_logs = (
            handle.by(name=DataCenterServerPage.performance_logs["title_es"])
            .find()
            .window_text()
        )
        check.equal(performance_logs, "Registro de rendimiento está más de ")

    def test_operation_logs(self, handle):
        operation_logs = (
            handle.by(name=DataCenterServerPage.operation_logs["title_es"])
            .find()
            .window_text()
        )
        check.equal(operation_logs, "Registro de operación está más de")

    def test_unmount_db_if(self, handle):
        unmount_db_if = (
            handle.by(name=DataCenterServerPage.unmount_db_if["title_es"])
            .find()
            .window_text()
        )
        check.equal(
            unmount_db_if,
            "Desmontar BD si el agente del DataCenter recibe información sobre la ausencia de la BD en el servidor SQL",
        )

    def test_use_tokens(self, handle):
        use_tokens = (
            handle.by(name=DataCenterServerPage.use_tokens["title_es"])
            .find()
            .window_text()
        )
        check.equal(use_tokens, "Usar tokens para autenticación segura de usuarios")

    def test_mail_notif_lan(self, handle):
        mail_notif_lan = (
            handle.by(name=DataCenterServerPage.mail_notif_lan["title_es"])
            .find()
            .window_text()
        )
        check.equal(mail_notif_lan, "Idioma de notificaciones por e-mail")

    def test_log_level(self, handle):
        log_level = (
            handle.by(name=DataCenterServerPage.log_level["title_es"])
            .find()
            .window_text()
        )
        check.equal(log_level, "Nivel de registro ")

    def test_automatic_update_agents(self, handle):
        automatic_update_agents = (
            handle.by(name=DataCenterServerPage.automatic_update_agents["title_es"])
            .find()
            .window_text()
        )
        check.equal(
            automatic_update_agents,
            "Actualización automática de agentes en servidores remotos",
        )
