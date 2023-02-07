class ProfileCenterSettingsPage:
    # Кнопки
    setup_connection_to_db = {
        "title_en": "Set up connection to DB ",
        "title_es": "Configurar conexión a base de datos",
        "title_ru": "Настроить подключение к БД",
        "control_type": "Button",
    }
    clear_database = {
        "title_en": "Clear database",
        "title_es": "Borrar base de datos",
        "title_ru": "Очистить БД",
        "control_type": "Button",
    }
    start_profiling = {
        "title_en": "Start profiling",
        "title_es": "Iniciar elaboración de perfiles",
        "title_ru": "Запустить профилирование",
        "control_type": "Button",
    }
    read_texts = {
        "title_en": "Read texts",
        "title_es": "Leer textos",
        "title_ru": "Вычитать тексты",
        "control_type": "Button",
    }
    stop_server = {
        "title_en": "Stop server",
        "title_es": "Detener servidor",
        "title_ru": "Остановить сервер",
        "control_type": "Button",
    }

    add = {
        "title_en": "Add",
        "title_es": "Añadir",
        "title_ru": "Добавить",
        "control_type": "Button",
    }
    delete = {
        "title_en": "Delete",
        "title_es": "Borrar",
        "title_ru": "Удалить",
        "control_type": "Button",
    }

    cancel_button = {
        "title_en": "Cancel",
        "title_es": "Cancelar",
        "title_ru": "Отменить",
        "control_type": "Button",
    }
    apply_button = {
        "title_en": "Apply",
        "title_es": "Aplicar",
        "title_ru": "Применить",
        "control_type": "Button",
    }
    edit_schedule_of_reading_button = "Button4"
    edit_schedule_of_profiling_button = "Button3"

    # Панели
    logging_of_server = {
        "title_en": "Logging of server",
        "title_es": "Registro de servidor",
        "title_ru": "Логирование сервера",
        "control_type": "Pane",
    }
    connection_to_database = {
        "title_en": "Connection to database",
        "title_es": "Conexión a la base de datos",
        "title_ru": "Подключение к БД",
        "control_type": "Pane",
    }
    control_of_services = {
        "title_en": "Control of services",
        "title_es": "Control de servicios",
        "title_ru": "Управление службами",
        "control_type": "Pane",
    }
    schedules = {
        "title_en": "Schedules",
        "title_es": "Horario",
        "title_ru": "Расписания",
        "control_type": "Pane",
    }
    schedule_of_profiling = {
        "title_en": "Schedule of profiling",
        "title_es": "Horario de elaboración de perfiles",
        "title_ru": "Расписание профилирования",
        "control_type": "Pane",
    }
    schedule_of_reading = {
        "title_en": "Schedule of reading",
        "title_es": "Horario de lectura",
        "title_ru": "Расписание вычитки",
        "control_type": "Pane",
    }

    data_for_profile_generation = {
        "title_en": "Data for profile generation",
        "title_es": "Datos para cálculo de perfil",
        "title_ru": "Данные для расчета профиля",
        "control_type": "Pane",
    }

    failure_to_read_texts_from_index = {
        "title_en": "Failure to read texts from index",
        "title_es": "Fracasó a leer textos del índice",
        "title_ru": "Неудачная вычитка текстов из индекса",
        "control_type": "Pane",
    }

    # Чекбоксы
    mail_outgoing_email_correspondence = {
        "title_en": "Mail (outgoing e-mail correspondence)",
        "title_es": "mail (correos electrónicos salientes)",
        "title_ru": "mail (исходящая почтовая переписка)",
        "control_type": "CheckBox",
    }
    im_outgoing_messages_in_im_clients_and_on_social_networks = {
        "title_en": "IM (outgoing messages in IM clients and on social networks)",
        "title_es": "im (mensajes salientes en clientes IM y en redes sociales)",
        "title_ru": "im (исходящие сообщения в IM-клиентах и в социальных сетях)",
        "control_type": "CheckBox",
    }
    skype_outgoing_messages_on_skype_lync_viber_telegram_and_whatsapp = {
        "title_en": "Skype (outgoing messages on Skype, Lync, Viber, Telegram, and WhatsApp)",
        "title_es": "skype (mensajes salientes en Skype, Lync, Viber, Telegram, WhatsApp)",
        "title_ru": "skype (исходящие сообщения Skype, Lync, Viber, Telegram, WhatsApp)",
        "control_type": "CheckBox",
    }

    automatically_repeat_reading_in_case_of_failure = {
        "title_en": "Automatically repeat reading in case of failure",
        "title_es": "Intentar lectura automáticamente si hay fracaso",
        "title_ru": "Автоматически повторять вычитку в случае неудачи",
        "control_type": "CheckBox",
    }

    # Окно настройки подключения к БД
    sql_server_connection_settings = {
        "title_en": "SQL Server connection settings",
        "title_es": "Parámetros de conexión a SQL Server",
        "title_ru": "Параметры подключения к SQL Server",
        "control_type": "Window",
    }
    create_button = {
        "title_en": "Create",
        "title_es": "Crear",
        "title_ru": "Создать",
        "control_type": "Button",
    }
    database_name = {
        "title_en": "Database name:",
        "title_es": "Nombre de base de datos:",
        "title_ru": "Имя базы данных:",
        "control_type": "Pane",
    }
    password = {
        "title_en": "Password:",
        "title_es": "Contraseña:",
        "title_ru": "Пароль:",
        "control_type": "Pane",
    }
    username = {
        "title_en": "Username:",
        "title_es": "Nombre de usuario:",
        "title_ru": "Имя пользователя:",
        "control_type": "Pane",
    }
    sql_server_authentication_mode = {
        "title_en": "SQL Server Authentication mode",
        "title_es": "Usar autenticación de SQL Server interna",
        "title_ru": "Использовать внутреннюю аутентификацию SQL Server",
        "control_type": "RadioButton",
    }
    windows_authentication_mode = {
        "title_en": "Windows Authentication mode",
        "title_es": "Usar autenticación Windows",
        "title_ru": "Использовать аутентификацию Windows",
        "control_type": "RadioButton",
    }
    read_from_dc = {
        "title_en": "Read from DC",
        "title_es": "Leer de DC",
        "title_ru": "Считать из DC",
        "control_type": "Button",
    }
    server_name = {
        "title_en": "Server name:",
        "title_es": "Nombre del servidor",
        "title_ru": "Имя сервера:",
        "control_type": "Pane",
    }
    server_type = {
        "title_en": "Server type:",
        "title_es": "Tipo del servidor",
        "title_ru": "Тип сервера:",
        "control_type": "Pane",
    }
    cancel_button2 = {
        "title_en": "Cancel",
        "title_es": "Cancelar",
        "title_ru": "Отменить",
        "found_index": 0,
        "control_type": "Button",
    }
    ok_button = {
        "title_en": "OK",
        "title_es": "OK",
        "title_ru": "OK",
        "control_type": "Button",
    }
    check_connection = {
        "title_en": "Check connection",
        "title_es": "Probar conexión ",
        "title_ru": "Проверка подключения",
        "control_type": "Button",
    }

    # Окно настройки расписания вычитки индексов
    modifying_schedule = {
        "title_en": "Modifying schedule",
        "title_es": "Cambio de horario",
        "title_ru": "Изменение расписания",
        "control_type": "Window",
    }
    select_name = {
        "title_en": "SelectName",
        "title_es": "SelectName",
        "title_ru": "SelectName",
        "control_type": "Pane",
    }
    schedule_is_enabled = {
        "title_en": "The schedule is enabled",
        "title_es": "Horario está habilitado.",
        "title_ru": "Расписание включено",
        "control_type": "CheckBox",
    }
    custom = {
        "title_en": "Custom",
        "title_es": "Customizado",
        "title_ru": "По настройке",
        "control_type": "RadioButton",
    }
    once = {
        "title_en": "Once",
        "title_es": "Una vez",
        "title_ru": "Единовременно",
        "control_type": "RadioButton",
    }
    monthly = {
        "title_en": "Monthly",
        "title_es": "Cada mes",
        "title_ru": "Ежемесячно",
        "control_type": "RadioButton",
    }
    weekly = {
        "title_en": "Weekly",
        "title_es": "Cada semana",
        "title_ru": "Еженедельно",
        "control_type": "RadioButton",
    }
    daily = {
        "title_en": "Daily",
        "title_es": "Cada día",
        "title_ru": "Ежедневно",
        "control_type": "RadioButton",
    }
    cancel_button3 = {
        "title_en": "Cancel",
        "title_es": "Cancelar",
        "title_ru": "Отмена",
        "found_index": 0,
        "control_type": "Button",
    }
    next_button = {
        "title_en": "Next >",
        "title_es": "Siguiente >",
        "title_ru": "Далее >",
        "control_type": "Button",
    }
    back_button = {
        "title_en": "< Back",
        "title_es": "< Volver",
        "title_ru": "< Назад",
        "control_type": "Button",
    }

    # Второе окно настройки расписания вычитки индексов
    modifying_schedule2 = {
        "title_en": "Modifying schedule",
        "title_es": "Cambio de horario",
        "title_ru": "Изменение расписания",
        "control_type": "Window",
    }
    repeat_every = {
        "title_en": "repeat every",
        "title_es": "repetir cada",
        "title_ru": "повторять каждые",
        "control_type": "CheckBox",
    }
    workdays_only = {
        "title_en": "Workdays only (Monday - Friday)",
        "title_es": "Considerar solo días de trabajo (Lu-Vie) ",
        "title_ru": "Считать только рабочие дни(Пн-Пт)",
        "control_type": "CheckBox",
    }
    every = {
        "title_en": "Every",
        "title_es": "Cad.",
        "title_ru": "Кажд.",
        "control_type": "RadioButton",
    }
    on_workdays = {
        "title_en": "On workdays",
        "title_es": "En días de trabajo",
        "title_ru": "По рабочим дням",
        "control_type": "RadioButton",
    }
    daily2 = {
        "title_en": "Daily",
        "title_es": "Cada día",
        "title_ru": "Ежедневно",
        "control_type": "RadioButton",
    }
    cancel_button4 = {
        "title_en": "Cancel",
        "title_es": "Cancelar",
        "title_ru": "Отмена",
        "found_index": 0,
        "control_type": "Button",
    }
    next_button2 = {
        "title_en": "Next >",
        "title_es": "Siguiente >",
        "title_ru": "Далее >",
        "control_type": "Button",
    }
    back_button2 = {
        "title_en": "< Back",
        "title_es": "< Volver",
        "title_ru": "< Назад",
        "control_type": "Button",
    }

    # Третье окно настройки расписания вычитки индексов
    modifying_schedule3 = {
        "title_en": "Modifying schedule",
        "title_es": "Cambio de horario",
        "title_ru": "Изменение расписания",
        "control_type": "Window",
    }
    cancel_button5 = {
        "title_en": "Cancel",
        "title_es": "Cancelar",
        "title_ru": "Отмена",
        "found_index": 0,
        "control_type": "Button",
    }
    finish_button = {
        "title_en": "Finish",
        "title_es": "Finalizar",
        "title_ru": "Завершить",
        "control_type": "Button",
    }
    back_button3 = {
        "title_en": "< Back",
        "title_es": "< Volver",
        "title_ru": "< Назад",
        "control_type": "Button",
    }

    # Окно настройки расписания профилирования
    modifying_schedule4 = {
        "title_en": "Modifying schedule",
        "title_es": "Cambio de horario",
        "title_ru": "Изменение расписания",
        "control_type": "Window",
    }
    schedule_is_enabled2 = {
        "title_en": "The schedule is enabled",
        "title_es": "Horario está habilitado.",
        "title_ru": "Расписание включено",
        "control_type": "CheckBox",
    }
    custom2 = {
        "title_en": "Custom",
        "title_es": "Customizado",
        "title_ru": "По настройке",
        "control_type": "RadioButton",
    }
    once2 = {
        "title_en": "Once",
        "title_es": "Una vez",
        "title_ru": "Единовременно",
        "control_type": "RadioButton",
    }
    monthly2 = {
        "title_en": "Monthly",
        "title_es": "Cada mes",
        "title_ru": "Ежемесячно",
        "control_type": "RadioButton",
    }
    weekly2 = {
        "title_en": "Weekly",
        "title_es": "Cada semana",
        "title_ru": "Еженедельно",
        "control_type": "RadioButton",
    }
    daily3 = {
        "title_en": "Daily",
        "title_es": "Cada día",
        "title_ru": "Ежедневно",
        "control_type": "RadioButton",
    }
    cancel_button6 = {
        "title_en": "Cancel",
        "title_es": "Cancelar",
        "title_ru": "Отмена",
        "found_index": 0,
        "control_type": "Button",
    }
    next_button3 = {
        "title_en": "Next >",
        "title_es": "Siguiente >",
        "title_ru": "Далее >",
        "control_type": "Button",
    }
    back_button4 = {
        "title_en": "< Back",
        "title_es": "< Volver",
        "title_ru": "< Назад",
        "control_type": "Button",
    }

    # Второе окно настройки расписания профилирования
    modifying_schedule5 = {
        "title_en": "Modifying schedule",
        "title_es": "Cambio de horario",
        "title_ru": "Изменение расписания",
        "control_type": "Window",
    }
    september = {
        "title_en": "September",
        "title_es": "Septiembre",
        "title_ru": "Сентябрь",
        "control_type": "CheckBox",
    }
    august = {
        "title_en": "August",
        "title_es": "Agosto",
        "title_ru": "Август",
        "control_type": "CheckBox",
    }
    july = {
        "title_en": "July",
        "title_es": "Julio",
        "title_ru": "Июль",
        "control_type": "CheckBox",
    }
    june = {
        "title_en": "June",
        "title_es": "Junio",
        "title_ru": "Июнь",
        "control_type": "CheckBox",
    }
    may = {
        "title_en": "May",
        "title_es": "Mayo",
        "title_ru": "Май",
        "control_type": "CheckBox",
    }
    april = {
        "title_en": "April",
        "title_es": "Abríl",
        "title_ru": "Апрель",
        "control_type": "CheckBox",
    }
    december = {
        "title_en": "December",
        "title_es": "Diciembre",
        "title_ru": "Декабрь",
        "control_type": "CheckBox",
    }
    november = {
        "title_en": "November",
        "title_es": "Noviembre",
        "title_ru": "Ноябрь",
        "control_type": "CheckBox",
    }
    october = {
        "title_en": "October",
        "title_es": "Octubre",
        "title_ru": "Октябрь",
        "control_type": "CheckBox",
    }
    march = {
        "title_en": "March",
        "title_es": "Marzo",
        "title_ru": "Март",
        "control_type": "CheckBox",
    }
    february = {
        "title_en": "February",
        "title_es": "Febrero",
        "title_ru": "Февраль",
        "control_type": "CheckBox",
    }
    january = {
        "title_en": "January",
        "title_es": "Enero",
        "title_ru": "Январь",
        "control_type": "CheckBox",
    }
    or_radiobutton = {
        "title_en": "or",
        "title_es": "o",
        "title_ru": "или",
        "control_type": "RadioButton",
    }
    date_radiobutton = {
        "title_en": "Date",
        "title_es": "Fecha",
        "title_ru": "Число",
        "control_type": "RadioButton",
    }
    cancel_button7 = {
        "title_en": "Cancel",
        "title_es": "Cancelar",
        "title_ru": "Отмена",
        "found_index": 0,
        "control_type": "Button",
    }
    next_button4 = {
        "title_en": "Next >",
        "title_es": "Siguiente >",
        "title_ru": "Далее >",
        "control_type": "Button",
    }
    back_button5 = {
        "title_en": "< Back",
        "title_es": "< Volver",
        "title_ru": "< Назад",
        "control_type": "Button",
    }

    # Третье окно настройки расписания профилирования
    modifying_schedule6 = {
        "title_en": "Modifying schedule",
        "title_es": "Cambio de horario",
        "title_ru": "Изменение расписания",
        "control_type": "Window",
    }
    cancel_button8 = {
        "title_en": "Cancel",
        "title_es": "Cancelar",
        "title_ru": "Отмена",
        "found_index": 0,
        "control_type": "Button",
    }
    finish_button2 = {
        "title_en": "Finish",
        "title_es": "Finalizar",
        "title_ru": "Завершить",
        "control_type": "Button",
    }
    back_button6 = {
        "title_en": "< Back",
        "title_es": "< Volver",
        "title_ru": "< Назад",
        "control_type": "Button",
    }
