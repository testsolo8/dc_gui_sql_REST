class DataCenterServerPage:
    # Кнопки
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

    # Кнопки блока настройки пароля
    block_account = {
        "title_eng": "Block account",
        "title_es": "Bloquear la cuenta",
        "title_rus": "блокировать учетную запись",
        "control_type": "Button",
    }
    block_interface = {
        "title_eng": "Block interface for a minute",
        "title_es": "Bloquear interfaz por un minuto",
        "title_rus": "блокировать интерфейс на 1 минуту",
        "control_type": "Button",
    }

    # Панели
    use_tokens = {
        "title_eng": "Use tokens for secure user authentication",
        "title_es": "Usar tokens para autenticación segura de usuarios",
        "title_rus": "Использовать токены для защищенной аутентификации пользователей",
        "control_type": "Pane",
    }

    unmount_db_if = {
        "title_eng": "Unmount DB if DataCenter agent receives information about DB absence on the SQL server",
        "title_es": "Desmontar BD si el agente del DataCenter recibe información sobre la ausencia de la BD en el servidor SQL",
        "title_rus": "Демонтировать БД при получении данных об ее отсутствии на сервере SQL от агента DataCenter",
        "control_type": "Pane",
    }

    mail_notif_lan = {
        "title_eng": "E-mail notifications language",
        "title_es": "Idioma de notificaciones por e-mail",
        "title_rus": "Язык почтовых уведомлений",
        "control_type": "Pane",
    }
    log_level = {
        "title_eng": "Log level",
        "title_es": "Nivel de registro",
        "title_rus": "Логирование",
        "control_type": "Pane",
    }
    automatic_update_agents = {
        "title_eng": "Automatic update of agents on remote servers",
        "title_es": "Actualización automática de agentes en servidores remotos",
        "title_rus": "Автоматическое обновление агентов на удаленных серверах",
        "control_type": "Pane",
    }

    # Панели блока настройки пароля
    setup_acc_pass = {
        "title_eng": "Set up account passwords",
        "title_es": "Configurar contraseñas para cuentas",
        "title_rus": "Настройка паролей для учетных записей",
        "control_type": "Pane",
    }
    failed_attempts = {
        "title_eng": "After 3 failed attempts to enter password:",
        "title_es": "Después de 3 intentos fracasados de entrar contraseña:",
        "title_rus": "После 3-х неудачных попыток ввода пароля:",
        "control_type": "Pane",
    }
    special_characters = {
        "title_eng": "Special characters",
        "title_es": "Carácteres especiales",
        "title_rus": "спецсимволы",
        "control_type": "Pane",
    }
    lower_upper_cases = {
        "title_eng": "Lower and upper cases",
        "title_es": "Minúsculas y mayúsculas",
        "title_rus": "разный регистр",
        "control_type": "Pane",
    }
    letters_figures = {
        "title_eng": "Letters and figures",
        "title_es": "Letras y cifras",
        "title_rus": "буквы и цифры",
        "control_type": "Pane",
    }
    password_contain = {
        "title_eng": "Password must contain:",
        "title_es": "La contraseña debe contener:",
        "title_rus": "Пароль должен содержать:",
        "control_type": "Pane",
    }
    minimum_characters = {
        "title_eng": "Minimum length, characters",
        "title_es": "Longitud mínima, carácteres",
        "title_rus": "Минимальная длина, символов:",
        "control_type": "Pane",
    }

    # Панели блока настройки критериев оповещений
    notify_if = {
        "title_eng": "Notify if:",
        "title_es": "Notificar si:",
        "title_rus": "Критерии оповещений:",
        "control_type": "Pane",
    }
    pcap = {
        "title_eng": "PCAP (saved traffic) files are over",
        "title_es": "Archivos de tráfico guardado están más de",
        "title_rus": "Файлы сохраненного трафика больше",
        "control_type": "Pane",
    }
    free_space_on_local_drive = {
        "title_eng": "Free space on local drive is less than  ",
        "title_es": "Espacio libre en el disco local está menos de",
        "title_rus": "Свободное место на локальном диске меньше ",
        "control_type": "Pane",
    }
    performance_logs = {
        "title_eng": "Performance logs are over",
        "title_es": "Registro de rendimiento está más de ",
        "title_rus": "Файлы журнала производительности больше",
        "control_type": "Pane",
    }
    operation_logs = {
        "title_eng": "Operation logs are over",
        "title_es": "Registro de operación está más de",
        "title_rus": "Файлы журналирования больше",
        "control_type": "Pane",
    }
