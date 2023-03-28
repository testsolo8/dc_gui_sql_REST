# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import OperationsWithIndexesAndDBPage


@pytest.fixture(scope="class")
def handle(start_test_page):
    send_keys("{VK_MENU down}Y3Y4{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Settings
@allure.story("тест главного окна настройки операций над индексами и БД")
class TestOperationsWithIndexesAndDBPage:
    def test_cancel_button(self, handle, title_key):
        cancel_button = handle.by(name=OperationsWithIndexesAndDBPage.cancel_button[title_key]).find().window_text()
        check.equal(cancel_button, OperationsWithIndexesAndDBPage.cancel_button[title_key])

    def test_apply_button(self, handle, title_key):
        apply_button = handle.by(name=OperationsWithIndexesAndDBPage.apply_button[title_key]).find().window_text()
        check.equal(apply_button, OperationsWithIndexesAndDBPage.apply_button[title_key])

    def test_export_button(self, handle, title_key):
        export_button = handle.by(name=OperationsWithIndexesAndDBPage.export_button[title_key]).find().window_text()
        check.equal(export_button, OperationsWithIndexesAndDBPage.export_button[title_key])

    def test_import_button(self, handle, title_key):
        import_button = handle.by(name=OperationsWithIndexesAndDBPage.import_button[title_key]).find().window_text()
        check.equal(import_button, OperationsWithIndexesAndDBPage.import_button[title_key])

    def test_location_of_databases(self, handle, title_key):
        location_of_databases = (
            handle.by(name=OperationsWithIndexesAndDBPage.location_of_databases[title_key]).find().window_text()
        )
        check.equal(location_of_databases, OperationsWithIndexesAndDBPage.location_of_databases[title_key])

    def test_inherit_databases_original(self, handle, title_key):
        inherit_databases_original = (
            handle.by(name=OperationsWithIndexesAndDBPage.inherit_databases_original[title_key]).find().window_text()
        )
        check.equal(
            inherit_databases_original,
            OperationsWithIndexesAndDBPage.inherit_databases_original[title_key],
        )

    def test_inherit_databases_mssql(self, handle, title_key):
        inherit_databases_mssql = (
            handle.by(name=OperationsWithIndexesAndDBPage.inherit_databases_mssql[title_key]).find().window_text()
        )
        check.equal(
            inherit_databases_mssql,
            OperationsWithIndexesAndDBPage.inherit_databases_mssql[title_key],
        )

    def test_weekdays_only(self, handle, title_key):
        weekdays_only = handle.by(name=OperationsWithIndexesAndDBPage.weekdays_only[title_key]).find().window_text()
        check.equal(weekdays_only, OperationsWithIndexesAndDBPage.weekdays_only[title_key])

    def test_control_new_data(self, handle, title_key):
        control_new_data = (
            handle.by(name=OperationsWithIndexesAndDBPage.control_new_data[title_key]).find().window_text()
        )
        check.equal(
            control_new_data,
            OperationsWithIndexesAndDBPage.control_new_data[title_key],
        )

    def test_delete_indexes_available_for_search(self, handle, title_key):
        delete_indexes_available_for_search = (
            handle.by(name=OperationsWithIndexesAndDBPage.delete_indexes_available_for_search[title_key])
            .find()
            .window_text()
        )
        check.equal(delete_indexes_available_for_search, OperationsWithIndexesAndDBPage.delete_indexes_available_for_search[title_key])

    def test_automatically_delete_indexes(self, handle, title_key):
        automatically_delete_indexes = (
            handle.by(name=OperationsWithIndexesAndDBPage.automatically_delete_indexes[title_key]).find().window_text()
        )
        check.equal(
            automatically_delete_indexes,
            OperationsWithIndexesAndDBPage.automatically_delete_indexes[title_key],
        )

    def test_add_suffix_index_filename(self, handle, title_key):
        add_suffix_index_filename = (
            handle.by(name=OperationsWithIndexesAndDBPage.add_suffix_index_filename[title_key]).find().window_text()
        )
        check.equal(add_suffix_index_filename, OperationsWithIndexesAndDBPage.add_suffix_index_filename[title_key])

    def test_create_index_in_new_folder(self, handle, title_key):
        create_index_in_new_folder = (
            handle.by(name=OperationsWithIndexesAndDBPage.create_index_in_new_folder[title_key]).find().window_text()
        )
        check.equal(create_index_in_new_folder, OperationsWithIndexesAndDBPage.create_index_in_new_folder[title_key])

    def test_index_size_over(self, handle, title_key):
        index_size_over = (
            handle.by(name=OperationsWithIndexesAndDBPage.index_size_over[title_key]).find().window_text()
        )
        check.equal(index_size_over, OperationsWithIndexesAndDBPage.index_size_over[title_key])

    def test_text_size(self, handle, title_key):
        text_size = handle.by(name=OperationsWithIndexesAndDBPage.text_size[title_key]).find().window_text()
        check.equal(text_size, OperationsWithIndexesAndDBPage.text_size[title_key])

    def test_on_schedule(self, handle, title_key):
        on_schedule = handle.by(name=OperationsWithIndexesAndDBPage.on_schedule[title_key]).find().window_text()
        check.equal(on_schedule, OperationsWithIndexesAndDBPage.on_schedule[title_key])

    def test_scheduler(self, handle, title_key):
        scheduler = handle.by(name=OperationsWithIndexesAndDBPage.scheduler[title_key]).find().window_text()
        check.equal(scheduler, OperationsWithIndexesAndDBPage.scheduler[title_key])

    def test_number_of_documents(self, handle, title_key):
        number_of_documents = (
            handle.by(name=OperationsWithIndexesAndDBPage.number_of_documents[title_key]).find().window_text()
        )
        check.equal(number_of_documents, OperationsWithIndexesAndDBPage.number_of_documents[title_key])

    def test_documents_size(self, handle, title_key):
        documents_size = handle.by(name=OperationsWithIndexesAndDBPage.documents_size[title_key]).find().window_text()
        check.equal(documents_size, OperationsWithIndexesAndDBPage.documents_size[title_key])

    def test_index_older_than(self, handle, title_key):
        index_older_than = (
            handle.by(name=OperationsWithIndexesAndDBPage.index_older_than[title_key]).find().window_text()
        )
        check.equal(index_older_than, OperationsWithIndexesAndDBPage.index_older_than[title_key])

    def test_number_of_db_records(self, handle, title_key):
        number_of_db_records = (
            handle.by(name=OperationsWithIndexesAndDBPage.number_of_db_records[title_key]).find().window_text()
        )
        check.equal(number_of_db_records, OperationsWithIndexesAndDBPage.number_of_db_records[title_key])

    def test_db_data_size(self, handle, title_key):
        db_data_size = handle.by(name=OperationsWithIndexesAndDBPage.db_data_size[title_key]).find().window_text()
        check.equal(db_data_size, OperationsWithIndexesAndDBPage.db_data_size[title_key])

    def test_number_of_unique_words(self, handle, title_key):
        number_of_unique_words = (
            handle.by(name=OperationsWithIndexesAndDBPage.number_of_unique_words[title_key]).find().window_text()
        )
        check.equal(number_of_unique_words, OperationsWithIndexesAndDBPage.number_of_unique_words[title_key])

    def test_only_in_time_period(self, handle, title_key):
        only_in_time_period = (
            handle.by(name=OperationsWithIndexesAndDBPage.only_in_time_period[title_key]).find().window_text()
        )
        check.equal(only_in_time_period, OperationsWithIndexesAndDBPage.only_in_time_period[title_key])

    def test_automatically_create_indexes(self, handle, title_key):
        automatically_create_indexes = (
            handle.by(name=OperationsWithIndexesAndDBPage.automatically_create_indexes[title_key]).find().window_text()
        )
        check.equal(
            automatically_create_indexes,
            OperationsWithIndexesAndDBPage.automatically_create_indexes[title_key],
        )
