# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import DigitalFingerprintsPage


@pytest.fixture(scope="class")
def handle(start_test_page_en):
    send_keys("{VK_MENU down}Y4Y03{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("ENG Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsEN
@pytest.mark.testGUI_EngVersionDCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки цифровых отпечатков")
class TestDigitalFingerprintsPage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=DigitalFingerprintsPage.cancel_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Cancel")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=DigitalFingerprintsPage.apply_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Apply")

    def test_digital_fingerprints_samples_folder_group(self, handle):
        digital_fingerprints_samples_folder = (
            handle.by(
                name=DigitalFingerprintsPage.digital_fingerprints_samples_folder[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            digital_fingerprints_samples_folder, "Digital fingerprints samples folder"
        )

    def test_replace(self, handle):
        replace = (
            handle.by(name=DigitalFingerprintsPage.replace["title_en"])
            .find()
            .window_text()
        )
        check.equal(replace, "Replace")

    def test_add(self, handle):
        add = (
            handle.by(name=DigitalFingerprintsPage.add["title_en"]).find().window_text()
        )
        check.equal(add, "Add")

    def test_delete(self, handle):
        delete = (
            handle.by(name=DigitalFingerprintsPage.delete["title_en"])
            .find()
            .window_text()
        )
        check.equal(delete, "Delete")

    def test_last_update(self, handle):
        last_update = (
            handle.by(name=DigitalFingerprintsPage.last_update["title_en"])
            .find()
            .window_text()
        )
        check.equal(last_update, "Last update")

    def test_processed_documents(self, handle):
        processed_documents = (
            handle.by(name=DigitalFingerprintsPage.processed_documents["title_en"])
            .find()
            .window_text()
        )
        check.equal(processed_documents, "Processed documents")

    def test_process_digital_fingerprints_on_search_server(self, handle):
        process_digital_fingerprints_on_search_server = (
            handle.by(
                name=DigitalFingerprintsPage.process_digital_fingerprints_on_search_server[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            process_digital_fingerprints_on_search_server,
            "Process digital fingerprints on Search Server",
        )
