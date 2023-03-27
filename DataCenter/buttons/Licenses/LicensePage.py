class LicensePage:
    class MainWindow:
        # Кнопки главной страницы License
        refresh_button = {
            "title_eng": "Refresh",
            "title_es": "Actualizar",
            "title_rus": "Обновить",
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
        # Панели главной страницы
        registered_to = {
            "title_eng": "Registered to:",
            "title_es": "Registrado en:",
            "title_rus": "Зарегистрировано на:",
            "control_type": "Pane",
        }
        technical_support = {
            "title_eng": "Technical support is provided up to:",
            "title_es": "Soporte técnico hasta",
            "title_rus": "Техническая поддержка до:",
            "control_type": "Pane",
        }
        id_license_key = {
            "title_eng": "ID of license key:",
            "title_es": "ID de clave de licencia",
            "title_rus": "Идентификатор лицензионного ключа:",
            "control_type": "Pane",
        }

    class UpdateLicenseWindow:
        # Кнопки страницы обновления лицензии
        from_file_button = {
            "title_eng": "From file",
            "title_es": "Del archivo",
            "title_rus": "Из файла",
            "control_type": "Button",
        }
        cancel_button = {
            "title_eng": "Cancel",
            "title_es": "Cancelar",
            "title_rus": "Отменить",
            "found_index": 0,
            "control_type": "Button",
        }
        apply_button = {
            "title_eng": "Apply",
            "title_es": "Aplicar",
            "title_rus": "Подтвердить",
            "found_index": 0,
            "control_type": "Button",
        }
        paste_from_clipboard_button = {
            "title_eng": "Paste from clipboard",
            "title_es": "Del portapapales",
            "title_rus": "Из буфера обмена",
            "control_type": "Button",
        }
        close_button = "Button5"
        # Заголовок окна
        window_header = {
            "title_eng": "DataCenter registration window",
            "title_es": "Entrada de licencia de DataCenter",
            "title_rus": "DataCenter ввод лицензии",
            "control_type": "Window",
        }

    class DistributeAutomaticallyWindow:
        # Кнопки страницы автоматического распределения лицензий
        no_button = {
            "title_eng": "No",
            "title_es": "No",
            "title_rus": "Нет",
            "control_type": "Button",
        }
        yes_button = {
            "title_eng": "Yes",
            "title_es": "Sí",
            "title_rus": "Да",
            "control_type": "Button",
        }
        close_button = "Button3"
        # Заголовок окна
        window_header = {
            "title_eng": "Confirm",
            "title_es": "Confirmación ",
            "title_rus": "Подтверждение",
            "control_type": "Window",
        }

    class StatisticsWindow:
        # Кнопки страницы статистики лицензирования
        export_button = {
            "title_eng": "Export",
            "title_es": "Exportar",
            "title_rus": "Экспорт",
            "control_type": "Button",
        }
        licenses_by_users_button = {
            "title_eng": "Licenses by users",
            "title_es": "Licencias por usuarios",
            "title_rus": "Лицензии по пользователям",
            "control_type": "Button",
        }
        days_button = {
            "title_eng": "days",
            "title_es": "días",
            "title_rus": "дням",
            "control_type": "Button",
        }
        months_button = {
            "title_eng": "months",
            "title_es": "meses",
            "title_rus": "месяцам",
            "control_type": "Button",
        }
        by_components_radiobutton = {
            "title_eng": "By components",
            "title_es": "Por componentes",
            "title_rus": "По компонентам",
            "control_type": "Button",
        }
        by_dc_agents_radiobutton = {
            "title_eng": "By DC agents",
            "title_es": "Por agentes de DC",
            "title_rus": "По агентам DC",
            "control_type": "Button",
        }
        apply_button = {
            "title_eng": "Apply",
            "title_es": "Aplicar",
            "title_rus": "Применить",
            "found_index": 0,
            "control_type": "Button",
        }
        close_button = "Button11"
        # Панели страницы статистики лицензирования
        details_by_pane = {
            "title_eng": "Details by: ",
            "title_es": "Detalles por: ",
            "title_rus": "Детализация по: ",
            "control_type": "Pane",
        }
        first_calendar_value = "Pane14"
        second_calendar_value = "Pane12"
        till_pane = {
            "title_eng": "till",
            "title_es": "a",
            "title_rus": "по",
            "control_type": "Pane",
        }
        from_pane = {
            "title_eng": "from",
            "title_es": "desde",
            "title_rus": "c",
            "control_type": "Pane",
        }
        # заголовок окна
        window_header = {
            "title_eng": "Statistics of licenses distribution",
            "title_es": "Estadística de distribución de licencias",
            "title_rus": "Статистика распределения лицензий",
            "control_type": "Window",
        }
