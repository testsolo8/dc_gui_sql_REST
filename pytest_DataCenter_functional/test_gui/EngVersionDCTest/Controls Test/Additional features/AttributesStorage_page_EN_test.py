# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import AttributesStoragePage


@pytest.fixture(scope="class")
def handle(start_test_page_en):
    send_keys("{VK_MENU down}Y4Y08{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("ENG Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsEN
@pytest.mark.testGUI_EngVersionDCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки хранилища атрибутов")
class TestAttributesStoragePage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=AttributesStoragePage.cancel_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Cancel")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=AttributesStoragePage.apply_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Apply")

    def test_clear_database_button(self, handle):
        clear_database = (
            handle.by(name=AttributesStoragePage.clear_database["title_en"])
            .find()
            .window_text()
        )
        check.equal(clear_database, "Clear database")

    def test_setup_connection_to_db(self, handle):
        setup_connection_to_db = (
            handle.by(name=AttributesStoragePage.setup_connection_to_db["title_en"])
            .find()
            .window_text()
        )
        check.equal(setup_connection_to_db, "Set up connection to DB ")

    def test_month_panel(self, handle):
        months = (
            handle.by(name=AttributesStoragePage.months["title_en"])
            .find()
            .window_text()
        )
        check.equal(months, "months")

    def test_read_data_for_the_last(self, handle):
        read_data_for_the_last = (
            handle.by(name=AttributesStoragePage.read_data_for_the_last["title_en"])
            .find()
            .window_text()
        )
        check.equal(read_data_for_the_last, "Read data for the last")

    def test_use_storage_of_attributes(self, handle):
        use_storage_of_attributes = (
            handle.by(name=AttributesStoragePage.use_storage_of_attributes["title_en"])
            .find()
            .window_text()
        )
        check.equal(use_storage_of_attributes, "Use storage of attributes")

    def test_log_level(self, handle):
        log_level = (
            handle.by(name=AttributesStoragePage.log_level["title_en"])
            .find()
            .window_text()
        )
        check.equal(log_level, "Log level  ")

    def test_connection_to_db(self, handle):
        connection_to_db = (
            handle.by(name=AttributesStoragePage.connection_to_db["title_en"])
            .find()
            .window_text()
        )
        check.equal(connection_to_db, "Connection to DB")

    def test_sql_server(self, handle):
        sql_server = (
            handle.by(name=AttributesStoragePage.sql_server["title_en"])
            .find()
            .window_text()
        )
        check.equal(sql_server, "SQL Server")

    def test_database(self, handle):
        database = (
            handle.by(name=AttributesStoragePage.database["title_en"])
            .find()
            .window_text()
        )
        check.equal(database, "Database")
