# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import EmailNotificationsPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y3Y7{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("RUS Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControlsRU
@pytest.mark.testGUI_RusVersionDCTest_ControlsTest_Settings
@allure.story("тест главного окна настройки почтовых уведомлений")
class TestEmailNotificationsPage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=EmailNotificationsPage.cancel_button["title_ru"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Отменить")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=EmailNotificationsPage.apply_button["title_ru"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Применить")

    def test_export_button(self, handle):
        export_button = (
            handle.by(name=EmailNotificationsPage.export_button["title_ru"])
            .find()
            .window_text()
        )
        check.equal(export_button, "Экспорт")

    def test_import_button(self, handle):
        import_button = (
            handle.by(name=EmailNotificationsPage.import_button["title_ru"])
            .find()
            .window_text()
        )
        check.equal(import_button, "Импорт")

    def test_test_email(self, handle):
        test_email = (
            handle.by(name=EmailNotificationsPage.test_email["title_ru"])
            .find()
            .window_text()
        )
        check.equal(test_email, "Тестовое сообщение")

    def test_check_connection(self, handle):
        check_connection = (
            handle.by(name=EmailNotificationsPage.check_connection["title_ru"])
            .find()
            .window_text()
        )
        check.equal(check_connection, "Проверить соединение")

    def test_authentication(self, handle):
        authentication = (
            handle.by(name=EmailNotificationsPage.authentication["title_ru"])
            .find()
            .window_text()
        )
        check.equal(authentication, "Авторизация на сервере")

    def test_send_notifications_email(self, handle):
        send_notifications_email = (
            handle.by(name=EmailNotificationsPage.send_notifications_email["title_ru"])
            .find()
            .window_text()
        )
        check.equal(send_notifications_email, "Отправлять отчеты по почте")

    def test_do_not_use_tls(self, handle):
        do_not_use_tls = (
            handle.by(name=EmailNotificationsPage.do_not_use_tls["title_ru"])
            .find()
            .window_text()
        )
        check.equal(do_not_use_tls, "Не использовать TLS")

    def test_select_all(self, handle):
        select_all = (
            handle.by(name=EmailNotificationsPage.select_all["title_ru"])
            .find()
            .window_text()
        )
        check.equal(select_all, "Отметить все")

    def test_access_rights_change(self, handle):
        access_rights_change = (
            handle.by(name=EmailNotificationsPage.access_rights_change["title_ru"])
            .find()
            .window_text()
        )
        check.equal(access_rights_change, "Изменение прав доступа")

    def test_indexes_and_database_operations_errors(self, handle):
        indexes_and_database_operations_errors = (
            handle.by(
                name=EmailNotificationsPage.indexes_and_database_operations_errors[
                    "title_ru"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            indexes_and_database_operations_errors, "Операции с индексами и БД (ошибки)"
        )

    def test_synchronization_with_active_directory(self, handle):
        synchronization_with_active_directory = (
            handle.by(
                name=EmailNotificationsPage.synchronization_with_active_directory[
                    "title_ru"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            synchronization_with_active_directory, "Синхронизация с Active Directory"
        )

    def test_siem_notification(self, handle):
        siem_notification = (
            handle.by(name=EmailNotificationsPage.siem_notification["title_ru"])
            .find()
            .window_text()
        )
        check.equal(siem_notification, "Уведомление SIEM")

    def test_search_server_notification(self, handle):
        search_server_notification = (
            handle.by(
                name=EmailNotificationsPage.search_server_notification["title_ru"]
            )
            .find()
            .window_text()
        )
        check.equal(search_server_notification, "Уведомление SearchServer")

    def test_smtp_integration_notification(self, handle):
        smtp_integration_notification = (
            handle.by(
                name=EmailNotificationsPage.smtp_integration_notification["title_ru"]
            )
            .find()
            .window_text()
        )
        check.equal(smtp_integration_notification, "Уведомление SMTP integration")

    def test_mail_integration_notification(self, handle):
        mail_integration_notification = (
            handle.by(
                name=EmailNotificationsPage.mail_integration_notification["title_ru"]
            )
            .find()
            .window_text()
        )
        check.equal(mail_integration_notification, "Уведомление Mail integration")

    def test_licenseserver_notification(self, handle):
        licenseserver_notification = (
            handle.by(
                name=EmailNotificationsPage.licenseserver_notification["title_ru"]
            )
            .find()
            .window_text()
        )
        check.equal(licenseserver_notification, "Уведомление LicenseServer")

    def test_networkcontroller_notification(self, handle):
        networkcontroller_notification = (
            handle.by(
                name=EmailNotificationsPage.networkcontroller_notification["title_ru"]
            )
            .find()
            .window_text()
        )
        check.equal(networkcontroller_notification, "Уведомление NetworkController")

    def test_endpointcontroller_notification(self, handle):
        endpointcontroller_notification = (
            handle.by(
                name=EmailNotificationsPage.endpointcontroller_notification["title_ru"]
            )
            .find()
            .window_text()
        )
        check.equal(endpointcontroller_notification, "Уведомление EndpointController")

    def test_recommendation_create_new_index_and_db(self, handle):
        recommendation_create_new_index_and_db = (
            handle.by(
                name=EmailNotificationsPage.recommendation_create_new_index_and_db[
                    "title_ru"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            recommendation_create_new_index_and_db, "Рекомендация создания индекса и БД"
        )

    def test_create_dump_file(self, handle):
        create_dump_file = (
            handle.by(name=EmailNotificationsPage.create_dump_file["title_ru"])
            .find()
            .window_text()
        )
        check.equal(create_dump_file, "Создание файла журнала диагностики")

    def test_active_indexes_updated(self, handle):
        active_indexes_updated = (
            handle.by(name=EmailNotificationsPage.active_indexes_updated["title_ru"])
            .find()
            .window_text()
        )
        check.equal(active_indexes_updated, "Обновление данных в текущих индексах и БД")

    def test_warnings(self, handle):
        warnings = (
            handle.by(name=EmailNotificationsPage.warnings["title_ru"])
            .find()
            .window_text()
        )
        check.equal(warnings, "Предупреждения")

    def test_indexes_and_database_operations(self, handle):
        indexes_and_database_operations = (
            handle.by(
                name=EmailNotificationsPage.indexes_and_database_operations["title_ru"]
            )
            .find()
            .window_text()
        )
        check.equal(indexes_and_database_operations, "Операции с индексами и БД")

    def test_service_startup_parameters_changed(self, handle):
        service_startup_parameters_changed = (
            handle.by(
                name=EmailNotificationsPage.service_startup_parameters_changed[
                    "title_ru"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            service_startup_parameters_changed, "Изменения параметров запуска служб"
        )

    def test_components_start_stop(self, handle):
        components_start_stop = (
            handle.by(name=EmailNotificationsPage.components_start_stop["title_ru"])
            .find()
            .window_text()
        )
        check.equal(components_start_stop, "Остановка \ Запуск продуктов")

    def test_connection_agent_lost_restored(self, handle):
        connection_agent_lost_restored = (
            handle.by(
                name=EmailNotificationsPage.connection_agent_lost_restored["title_ru"]
            )
            .find()
            .window_text()
        )
        check.equal(
            connection_agent_lost_restored, "Потеряна \ Восстановлена связь с агентом"
        )

    def test_dataCenter_server_starts_stops(self, handle):
        dataCenter_server_starts_stops = (
            handle.by(
                name=EmailNotificationsPage.dataCenter_server_starts_stops["title_ru"]
            )
            .find()
            .window_text()
        )
        check.equal(
            dataCenter_server_starts_stops, "Остановка \ Запуск DataCenter сервера"
        )
