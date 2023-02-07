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
def handle(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def sql_server_connection_setting_window(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.by(name=ProfileCenterSettingsPage.setup_connection_to_db["title_es"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_reading_window(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_reading_button
    ).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_reading_second_window(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_reading_button
    ).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button["title_es"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_reading_third_window(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_reading_button
    ).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button["title_es"]).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button2["title_es"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_profiling_window(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_profiling_button
    ).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_profiling_second_window(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_profiling_button
    ).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button3["title_es"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def schedule_of_profiling_third_window(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y11{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.__getattribute__(
        ProfileCenterSettingsPage.edit_schedule_of_profiling_button
    ).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button3["title_es"]).click()
    time.sleep(1)
    handle.by(name=ProfileCenterSettingsPage.next_button4["title_es"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("ESP Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsES
@pytest.mark.testGUI_EspVersionDCTest_ControlsTest_Additionalfeatures
class TestProfileCenterSettingsPage:
    @allure.story("тест главного окна ProfileCenter")
    class TestProfileCenterSettingsMainPage:
        def test_logging_of_server(self, handle):
            logging_of_server = (
                handle.by(name=ProfileCenterSettingsPage.logging_of_server["title_es"])
                .find()
                .window_text()
            )
            check.equal(logging_of_server, "Registro de servidor")

        def test_connection_to_database(self, handle):
            connection_to_database = (
                handle.by(
                    name=ProfileCenterSettingsPage.connection_to_database["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(connection_to_database, "Conexión a la base de datos")

        def test_control_of_services(self, handle):
            control_of_services = (
                handle.by(
                    name=ProfileCenterSettingsPage.control_of_services["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(control_of_services, "Control de servicios")

        def test_schedules(self, handle):
            schedules = (
                handle.by(name=ProfileCenterSettingsPage.schedules["title_es"])
                .find()
                .window_text()
            )
            check.equal(schedules, "Horario")

        def test_schedule_of_profiling(self, handle):
            schedule_of_profiling = (
                handle.by(
                    name=ProfileCenterSettingsPage.schedule_of_profiling["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(schedule_of_profiling, "Horario de elaboración de perfiles")

        def test_schedule_of_reading(self, handle):
            schedule_of_reading = (
                handle.by(
                    name=ProfileCenterSettingsPage.schedule_of_reading["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(schedule_of_reading, "Horario de lectura")

        def test_setup_connection_to_db(self, handle):
            setup_connection_to_db = (
                handle.by(
                    name=ProfileCenterSettingsPage.setup_connection_to_db["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(setup_connection_to_db, "Configurar conexión a base de datos")

        def test_clear_database(self, handle):
            clear_database = (
                handle.by(name=ProfileCenterSettingsPage.clear_database["title_es"])
                .find()
                .window_text()
            )
            check.equal(clear_database, "Borrar base de datos")

        def test_start_profiling(self, handle):
            start_profiling = (
                handle.by(name=ProfileCenterSettingsPage.start_profiling["title_es"])
                .find()
                .window_text()
            )
            check.equal(start_profiling, "Iniciar elaboración de perfiles")

        def test_read_texts(self, handle):
            read_texts = (
                handle.by(name=ProfileCenterSettingsPage.read_texts["title_es"])
                .find()
                .window_text()
            )
            check.equal(read_texts, "Leer textos")

        def test_stop_server(self, handle):
            stop_server = (
                handle.by(name=ProfileCenterSettingsPage.stop_server["title_es"])
                .find()
                .window_text()
            )
            check.equal(stop_server, "Detener servidor")

        def test_data_for_profile_generation(self, handle):
            data_for_profile_generation = (
                handle.by(
                    name=ProfileCenterSettingsPage.data_for_profile_generation[
                        "title_es"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(data_for_profile_generation, "Datos para cálculo de perfil")

        def test_add(self, handle):
            add = (
                handle.by(name=ProfileCenterSettingsPage.add["title_es"])
                .find()
                .window_text()
            )
            check.equal(add, "Añadir")

        def test_delete(self, handle):
            delete = (
                handle.by(name=ProfileCenterSettingsPage.delete["title_es"])
                .find()
                .window_text()
            )
            check.equal(delete, "Borrar")

        def test_mail_outgoing_email_correspondence(self, handle):
            mail_outgoing_email_correspondence = (
                handle.by(
                    name=ProfileCenterSettingsPage.mail_outgoing_email_correspondence[
                        "title_es"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                mail_outgoing_email_correspondence,
                "mail (correos electrónicos salientes)",
            )

        def test_im_outgoing_messages_in_im_clients_and_on_social_networks(
            self, handle
        ):
            im_outgoing_messages_in_im_clients_and_on_social_networks = (
                handle.by(
                    name=ProfileCenterSettingsPage.im_outgoing_messages_in_im_clients_and_on_social_networks[
                        "title_es"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                im_outgoing_messages_in_im_clients_and_on_social_networks,
                "im (mensajes salientes en clientes IM y en redes sociales)",
            )

        def test_skype_outgoing_messages_on_skype_lync_viber_telegram_and_whatsapp(
            self, handle
        ):
            skype_outgoing_messages_on_skype_lync_viber_telegram_and_whatsapp = (
                handle.by(
                    name=ProfileCenterSettingsPage.skype_outgoing_messages_on_skype_lync_viber_telegram_and_whatsapp[
                        "title_es"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                skype_outgoing_messages_on_skype_lync_viber_telegram_and_whatsapp,
                "skype (mensajes salientes en Skype, Lync, Viber, Telegram, WhatsApp)",
            )

        def test_failure_to_read_texts_from_index(self, handle):
            failure_to_read_texts_from_index = (
                handle.by(
                    name=ProfileCenterSettingsPage.failure_to_read_texts_from_index[
                        "title_es"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                failure_to_read_texts_from_index, "Fracasó a leer textos del índice"
            )

        def test_cancel_button(self, handle):
            cancel_button = (
                handle.by(name=ProfileCenterSettingsPage.cancel_button["title_es"])
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Cancelar")

        def test_apply_button(self, handle):
            apply_button = (
                handle.by(name=ProfileCenterSettingsPage.apply_button["title_es"])
                .find()
                .window_text()
            )
            check.equal(apply_button, "Aplicar")

        def test_automatically_repeat_reading_in_case_of_failure(self, handle):
            automatically_repeat_reading_in_case_of_failure = (
                handle.by(
                    name=ProfileCenterSettingsPage.automatically_repeat_reading_in_case_of_failure[
                        "title_es"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                automatically_repeat_reading_in_case_of_failure,
                "Intentar lectura automáticamente si hay fracaso",
            )

    @allure.story("тест окна нстройки подключения к БД ProfileCenter")
    class TestSQLServerConnectionSettingWindow:
        def test_sql_server_connection_settings(
            self, sql_server_connection_setting_window
        ):
            sql_server_connection_settings = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.sql_server_connection_settings[
                        "title_es"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_connection_settings, "Parámetros de conexión a SQL Server"
            )

        def test_create_button(self, sql_server_connection_setting_window):
            create_button = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.create_button["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(create_button, "Crear")

        def test_database_name(self, sql_server_connection_setting_window):
            database_name = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.database_name["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(database_name, "Nombre de base de datos:")

        def test_password(self, sql_server_connection_setting_window):
            password = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.password["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(password, "Contraseña:")

        def test_username(self, sql_server_connection_setting_window):
            username = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.username["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(username, "Nombre de usuario:")

        def test_sql_server_authentication_mode(
            self, sql_server_connection_setting_window
        ):
            sql_server_authentication_mode = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.sql_server_authentication_mode[
                        "title_es"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                sql_server_authentication_mode,
                "Usar autenticación de SQL Server interna",
            )

        def test_windows_authentication_mode(
            self, sql_server_connection_setting_window
        ):
            windows_authentication_mode = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.windows_authentication_mode[
                        "title_es"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(windows_authentication_mode, "Usar autenticación Windows")

        def test_read_from_dc(self, sql_server_connection_setting_window):
            read_from_dc = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.read_from_dc["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(read_from_dc, "Leer de DC")

        def test_server_name(self, sql_server_connection_setting_window):
            server_name = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.server_name["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(server_name, "Nombre del servidor")

        def test_server_type(self, sql_server_connection_setting_window):
            server_type = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.server_type["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(server_type, "Tipo del servidor")

        def test_cancel_button2(self, sql_server_connection_setting_window):
            cancel_button2 = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.cancel_button2["title_es"],
                    found_index=ProfileCenterSettingsPage.cancel_button2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button2, "Cancelar")

        def test_ok_button(self, sql_server_connection_setting_window):
            ok_button = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.ok_button["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(ok_button, "OK")

        def test_check_connection(self, sql_server_connection_setting_window):
            check_connection = (
                sql_server_connection_setting_window.by(
                    name=ProfileCenterSettingsPage.check_connection["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection, "Probar conexión ")

    @allure.story("тест окна настройки расписания вычитки индексов ProfileCenter")
    class TestScheduleOfReadingWindow:
        def test_modifying_schedule(self, schedule_of_reading_window):
            modifying_schedule = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.modifying_schedule["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(modifying_schedule, "Cambio de horario")

        def test_select_name(self, schedule_of_reading_window):
            select_name = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.select_name["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(select_name, "SelectName")

        def test_schedule_is_enabled(self, schedule_of_reading_window):
            schedule_is_enabled = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.schedule_is_enabled["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(schedule_is_enabled, "Horario está habilitado.")

        def test_custom(self, schedule_of_reading_window):
            custom = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.custom["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(custom, "Customizado")

        def test_once(self, schedule_of_reading_window):
            once = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.once["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(once, "Una vez")

        def test_monthly(self, schedule_of_reading_window):
            monthly = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.monthly["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(monthly, "Cada mes")

        def test_weekly(self, schedule_of_reading_window):
            weekly = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.weekly["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(weekly, "Cada semana")

        def test_daily(self, schedule_of_reading_window):
            daily = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.daily["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(daily, "Cada día")

        def test_cancel_button3(self, schedule_of_reading_window):
            cancel_button3 = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.cancel_button3["title_es"],
                    found_index=ProfileCenterSettingsPage.cancel_button3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button3, "Cancelar")

        def test_next_button(self, schedule_of_reading_window):
            next_button = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.next_button["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(next_button, "Siguiente >")

        def test_back_button(self, schedule_of_reading_window):
            back_button = (
                schedule_of_reading_window.by(
                    name=ProfileCenterSettingsPage.back_button["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(back_button, "< Volver")

    @allure.story(
        "тест второго окна настройки расписания вычитки индексов ProfileCenter"
    )
    class TestScheduleOfReadingSecondWindow:
        def test_modifying_schedule2(self, schedule_of_reading_second_window):
            modifying_schedule2 = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.modifying_schedule2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(modifying_schedule2, "Cambio de horario")

        def test_repeat_every(self, schedule_of_reading_second_window):
            repeat_every = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.repeat_every["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(repeat_every, "repetir cada")

        def test_workdays_only(self, schedule_of_reading_second_window):
            workdays_only = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.workdays_only["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(workdays_only, "Considerar solo días de trabajo (Lu-Vie) ")

        def test_every(self, schedule_of_reading_second_window):
            every = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.every["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(every, "Cad.")

        def test_on_workdays(self, schedule_of_reading_second_window):
            on_workdays = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.on_workdays["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(on_workdays, "En días de trabajo")

        def test_daily3(self, schedule_of_reading_second_window):
            daily2 = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.daily2["title_es"],
                    control_type=ProfileCenterSettingsPage.daily2["control_type"],
                )
                .find()
                .window_text()
            )
            check.equal(daily2, "Cada día")

        def test_cancel_button4(self, schedule_of_reading_second_window):
            cancel_button4 = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.cancel_button4["title_es"],
                    found_index=ProfileCenterSettingsPage.cancel_button4["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button4, "Cancelar")

        def test_next_button2(self, schedule_of_reading_second_window):
            next_button2 = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.next_button2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(next_button2, "Siguiente >")

        def test_back_button2(self, schedule_of_reading_second_window):
            back_button2 = (
                schedule_of_reading_second_window.by(
                    name=ProfileCenterSettingsPage.back_button2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(back_button2, "< Volver")

    @allure.story(
        "тест третьего окна настройки расписания вычитки индексов ProfileCenter"
    )
    class TestScheduleOfReadingThirdWindow:
        def test_modifying_schedule3(self, schedule_of_reading_third_window):
            modifying_schedule3 = (
                schedule_of_reading_third_window.by(
                    name=ProfileCenterSettingsPage.modifying_schedule3["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(modifying_schedule3, "Cambio de horario")

        def test_cancel_button5(self, schedule_of_reading_third_window):
            cancel_button5 = (
                schedule_of_reading_third_window.by(
                    name=ProfileCenterSettingsPage.cancel_button5["title_es"],
                    found_index=ProfileCenterSettingsPage.cancel_button5["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button5, "Cancelar")

        def test_finish_button(self, schedule_of_reading_third_window):
            finish_button = (
                schedule_of_reading_third_window.by(
                    name=ProfileCenterSettingsPage.finish_button["title_es"],
                    control_type=ProfileCenterSettingsPage.finish_button[
                        "control_type"
                    ],
                )
                .find()
                .window_text()
            )
            check.equal(finish_button, "Finalizar")

        def test_back_button3(self, schedule_of_reading_third_window):
            back_button3 = (
                schedule_of_reading_third_window.by(
                    name=ProfileCenterSettingsPage.back_button3["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(back_button3, "< Volver")

    @allure.story("тест окна настройки расписания профилирования ProfileCenter")
    class TestScheduleOfProfilingWindow:
        def test_modifying_schedule(self, schedule_of_profiling_window):
            modifying_schedule = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.modifying_schedule["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(modifying_schedule, "Cambio de horario")

        def test_schedule_is_enabled2(self, schedule_of_profiling_window):
            schedule_is_enabled2 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.schedule_is_enabled2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(schedule_is_enabled2, "Horario está habilitado.")

        def test_custom2(self, schedule_of_profiling_window):
            custom2 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.custom2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(custom2, "Customizado")

        def test_once2(self, schedule_of_profiling_window):
            once2 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.once2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(once2, "Una vez")

        def test_monthly2(self, schedule_of_profiling_window):
            monthly2 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.monthly2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(monthly2, "Cada mes")

        def test_weekly2(self, schedule_of_profiling_window):
            weekly2 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.weekly2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(weekly2, "Cada semana")

        def test_daily3(self, schedule_of_profiling_window):
            daily3 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.daily3["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(daily3, "Cada día")

        def test_cancel_button6(self, schedule_of_profiling_window):
            cancel_button6 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.cancel_button6["title_es"],
                    found_index=ProfileCenterSettingsPage.cancel_button6["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button6, "Cancelar")

        def test_next_button3(self, schedule_of_profiling_window):
            next_button3 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.next_button3["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(next_button3, "Siguiente >")

        def test_back_button4(self, schedule_of_profiling_window):
            back_button4 = (
                schedule_of_profiling_window.by(
                    name=ProfileCenterSettingsPage.back_button4["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(back_button4, "< Volver")

    @allure.story("тест второго окна настройки расписания профилирования ProfileCenter")
    class TestScheduleOfProfilingSecondWindow:
        def test_modifying_schedule5(self, schedule_of_profiling_second_window):
            modifying_schedule5 = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.modifying_schedule5["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(modifying_schedule5, "Cambio de horario")

        def test_september(self, schedule_of_profiling_second_window):
            september = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.september["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(september, "Septiembre")

        def test_august(self, schedule_of_profiling_second_window):
            august = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.august["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(august, "Agosto")

        def test_july(self, schedule_of_profiling_second_window):
            july = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.july["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(july, "Julio")

        def test_june(self, schedule_of_profiling_second_window):
            june = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.june["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(june, "Junio")

        def test_may(self, schedule_of_profiling_second_window):
            may = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.may["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(may, "Mayo")

        def test_april(self, schedule_of_profiling_second_window):
            april = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.april["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(april, "Abríl")

        def test_december(self, schedule_of_profiling_second_window):
            december = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.december["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(december, "Diciembre")

        def test_november(self, schedule_of_profiling_second_window):
            november = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.november["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(november, "Noviembre")

        def test_october(self, schedule_of_profiling_second_window):
            october = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.october["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(october, "Octubre")

        def test_march(self, schedule_of_profiling_second_window):
            march = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.march["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(march, "Marzo")

        def test_february(self, schedule_of_profiling_second_window):
            february = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.february["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(february, "Febrero")

        def test_january(self, schedule_of_profiling_second_window):
            january = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.january["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(january, "Enero")

        def test_or_radiobutton(self, schedule_of_profiling_second_window):
            or_radiobutton = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.or_radiobutton["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(or_radiobutton, "o")

        def test_date_radiobutton(self, schedule_of_profiling_second_window):
            date_radiobutton = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.date_radiobutton["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(date_radiobutton, "Fecha")

        def test_cancel_button7(self, schedule_of_profiling_second_window):
            cancel_button7 = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.cancel_button7["title_es"],
                    found_index=ProfileCenterSettingsPage.cancel_button7["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button7, "Cancelar")

        def test_next_button4(self, schedule_of_profiling_second_window):
            next_button4 = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.next_button4["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(next_button4, "Siguiente >")

        def test_back_button5(self, schedule_of_profiling_second_window):
            back_button5 = (
                schedule_of_profiling_second_window.by(
                    name=ProfileCenterSettingsPage.back_button5["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(back_button5, "< Volver")

    @allure.story(
        "тест третьего окна настройки расписания профилирования ProfileCenter"
    )
    class TestScheduleOfProfilingThirdWindow:
        def test_modifying_schedule6(self, schedule_of_profiling_third_window):
            modifying_schedule6 = (
                schedule_of_profiling_third_window.by(
                    name=ProfileCenterSettingsPage.modifying_schedule6["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(modifying_schedule6, "Cambio de horario")

        def test_cancel_button8(self, schedule_of_profiling_third_window):
            cancel_button8 = (
                schedule_of_profiling_third_window.by(
                    name=ProfileCenterSettingsPage.cancel_button8["title_es"],
                    found_index=ProfileCenterSettingsPage.cancel_button8["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button8, "Cancelar")

        def test_finish_button2(self, schedule_of_profiling_third_window):
            finish_button2 = (
                schedule_of_profiling_third_window.by(
                    name=ProfileCenterSettingsPage.finish_button2["title_es"],
                    control_type=ProfileCenterSettingsPage.finish_button2[
                        "control_type"
                    ],
                )
                .find()
                .window_text()
            )
            check.equal(finish_button2, "Finalizar")

        def test_back_button6(self, schedule_of_profiling_third_window):
            back_button6 = (
                schedule_of_profiling_third_window.by(
                    name=ProfileCenterSettingsPage.back_button6["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(back_button6, "< Volver")
