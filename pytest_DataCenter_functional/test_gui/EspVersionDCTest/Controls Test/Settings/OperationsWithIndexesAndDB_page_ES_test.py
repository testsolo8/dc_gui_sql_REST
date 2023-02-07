# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import OperationsWithIndexesAndDBPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y3Y4{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("ESP Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControlsES
@pytest.mark.testGUI_EspVersionDCTest_ControlsTest_Settings
@allure.story("тест главного окна настройки операций над индексами и БД")
class TestOperationsWithIndexesAndDBPage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=OperationsWithIndexesAndDBPage.cancel_button["title_es"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Cancelar")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=OperationsWithIndexesAndDBPage.apply_button["title_es"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Aplicar")

    def test_export_button(self, handle):
        export_button = (
            handle.by(name=OperationsWithIndexesAndDBPage.export_button["title_es"])
            .find()
            .window_text()
        )
        check.equal(export_button, "Exportar")

    def test_import_button(self, handle):
        import_button = (
            handle.by(name=OperationsWithIndexesAndDBPage.import_button["title_es"])
            .find()
            .window_text()
        )
        check.equal(import_button, "Importar")

    def test_location_of_databases(self, handle):
        location_of_databases = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.location_of_databases["title_es"]
            )
            .find()
            .window_text()
        )
        check.equal(location_of_databases, "Ubicación de bases de datos")

    def test_inherit_databases_original(self, handle):
        inherit_databases_original = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.inherit_databases_original[
                    "title_es"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            inherit_databases_original,
            "Heredar rutas de creación de bases de datos desde la BD original (dividida)",
        )

    def test_inherit_databases_mssql(self, handle):
        inherit_databases_mssql = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.inherit_databases_mssql["title_es"]
            )
            .find()
            .window_text()
        )
        check.equal(
            inherit_databases_mssql,
            "Heredar rutas de creación de bases de datos desde los ajustes del MS SQL Server",
        )

    def test_weekdays_only(self, handle):
        weekdays_only = (
            handle.by(name=OperationsWithIndexesAndDBPage.weekdays_only["title_es"])
            .find()
            .window_text()
        )
        check.equal(weekdays_only, "solo días de trabajo")

    def test_control_new_data(self, handle):
        control_new_data = (
            handle.by(name=OperationsWithIndexesAndDBPage.control_new_data["title_es"])
            .find()
            .window_text()
        )
        check.equal(
            control_new_data,
            "Controlar datos nuevos recibidos en índice en el período de tiempo de",
        )

    def test_delete_indexes_available_for_search(self, handle):
        delete_indexes_available_for_search = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.delete_indexes_available_for_search[
                    "title_es"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            delete_indexes_available_for_search,
            "Borrar índices disponibles para búsqueda",
        )

    def test_automatically_delete_indexes(self, handle):
        automatically_delete_indexes = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.automatically_delete_indexes[
                    "title_es"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            automatically_delete_indexes,
            "Automáticamente borrar índices no disponibles para búsqueda al cumplir algunas de condiciones",
        )

    def test_add_suffix_index_filename(self, handle):
        add_suffix_index_filename = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.add_suffix_index_filename[
                    "title_es"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(add_suffix_index_filename, "Añadir sufijo a nombre de índice")

    def test_create_index_in_new_folder(self, handle):
        create_index_in_new_folder = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.create_index_in_new_folder[
                    "title_es"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(create_index_in_new_folder, "Crear índice en carpeta nueva")

    def test_index_size_over(self, handle):
        index_size_over = (
            handle.by(name=OperationsWithIndexesAndDBPage.index_size_over["title_es"])
            .find()
            .window_text()
        )
        check.equal(index_size_over, "Tamaño de índice es más de (GB)")

    def test_text_size(self, handle):
        text_size = (
            handle.by(name=OperationsWithIndexesAndDBPage.text_size["title_es"])
            .find()
            .window_text()
        )
        check.equal(text_size, "Tamaño de texto en índice (GB)")

    def test_on_schedule(self, handle):
        on_schedule = (
            handle.by(name=OperationsWithIndexesAndDBPage.on_schedule["title_es"])
            .find()
            .window_text()
        )
        check.equal(on_schedule, "Dividir según horario")

    def test_scheduler(self, handle):
        scheduler = (
            handle.by(name=OperationsWithIndexesAndDBPage.scheduler["title_es"])
            .find()
            .window_text()
        )
        check.equal(scheduler, "Configurar...")

    def test_number_of_documents(self, handle):
        number_of_documents = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.number_of_documents["title_es"]
            )
            .find()
            .window_text()
        )
        check.equal(number_of_documents, "Número de documentos (millón)")

    def test_documents_size(self, handle):
        documents_size = (
            handle.by(name=OperationsWithIndexesAndDBPage.documents_size["title_es"])
            .find()
            .window_text()
        )
        check.equal(documents_size, "Tamaño de documentos (GB)")

    def test_index_older_than(self, handle):
        index_older_than = (
            handle.by(name=OperationsWithIndexesAndDBPage.index_older_than["title_es"])
            .find()
            .window_text()
        )
        check.equal(index_older_than, "Índice es más antiguo de (días)")

    def test_number_of_db_records(self, handle):
        number_of_db_records = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.number_of_db_records["title_es"]
            )
            .find()
            .window_text()
        )
        check.equal(number_of_db_records, "Número de registros en BD (millón)")

    def test_db_data_size(self, handle):
        db_data_size = (
            handle.by(name=OperationsWithIndexesAndDBPage.db_data_size["title_es"])
            .find()
            .window_text()
        )
        check.equal(db_data_size, "Tamaño de datos en BD (GB)")

    def test_number_of_unique_words(self, handle):
        number_of_unique_words = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.number_of_unique_words["title_es"]
            )
            .find()
            .window_text()
        )
        check.equal(number_of_unique_words, "Número de palabras únicas (millón)")

    def test_only_in_time_period(self, handle):
        only_in_time_period = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.only_in_time_period["title_es"]
            )
            .find()
            .window_text()
        )
        check.equal(only_in_time_period, "solo en el período de tiempo desde")

    def test_automatically_create_indexes(self, handle):
        automatically_create_indexes = (
            handle.by(
                name=OperationsWithIndexesAndDBPage.automatically_create_indexes[
                    "title_es"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            automatically_create_indexes,
            "Automáticamente crear índices al cumplir algunas de condiciones ",
        )
