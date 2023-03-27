# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import DigitalFingerprintsPage


@pytest.fixture(scope="class")
def handle(start_test_page):
    send_keys("{VK_MENU down}Y4Y03{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки цифровых отпечатков")
class TestDigitalFingerprintsPage:
    def test_cancel_button(self, handle, title_key):
        cancel_button = handle.by(name=DigitalFingerprintsPage.cancel_button[title_key]).find().window_text()
        check.equal(cancel_button, DigitalFingerprintsPage.cancel_button[title_key])

    def test_apply_button(self, handle, title_key):
        apply_button = handle.by(name=DigitalFingerprintsPage.apply_button[title_key]).find().window_text()
        check.equal(apply_button, DigitalFingerprintsPage.apply_button[title_key])

    def test_digital_fingerprints_samples_folder_group(self, handle, title_key):
        digital_fingerprints_samples_folder = (
            handle.by(name=DigitalFingerprintsPage.digital_fingerprints_samples_folder[title_key]).find().window_text()
        )
        check.equal(digital_fingerprints_samples_folder, DigitalFingerprintsPage.digital_fingerprints_samples_folder[title_key])

    def test_replace(self, handle, title_key):
        replace = handle.by(name=DigitalFingerprintsPage.replace[title_key]).find().window_text()
        check.equal(replace, DigitalFingerprintsPage.replace[title_key])

    def test_add(self, handle, title_key):
        add = handle.by(name=DigitalFingerprintsPage.add[title_key]).find().window_text()
        check.equal(add, DigitalFingerprintsPage.add[title_key])

    def test_delete(self, handle, title_key):
        delete = handle.by(name=DigitalFingerprintsPage.delete[title_key]).find().window_text()
        check.equal(delete, DigitalFingerprintsPage.delete[title_key])

    def test_last_update(self, handle, title_key):
        last_update = handle.by(name=DigitalFingerprintsPage.last_update[title_key]).find().window_text()
        check.equal(last_update, DigitalFingerprintsPage.last_update[title_key])

    def test_processed_documents(self, handle, title_key):
        processed_documents = (
            handle.by(name=DigitalFingerprintsPage.processed_documents[title_key]).find().window_text()
        )
        check.equal(processed_documents, DigitalFingerprintsPage.processed_documents[title_key])

    def test_process_digital_fingerprints_on_search_server(self, handle, title_key):
        process_digital_fingerprints_on_search_server = (
            handle.by(name=DigitalFingerprintsPage.process_digital_fingerprints_on_search_server[title_key])
            .find()
            .window_text()
        )
        check.equal(
            process_digital_fingerprints_on_search_server,
            DigitalFingerprintsPage.process_digital_fingerprints_on_search_server[title_key],
        )
