# Standart libraries
import time

# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import OutlookCalendarsPage


@pytest.fixture(scope="class")
def handle(start_test_page):
    send_keys("{VK_MENU down}Y4Y10{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Additionalfeatures
@allure.story("тест главного окна настройки Outlook calendars")
class TestOutlookCalendarsPage:
    def test_cancel(self, handle, title_key):
        cancel = handle.by(name=OutlookCalendarsPage.cancel[title_key]).find().window_text()
        check.equal(cancel, OutlookCalendarsPage.cancel[title_key])

    def test_apply(self, handle, title_key):
        apply = handle.by(name=OutlookCalendarsPage.apply[title_key]).find().window_text()
        check.equal(apply, OutlookCalendarsPage.apply[title_key])

    def test_min_1(self, handle, title_key):
        min_1 = handle.by(name=OutlookCalendarsPage.min_1[title_key], found_index=OutlookCalendarsPage.min_1["found_index"]).find().window_text()
        check.equal(min_1, OutlookCalendarsPage.min_1[title_key])

    def test_min_2(self, handle, title_key):
        min_2 = handle.by(name=OutlookCalendarsPage.min_2[title_key], found_index=OutlookCalendarsPage.min_2["found_index"]).find().window_text()
        check.equal(min_2, OutlookCalendarsPage.min_2[title_key])

    def test_connection_to_exchange_server(self, handle, title_key):
        connection_to_exchange_server = (
            handle.by(name=OutlookCalendarsPage.connection_to_exchange_server[title_key]).find().window_text()
        )
        check.equal(connection_to_exchange_server, OutlookCalendarsPage.connection_to_exchange_server[title_key])

    def test_server_address(self, handle, title_key):
        server_address = handle.by(name=OutlookCalendarsPage.server_address[title_key]).find().window_text()
        check.equal(server_address, OutlookCalendarsPage.server_address[title_key])

    def test_username(self, handle, title_key):
        username = handle.by(name=OutlookCalendarsPage.username[title_key]).find().window_text()
        check.equal(username, OutlookCalendarsPage.username[title_key])

    def test_password(self, handle, title_key):
        password = handle.by(name=OutlookCalendarsPage.password[title_key]).find().window_text()
        check.equal(password, OutlookCalendarsPage.password[title_key])

    def test_maximum_time_of_script_execution(self, handle, title_key):
        maximum_time_of_script_execution = (
            handle.by(name=OutlookCalendarsPage.maximum_time_of_script_execution[title_key]).find().window_text()
        )
        check.equal(maximum_time_of_script_execution, OutlookCalendarsPage.maximum_time_of_script_execution[title_key])

    def test_read_calendars_every(self, handle, title_key):
        read_calendars_every = (
            handle.by(name=OutlookCalendarsPage.read_calendars_every[title_key]).find().window_text()
        )
        check.equal(read_calendars_every, OutlookCalendarsPage.read_calendars_every[title_key])

    def test_externalAPI_address(self, handle, title_key):
        externalAPI_address = handle.by(name=OutlookCalendarsPage.externalAPI_address[title_key]).find().window_text()
        check.equal(externalAPI_address, OutlookCalendarsPage.externalAPI_address[title_key])

    def test_disabled(self, handle, title_key):
        disabled = handle.by(name=OutlookCalendarsPage.disabled[title_key]).find().window_text()
        check.equal(disabled, OutlookCalendarsPage.disabled[title_key])

    def test_log_level(self, handle, title_key):
        log_level = handle.by(name=OutlookCalendarsPage.log_level[title_key]).find().window_text()
        check.equal(log_level, OutlookCalendarsPage.log_level[title_key])

    def test_start_service_of_reading_outlook_calendars(self, handle, title_key):
        start_service_of_reading_outlook_calendars = (
            handle.by(name=OutlookCalendarsPage.start_service_of_reading_outlook_calendars[title_key])
            .find()
            .window_text()
        )
        check.equal(
            start_service_of_reading_outlook_calendars,
            OutlookCalendarsPage.start_service_of_reading_outlook_calendars[title_key],
        )
