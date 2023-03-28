# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import EmailNotificationsPage


@pytest.fixture(scope="class")
def handle(start_test_page):
    send_keys("{VK_MENU down}Y3Y7{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Settings
@allure.story("тест главного окна настройки почтовых уведомлений")
class TestEmailNotificationsPage:
    def test_cancel_button(self, handle, title_key):
        cancel_button = handle.by(name=EmailNotificationsPage.cancel_button[title_key]).find().window_text()
        check.equal(cancel_button, EmailNotificationsPage.cancel_button[title_key])

    def test_apply_button(self, handle, title_key):
        apply_button = handle.by(name=EmailNotificationsPage.apply_button[title_key]).find().window_text()
        check.equal(apply_button, EmailNotificationsPage.apply_button[title_key])

    def test_export_button(self, handle, title_key):
        export_button = handle.by(name=EmailNotificationsPage.export_button[title_key]).find().window_text()
        check.equal(export_button, EmailNotificationsPage.export_button[title_key])

    def test_import_button(self, handle, title_key):
        import_button = handle.by(name=EmailNotificationsPage.import_button[title_key]).find().window_text()
        check.equal(import_button, EmailNotificationsPage.import_button[title_key])

    def test_test_email(self, handle, title_key):
        test_email = handle.by(name=EmailNotificationsPage.test_email[title_key]).find().window_text()
        check.equal(test_email, EmailNotificationsPage.test_email[title_key])

    def test_check_connection(self, handle, title_key):
        check_connection = handle.by(name=EmailNotificationsPage.check_connection[title_key]).find().window_text()
        check.equal(check_connection, EmailNotificationsPage.check_connection[title_key])

    def test_authentication(self, handle, title_key):
        authentication = handle.by(name=EmailNotificationsPage.authentication[title_key]).find().window_text()
        check.equal(authentication, EmailNotificationsPage.authentication[title_key])

    def test_send_notifications_email(self, handle, title_key):
        send_notifications_email = (
            handle.by(name=EmailNotificationsPage.send_notifications_email[title_key]).find().window_text()
        )
        check.equal(send_notifications_email, EmailNotificationsPage.send_notifications_email[title_key])

    def test_do_not_use_tls(self, handle, title_key):
        do_not_use_tls = handle.by(name=EmailNotificationsPage.do_not_use_tls[title_key]).find().window_text()
        check.equal(do_not_use_tls, EmailNotificationsPage.do_not_use_tls[title_key])

    def test_select_all(self, handle, title_key):
        select_all = handle.by(name=EmailNotificationsPage.select_all[title_key]).find().window_text()
        check.equal(select_all, EmailNotificationsPage.select_all[title_key])

    def test_access_rights_change(self, handle, title_key):
        access_rights_change = (
            handle.by(name=EmailNotificationsPage.access_rights_change[title_key]).find().window_text()
        )
        check.equal(access_rights_change, EmailNotificationsPage.access_rights_change[title_key])

    def test_indexes_and_database_operations_errors(self, handle, title_key):
        indexes_and_database_operations_errors = (
            handle.by(name=EmailNotificationsPage.indexes_and_database_operations_errors[title_key])
            .find()
            .window_text()
        )
        check.equal(
            indexes_and_database_operations_errors,
            EmailNotificationsPage.indexes_and_database_operations_errors[title_key],
        )

    def test_synchronization_with_active_directory(self, handle, title_key):
        synchronization_with_active_directory = (
            handle.by(name=EmailNotificationsPage.synchronization_with_active_directory[title_key])
            .find()
            .window_text()
        )
        check.equal(
            synchronization_with_active_directory,
            EmailNotificationsPage.synchronization_with_active_directory[title_key],
        )

    def test_siem_notification(self, handle, title_key):
        siem_notification = handle.by(name=EmailNotificationsPage.siem_notification[title_key]).find().window_text()
        check.equal(siem_notification, EmailNotificationsPage.siem_notification[title_key])

    def test_search_server_notification(self, handle, title_key):
        search_server_notification = (
            handle.by(name=EmailNotificationsPage.search_server_notification[title_key]).find().window_text()
        )
        check.equal(search_server_notification, EmailNotificationsPage.search_server_notification[title_key])

    def test_smtp_integration_notification(self, handle, title_key):
        smtp_integration_notification = (
            handle.by(name=EmailNotificationsPage.smtp_integration_notification[title_key]).find().window_text()
        )
        check.equal(smtp_integration_notification, EmailNotificationsPage.smtp_integration_notification[title_key])

    def test_mail_integration_notification(self, handle, title_key):
        mail_integration_notification = (
            handle.by(name=EmailNotificationsPage.mail_integration_notification[title_key]).find().window_text()
        )
        check.equal(mail_integration_notification, EmailNotificationsPage.mail_integration_notification[title_key])

    def test_licenseserver_notification(self, handle, title_key):
        licenseserver_notification = (
            handle.by(name=EmailNotificationsPage.licenseserver_notification[title_key]).find().window_text()
        )
        check.equal(licenseserver_notification, EmailNotificationsPage.licenseserver_notification[title_key])

    def test_networkcontroller_notification(self, handle, title_key):
        networkcontroller_notification = (
            handle.by(name=EmailNotificationsPage.networkcontroller_notification[title_key]).find().window_text()
        )
        check.equal(networkcontroller_notification, EmailNotificationsPage.networkcontroller_notification[title_key])

    def test_endpointcontroller_notification(self, handle, title_key):
        endpointcontroller_notification = (
            handle.by(name=EmailNotificationsPage.endpointcontroller_notification[title_key]).find().window_text()
        )
        check.equal(endpointcontroller_notification, EmailNotificationsPage.endpointcontroller_notification[title_key])

    def test_recommendation_create_new_index_and_db(self, handle, title_key):
        recommendation_create_new_index_and_db = (
            handle.by(name=EmailNotificationsPage.recommendation_create_new_index_and_db[title_key])
            .find()
            .window_text()
        )
        check.equal(
            recommendation_create_new_index_and_db,
            EmailNotificationsPage.recommendation_create_new_index_and_db[title_key],
        )

    def test_create_dump_file(self, handle, title_key):
        create_dump_file = handle.by(name=EmailNotificationsPage.create_dump_file[title_key]).find().window_text()
        check.equal(create_dump_file, EmailNotificationsPage.create_dump_file[title_key])

    def test_active_indexes_updated(self, handle, title_key):
        active_indexes_updated = (
            handle.by(name=EmailNotificationsPage.active_indexes_updated[title_key]).find().window_text()
        )
        check.equal(active_indexes_updated, EmailNotificationsPage.active_indexes_updated[title_key])

    def test_warnings(self, handle, title_key):
        warnings = handle.by(name=EmailNotificationsPage.warnings[title_key]).find().window_text()
        check.equal(warnings, EmailNotificationsPage.warnings[title_key])

    def test_indexes_and_database_operations(self, handle, title_key):
        indexes_and_database_operations = (
            handle.by(name=EmailNotificationsPage.indexes_and_database_operations[title_key]).find().window_text()
        )
        check.equal(indexes_and_database_operations, EmailNotificationsPage.indexes_and_database_operations[title_key])

    def test_service_startup_parameters_changed(self, handle, title_key):
        service_startup_parameters_changed = (
            handle.by(name=EmailNotificationsPage.service_startup_parameters_changed[title_key]).find().window_text()
        )
        check.equal(service_startup_parameters_changed, EmailNotificationsPage.service_startup_parameters_changed[title_key])

    def test_components_start_stop(self, handle, title_key):
        components_start_stop = (
            handle.by(name=EmailNotificationsPage.components_start_stop[title_key]).find().window_text()
        )
        check.equal(components_start_stop, EmailNotificationsPage.components_start_stop[title_key])

    def test_connection_agent_lost_restored(self, handle, title_key):
        connection_agent_lost_restored = (
            handle.by(name=EmailNotificationsPage.connection_agent_lost_restored[title_key]).find().window_text()
        )
        check.equal(connection_agent_lost_restored, EmailNotificationsPage.connection_agent_lost_restored[title_key])

    def test_dataCenter_server_starts_stops(self, handle, title_key):
        dataCenter_server_starts_stops = (
            handle.by(name=EmailNotificationsPage.dataCenter_server_starts_stops[title_key]).find().window_text()
        )
        check.equal(dataCenter_server_starts_stops, EmailNotificationsPage.dataCenter_server_starts_stops[title_key])
