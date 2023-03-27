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
def handle(start_test_page):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def sql_server_connection_setting_window(start_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=ProfileCenterSettingsPage.setup_connection_to_db[title_key]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_reading_window(start_test_page):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(ProfileCenterSettingsPage.edit_schedule_of_reading_button).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_reading_second_window(start_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(ProfileCenterSettingsPage.edit_schedule_of_reading_button).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button[title_key]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_reading_third_window(start_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(ProfileCenterSettingsPage.edit_schedule_of_reading_button).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button[title_key]).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button2[title_key]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_profiling_window(start_test_page):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(ProfileCenterSettingsPage.edit_schedule_of_profiling_button).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_profiling_second_window(start_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(ProfileCenterSettingsPage.edit_schedule_of_profiling_button).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button3[title_key]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_profiling_third_window(start_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(ProfileCenterSettingsPage.edit_schedule_of_profiling_button).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button3[title_key]).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button4[title_key]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Additionalfeatures
class TestProfileCenterSettingsPage:
    @allure.story("тест главного окна ProfileCenter")
    class TestProfileCenterSettingsMainPage:
        def test_logging_of_server(self, handle, title_key):
            logging_of_server = (
                handle.by(name=ProfileCenterSettingsPage.logging_of_server[title_key]).find().window_text()
            )
            check.equal(logging_of_server, ProfileCenterSettingsPage.logging_of_server[title_key])

        def test_connection_to_database(self, handle, title_key):
            connection_to_database = (
                handle.by(name=ProfileCenterSettingsPage.connection_to_database[title_key]).find().window_text()
            )
            check.equal(connection_to_database, ProfileCenterSettingsPage.connection_to_database[title_key])

        def test_control_of_services(self, handle, title_key):
            control_of_services = (
                handle.by(name=ProfileCenterSettingsPage.control_of_services[title_key]).find().window_text()
            )
            check.equal(control_of_services, ProfileCenterSettingsPage.control_of_services[title_key])

        def test_schedules(self, handle, title_key):
            schedules = handle.by(name=ProfileCenterSettingsPage.schedules[title_key]).find().window_text()
            check.equal(schedules, ProfileCenterSettingsPage.schedules[title_key])

        def test_schedule_of_profiling(self, handle, title_key):
            schedule_of_profiling = (
                handle.by(name=ProfileCenterSettingsPage.schedule_of_profiling[title_key]).find().window_text()
            )
            check.equal(schedule_of_profiling, ProfileCenterSettingsPage.schedule_of_profiling[title_key])

        def test_schedule_of_reading(self, handle, title_key):
            schedule_of_reading = (
                handle.by(name=ProfileCenterSettingsPage.schedule_of_reading[title_key]).find().window_text()
            )
            check.equal(schedule_of_reading, ProfileCenterSettingsPage.schedule_of_reading[title_key])

        def test_setup_connection_to_db(self, handle, title_key):
            setup_connection_to_db = (
                handle.by(name=ProfileCenterSettingsPage.setup_connection_to_db[title_key]).find().window_text()
            )
            check.equal(setup_connection_to_db, ProfileCenterSettingsPage.setup_connection_to_db[title_key])

        def test_clear_database(self, handle, title_key):
            clear_database = handle.by(name=ProfileCenterSettingsPage.clear_database[title_key]).find().window_text()
            check.equal(clear_database, ProfileCenterSettingsPage.clear_database[title_key])

        def test_start_profiling(self, handle, title_key):
            start_profiling = handle.by(name=ProfileCenterSettingsPage.start_profiling[title_key]).find().window_text()
            check.equal(start_profiling, ProfileCenterSettingsPage.start_profiling[title_key])

        def test_read_texts(self, handle, title_key):
            read_texts = handle.by(name=ProfileCenterSettingsPage.read_texts[title_key]).find().window_text()
            check.equal(read_texts, ProfileCenterSettingsPage.read_texts[title_key])

        def test_stop_server(self, handle, title_key):
            stop_server = handle.by(name=ProfileCenterSettingsPage.stop_server[title_key]).find().window_text()
            check.equal(stop_server, ProfileCenterSettingsPage.stop_server[title_key])

        def test_data_for_profile_generation(self, handle, title_key):
            data_for_profile_generation = (
                handle.by(name=ProfileCenterSettingsPage.data_for_profile_generation[title_key]).find().window_text()
            )
            check.equal(data_for_profile_generation, ProfileCenterSettingsPage.data_for_profile_generation[title_key])

        def test_add(self, handle, title_key):
            add = handle.by(name=ProfileCenterSettingsPage.add[title_key]).find().window_text()
            check.equal(add, ProfileCenterSettingsPage.add[title_key])

        def test_delete(self, handle, title_key):
            delete = handle.by(name=ProfileCenterSettingsPage.delete[title_key]).find().window_text()
            check.equal(delete, ProfileCenterSettingsPage.delete[title_key])

        def test_mail_outgoing_email_correspondence(self, handle, title_key):
            mail_outgoing_email_correspondence = (
                handle.by(name=ProfileCenterSettingsPage.mail_outgoing_email_correspondence[title_key])
                .find()
                .window_text()
            )
            check.equal(
                mail_outgoing_email_correspondence,
                ProfileCenterSettingsPage.mail_outgoing_email_correspondence[title_key],
            )

        def test_im_outgoing_messages_in_im_clients_and_on_social_networks(self, handle, title_key):
            im_outgoing_messages_in_im_clients_and_on_social_networks = (
                handle.by(
                    name=ProfileCenterSettingsPage.im_outgoing_messages_in_im_clients_and_on_social_networks[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(
                im_outgoing_messages_in_im_clients_and_on_social_networks,
                ProfileCenterSettingsPage.im_outgoing_messages_in_im_clients_and_on_social_networks[title_key],
            )

        def test_skype_outgoing_messages_on_skype_lync_viber_telegram_and_whatsapp(self, handle, title_key):
            skype_outgoing_messages_on_skype_lync_viber_telegram_and_whatsapp = (
                handle.by(
                    name=ProfileCenterSettingsPage.skype_outgoing_messages_on_skype_lync_viber_telegram_and_whatsapp[
                        title_key
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                skype_outgoing_messages_on_skype_lync_viber_telegram_and_whatsapp,
                ProfileCenterSettingsPage.skype_outgoing_messages_on_skype_lync_viber_telegram_and_whatsapp[title_key],
            )

        def test_failure_to_read_texts_from_index(self, handle, title_key):
            failure_to_read_texts_from_index = (
                handle.by(name=ProfileCenterSettingsPage.failure_to_read_texts_from_index[title_key])
                .find()
                .window_text()
            )
            check.equal(failure_to_read_texts_from_index, ProfileCenterSettingsPage.failure_to_read_texts_from_index[title_key])

        def test_cancel_button(self, handle, title_key):
            cancel_button = handle.by(name=ProfileCenterSettingsPage.cancel_button[title_key]).find().window_text()
            check.equal(cancel_button, ProfileCenterSettingsPage.cancel_button[title_key])

        def test_apply_button(self, handle, title_key):
            apply_button = handle.by(name=ProfileCenterSettingsPage.apply_button[title_key]).find().window_text()
            check.equal(apply_button, ProfileCenterSettingsPage.apply_button[title_key])

        def test_automatically_repeat_reading_in_case_of_failure(self, handle, title_key):
            automatically_repeat_reading_in_case_of_failure = (
                handle.by(name=ProfileCenterSettingsPage.automatically_repeat_reading_in_case_of_failure[title_key])
                .find()
                .window_text()
            )
            check.equal(
                automatically_repeat_reading_in_case_of_failure,
                ProfileCenterSettingsPage.automatically_repeat_reading_in_case_of_failure[title_key],
            )

    @allure.story("тест окна настройки подключения к БД ProfileCenter")
    class TestSQLServerConnectionSettingWindow:
        def test_sql_server_connection_settings(self, sql_server_connection_setting_window, title_key):
            sql_server_connection_settings = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.sql_server_connection_settings[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(sql_server_connection_settings, ProfileCenterSettingsPage.sql_server_connection_settings[title_key])

        def test_create_button(self, sql_server_connection_setting_window, title_key):
            create_button = (
                sql_server_connection_setting_window.by(name=ProfileCenterSettingsPage.create_button[title_key])
                .find()
                .window_text()
            )
            check.equal(create_button, ProfileCenterSettingsPage.create_button[title_key])

        def test_database_name(self, sql_server_connection_setting_window, title_key):
            database_name = (
                sql_server_connection_setting_window.by(name=ProfileCenterSettingsPage.database_name[title_key])
                .find()
                .window_text()
            )
            check.equal(database_name, ProfileCenterSettingsPage.database_name[title_key])

        def test_password(self, sql_server_connection_setting_window, title_key):
            password = (
                sql_server_connection_setting_window.by(name=ProfileCenterSettingsPage.password[title_key])
                .find()
                .window_text()
            )
            check.equal(password, ProfileCenterSettingsPage.password[title_key])

        def test_username(self, sql_server_connection_setting_window, title_key):
            username = (
                sql_server_connection_setting_window.by(name=ProfileCenterSettingsPage.username[title_key])
                .find()
                .window_text()
            )
            check.equal(username, ProfileCenterSettingsPage.username[title_key])

        def test_sql_server_authentication_mode(self, sql_server_connection_setting_window, title_key):
            sql_server_authentication_mode = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.sql_server_authentication_mode[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(sql_server_authentication_mode, ProfileCenterSettingsPage.sql_server_authentication_mode[title_key])

        def test_windows_authentication_mode(self, sql_server_connection_setting_window, title_key):
            windows_authentication_mode = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.windows_authentication_mode[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(windows_authentication_mode, ProfileCenterSettingsPage.windows_authentication_mode[title_key])

        def test_read_from_dc(self, sql_server_connection_setting_window, title_key):
            read_from_dc = (
                sql_server_connection_setting_window.by(name=ProfileCenterSettingsPage.read_from_dc[title_key])
                .find()
                .window_text()
            )
            check.equal(read_from_dc, ProfileCenterSettingsPage.read_from_dc[title_key])

        def test_server_name(self, sql_server_connection_setting_window, title_key):
            server_name = (
                sql_server_connection_setting_window.by(name=ProfileCenterSettingsPage.server_name[title_key])
                .find()
                .window_text()
            )
            check.equal(server_name, ProfileCenterSettingsPage.server_name[title_key])

        def test_server_type(self, sql_server_connection_setting_window, title_key):
            server_type = (
                sql_server_connection_setting_window.by(name=ProfileCenterSettingsPage.server_type[title_key])
                .find()
                .window_text()
            )
            check.equal(server_type, ProfileCenterSettingsPage.server_type[title_key])

        def test_cancel_button2(self, sql_server_connection_setting_window, title_key):
            cancel_button2 = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.cancel_button2[title_key],
                    found_index=ProfileCenterSettingsPage.cancel_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button2, ProfileCenterSettingsPage.cancel_button2[title_key])

        def test_ok_button(self, sql_server_connection_setting_window, title_key):
            ok_button = (
                sql_server_connection_setting_window.by(name=ProfileCenterSettingsPage.ok_button[title_key])
                .find()
                .window_text()
            )
            check.equal(ok_button, ProfileCenterSettingsPage.ok_button[title_key])

        def test_check_connection(self, sql_server_connection_setting_window, title_key):
            check_connection = (
                sql_server_connection_setting_window.by(name=ProfileCenterSettingsPage.check_connection[title_key])
                .find()
                .window_text()
            )
            check.equal(check_connection, ProfileCenterSettingsPage.check_connection[title_key])

    @allure.story("тест окна настройки расписания вычитки индексов ProfileCenter")
    class TestScheduleOfReadingWindow:
        def test_modifying_schedule(self, schedule_of_reading_window, title_key):
            modifying_schedule = (
                schedule_of_reading_window.by(name=ProfileCenterSettingsPage.modifying_schedule[title_key])
                .find()
                .window_text()
            )
            check.equal(modifying_schedule, ProfileCenterSettingsPage.modifying_schedule[title_key])

        def test_select_name(self, schedule_of_reading_window, title_key):
            select_name = (
                schedule_of_reading_window.by(name=ProfileCenterSettingsPage.select_name[title_key])
                .find()
                .window_text()
            )
            check.equal(select_name, ProfileCenterSettingsPage.select_name[title_key])

        def test_schedule_is_enabled(self, schedule_of_reading_window, title_key):
            schedule_is_enabled = (
                schedule_of_reading_window.by(name=ProfileCenterSettingsPage.schedule_is_enabled[title_key])
                .find()
                .window_text()
            )
            check.equal(schedule_is_enabled, ProfileCenterSettingsPage.schedule_is_enabled[title_key])

        def test_custom(self, schedule_of_reading_window, title_key):
            custom = (
                schedule_of_reading_window.by(name=ProfileCenterSettingsPage.custom[title_key]).find().window_text()
            )
            check.equal(custom, ProfileCenterSettingsPage.custom[title_key])

        def test_once(self, schedule_of_reading_window, title_key):
            once = schedule_of_reading_window.by(name=ProfileCenterSettingsPage.once[title_key]).find().window_text()
            check.equal(once, ProfileCenterSettingsPage.once[title_key])

        def test_monthly(self, schedule_of_reading_window, title_key):
            monthly = (
                schedule_of_reading_window.by(name=ProfileCenterSettingsPage.monthly[title_key]).find().window_text()
            )
            check.equal(monthly, ProfileCenterSettingsPage.monthly[title_key])

        def test_weekly(self, schedule_of_reading_window, title_key):
            weekly = (
                schedule_of_reading_window.by(name=ProfileCenterSettingsPage.weekly[title_key]).find().window_text()
            )
            check.equal(weekly, ProfileCenterSettingsPage.weekly[title_key])

        def test_daily(self, schedule_of_reading_window, title_key):
            daily = schedule_of_reading_window.by(name=ProfileCenterSettingsPage.daily[title_key]).find().window_text()
            check.equal(daily, ProfileCenterSettingsPage.daily[title_key])

        def test_cancel_button3(self, schedule_of_reading_window, title_key):
            cancel_button3 = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.cancel_button3[title_key],
                    found_index=ProfileCenterSettingsPage.cancel_button3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button3, ProfileCenterSettingsPage.cancel_button3[title_key])

        def test_next_button(self, schedule_of_reading_window, title_key):
            next_button = (
                schedule_of_reading_window.by(name=ProfileCenterSettingsPage.next_button[title_key])
                .find()
                .window_text()
            )
            check.equal(next_button, ProfileCenterSettingsPage.next_button[title_key])

        def test_back_button(self, schedule_of_reading_window, title_key):
            back_button = (
                schedule_of_reading_window.by(name=ProfileCenterSettingsPage.back_button[title_key])
                .find()
                .window_text()
            )
            check.equal(back_button, ProfileCenterSettingsPage.back_button[title_key])

    @allure.story("тест второго окна настройки расписания вычитки индексов ProfileCenter")
    class TestScheduleOfReadingSecondWindow:
        def test_modifying_schedule2(self, schedule_of_reading_second_window, title_key):
            modifying_schedule2 = (
                schedule_of_reading_second_window.by(name=ProfileCenterSettingsPage.modifying_schedule2[title_key])
                .find()
                .window_text()
            )
            check.equal(modifying_schedule2, ProfileCenterSettingsPage.modifying_schedule2[title_key])

        def test_repeat_every(self, schedule_of_reading_second_window, title_key):
            repeat_every = (
                schedule_of_reading_second_window.by(name=ProfileCenterSettingsPage.repeat_every[title_key])
                .find()
                .window_text()
            )
            check.equal(repeat_every, ProfileCenterSettingsPage.repeat_every[title_key])

        def test_workdays_only(self, schedule_of_reading_second_window, title_key):
            workdays_only = (
                schedule_of_reading_second_window.by(name=ProfileCenterSettingsPage.workdays_only[title_key])
                .find()
                .window_text()
            )
            check.equal(workdays_only, ProfileCenterSettingsPage.workdays_only[title_key])

        def test_every(self, schedule_of_reading_second_window, title_key):
            every = (
                schedule_of_reading_second_window.by(name=ProfileCenterSettingsPage.every[title_key])
                .find()
                .window_text()
            )
            check.equal(every, ProfileCenterSettingsPage.every[title_key])

        def test_on_workdays(self, schedule_of_reading_second_window, title_key):
            on_workdays = (
                schedule_of_reading_second_window.by(name=ProfileCenterSettingsPage.on_workdays[title_key])
                .find()
                .window_text()
            )
            check.equal(on_workdays, ProfileCenterSettingsPage.on_workdays[title_key])

        def test_daily3(self, schedule_of_reading_second_window, title_key):
            daily2 = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.daily2[title_key],
                    control_type=ProfileCenterSettingsPage.daily2["control_type"],
                )
                .find()
                .window_text()
            )
            check.equal(daily2, ProfileCenterSettingsPage.daily2[title_key])

        def test_cancel_button4(self, schedule_of_reading_second_window, title_key):
            cancel_button4 = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.cancel_button4[title_key],
                    found_index=ProfileCenterSettingsPage.cancel_button4["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button4, ProfileCenterSettingsPage.cancel_button4[title_key])

        def test_next_button2(self, schedule_of_reading_second_window, title_key):
            next_button2 = (
                schedule_of_reading_second_window.by(name=ProfileCenterSettingsPage.next_button2[title_key])
                .find()
                .window_text()
            )
            check.equal(next_button2, ProfileCenterSettingsPage.next_button2[title_key])

        def test_back_button2(self, schedule_of_reading_second_window, title_key):
            back_button2 = (
                schedule_of_reading_second_window.by(name=ProfileCenterSettingsPage.back_button2[title_key])
                .find()
                .window_text()
            )
            check.equal(back_button2, ProfileCenterSettingsPage.back_button2[title_key])

    @allure.story("тест третьего окна настройки расписания вычитки индексов ProfileCenter")
    class TestScheduleOfReadingThirdWindow:
        def test_modifying_schedule3(self, schedule_of_reading_third_window, title_key):
            modifying_schedule3 = (
                schedule_of_reading_third_window.by(name=ProfileCenterSettingsPage.modifying_schedule3[title_key])
                .find()
                .window_text()
            )
            check.equal(modifying_schedule3, ProfileCenterSettingsPage.modifying_schedule3[title_key])

        def test_cancel_button5(self, schedule_of_reading_third_window, title_key):
            cancel_button5 = (
                schedule_of_reading_third_window.by(
                    name=ProfileCenterSettingsPage.cancel_button5[title_key],
                    found_index=ProfileCenterSettingsPage.cancel_button5["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button5, ProfileCenterSettingsPage.cancel_button5[title_key])

        def test_finish_button(self, schedule_of_reading_third_window, title_key):
            finish_button = (
                schedule_of_reading_third_window.by(
                    name=ProfileCenterSettingsPage.finish_button[title_key],
                    control_type=ProfileCenterSettingsPage.finish_button["control_type"],
                )
                .find()
                .window_text()
            )
            check.equal(finish_button, ProfileCenterSettingsPage.finish_button[title_key])

        def test_back_button3(self, schedule_of_reading_third_window, title_key):
            back_button3 = (
                schedule_of_reading_third_window.by(name=ProfileCenterSettingsPage.back_button3[title_key])
                .find()
                .window_text()
            )
            check.equal(back_button3, ProfileCenterSettingsPage.back_button3[title_key])

    @allure.story("тест окна настройки расписания профилирования ProfileCenter")
    class TestScheduleOfProfilingWindow:
        def test_modifying_schedule(self, schedule_of_profiling_window, title_key):
            modifying_schedule = (
                schedule_of_profiling_window.by(name=ProfileCenterSettingsPage.modifying_schedule[title_key])
                .find()
                .window_text()
            )
            check.equal(modifying_schedule, ProfileCenterSettingsPage.modifying_schedule[title_key])

        def test_schedule_is_enabled2(self, schedule_of_profiling_window, title_key):
            schedule_is_enabled2 = (
                schedule_of_profiling_window.by(name=ProfileCenterSettingsPage.schedule_is_enabled2[title_key])
                .find()
                .window_text()
            )
            check.equal(schedule_is_enabled2, ProfileCenterSettingsPage.schedule_is_enabled2[title_key])

        def test_custom2(self, schedule_of_profiling_window, title_key):
            custom2 = (
                schedule_of_profiling_window.by(name=ProfileCenterSettingsPage.custom2[title_key]).find().window_text()
            )
            check.equal(custom2, ProfileCenterSettingsPage.custom2[title_key])

        def test_once2(self, schedule_of_profiling_window, title_key):
            once2 = (
                schedule_of_profiling_window.by(name=ProfileCenterSettingsPage.once2[title_key]).find().window_text()
            )
            check.equal(once2, ProfileCenterSettingsPage.once2[title_key])

        def test_monthly2(self, schedule_of_profiling_window, title_key):
            monthly2 = (
                schedule_of_profiling_window.by(name=ProfileCenterSettingsPage.monthly2[title_key])
                .find()
                .window_text()
            )
            check.equal(monthly2, ProfileCenterSettingsPage.monthly2[title_key])

        def test_weekly2(self, schedule_of_profiling_window, title_key):
            weekly2 = (
                schedule_of_profiling_window.by(name=ProfileCenterSettingsPage.weekly2[title_key]).find().window_text()
            )
            check.equal(weekly2, ProfileCenterSettingsPage.weekly2[title_key])

        def test_daily3(self, schedule_of_profiling_window, title_key):
            daily3 = (
                schedule_of_profiling_window.by(name=ProfileCenterSettingsPage.daily3[title_key]).find().window_text()
            )
            check.equal(daily3, ProfileCenterSettingsPage.daily3[title_key])

        def test_cancel_button6(self, schedule_of_profiling_window, title_key):
            cancel_button6 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.cancel_button6[title_key],
                    found_index=ProfileCenterSettingsPage.cancel_button6["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button6, ProfileCenterSettingsPage.cancel_button6[title_key])

        def test_next_button3(self, schedule_of_profiling_window, title_key):
            next_button3 = (
                schedule_of_profiling_window.by(name=ProfileCenterSettingsPage.next_button3[title_key])
                .find()
                .window_text()
            )
            check.equal(next_button3, ProfileCenterSettingsPage.next_button3[title_key])

        def test_back_button4(self, schedule_of_profiling_window, title_key):
            back_button4 = (
                schedule_of_profiling_window.by(name=ProfileCenterSettingsPage.back_button4[title_key])
                .find()
                .window_text()
            )
            check.equal(back_button4, ProfileCenterSettingsPage.back_button4[title_key])

    @allure.story("тест второго окна настройки расписания профилирования ProfileCenter")
    class TestScheduleOfProfilingSecondWindow:
        def test_modifying_schedule5(self, schedule_of_profiling_second_window, title_key):
            modifying_schedule5 = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.modifying_schedule5[title_key])
                .find()
                .window_text()
            )
            check.equal(modifying_schedule5, ProfileCenterSettingsPage.modifying_schedule5[title_key])

        def test_september(self, schedule_of_profiling_second_window, title_key):
            september = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.september[title_key])
                .find()
                .window_text()
            )
            check.equal(september, ProfileCenterSettingsPage.september[title_key])

        def test_august(self, schedule_of_profiling_second_window, title_key):
            august = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.august[title_key])
                .find()
                .window_text()
            )
            check.equal(august, ProfileCenterSettingsPage.august[title_key])

        def test_july(self, schedule_of_profiling_second_window, title_key):
            july = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.july[title_key])
                .find()
                .window_text()
            )
            check.equal(july, ProfileCenterSettingsPage.july[title_key])

        def test_june(self, schedule_of_profiling_second_window, title_key):
            june = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.june[title_key])
                .find()
                .window_text()
            )
            check.equal(june, ProfileCenterSettingsPage.june[title_key])

        def test_may(self, schedule_of_profiling_second_window, title_key):
            may = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.may[title_key])
                .find()
                .window_text()
            )
            check.equal(may, ProfileCenterSettingsPage.may[title_key])

        def test_april(self, schedule_of_profiling_second_window, title_key):
            april = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.april[title_key])
                .find()
                .window_text()
            )
            check.equal(april, ProfileCenterSettingsPage.april[title_key])

        def test_december(self, schedule_of_profiling_second_window, title_key):
            december = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.december[title_key])
                .find()
                .window_text()
            )
            check.equal(december, ProfileCenterSettingsPage.december[title_key])

        def test_november(self, schedule_of_profiling_second_window, title_key):
            november = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.november[title_key])
                .find()
                .window_text()
            )
            check.equal(november, ProfileCenterSettingsPage.november[title_key])

        def test_october(self, schedule_of_profiling_second_window, title_key):
            october = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.october[title_key])
                .find()
                .window_text()
            )
            check.equal(october, ProfileCenterSettingsPage.october[title_key])

        def test_march(self, schedule_of_profiling_second_window, title_key):
            march = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.march[title_key])
                .find()
                .window_text()
            )
            check.equal(march, ProfileCenterSettingsPage.march[title_key])

        def test_february(self, schedule_of_profiling_second_window, title_key):
            february = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.february[title_key])
                .find()
                .window_text()
            )
            check.equal(february, ProfileCenterSettingsPage.february[title_key])

        def test_january(self, schedule_of_profiling_second_window, title_key):
            january = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.january[title_key])
                .find()
                .window_text()
            )
            check.equal(january, ProfileCenterSettingsPage.january[title_key])

        def test_or_radiobutton(self, schedule_of_profiling_second_window, title_key):
            or_radiobutton = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.or_radiobutton[title_key])
                .find()
                .window_text()
            )
            check.equal(or_radiobutton, ProfileCenterSettingsPage.or_radiobutton[title_key])

        def test_date_radiobutton(self, schedule_of_profiling_second_window, title_key):
            date_radiobutton = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.date_radiobutton[title_key])
                .find()
                .window_text()
            )
            check.equal(date_radiobutton, ProfileCenterSettingsPage.date_radiobutton[title_key])

        def test_cancel_button7(self, schedule_of_profiling_second_window, title_key):
            cancel_button7 = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.cancel_button7[title_key],
                    found_index=ProfileCenterSettingsPage.cancel_button7["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button7, ProfileCenterSettingsPage.cancel_button7[title_key])

        def test_next_button4(self, schedule_of_profiling_second_window, title_key):
            next_button4 = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.next_button4[title_key])
                .find()
                .window_text()
            )
            check.equal(next_button4, ProfileCenterSettingsPage.next_button4[title_key])

        def test_back_button5(self, schedule_of_profiling_second_window, title_key):
            back_button5 = (
                schedule_of_profiling_second_window.by(name=ProfileCenterSettingsPage.back_button5[title_key])
                .find()
                .window_text()
            )
            check.equal(back_button5, ProfileCenterSettingsPage.back_button5[title_key])

    @allure.story("тест третьего окна настройки расписания профилирования ProfileCenter")
    class TestScheduleOfProfilingThirdWindow:
        def test_modifying_schedule6(self, schedule_of_profiling_third_window, title_key):
            modifying_schedule6 = (
                schedule_of_profiling_third_window.by(name=ProfileCenterSettingsPage.modifying_schedule6[title_key])
                .find()
                .window_text()
            )
            check.equal(modifying_schedule6, ProfileCenterSettingsPage.modifying_schedule6[title_key])

        def test_cancel_button8(self, schedule_of_profiling_third_window, title_key):
            cancel_button8 = (
                schedule_of_profiling_third_window.by(
                    name=ProfileCenterSettingsPage.cancel_button8[title_key],
                    found_index=ProfileCenterSettingsPage.cancel_button8["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button8, ProfileCenterSettingsPage.cancel_button8[title_key])

        def test_finish_button2(self, schedule_of_profiling_third_window, title_key):
            finish_button2 = (
                schedule_of_profiling_third_window.by(
                    name=ProfileCenterSettingsPage.finish_button2[title_key],
                    control_type=ProfileCenterSettingsPage.finish_button2["control_type"],
                )
                .find()
                .window_text()
            )
            check.equal(finish_button2, ProfileCenterSettingsPage.finish_button2[title_key])

        def test_back_button6(self, schedule_of_profiling_third_window, title_key):
            back_button6 = (
                schedule_of_profiling_third_window.by(name=ProfileCenterSettingsPage.back_button6[title_key])
                .find()
                .window_text()
            )
            check.equal(back_button6, ProfileCenterSettingsPage.back_button6[title_key])
