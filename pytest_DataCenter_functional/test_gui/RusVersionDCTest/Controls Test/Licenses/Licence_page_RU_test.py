# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import LicensePage


@pytest.fixture(scope="class")
def handle_main(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y2{VK_MENU up}%")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def handle_licence_key(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y2Y1{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_auto_license(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y2Y3{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def handle_statistic_license(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y2Y2{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("RUS Controls Test")
@allure.feature("Licenses")
@pytest.mark.testGUI_TestControlsRU
@pytest.mark.testGUI_RusVersionDCTest_ControlsTest_Licenses
class TestLicensePage:
    @allure.story("тест главного окна работы с лицензиями")
    class TestLicenseMainPage:
        def test_refresh_button(self, handle_main):
            refresh_button = (
                handle_main.by(name=LicensePage.MainWindow.refresh_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(refresh_button, "Обновить")

        def test_cancel_button(self, handle_main):
            cancel_button = (
                handle_main.by(name=LicensePage.MainWindow.cancel_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Отменить")

        def test_apply_button(self, handle_main):
            apply_button = (
                handle_main.by(name=LicensePage.MainWindow.apply_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(apply_button, "Применить")

        def test_registered_to(self, handle_main):
            registered_to = (
                handle_main.by(name=LicensePage.MainWindow.registered_to["title_ru"])
                .find()
                .window_text()
            )
            check.equal(registered_to, "Зарегистрировано на:")

        def test_technical_support(self, handle_main):
            technical_support = (
                handle_main.by(
                    name=LicensePage.MainWindow.technical_support["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(technical_support, "Техническая поддержка до:")

        def test_id_license_key(self, handle_main):
            id_license_key = (
                handle_main.by(name=LicensePage.MainWindow.id_license_key["title_ru"])
                .find()
                .window_text()
            )
            check.equal(id_license_key, "Идентификатор лицензионного ключа:")

    @allure.story("тест окна ввода лицензий")
    class TestLicenseLicenseKeyWindow:
        def test_window_header(self, handle_licence_key):
            # Заголовок окна
            window_header = (
                handle_licence_key.by(
                    name=LicensePage.UpdateLicenseWindow.window_header["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(window_header, "DataCenter ввод лицензии")

        def test_from_file_button(self, handle_licence_key):
            # Кнопки окна
            from_file_button = (
                handle_licence_key.by(
                    name=LicensePage.UpdateLicenseWindow.from_file_button["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(from_file_button, "Из файла")

        def test_cancel_butto2(self, handle_licence_key):
            cancel_button = (
                handle_licence_key.by(
                    name=LicensePage.UpdateLicenseWindow.cancel_button["title_ru"],
                    found_index=LicensePage.UpdateLicenseWindow.cancel_button[
                        "found_index"
                    ],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Отменить")

        def test_apply_button2(self, handle_licence_key):
            apply_button = (
                handle_licence_key.by(
                    name=LicensePage.UpdateLicenseWindow.apply_button["title_ru"],
                    found_index=LicensePage.UpdateLicenseWindow.apply_button[
                        "found_index"
                    ],
                )
                .find()
                .window_text()
            )
            check.equal(apply_button, "Подтвердить")

        def test_paste_from_clipboard_button(self, handle_licence_key):
            paste_from_clipboard_button = (
                handle_licence_key.by(
                    name=LicensePage.UpdateLicenseWindow.paste_from_clipboard_button[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(paste_from_clipboard_button, "Из буфера обмена")

    @allure.story("тест окна автораспределения лицензий")
    class TestLicenseAutoLicenseWindow:
        def test_window_header2(self, handle_auto_license):
            # Заголовок окна
            window_header = (
                handle_auto_license.by(
                    name=LicensePage.DistributeAutomaticallyWindow.window_header[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(window_header, "Подтверждение")

        def test_no_button(self, handle_auto_license):
            # Кнопки окна
            no_button = (
                handle_auto_license.by(
                    name=LicensePage.DistributeAutomaticallyWindow.no_button["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(no_button, "Нет")

        def test_yes_button(self, handle_auto_license):
            yes_button = (
                handle_auto_license.by(
                    name=LicensePage.DistributeAutomaticallyWindow.yes_button[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(yes_button, "Да")

    @allure.story("тест окна статистики лицензирования")
    class TestLicenseStatisticLicenseWindow:
        def test_window_header3(self, handle_statistic_license):
            # Заголовок окна
            window_header = (
                handle_statistic_license.by(
                    name=LicensePage.StatisticsWindow.window_header["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(window_header, "Статистика распределения лицензий")

        def test_export_button(self, handle_statistic_license):
            # Кнопки окна
            export_button = (
                handle_statistic_license.by(
                    name=LicensePage.StatisticsWindow.export_button["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(export_button, "Экспорт")

        def test_licenses_by_users_button(self, handle_statistic_license):
            licenses_by_users_button = (
                handle_statistic_license.by(
                    name=LicensePage.StatisticsWindow.licenses_by_users_button[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(licenses_by_users_button, "Лицензии по пользователям")

        def test_days_button(self, handle_statistic_license):
            days_button = (
                handle_statistic_license.by(
                    name=LicensePage.StatisticsWindow.days_button["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(days_button, "дням")

        def test_months_button(self, handle_statistic_license):
            months_button = (
                handle_statistic_license.by(
                    name=LicensePage.StatisticsWindow.months_button["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(months_button, "месяцам")

        def test_by_components_radiobutton(self, handle_statistic_license):
            by_components_radiobutton = (
                handle_statistic_license.by(
                    name=LicensePage.StatisticsWindow.by_components_radiobutton[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(by_components_radiobutton, "По компонентам")

        def test_by_dc_agents_radiobutton(self, handle_statistic_license):
            by_dc_agents_radiobutton = (
                handle_statistic_license.by(
                    name=LicensePage.StatisticsWindow.by_dc_agents_radiobutton[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(by_dc_agents_radiobutton, "По агентам DC")

        def test_apply_button3(self, handle_statistic_license):
            apply_button = (
                handle_statistic_license.by(
                    name=LicensePage.StatisticsWindow.apply_button["title_ru"],
                    found_index=LicensePage.StatisticsWindow.apply_button[
                        "found_index"
                    ],
                )
                .find()
                .window_text()
            )
            check.equal(apply_button, "Применить")

        def test_details_by_pane(self, handle_statistic_license):
            #  Панели окна
            details_by_pane = (
                handle_statistic_license.by(
                    name=LicensePage.StatisticsWindow.details_by_pane["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(details_by_pane, "Детализация по: ")

        def test_first_calendar_value(self, handle_statistic_license):
            first_calendar_value = (
                handle_statistic_license.__getattribute__(
                    LicensePage.StatisticsWindow.first_calendar_value
                )
                .find()
                .window_text()
            )
            check.is_not_none(first_calendar_value)

        def test_second_calendar_value(self, handle_statistic_license):
            second_calendar_value = (
                handle_statistic_license.__getattribute__(
                    LicensePage.StatisticsWindow.second_calendar_value
                )
                .find()
                .window_text()
            )
            check.is_not_none(second_calendar_value)

        def test_till_pane(self, handle_statistic_license):
            till_pane = (
                handle_statistic_license.by(
                    name=LicensePage.StatisticsWindow.till_pane["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(till_pane, "по")

        def test_from_pane(self, handle_statistic_license):
            from_pane = (
                handle_statistic_license.by(
                    name=LicensePage.StatisticsWindow.from_pane["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(from_pane, "c")
