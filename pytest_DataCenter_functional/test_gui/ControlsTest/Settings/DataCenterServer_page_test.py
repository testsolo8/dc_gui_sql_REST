# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import DataCenterServerPage


@pytest.fixture(scope="class")
def handle(start_test_page):
    send_keys("{VK_MENU down}Y3Y1{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Settings
@allure.story("тест главного окна настройки сервера DataCenter")
class TestDataCenterServerPage:
    def test_cancel_button(self, handle, title_key):
        cancel_button = handle.by(name=DataCenterServerPage.cancel_button[title_key]).find().window_text()
        check.equal(cancel_button, DataCenterServerPage.cancel_button[title_key])

    def test_apply_button(self, handle, title_key):
        apply_button = handle.by(name=DataCenterServerPage.apply_button[title_key]).find().window_text()
        check.equal(apply_button, DataCenterServerPage.apply_button[title_key])

    def test_block_account(self, handle, title_key):
        block_account = handle.by(name=DataCenterServerPage.block_account[title_key]).find().window_text()
        check.equal(block_account, DataCenterServerPage.block_account[title_key])

    def test_block_interface(self, handle, title_key):
        block_interface = handle.by(name=DataCenterServerPage.block_interface[title_key]).find().window_text()
        check.equal(block_interface, DataCenterServerPage.block_interface[title_key])

    def test_setup_acc_pass(self, handle, title_key):
        setup_acc_pass = handle.by(name=DataCenterServerPage.setup_acc_pass[title_key]).find().window_text()
        check.equal(setup_acc_pass, DataCenterServerPage.setup_acc_pass[title_key])

    def test_failed_attempts(self, handle, title_key):
        failed_attempts = handle.by(name=DataCenterServerPage.failed_attempts[title_key]).find().window_text()
        check.equal(failed_attempts, DataCenterServerPage.failed_attempts[title_key])

    def test_special_characters(self, handle, title_key):
        special_characters = handle.by(name=DataCenterServerPage.special_characters[title_key]).find().window_text()
        check.equal(special_characters, DataCenterServerPage.special_characters[title_key])

    def test_lower_upper_cases(self, handle, title_key):
        lower_upper_cases = handle.by(name=DataCenterServerPage.lower_upper_cases[title_key]).find().window_text()
        check.equal(lower_upper_cases, DataCenterServerPage.lower_upper_cases[title_key])

    def test_letters_figures(self, handle, title_key):
        letters_figures = handle.by(name=DataCenterServerPage.letters_figures[title_key]).find().window_text()
        check.equal(letters_figures, DataCenterServerPage.letters_figures[title_key])

    def test_password_contain(self, handle, title_key):
        password_contain = handle.by(name=DataCenterServerPage.password_contain[title_key]).find().window_text()
        check.equal(password_contain, DataCenterServerPage.password_contain[title_key])

    def test_minimum_characters(self, handle, title_key):
        minimum_characters = handle.by(name=DataCenterServerPage.minimum_characters[title_key]).find().window_text()
        check.equal(minimum_characters, DataCenterServerPage.minimum_characters[title_key])

    def test_notify_if(self, handle, title_key):
        notify_if = handle.by(name=DataCenterServerPage.notify_if[title_key]).find().window_text()
        check.equal(notify_if, DataCenterServerPage.notify_if[title_key])

    def test_pcap(self, handle, title_key):
        pcap = handle.by(name=DataCenterServerPage.pcap[title_key]).find().window_text()
        check.equal(pcap, DataCenterServerPage.pcap[title_key])

    def test_free_space_on_local_drive(self, handle, title_key):
        free_space_on_local_drive = (
            handle.by(name=DataCenterServerPage.free_space_on_local_drive[title_key]).find().window_text()
        )
        check.equal(free_space_on_local_drive, DataCenterServerPage.free_space_on_local_drive[title_key])

    def test_performance_logs(self, handle, title_key):
        performance_logs = handle.by(name=DataCenterServerPage.performance_logs[title_key]).find().window_text()
        check.equal(performance_logs, DataCenterServerPage.performance_logs[title_key])

    def test_operation_logs(self, handle, title_key):
        operation_logs = handle.by(name=DataCenterServerPage.operation_logs[title_key]).find().window_text()
        check.equal(operation_logs, DataCenterServerPage.operation_logs[title_key])

    def test_unmount_db_if(self, handle, title_key):
        unmount_db_if = handle.by(name=DataCenterServerPage.unmount_db_if[title_key]).find().window_text()
        check.equal(
            unmount_db_if,
            DataCenterServerPage.unmount_db_if[title_key],
        )

    def test_use_tokens(self, handle, title_key):
        use_tokens = handle.by(name=DataCenterServerPage.use_tokens[title_key]).find().window_text()
        check.equal(use_tokens, DataCenterServerPage.use_tokens[title_key])

    def test_mail_notif_lan(self, handle, title_key):
        mail_notif_lan = handle.by(name=DataCenterServerPage.mail_notif_lan[title_key]).find().window_text()
        check.equal(mail_notif_lan, DataCenterServerPage.mail_notif_lan[title_key])

    def test_log_level(self, handle, title_key):
        log_level = handle.by(name=DataCenterServerPage.log_level[title_key]).find().window_text()
        check.equal(log_level, DataCenterServerPage.log_level[title_key])

    def test_automatic_update_agents(self, handle, title_key):
        automatic_update_agents = (
            handle.by(name=DataCenterServerPage.automatic_update_agents[title_key]).find().window_text()
        )
        check.equal(automatic_update_agents, DataCenterServerPage.automatic_update_agents[title_key])
