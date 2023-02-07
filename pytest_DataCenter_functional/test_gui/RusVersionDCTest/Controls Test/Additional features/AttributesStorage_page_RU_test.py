# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import AttributesStoragePage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y08{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("RUS Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsRU
@pytest.mark.testGUI_RusVersionDCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки хранилища атрибутов")
class TestAttributesStoragePage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=AttributesStoragePage.cancel_button["title_ru"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Отменить")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=AttributesStoragePage.apply_button["title_ru"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Применить")

    def test_clear_database(self, handle):
        clear_database = (
            handle.by(name=AttributesStoragePage.clear_database["title_ru"])
            .find()
            .window_text()
        )
        check.equal(clear_database, "Очистить БД")

    def test_setup_connection_to_db(self, handle):
        setup_connection_to_db = (
            handle.by(name=AttributesStoragePage.setup_connection_to_db["title_ru"])
            .find()
            .window_text()
        )
        check.equal(setup_connection_to_db, "Настроить подключение к БД")

    def test_months(self, handle):
        months = (
            handle.by(name=AttributesStoragePage.months["title_ru"])
            .find()
            .window_text()
        )
        check.equal(months, "месяцев")

    def test_read_data_for_the_last(self, handle):
        read_data_for_the_last = (
            handle.by(name=AttributesStoragePage.read_data_for_the_last["title_ru"])
            .find()
            .window_text()
        )
        check.equal(read_data_for_the_last, "Вычитывать данные за последние")

    def test_use_storage_of_attributes(self, handle):
        use_storage_of_attributes = (
            handle.by(name=AttributesStoragePage.use_storage_of_attributes["title_ru"])
            .find()
            .window_text()
        )
        check.equal(use_storage_of_attributes, "Использовать хранилище атрибутов")

    def test_log_level(self, handle):
        log_level = (
            handle.by(name=AttributesStoragePage.log_level["title_ru"])
            .find()
            .window_text()
        )
        check.equal(log_level, "Логирование")

    def test_connection_to_db(self, handle):
        connection_to_db = (
            handle.by(name=AttributesStoragePage.connection_to_db["title_ru"])
            .find()
            .window_text()
        )
        check.equal(connection_to_db, "Подключение к БД")

    def test_sql_server(self, handle):
        sql_server = (
            handle.by(name=AttributesStoragePage.sql_server["title_ru"])
            .find()
            .window_text()
        )
        check.equal(sql_server, "SQL cервер")

    def test_database(self, handle):
        database = (
            handle.by(name=AttributesStoragePage.database["title_ru"])
            .find()
            .window_text()
        )
        check.equal(database, "База данных")
