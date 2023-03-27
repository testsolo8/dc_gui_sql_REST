class ProfileCenterSettingsPage:
    # Кнопки
    setup_connection_to_db = {
        "title_eng": "Set up connection to DB ",
        "title_es": "Configurar conexión a base de datos",
        "title_rus": "Настроить подключение к БД",
        "control_type": "Button",
    }
    clear_database = {
        "title_eng": "Clear database",
        "title_es": "Borrar base de datos",
        "title_rus": "Очистить БД",
        "control_type": "Button",
    }
    start_profiling = {
        "title_eng": "Start profiling",
        "title_es": "Iniciar elaboración de perfiles",
        "title_rus": "Запустить профилирование",
        "control_type": "Button",
    }
    read_texts = {
        "title_eng": "Read texts",
        "title_es": "Leer textos",
        "title_rus": "Вычитать тексты",
        "control_type": "Button",
    }
    stop_server = {
        "title_eng": "Stop server",
        "title_es": "Detener servidor",
        "title_rus": "Остановить сервер",
        "control_type": "Button",
    }

    add = {
        "title_eng": "Add",
        "title_es": "Añadir",
        "title_rus": "Добавить",
        "control_type": "Button",
    }
    delete = {
        "title_eng": "Delete",
        "title_es": "Borrar",
        "title_rus": "Удалить",
        "control_type": "Button",
    }

    cancel_button = {
        "title_eng": "Cancel",
        "title_es": "Cancelar",
        "title_rus": "Отменить",
        "control_type": "Button",
    }
    apply_button = {
        "title_eng": "Apply",
        "title_es": "Aplicar",
        "title_rus": "Применить",
        "control_type": "Button",
    }
    edit_schedule_of_reading_button = "Button4"
    edit_schedule_of_profiling_button = "Button3"

    # Панели
    logging_of_server = {
        "title_eng": "Logging of server",
        "title_es": "Registro de servidor",
        "title_rus": "Логирование сервера",
        "control_type": "Pane",
    }
    connection_to_database = {
        "title_eng": "Connection to database",
        "title_es": "Conexión a la base de datos",
        "title_rus": "Подключение к БД",
        "control_type": "Pane",
    }
    control_of_services = {
        "title_eng": "Control of services",
        "title_es": "Control de servicios",
        "title_rus": "Управление службами",
        "control_type": "Pane",
    }
    schedules = {
        "title_eng": "Schedules",
        "title_es": "Horario",
        "title_rus": "Расписания",
        "control_type": "Pane",
    }
    schedule_of_profiling = {
        "title_eng": "Schedule of profiling",
        "title_es": "Horario de elaboración de perfiles",
        "title_rus": "Расписание профилирования",
        "control_type": "Pane",
    }
    schedule_of_reading = {
        "title_eng": "Schedule of reading",
        "title_es": "Horario de lectura",
        "title_rus": "Расписание вычитки",
        "control_type": "Pane",
    }

    data_for_profile_generation = {
        "title_eng": "Data for profile generation",
        "title_es": "Datos para cálculo de perfil",
        "title_rus": "Данные для расчета профиля",
        "control_type": "Pane",
    }

    failure_to_read_texts_from_index = {
        "title_eng": "Failure to read texts from index",
        "title_es": "Fracasó a leer textos del índice",
        "title_rus": "Неудачная вычитка текстов из индекса",
        "control_type": "Pane",
    }

    # Чекбоксы
    mail_outgoing_email_correspondence = {
        "title_eng": "Mail (outgoing e-mail correspondence)",
        "title_es": "mail (correos electrónicos salientes)",
        "title_rus": "mail (исходящая почтовая переписка)",
        "control_type": "CheckBox",
    }
    im_outgoing_messages_in_im_clients_and_on_social_networks = {
        "title_eng": "IM (outgoing messages in IM clients and on social networks)",
        "title_es": "im (mensajes salientes en clientes IM y en redes sociales)",
        "title_rus": "im (исходящие сообщения в IM-клиентах и в социальных сетях)",
        "control_type": "CheckBox",
    }
    skype_outgoing_messages_on_skype_lync_viber_telegram_and_whatsapp = {
        "title_eng": "Skype (outgoing messages on Skype, Lync, Viber, Telegram, and WhatsApp)",
        "title_es": "skype (mensajes salientes en Skype, Lync, Viber, Telegram, WhatsApp)",
        "title_rus": "skype (исходящие сообщения Skype, Lync, Viber, Telegram, WhatsApp)",
        "control_type": "CheckBox",
    }

    automatically_repeat_reading_in_case_of_failure = {
        "title_eng": "Automatically repeat reading in case of failure",
        "title_es": "Intentar lectura automáticamente si hay fracaso",
        "title_rus": "Автоматически повторять вычитку в случае неудачи",
        "control_type": "CheckBox",
    }

    # Окно настройки подключения к БД
    sql_server_connection_settings = {
        "title_eng": "SQL Server connection settings",
        "title_es": "Parámetros de conexión a SQL Server",
        "title_rus": "Параметры подключения к SQL Server",
        "control_type": "Window",
    }
    create_button = {
        "title_eng": "Create",
        "title_es": "Crear",
        "title_rus": "Создать",
        "control_type": "Button",
    }
    database_name = {
        "title_eng": "Database name:",
        "title_es": "Nombre de base de datos:",
        "title_rus": "Имя базы данных:",
        "control_type": "Pane",
    }
    password = {
        "title_eng": "Password:",
        "title_es": "Contraseña:",
        "title_rus": "Пароль:",
        "control_type": "Pane",
    }
    username = {
        "title_eng": "Username:",
        "title_es": "Nombre de usuario:",
        "title_rus": "Имя пользователя:",
        "control_type": "Pane",
    }
    sql_server_authentication_mode = {
        "title_eng": "SQL Server Authentication mode",
        "title_es": "Usar autenticación de SQL Server interna",
        "title_rus": "Использовать внутреннюю аутентификацию SQL Server",
        "control_type": "RadioButton",
    }
    windows_authentication_mode = {
        "title_eng": "Windows Authentication mode",
        "title_es": "Usar autenticación Windows",
        "title_rus": "Использовать аутентификацию Windows",
        "control_type": "RadioButton",
    }
    read_from_dc = {
        "title_eng": "Read from DC",
        "title_es": "Leer de DC",
        "title_rus": "Считать из DC",
        "control_type": "Button",
    }
    server_name = {
        "title_eng": "Server name:",
        "title_es": "Nombre del servidor",
        "title_rus": "Имя сервера:",
        "control_type": "Pane",
    }
    server_type = {
        "title_eng": "Server type:",
        "title_es": "Tipo del servidor",
        "title_rus": "Тип сервера:",
        "control_type": "Pane",
    }
    cancel_button2 = {
        "title_eng": "Cancel",
        "title_es": "Cancelar",
        "title_rus": "Отменить",
        "found_index": 0,
        "control_type": "Button",
    }
    ok_button = {
        "title_eng": "OK",
        "title_es": "OK",
        "title_rus": "OK",
        "control_type": "Button",
    }
    check_connection = {
        "title_eng": "Check connection",
        "title_es": "Probar conexión ",
        "title_rus": "Проверка подключения",
        "control_type": "Button",
    }

    # Окно настройки расписания вычитки индексов
    modifying_schedule = {
        "title_eng": "Modifying schedule",
        "title_es": "Cambio de horario",
        "title_rus": "Изменение расписания",
        "control_type": "Window",
    }
    select_name = {
        "title_eng": "SelectName",
        "title_es": "SelectName",
        "title_rus": "SelectName",
        "control_type": "Pane",
    }
    schedule_is_enabled = {
        "title_eng": "The schedule is enabled",
        "title_es": "Horario está habilitado.",
        "title_rus": "Расписание включено",
        "control_type": "CheckBox",
    }
    custom = {
        "title_eng": "Custom",
        "title_es": "Customizado",
        "title_rus": "По настройке",
        "control_type": "RadioButton",
    }
    once = {
        "title_eng": "Once",
        "title_es": "Una vez",
        "title_rus": "Единовременно",
        "control_type": "RadioButton",
    }
    monthly = {
        "title_eng": "Monthly",
        "title_es": "Cada mes",
        "title_rus": "Ежемесячно",
        "control_type": "RadioButton",
    }
    weekly = {
        "title_eng": "Weekly",
        "title_es": "Cada semana",
        "title_rus": "Еженедельно",
        "control_type": "RadioButton",
    }
    daily = {
        "title_eng": "Daily",
        "title_es": "Cada día",
        "title_rus": "Ежедневно",
        "control_type": "RadioButton",
    }
    cancel_button3 = {
        "title_eng": "Cancel",
        "title_es": "Cancelar",
        "title_rus": "Отмена",
        "found_index": 0,
        "control_type": "Button",
    }
    next_button = {
        "title_eng": "Next >",
        "title_es": "Siguiente >",
        "title_rus": "Далее >",
        "control_type": "Button",
    }
    back_button = {
        "title_eng": "< Back",
        "title_es": "< Volver",
        "title_rus": "< Назад",
        "control_type": "Button",
    }

    # Второе окно настройки расписания вычитки индексов
    modifying_schedule2 = {
        "title_eng": "Modifying schedule",
        "title_es": "Cambio de horario",
        "title_rus": "Изменение расписания",
        "control_type": "Window",
    }
    repeat_every = {
        "title_eng": "repeat every",
        "title_es": "repetir cada",
        "title_rus": "повторять каждые",
        "control_type": "CheckBox",
    }
    workdays_only = {
        "title_eng": "Workdays only (Monday - Friday)",
        "title_es": "Considerar solo días de trabajo (Lu-Vie) ",
        "title_rus": "Считать только рабочие дни(Пн-Пт)",
        "control_type": "CheckBox",
    }
    every = {
        "title_eng": "Every",
        "title_es": "Cad.",
        "title_rus": "Кажд.",
        "control_type": "RadioButton",
    }
    on_workdays = {
        "title_eng": "On workdays",
        "title_es": "En días de trabajo",
        "title_rus": "По рабочим дням",
        "control_type": "RadioButton",
    }
    daily2 = {
        "title_eng": "Daily",
        "title_es": "Cada día",
        "title_rus": "Ежедневно",
        "control_type": "RadioButton",
    }
    cancel_button4 = {
        "title_eng": "Cancel",
        "title_es": "Cancelar",
        "title_rus": "Отмена",
        "found_index": 0,
        "control_type": "Button",
    }
    next_button2 = {
        "title_eng": "Next >",
        "title_es": "Siguiente >",
        "title_rus": "Далее >",
        "control_type": "Button",
    }
    back_button2 = {
        "title_eng": "< Back",
        "title_es": "< Volver",
        "title_rus": "< Назад",
        "control_type": "Button",
    }

    # Третье окно настройки расписания вычитки индексов
    modifying_schedule3 = {
        "title_eng": "Modifying schedule",
        "title_es": "Cambio de horario",
        "title_rus": "Изменение расписания",
        "control_type": "Window",
    }
    cancel_button5 = {
        "title_eng": "Cancel",
        "title_es": "Cancelar",
        "title_rus": "Отмена",
        "found_index": 0,
        "control_type": "Button",
    }
    finish_button = {
        "title_eng": "Finish",
        "title_es": "Finalizar",
        "title_rus": "Завершить",
        "control_type": "Button",
    }
    back_button3 = {
        "title_eng": "< Back",
        "title_es": "< Volver",
        "title_rus": "< Назад",
        "control_type": "Button",
    }

    # Окно настройки расписания профилирования
    modifying_schedule4 = {
        "title_eng": "Modifying schedule",
        "title_es": "Cambio de horario",
        "title_rus": "Изменение расписания",
        "control_type": "Window",
    }
    schedule_is_enabled2 = {
        "title_eng": "The schedule is enabled",
        "title_es": "Horario está habilitado.",
        "title_rus": "Расписание включено",
        "control_type": "CheckBox",
    }
    custom2 = {
        "title_eng": "Custom",
        "title_es": "Customizado",
        "title_rus": "По настройке",
        "control_type": "RadioButton",
    }
    once2 = {
        "title_eng": "Once",
        "title_es": "Una vez",
        "title_rus": "Единовременно",
        "control_type": "RadioButton",
    }
    monthly2 = {
        "title_eng": "Monthly",
        "title_es": "Cada mes",
        "title_rus": "Ежемесячно",
        "control_type": "RadioButton",
    }
    weekly2 = {
        "title_eng": "Weekly",
        "title_es": "Cada semana",
        "title_rus": "Еженедельно",
        "control_type": "RadioButton",
    }
    daily3 = {
        "title_eng": "Daily",
        "title_es": "Cada día",
        "title_rus": "Ежедневно",
        "control_type": "RadioButton",
    }
    cancel_button6 = {
        "title_eng": "Cancel",
        "title_es": "Cancelar",
        "title_rus": "Отмена",
        "found_index": 0,
        "control_type": "Button",
    }
    next_button3 = {
        "title_eng": "Next >",
        "title_es": "Siguiente >",
        "title_rus": "Далее >",
        "control_type": "Button",
    }
    back_button4 = {
        "title_eng": "< Back",
        "title_es": "< Volver",
        "title_rus": "< Назад",
        "control_type": "Button",
    }

    # Второе окно настройки расписания профилирования
    modifying_schedule5 = {
        "title_eng": "Modifying schedule",
        "title_es": "Cambio de horario",
        "title_rus": "Изменение расписания",
        "control_type": "Window",
    }
    september = {
        "title_eng": "September",
        "title_es": "Septiembre",
        "title_rus": "Сентябрь",
        "control_type": "CheckBox",
    }
    august = {
        "title_eng": "August",
        "title_es": "Agosto",
        "title_rus": "Август",
        "control_type": "CheckBox",
    }
    july = {
        "title_eng": "July",
        "title_es": "Julio",
        "title_rus": "Июль",
        "control_type": "CheckBox",
    }
    june = {
        "title_eng": "June",
        "title_es": "Junio",
        "title_rus": "Июнь",
        "control_type": "CheckBox",
    }
    may = {
        "title_eng": "May",
        "title_es": "Mayo",
        "title_rus": "Май",
        "control_type": "CheckBox",
    }
    april = {
        "title_eng": "April",
        "title_es": "Abríl",
        "title_rus": "Апрель",
        "control_type": "CheckBox",
    }
    december = {
        "title_eng": "December",
        "title_es": "Diciembre",
        "title_rus": "Декабрь",
        "control_type": "CheckBox",
    }
    november = {
        "title_eng": "November",
        "title_es": "Noviembre",
        "title_rus": "Ноябрь",
        "control_type": "CheckBox",
    }
    october = {
        "title_eng": "October",
        "title_es": "Octubre",
        "title_rus": "Октябрь",
        "control_type": "CheckBox",
    }
    march = {
        "title_eng": "March",
        "title_es": "Marzo",
        "title_rus": "Март",
        "control_type": "CheckBox",
    }
    february = {
        "title_eng": "February",
        "title_es": "Febrero",
        "title_rus": "Февраль",
        "control_type": "CheckBox",
    }
    january = {
        "title_eng": "January",
        "title_es": "Enero",
        "title_rus": "Январь",
        "control_type": "CheckBox",
    }
    or_radiobutton = {
        "title_eng": "or",
        "title_es": "o",
        "title_rus": "или",
        "control_type": "RadioButton",
    }
    date_radiobutton = {
        "title_eng": "Date",
        "title_es": "Fecha",
        "title_rus": "Число",
        "control_type": "RadioButton",
    }
    cancel_button7 = {
        "title_eng": "Cancel",
        "title_es": "Cancelar",
        "title_rus": "Отмена",
        "found_index": 0,
        "control_type": "Button",
    }
    next_button4 = {
        "title_eng": "Next >",
        "title_es": "Siguiente >",
        "title_rus": "Далее >",
        "control_type": "Button",
    }
    back_button5 = {
        "title_eng": "< Back",
        "title_es": "< Volver",
        "title_rus": "< Назад",
        "control_type": "Button",
    }

    # Третье окно настройки расписания профилирования
    modifying_schedule6 = {
        "title_eng": "Modifying schedule",
        "title_es": "Cambio de horario",
        "title_rus": "Изменение расписания",
        "control_type": "Window",
    }
    cancel_button8 = {
        "title_eng": "Cancel",
        "title_es": "Cancelar",
        "title_rus": "Отмена",
        "found_index": 0,
        "control_type": "Button",
    }
    finish_button2 = {
        "title_eng": "Finish",
        "title_es": "Finalizar",
        "title_rus": "Завершить",
        "control_type": "Button",
    }
    back_button6 = {
        "title_eng": "< Back",
        "title_es": "< Volver",
        "title_rus": "< Назад",
        "control_type": "Button",
    }
