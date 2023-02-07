# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import OperationsLoggingPage


@pytest.fixture(scope="class")
def handle(start_test_page_en):
    send_keys("{VK_MENU down}Y4Y01{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("ENG Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsEN
@pytest.mark.testGUI_EngVersionDCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки журналирования операций")
class TestOperationsLoggingPage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=OperationsLoggingPage.cancel_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Cancel")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=OperationsLoggingPage.apply_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Apply")

    def test_setup_connection_to_db(self, handle):
        setup_connection_to_db = (
            handle.by(name=OperationsLoggingPage.setup_connection_to_db["title_en"])
            .find()
            .window_text()
        )
        check.equal(setup_connection_to_db, "Set up connection to DB ")

    def test_data_restriction_when_logging_operations(self, handle):
        data_restriction_when_logging_operations = (
            handle.by(
                name=OperationsLoggingPage.data_restriction_when_logging_operations[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            data_restriction_when_logging_operations,
            "Data restriction when logging operations",
        )

    def test_list_of_products(self, handle):
        list_of_products = (
            handle.by(name=OperationsLoggingPage.list_of_products["title_en"])
            .find()
            .window_text()
        )
        check.equal(list_of_products, "List of products")

    def test_connection_to_db(self, handle):
        connection_to_db = (
            handle.by(name=OperationsLoggingPage.connection_to_db["title_en"])
            .find()
            .window_text()
        )
        check.equal(connection_to_db, "Connection to DB")

    def test_enable_logging_of_auditors(self, handle):
        enable_logging_of_auditors = (
            handle.by(name=OperationsLoggingPage.enable_logging_of_auditors["title_en"])
            .find()
            .window_text()
        )
        check.equal(
            enable_logging_of_auditors,
            "Enable logging of auditors' actions in the product consoles",
        )
