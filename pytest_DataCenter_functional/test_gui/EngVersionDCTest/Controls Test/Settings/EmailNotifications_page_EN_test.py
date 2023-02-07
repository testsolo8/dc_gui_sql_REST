# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import EmailNotificationsPage


@pytest.fixture(scope="class")
def handle(start_test_page_en):
    send_keys("{VK_MENU down}Y3Y7{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("ENG Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControlsEN
@pytest.mark.testGUI_EngVersionDCTest_ControlsTest_Settings
@allure.story("тест главного окна настройки почтовых уведомлений")
class TestEmailNotificationsPage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=EmailNotificationsPage.cancel_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Cancel")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=EmailNotificationsPage.apply_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Apply")

    def test_export_button(self, handle):
        export_button = (
            handle.by(name=EmailNotificationsPage.export_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(export_button, "Export")

    def test_import_button(self, handle):
        import_button = (
            handle.by(name=EmailNotificationsPage.import_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(import_button, "Import")

    def test_test_email(self, handle):
        test_email = (
            handle.by(name=EmailNotificationsPage.test_email["title_en"])
            .find()
            .window_text()
        )
        check.equal(test_email, "Test e-mail")

    def test_check_connection(self, handle):
        check_connection = (
            handle.by(name=EmailNotificationsPage.check_connection["title_en"])
            .find()
            .window_text()
        )
        check.equal(check_connection, "Check connection")

    def test_authentication(self, handle):
        authentication = (
            handle.by(name=EmailNotificationsPage.authentication["title_en"])
            .find()
            .window_text()
        )
        check.equal(authentication, "Authentication")

    def test_send_notifications_email(self, handle):
        send_notifications_email = (
            handle.by(name=EmailNotificationsPage.send_notifications_email["title_en"])
            .find()
            .window_text()
        )
        check.equal(send_notifications_email, "Send notifications by e-mail")

    def test_do_not_use_tls(self, handle):
        do_not_use_tls = (
            handle.by(name=EmailNotificationsPage.do_not_use_tls["title_en"])
            .find()
            .window_text()
        )
        check.equal(do_not_use_tls, "Do not use TLS")

    def test_select_all(self, handle):
        select_all = (
            handle.by(name=EmailNotificationsPage.select_all["title_en"])
            .find()
            .window_text()
        )
        check.equal(select_all, "Select all")

    def test_access_rights_change(self, handle):
        access_rights_change = (
            handle.by(name=EmailNotificationsPage.access_rights_change["title_en"])
            .find()
            .window_text()
        )
        check.equal(access_rights_change, "Access rights change")

    def test_indexes_and_database_operations_errors(self, handle):
        indexes_and_database_operations_errors = (
            handle.by(
                name=EmailNotificationsPage.indexes_and_database_operations_errors[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            indexes_and_database_operations_errors,
            "Indexes and database operations (errors)",
        )

    def test_synchronization_with_active_directory(self, handle):
        synchronization_with_active_directory = (
            handle.by(
                name=EmailNotificationsPage.synchronization_with_active_directory[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            synchronization_with_active_directory,
            "Synchronization with Active Directory",
        )

    def test_siem_notification(self, handle):
        siem_notification = (
            handle.by(name=EmailNotificationsPage.siem_notification["title_en"])
            .find()
            .window_text()
        )
        check.equal(siem_notification, "SIEM notification")

    def test_search_server_notification(self, handle):
        search_server_notification = (
            handle.by(
                name=EmailNotificationsPage.search_server_notification["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(search_server_notification, "Search Server notification")

    def test_smtp_integration_notification(self, handle):
        smtp_integration_notification = (
            handle.by(
                name=EmailNotificationsPage.smtp_integration_notification["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(smtp_integration_notification, "SMTP integration notification")

    def test_mail_integration_notification(self, handle):
        mail_integration_notification = (
            handle.by(
                name=EmailNotificationsPage.mail_integration_notification["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(mail_integration_notification, "Mail integration notification")

    def test_licenseserver_notification(self, handle):
        licenseserver_notification = (
            handle.by(
                name=EmailNotificationsPage.licenseserver_notification["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(licenseserver_notification, "LicenseServer notification")

    def test_networkcontroller_notification(self, handle):
        networkcontroller_notification = (
            handle.by(
                name=EmailNotificationsPage.networkcontroller_notification["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(networkcontroller_notification, "NetworkController notification")

    def test_endpointcontroller_notification(self, handle):
        endpointcontroller_notification = (
            handle.by(
                name=EmailNotificationsPage.endpointcontroller_notification["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(endpointcontroller_notification, "EndpointController notification")

    def test_recommendation_create_new_index_and_db(self, handle):
        recommendation_create_new_index_and_db = (
            handle.by(
                name=EmailNotificationsPage.recommendation_create_new_index_and_db[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            recommendation_create_new_index_and_db,
            "Recommendation to create new index and DB",
        )

    def test_create_dump_file(self, handle):
        create_dump_file = (
            handle.by(name=EmailNotificationsPage.create_dump_file["title_en"])
            .find()
            .window_text()
        )
        check.equal(create_dump_file, "Create dump file")

    def test_active_indexes_updated(self, handle):
        active_indexes_updated = (
            handle.by(name=EmailNotificationsPage.active_indexes_updated["title_en"])
            .find()
            .window_text()
        )
        check.equal(active_indexes_updated, "Active indexes are updated ")

    def test_warnings(self, handle):
        warnings = (
            handle.by(name=EmailNotificationsPage.warnings["title_en"])
            .find()
            .window_text()
        )
        check.equal(warnings, "Warnings")

    def test_indexes_and_database_operations(self, handle):
        indexes_and_database_operations = (
            handle.by(
                name=EmailNotificationsPage.indexes_and_database_operations["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(
            indexes_and_database_operations, "Indexes and database operations  "
        )

    def test_service_startup_parameters_changed(self, handle):
        service_startup_parameters_changed = (
            handle.by(
                name=EmailNotificationsPage.service_startup_parameters_changed[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            service_startup_parameters_changed, "Service startup parameters are changed"
        )

    def test_components_start_stop(self, handle):
        components_start_stop = (
            handle.by(name=EmailNotificationsPage.components_start_stop["title_en"])
            .find()
            .window_text()
        )
        check.equal(components_start_stop, "Components start/stop")

    def test_connection_agent_lost_restored(self, handle):
        connection_agent_lost_restored = (
            handle.by(
                name=EmailNotificationsPage.connection_agent_lost_restored["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(
            connection_agent_lost_restored, "Connection to agent is lost/restored"
        )

    def test_dataCenter_server_starts_stops(self, handle):
        dataCenter_server_starts_stops = (
            handle.by(
                name=EmailNotificationsPage.dataCenter_server_starts_stops["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(dataCenter_server_starts_stops, "DataCenter Server starts/stops")
