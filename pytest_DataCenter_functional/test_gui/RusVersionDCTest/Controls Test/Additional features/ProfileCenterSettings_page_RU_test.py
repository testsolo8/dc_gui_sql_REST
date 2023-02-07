# Standart libraries
import time

# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import ProfileCenterSettingsPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def sql_server_connection_setting_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=ProfileCenterSettingsPage.setup_connection_to_db["title_ru"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_reading_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_reading_button
    ).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_reading_second_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_reading_button
    ).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button["title_ru"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_reading_third_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_reading_button
    ).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button["title_ru"]).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button2["title_ru"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_profiling_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_profiling_button
    ).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_profiling_second_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_profiling_button
    ).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button3["title_ru"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_profiling_third_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_profiling_button
    ).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button3["title_ru"]).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button4["title_ru"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("RUS Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsRU
@pytest.mark.testGUI_RusVersionDCTest_ControlsTest_Additionalfeatures
class TestProfileCenterSettingsPage:
    @allure.story("тест главного окна ProfileCenter")
    class TestProfileCenterSettingsMainPage:
        def test_logging_of_server(self, handle):
            logging_of_server = (
                handle.by(name=ProfileCenterSettingsPage.logging_of_server["title_ru"])
                .find()
                .window_text()
            )
            check.equal(logging_of_server, "Логирование сервера")

        def test_connection_to_database(self, handle):
            connection_to_database = (
                handle.by(
                    name=ProfileCenterSettingsPage.connection_to_database["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(connection_to_database, "Подключение к БД")

        def test_control_of_services(self, handle):
            control_of_services = (
                handle.by(
                    name=ProfileCenterSettingsPage.control_of_services["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(control_of_services, "Управление службами")

        def test_schedules(self, handle):
            schedules = (
                handle.by(name=ProfileCenterSettingsPage.schedules["title_ru"])
                .find()
                .window_text()
            )
            check.equal(schedules, "Расписания")

        def test_schedule_of_profiling(self, handle):
            schedule_of_profiling = (
                handle.by(
                    name=ProfileCenterSettingsPage.schedule_of_profiling["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(schedule_of_profiling, "Расписание профилирования")

        def test_schedule_of_reading(self, handle):
            schedule_of_reading = (
                handle.by(
                    name=ProfileCenterSettingsPage.schedule_of_reading["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(schedule_of_reading, "Расписание вычитки")

        def test_setup_connection_to_db(self, handle):
            setup_connection_to_db = (
                handle.by(
                    name=ProfileCenterSettingsPage.setup_connection_to_db["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(setup_connection_to_db, "Настроить подключение к БД")

        def test_clear_database(self, handle):
            clear_database = (
                handle.by(name=ProfileCenterSettingsPage.clear_database["title_ru"])
                .find()
                .window_text()
            )
            check.equal(clear_database, "Очистить БД")

        def test_start_profiling(self, handle):
            start_profiling = (
                handle.by(name=ProfileCenterSettingsPage.start_profiling["title_ru"])
                .find()
                .window_text()
            )
            check.equal(start_profiling, "Запустить профилирование")

        def test_read_texts(self, handle):
            read_texts = (
                handle.by(name=ProfileCenterSettingsPage.read_texts["title_ru"])
                .find()
                .window_text()
            )
            check.equal(read_texts, "Вычитать тексты")

        def test_stop_server(self, handle):
            stop_server = (
                handle.by(name=ProfileCenterSettingsPage.stop_server["title_ru"])
                .find()
                .window_text()
            )
            check.equal(stop_server, "Остановить сервер")

        def test_data_for_profile_generation(self, handle):
            data_for_profile_generation = (
                handle.by(
                    name=ProfileCenterSettingsPage.data_for_profile_generation[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(data_for_profile_generation, "Данные для расчета профиля")

        def test_add(self, handle):
            add = (
                handle.by(name=ProfileCenterSettingsPage.add["title_ru"])
                .find()
                .window_text()
            )
            check.equal(add, "Добавить")

        def test_delete(self, handle):
            delete = (
                handle.by(name=ProfileCenterSettingsPage.delete["title_ru"])
                .find()
                .window_text()
            )
            check.equal(delete, "Удалить")

        def test_mail_outgoing_email_correspondence(self, handle):
            mail_outgoing_email_correspondence = (
                handle.by(
                    name=ProfileCenterSettingsPage.mail_outgoing_email_correspondence[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                mail_outgoing_email_correspondence,
                "mail (исходящая почтовая переписка)",
            )

        def test_im_outgoing_messages_in_im_clients_and_on_social_networks(
            self, handle
        ):
            im_outgoing_messages_in_im_clients_and_on_social_networks = (
                handle.by(
                    name=ProfileCenterSettingsPage.im_outgoing_messages_in_im_clients_and_on_social_networks[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                im_outgoing_messages_in_im_clients_and_on_social_networks,
                "im (исходящие сообщения в IM-клиентах и в социальных сетях)",
            )

        def test_skype_outgoing_messages_on_skype_lync_viber_telegram_and_whatsapp(
            self, handle
        ):
            skype_outgoing_messages_on_skype_lync_viber_telegram_and_whatsapp = (
                handle.by(
                    name=ProfileCenterSettingsPage.skype_outgoing_messages_on_skype_lync_viber_telegram_and_whatsapp[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                skype_outgoing_messages_on_skype_lync_viber_telegram_and_whatsapp,
                "skype (исходящие сообщения Skype, Lync, Viber, Telegram, WhatsApp)",
            )

        def test_failure_to_read_texts_from_index(self, handle):
            failure_to_read_texts_from_index = (
                handle.by(
                    name=ProfileCenterSettingsPage.failure_to_read_texts_from_index[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                failure_to_read_texts_from_index, "Неудачная вычитка текстов из индекса"
            )

        def test_cancel_button(self, handle):
            cancel_button = (
                handle.by(name=ProfileCenterSettingsPage.cancel_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Отменить")

        def test_apply_button(self, handle):
            apply_button = (
                handle.by(name=ProfileCenterSettingsPage.apply_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(apply_button, "Применить")

        def test_automatically_repeat_reading_in_case_of_failure(self, handle):
            automatically_repeat_reading_in_case_of_failure = (
                handle.by(
                    name=ProfileCenterSettingsPage.automatically_repeat_reading_in_case_of_failure[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                automatically_repeat_reading_in_case_of_failure,
                "Автоматически повторять вычитку в случае неудачи",
            )

    @allure.story("тест окна настройки подключения к БД ProfileCenter")
    class TestSQLServerConnectionSettingWindow:
        def test_sql_server_connection_settings(
            self, sql_server_connection_setting_window
        ):
            sql_server_connection_settings = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.sql_server_connection_settings[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_connection_settings, "Параметры подключения к SQL Server"
            )

        def test_create_button(self, sql_server_connection_setting_window):
            create_button = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.create_button["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(create_button, "Создать")

        def test_database_name(self, sql_server_connection_setting_window):
            database_name = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.database_name["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(database_name, "Имя базы данных:")

        def test_password(self, sql_server_connection_setting_window):
            password = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.password["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(password, "Пароль:")

        def test_username(self, sql_server_connection_setting_window):
            username = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.username["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(username, "Имя пользователя:")

        def test_sql_server_authentication_mode(
            self, sql_server_connection_setting_window
        ):
            sql_server_authentication_mode = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.sql_server_authentication_mode[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_authentication_mode,
                "Использовать внутреннюю аутентификацию SQL Server",
            )

        def test_windows_authentication_mode(
            self, sql_server_connection_setting_window
        ):
            windows_authentication_mode = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.windows_authentication_mode[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                windows_authentication_mode, "Использовать аутентификацию Windows"
            )

        def test_read_from_dc(self, sql_server_connection_setting_window):
            read_from_dc = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.read_from_dc["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(read_from_dc, "Считать из DC")

        def test_server_name(self, sql_server_connection_setting_window):
            server_name = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.server_name["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(server_name, "Имя сервера:")

        def test_server_type(self, sql_server_connection_setting_window):
            server_type = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.server_type["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(server_type, "Тип сервера:")

        def test_cancel_button2(self, sql_server_connection_setting_window):
            cancel_button2 = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.cancel_button2["title_ru"],
                    found_index=ProfileCenterSettingsPage.cancel_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button2, "Отменить")

        def test_ok_button(self, sql_server_connection_setting_window):
            ok_button = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.ok_button["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(ok_button, "OK")

        def test_check_connection(self, sql_server_connection_setting_window):
            check_connection = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.check_connection["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection, "Проверка подключения")

    @allure.story("тест окна настройки расписания вычитки индексов ProfileCenter")
    class TestScheduleOfReadingWindow:
        def test_modifying_schedule(self, schedule_of_reading_window):
            modifying_schedule = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.modifying_schedule["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(modifying_schedule, "Изменение расписания")

        def test_select_name(self, schedule_of_reading_window):
            select_name = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.select_name["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(select_name, "SelectName")

        def test_schedule_is_enabled(self, schedule_of_reading_window):
            schedule_is_enabled = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.schedule_is_enabled["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(schedule_is_enabled, "Расписание включено")

        def test_custom(self, schedule_of_reading_window):
            custom = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.custom["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(custom, "По настройке")

        def test_once(self, schedule_of_reading_window):
            once = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.once["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(once, "Единовременно")

        def test_monthly(self, schedule_of_reading_window):
            monthly = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.monthly["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(monthly, "Ежемесячно")

        def test_weekly(self, schedule_of_reading_window):
            weekly = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.weekly["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(weekly, "Еженедельно")

        def test_daily(self, schedule_of_reading_window):
            daily = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.daily["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(daily, "Ежедневно")

        def test_cancel_button3(self, schedule_of_reading_window):
            cancel_button3 = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.cancel_button3["title_ru"],
                    found_index=ProfileCenterSettingsPage.cancel_button3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button3, "Отмена")

        def test_next_button(self, schedule_of_reading_window):
            next_button = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.next_button["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(next_button, "Далее >")

        def test_back_button(self, schedule_of_reading_window):
            back_button = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.back_button["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(back_button, "< Назад")

    @allure.story(
        "тест второго окна настройки расписания вычитки индексов ProfileCenter"
    )
    class TestScheduleOfReadingSecondWindow:
        def test_modifying_schedule2(self, schedule_of_reading_second_window):
            modifying_schedule2 = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.modifying_schedule2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(modifying_schedule2, "Изменение расписания")

        def test_repeat_every(self, schedule_of_reading_second_window):
            repeat_every = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.repeat_every["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(repeat_every, "повторять каждые")

        def test_workdays_only(self, schedule_of_reading_second_window):
            workdays_only = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.workdays_only["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(workdays_only, "Считать только рабочие дни(Пн-Пт)")

        def test_every(self, schedule_of_reading_second_window):
            every = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.every["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(every, "Кажд.")

        def test_on_workdays(self, schedule_of_reading_second_window):
            on_workdays = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.on_workdays["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(on_workdays, "По рабочим дням")

        def test_daily3(self, schedule_of_reading_second_window):
            daily2 = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.daily2["title_ru"],
                    control_type=ProfileCenterSettingsPage.daily2["control_type"],
                )
                .find()
                .window_text()
            )
            check.equal(daily2, "Ежедневно")

        def test_cancel_button4(self, schedule_of_reading_second_window):
            cancel_button4 = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.cancel_button4["title_ru"],
                    found_index=ProfileCenterSettingsPage.cancel_button4["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button4, "Отмена")

        def test_next_button2(self, schedule_of_reading_second_window):
            next_button2 = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.next_button2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(next_button2, "Далее >")

        def test_back_button2(self, schedule_of_reading_second_window):
            back_button2 = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.back_button2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(back_button2, "< Назад")

    @allure.story(
        "тест третьего окна настройки расписания вычитки индексов ProfileCenter"
    )
    class TestScheduleOfReadingThirdWindow:
        def test_modifying_schedule3(self, schedule_of_reading_third_window):
            modifying_schedule3 = (
                schedule_of_reading_third_window.by(
                    name=ProfileCenterSettingsPage.modifying_schedule3["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(modifying_schedule3, "Изменение расписания")

        def test_cancel_button5(self, schedule_of_reading_third_window):
            cancel_button5 = (
                schedule_of_reading_third_window.by(
                    name=ProfileCenterSettingsPage.cancel_button5["title_ru"],
                    found_index=ProfileCenterSettingsPage.cancel_button5["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button5, "Отмена")

        def test_finish_button(self, schedule_of_reading_third_window):
            finish_button = (
                schedule_of_reading_third_window.by(
                    name=ProfileCenterSettingsPage.finish_button["title_ru"],
                    control_type=ProfileCenterSettingsPage.finish_button[
                        "control_type"
                    ],
                )
                .find()
                .window_text()
            )
            check.equal(finish_button, "Завершить")

        def test_back_button3(self, schedule_of_reading_third_window):
            back_button3 = (
                schedule_of_reading_third_window.by(
                    name=ProfileCenterSettingsPage.back_button3["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(back_button3, "< Назад")

    @allure.story("тест окна настройки расписания профилирования ProfileCenter")
    class TestScheduleOfProfilingWindow:
        def test_modifying_schedule(self, schedule_of_profiling_window):
            modifying_schedule = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.modifying_schedule["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(modifying_schedule, "Изменение расписания")

        def test_schedule_is_enabled2(self, schedule_of_profiling_window):
            schedule_is_enabled2 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.schedule_is_enabled2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(schedule_is_enabled2, "Расписание включено")

        def test_custom2(self, schedule_of_profiling_window):
            custom2 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.custom2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(custom2, "По настройке")

        def test_once2(self, schedule_of_profiling_window):
            once2 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.once2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(once2, "Единовременно")

        def test_monthly2(self, schedule_of_profiling_window):
            monthly2 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.monthly2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(monthly2, "Ежемесячно")

        def test_weekly2(self, schedule_of_profiling_window):
            weekly2 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.weekly2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(weekly2, "Еженедельно")

        def test_daily3(self, schedule_of_profiling_window):
            daily3 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.daily3["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(daily3, "Ежедневно")

        def test_cancel_button6(self, schedule_of_profiling_window):
            cancel_button6 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.cancel_button6["title_ru"],
                    found_index=ProfileCenterSettingsPage.cancel_button6["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button6, "Отмена")

        def test_next_button3(self, schedule_of_profiling_window):
            next_button3 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.next_button3["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(next_button3, "Далее >")

        def test_back_button4(self, schedule_of_profiling_window):
            back_button4 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.back_button4["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(back_button4, "< Назад")

    @allure.story("тест второго окна настройки расписания профилирования ProfileCenter")
    class TestScheduleOfProfilingSecondWindow:
        def test_modifying_schedule5(self, schedule_of_profiling_second_window):
            modifying_schedule5 = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.modifying_schedule5["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(modifying_schedule5, "Изменение расписания")

        def test_september(self, schedule_of_profiling_second_window):
            september = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.september["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(september, "Сентябрь")

        def test_august(self, schedule_of_profiling_second_window):
            august = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.august["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(august, "Август")

        def test_july(self, schedule_of_profiling_second_window):
            july = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.july["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(july, "Июль")

        def test_june(self, schedule_of_profiling_second_window):
            june = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.june["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(june, "Июнь")

        def test_may(self, schedule_of_profiling_second_window):
            may = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.may["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(may, "Май")

        def test_april(self, schedule_of_profiling_second_window):
            april = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.april["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(april, "Апрель")

        def test_december(self, schedule_of_profiling_second_window):
            december = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.december["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(december, "Декабрь")

        def test_november(self, schedule_of_profiling_second_window):
            november = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.november["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(november, "Ноябрь")

        def test_october(self, schedule_of_profiling_second_window):
            october = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.october["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(october, "Октябрь")

        def test_march(self, schedule_of_profiling_second_window):
            march = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.march["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(march, "Март")

        def test_february(self, schedule_of_profiling_second_window):
            february = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.february["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(february, "Февраль")

        def test_january(self, schedule_of_profiling_second_window):
            january = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.january["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(january, "Январь")

        def test_or_radiobutton(self, schedule_of_profiling_second_window):
            or_radiobutton = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.or_radiobutton["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(or_radiobutton, "или")

        def test_date_radiobutton(self, schedule_of_profiling_second_window):
            date_radiobutton = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.date_radiobutton["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(date_radiobutton, "Число")

        def test_cancel_button7(self, schedule_of_profiling_second_window):
            cancel_button7 = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.cancel_button7["title_ru"],
                    found_index=ProfileCenterSettingsPage.cancel_button7["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button7, "Отмена")

        def test_next_button4(self, schedule_of_profiling_second_window):
            next_button4 = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.next_button4["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(next_button4, "Далее >")

        def test_back_button5(self, schedule_of_profiling_second_window):
            back_button5 = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.back_button5["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(back_button5, "< Назад")

    @allure.story(
        "тест третьего окна настройки расписания профилирования ProfileCenter"
    )
    class TestScheduleOfProfilingThirdWindow:
        def test_modifying_schedule6(self, schedule_of_profiling_third_window):
            modifying_schedule6 = (
                schedule_of_profiling_third_window.by(
                    name=ProfileCenterSettingsPage.modifying_schedule6["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(modifying_schedule6, "Изменение расписания")

        def test_cancel_button8(self, schedule_of_profiling_third_window):
            cancel_button8 = (
                schedule_of_profiling_third_window.by(
                    name=ProfileCenterSettingsPage.cancel_button8["title_ru"],
                    found_index=ProfileCenterSettingsPage.cancel_button8["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button8, "Отмена")

        def test_finish_button2(self, schedule_of_profiling_third_window):
            finish_button2 = (
                schedule_of_profiling_third_window.by(
                    name=ProfileCenterSettingsPage.finish_button2["title_ru"],
                    control_type=ProfileCenterSettingsPage.finish_button2[
                        "control_type"
                    ],
                )
                .find()
                .window_text()
            )
            check.equal(finish_button2, "Завершить")

        def test_back_button6(self, schedule_of_profiling_third_window):
            back_button6 = (
                schedule_of_profiling_third_window.by(
                    name=ProfileCenterSettingsPage.back_button6["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(back_button6, "< Назад")
