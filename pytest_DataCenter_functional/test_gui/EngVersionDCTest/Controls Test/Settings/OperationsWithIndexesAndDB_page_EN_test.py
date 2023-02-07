# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import OperationsWithIndexesAndDBPage


@pytest.fixture(scope="class")
def handle(start_test_page_en):
    send_keys("{VK_MENU down}Y3Y4{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("ENG Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControlsEN
@pytest.mark.testGUI_EngVersionDCTest_ControlsTest_Settings
@allure.story("тест главного окна настройки операций над индексами и БД")
class TestOperationsWithIndexesAndDBPage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=OperationsWithIndexesAndDBPage.cancel_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Cancel")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=OperationsWithIndexesAndDBPage.apply_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Apply")

    def test_export_button(self, handle):
        export_button = (
            handle.by(name=OperationsWithIndexesAndDBPage.export_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(export_button, "Export")

    def test_import_button(self, handle):
        import_button = (
            handle.by(name=OperationsWithIndexesAndDBPage.import_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(import_button, "Import")

    def test_location_of_databases(self, handle):
        location_of_databases = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.location_of_databases["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(location_of_databases, "Location of databases")

    def test_inherit_databases_original(self, handle):
        inherit_databases_original = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.inherit_databases_original[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            inherit_databases_original,
            "Inherit databases creation paths from the original (split) database",
        )

    def test_inherit_databases_mssql(self, handle):
        inherit_databases_mssql = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.inherit_databases_mssql["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(
            inherit_databases_mssql,
            "Inherit databases creation paths from the MS SQL Server settings",
        )

    def test_weekdays_only(self, handle):
        weekdays_only = (
            handle.by(name=OperationsWithIndexesAndDBPage.weekdays_only["title_en"])
            .find()
            .window_text()
        )
        check.equal(weekdays_only, "weekdays only")

    def test_control_new_data(self, handle):
        control_new_data = (
            handle.by(name=OperationsWithIndexesAndDBPage.control_new_data["title_en"])
            .find()
            .window_text()
        )
        check.equal(
            control_new_data,
            "Control new data received in index in the time period from ",
        )

    def test_delete_indexes_available_for_search(self, handle):
        delete_indexes_available_for_search = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.delete_indexes_available_for_search[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            delete_indexes_available_for_search, "Delete indexes available for search"
        )

    def test_automatically_delete_indexes(self, handle):
        automatically_delete_indexes = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.automatically_delete_indexes[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            automatically_delete_indexes,
            "Automatically delete indexes unavailable for search if the following conditions are met:",
        )

    def test_add_suffix_index_filename(self, handle):
        add_suffix_index_filename = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.add_suffix_index_filename[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(add_suffix_index_filename, "Add a suffix to index file name")

    def test_create_index_in_new_folder(self, handle):
        create_index_in_new_folder = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.create_index_in_new_folder[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(create_index_in_new_folder, "Create index in a new folder")

    def test_index_size_over(self, handle):
        index_size_over = (
            handle.by(name=OperationsWithIndexesAndDBPage.index_size_over["title_en"])
            .find()
            .window_text()
        )
        check.equal(index_size_over, "Index size over (GB)")

    def test_text_size(self, handle):
        text_size = (
            handle.by(name=OperationsWithIndexesAndDBPage.text_size["title_en"])
            .find()
            .window_text()
        )
        check.equal(text_size, "Text size (GB)")

    def test_on_schedule(self, handle):
        on_schedule = (
            handle.by(name=OperationsWithIndexesAndDBPage.on_schedule["title_en"])
            .find()
            .window_text()
        )
        check.equal(on_schedule, "On schedule")

    def test_scheduler(self, handle):
        scheduler = (
            handle.by(name=OperationsWithIndexesAndDBPage.scheduler["title_en"])
            .find()
            .window_text()
        )
        check.equal(scheduler, "Scheduler...")

    def test_number_of_documents(self, handle):
        number_of_documents = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.number_of_documents["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(number_of_documents, "Number of documents (MIO)")

    def test_documents_size(self, handle):
        documents_size = (
            handle.by(name=OperationsWithIndexesAndDBPage.documents_size["title_en"])
            .find()
            .window_text()
        )
        check.equal(documents_size, "Documents size (GB)")

    def test_index_older_than(self, handle):
        index_older_than = (
            handle.by(name=OperationsWithIndexesAndDBPage.index_older_than["title_en"])
            .find()
            .window_text()
        )
        check.equal(index_older_than, "Index older than (days)")

    def test_number_of_db_records(self, handle):
        number_of_db_records = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.number_of_db_records["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(number_of_db_records, "Number of DB records (MIO)")

    def test_db_data_size(self, handle):
        db_data_size = (
            handle.by(name=OperationsWithIndexesAndDBPage.db_data_size["title_en"])
            .find()
            .window_text()
        )
        check.equal(db_data_size, "DB data size (GB)")

    def test_number_of_unique_words(self, handle):
        number_of_unique_words = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.number_of_unique_words["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(number_of_unique_words, "Number of unique words (MIO)")

    def test_only_in_time_period(self, handle):
        only_in_time_period = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.only_in_time_period["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(only_in_time_period, "only in the time period from ")

    def test_automatically_create_indexes(self, handle):
        automatically_create_indexes = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.automatically_create_indexes[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            automatically_create_indexes,
            "Automatically create indexes if any of the following conditions are met:",
        )
