# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import DigitalFingerprintsPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y03{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("RUS Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsRU
@pytest.mark.testGUI_RusVersionDCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки цифровых отпечатков")
class TestDigitalFingerprintsPage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=DigitalFingerprintsPage.cancel_button["title_ru"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Отменить")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=DigitalFingerprintsPage.apply_button["title_ru"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Применить")

    def test_digital_fingerprints_samples_folder(self, handle):
        digital_fingerprints_samples_folder = (
            handle.by(
                name=DigitalFingerprintsPage.digital_fingerprints_samples_folder[
                    "title_ru"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            digital_fingerprints_samples_folder, "Каталог образцов цифровых отпечатков"
        )

    def test_replace(self, handle):
        replace = (
            handle.by(name=DigitalFingerprintsPage.replace["title_ru"])
            .find()
            .window_text()
        )
        check.equal(replace, "Заменить")

    def test_add(self, handle):
        add = (
            handle.by(name=DigitalFingerprintsPage.add["title_ru"]).find().window_text()
        )
        check.equal(add, "Добавить")

    def test_delete(self, handle):
        delete = (
            handle.by(name=DigitalFingerprintsPage.delete["title_ru"])
            .find()
            .window_text()
        )
        check.equal(delete, "Удалить")

    def test_last_update(self, handle):
        last_update = (
            handle.by(name=DigitalFingerprintsPage.last_update["title_ru"])
            .find()
            .window_text()
        )
        check.equal(last_update, "Время последнего обновления")

    def test_processed_documents(self, handle):
        processed_documents = (
            handle.by(name=DigitalFingerprintsPage.processed_documents["title_ru"])
            .find()
            .window_text()
        )
        check.equal(processed_documents, "Обработано документов")

    def test_process_digital_fingerprints_on_search_server(self, handle):
        process_digital_fingerprints_on_search_server = (
            handle.by(
                name=DigitalFingerprintsPage.process_digital_fingerprints_on_search_server[
                    "title_ru"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            process_digital_fingerprints_on_search_server,
            "Обрабатывать цифровые отпечатки на Search Server",
        )
