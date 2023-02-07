# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import DataCenterServerPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y3Y1{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("RUS Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControlsRU
@pytest.mark.testGUI_RusVersionDCTest_ControlsTest_Settings
@allure.story("тест главного окна настройки сервера DataCenter")
class TestDataCenterServerPage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=DataCenterServerPage.cancel_button["title_ru"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Отменить")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=DataCenterServerPage.apply_button["title_ru"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Применить")

    def test_block_account(self, handle):
        block_account = (
            handle.by(name=DataCenterServerPage.block_account["title_ru"])
            .find()
            .window_text()
        )
        check.equal(block_account, "блокировать учетную запись")

    def test_block_interface(self, handle):
        block_interface = (
            handle.by(name=DataCenterServerPage.block_interface["title_ru"])
            .find()
            .window_text()
        )
        check.equal(block_interface, "блокировать интерфейс на 1 минуту")

    def test_setup_acc_pass(self, handle):
        setup_acc_pass = (
            handle.by(name=DataCenterServerPage.setup_acc_pass["title_ru"])
            .find()
            .window_text()
        )
        check.equal(setup_acc_pass, "Настройка паролей для учетных записей")

    def test_failed_attempts(self, handle):
        failed_attempts = (
            handle.by(name=DataCenterServerPage.failed_attempts["title_ru"])
            .find()
            .window_text()
        )
        check.equal(failed_attempts, "После 3-х неудачных попыток ввода пароля:")

    def test_special_characters(self, handle):
        special_characters = (
            handle.by(name=DataCenterServerPage.special_characters["title_ru"])
            .find()
            .window_text()
        )
        check.equal(special_characters, "спецсимволы")

    def test_lower_upper_cases(self, handle):
        lower_upper_cases = (
            handle.by(name=DataCenterServerPage.lower_upper_cases["title_ru"])
            .find()
            .window_text()
        )
        check.equal(lower_upper_cases, "разный регистр")

    def test_letters_figures(self, handle):
        letters_figures = (
            handle.by(name=DataCenterServerPage.letters_figures["title_ru"])
            .find()
            .window_text()
        )
        check.equal(letters_figures, "буквы и цифры")

    def test_password_contain(self, handle):
        password_contain = (
            handle.by(name=DataCenterServerPage.password_contain["title_ru"])
            .find()
            .window_text()
        )
        check.equal(password_contain, "Пароль должен содержать:")

    def test_minimum_characters(self, handle):
        minimum_characters = (
            handle.by(name=DataCenterServerPage.minimum_characters["title_ru"])
            .find()
            .window_text()
        )
        check.equal(minimum_characters, "Минимальная длина, символов:")

    def test_notify_if(self, handle):
        notify_if = (
            handle.by(name=DataCenterServerPage.notify_if["title_ru"])
            .find()
            .window_text()
        )
        check.equal(notify_if, "Критерии оповещений:")

    def test_pcap(self, handle):
        pcap = (
            handle.by(name=DataCenterServerPage.pcap["title_ru"]).find().window_text()
        )
        check.equal(pcap, "Файлы сохраненного трафика больше")

    def test_free_space_on_local_drive(self, handle):
        free_space_on_local_drive = (
            handle.by(name=DataCenterServerPage.free_space_on_local_drive["title_ru"])
            .find()
            .window_text()
        )
        check.equal(
            free_space_on_local_drive, "Свободное место на локальном диске меньше "
        )

    def test_performance_logs(self, handle):
        performance_logs = (
            handle.by(name=DataCenterServerPage.performance_logs["title_ru"])
            .find()
            .window_text()
        )
        check.equal(performance_logs, "Файлы журнала производительности больше")

    def test_operation_logs(self, handle):
        operation_logs = (
            handle.by(name=DataCenterServerPage.operation_logs["title_ru"])
            .find()
            .window_text()
        )
        check.equal(operation_logs, "Файлы журналирования больше")

    def test_unmount_db_if(self, handle):
        unmount_db_if = (
            handle.by(name=DataCenterServerPage.unmount_db_if["title_ru"])
            .find()
            .window_text()
        )
        check.equal(
            unmount_db_if,
            "Демонтировать БД при получении данных об ее отсутствии на сервере SQL от агента DataCenter",
        )

    def test_use_tokens(self, handle):
        use_tokens = (
            handle.by(name=DataCenterServerPage.use_tokens["title_ru"])
            .find()
            .window_text()
        )
        check.equal(
            use_tokens,
            "Использовать токены для защищенной аутентификации пользователей",
        )

    def test_mail_notif_lan(self, handle):
        mail_notif_lan = (
            handle.by(name=DataCenterServerPage.mail_notif_lan["title_ru"])
            .find()
            .window_text()
        )
        check.equal(mail_notif_lan, "Язык почтовых уведомлений")

    def test_log_level(self, handle):
        log_level = (
            handle.by(name=DataCenterServerPage.log_level["title_ru"])
            .find()
            .window_text()
        )
        check.equal(log_level, "Логирование")

    def test_automatic_update_agents(self, handle):
        automatic_update_agents = (
            handle.by(name=DataCenterServerPage.automatic_update_agents["title_ru"])
            .find()
            .window_text()
        )
        check.equal(
            automatic_update_agents,
            "Автоматическое обновление агентов на удаленных серверах",
        )
