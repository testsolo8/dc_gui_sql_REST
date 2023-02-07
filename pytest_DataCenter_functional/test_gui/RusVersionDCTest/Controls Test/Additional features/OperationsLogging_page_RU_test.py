# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import OperationsLoggingPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y01{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("RUS Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsRU
@pytest.mark.testGUI_RusVersionDCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки журналирования операций")
class TestOperationsLoggingPage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=OperationsLoggingPage.cancel_button["title_ru"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Отменить")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=OperationsLoggingPage.apply_button["title_ru"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Применить")

    def test_setup_connection_to_db(self, handle):
        setup_connection_to_db = (
            handle.by(name=OperationsLoggingPage.setup_connection_to_db["title_ru"])
            .find()
            .window_text()
        )
        check.equal(setup_connection_to_db, "Настроить подключение к БД")

    def test_data_restriction_when_logging_operations(self, handle):
        data_restriction_when_logging_operations = (
            handle.by(
                name=OperationsLoggingPage.data_restriction_when_logging_operations[
                    "title_ru"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            data_restriction_when_logging_operations,
            "Ограничение данных при журналировании операций",
        )

    def test_list_of_products(self, handle):
        list_of_products = (
            handle.by(name=OperationsLoggingPage.list_of_products["title_ru"])
            .find()
            .window_text()
        )
        check.equal(list_of_products, "Список продуктов")

    def test_connection_to_db(self, handle):
        connection_to_db = (
            handle.by(name=OperationsLoggingPage.connection_to_db["title_ru"])
            .find()
            .window_text()
        )
        check.equal(connection_to_db, "Подключение к БД")

    def test_enable_logging_of_auditors(self, handle):
        enable_logging_of_auditors = (
            handle.by(name=OperationsLoggingPage.enable_logging_of_auditors["title_ru"])
            .find()
            .window_text()
        )
        check.equal(
            enable_logging_of_auditors,
            "Включить журналирование действий аудиторов в консолях продуктов",
        )
