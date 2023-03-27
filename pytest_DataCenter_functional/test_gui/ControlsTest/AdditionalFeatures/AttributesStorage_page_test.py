# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import AttributesStoragePage


@pytest.fixture(scope="class")
def handle(start_test_page):
    send_keys("{VK_MENU down}Y4Y08{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки хранилища атрибутов")
class TestAttributesStoragePage:
    def test_cancel_button(self, handle, title_key):
        cancel_button = handle.by(name=AttributesStoragePage.cancel_button[title_key]).find().window_text()
        check.equal(cancel_button, AttributesStoragePage.cancel_button[title_key])

    def test_apply_button(self, handle, title_key):
        apply_button = handle.by(name=AttributesStoragePage.apply_button[title_key]).find().window_text()
        check.equal(apply_button, AttributesStoragePage.apply_button[title_key])

    def test_clear_database_button(self, handle, title_key):
        clear_database = handle.by(name=AttributesStoragePage.clear_database[title_key]).find().window_text()
        check.equal(clear_database, AttributesStoragePage.clear_database[title_key])

    def test_setup_connection_to_db(self, handle, title_key):
        setup_connection_to_db = (
            handle.by(name=AttributesStoragePage.setup_connection_to_db[title_key]).find().window_text()
        )
        check.equal(setup_connection_to_db, AttributesStoragePage.setup_connection_to_db[title_key])

    def test_month_panel(self, handle, title_key):
        months = handle.by(name=AttributesStoragePage.months[title_key]).find().window_text()
        check.equal(months, AttributesStoragePage.months[title_key])

    def test_read_data_for_the_last(self, handle, title_key):
        read_data_for_the_last = (
            handle.by(name=AttributesStoragePage.read_data_for_the_last[title_key]).find().window_text()
        )
        check.equal(read_data_for_the_last, AttributesStoragePage.read_data_for_the_last[title_key])

    def test_use_storage_of_attributes(self, handle, title_key):
        use_storage_of_attributes = (
            handle.by(name=AttributesStoragePage.use_storage_of_attributes[title_key]).find().window_text()
        )
        check.equal(use_storage_of_attributes, AttributesStoragePage.use_storage_of_attributes[title_key])

    def test_log_level(self, handle, title_key):
        log_level = handle.by(name=AttributesStoragePage.log_level[title_key]).find().window_text()
        check.equal(log_level, AttributesStoragePage.log_level[title_key])

    def test_connection_to_db(self, handle, title_key):
        connection_to_db = handle.by(name=AttributesStoragePage.connection_to_db[title_key]).find().window_text()
        check.equal(connection_to_db, AttributesStoragePage.connection_to_db[title_key])

    def test_sql_server(self, handle, title_key):
        sql_server = handle.by(name=AttributesStoragePage.sql_server[title_key]).find().window_text()
        check.equal(sql_server, AttributesStoragePage.sql_server[title_key])

    def test_database(self, handle, title_key):
        database = handle.by(name=AttributesStoragePage.database[title_key]).find().window_text()
        check.equal(database, AttributesStoragePage.database[title_key])
