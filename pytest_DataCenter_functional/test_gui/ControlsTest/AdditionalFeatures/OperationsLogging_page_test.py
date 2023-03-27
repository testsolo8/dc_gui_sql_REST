# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import OperationsLoggingPage


@pytest.fixture(scope="class")
def handle(start_test_page):
    send_keys("{VK_MENU down}Y4Y01{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки журналирования операций")
class TestOperationsLoggingPage:
    def test_cancel_button(self, handle, title_key):
        cancel_button = handle.by(name=OperationsLoggingPage.cancel_button[title_key]).find().window_text()
        check.equal(cancel_button, OperationsLoggingPage.cancel_button[title_key])

    def test_apply_button(self, handle, title_key):
        apply_button = handle.by(name=OperationsLoggingPage.apply_button[title_key]).find().window_text()
        check.equal(apply_button, OperationsLoggingPage.apply_button[title_key])

    def test_setup_connection_to_db(self, handle, title_key):
        setup_connection_to_db = (
            handle.by(name=OperationsLoggingPage.setup_connection_to_db[title_key]).find().window_text()
        )
        check.equal(setup_connection_to_db, OperationsLoggingPage.setup_connection_to_db[title_key])

    def test_data_restriction_when_logging_operations(self, handle, title_key):
        data_restriction_when_logging_operations = (
            handle.by(name=OperationsLoggingPage.data_restriction_when_logging_operations[title_key])
            .find()
            .window_text()
        )
        check.equal(
            data_restriction_when_logging_operations,
            OperationsLoggingPage.data_restriction_when_logging_operations[title_key],
        )

    def test_list_of_products(self, handle, title_key):
        list_of_products = handle.by(name=OperationsLoggingPage.list_of_products[title_key]).find().window_text()
        check.equal(list_of_products, OperationsLoggingPage.list_of_products[title_key])

    def test_connection_to_db(self, handle, title_key):
        connection_to_db = handle.by(name=OperationsLoggingPage.connection_to_db[title_key]).find().window_text()
        check.equal(connection_to_db, OperationsLoggingPage.connection_to_db[title_key])

    def test_enable_logging_of_auditors(self, handle, title_key):
        enable_logging_of_auditors = (
            handle.by(name=OperationsLoggingPage.enable_logging_of_auditors[title_key]).find().window_text()
        )
        check.equal(
            enable_logging_of_auditors,
            OperationsLoggingPage.enable_logging_of_auditors[title_key],
        )
