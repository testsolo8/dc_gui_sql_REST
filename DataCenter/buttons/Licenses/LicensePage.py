class LicensePage:
    class MainWindow:
        # Кнопки главной страницы License
        refresh_button = {
            "title_en": "Refresh",
            "title_es": "Actualizar",
            "title_ru": "Обновить",
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
        # Панели главной страницы
        registered_to = {
            "title_en": "Registered to:",
            "title_es": "Registrado en:",
            "title_ru": "Зарегистрировано на:",
            "control_type": "Pane",
        }
        technical_support = {
            "title_en": "Technical support is provided up to:",
            "title_es": "Soporte técnico hasta",
            "title_ru": "Техническая поддержка до:",
            "control_type": "Pane",
        }
        id_license_key = {
            "title_en": "ID of license key:",
            "title_es": "ID de clave de licencia",
            "title_ru": "Идентификатор лицензионного ключа:",
            "control_type": "Pane",
        }

    class UpdateLicenseWindow:
        # Кнопки страницы обновления лицензии
        from_file_button = {
            "title_en": "From file",
            "title_es": "Del archivo",
            "title_ru": "Из файла",
            "control_type": "Button",
        }
        cancel_button = {
            "title_en": "Cancel",
            "title_es": "Cancelar",
            "title_ru": "Отменить",
            "found_index": 0,
            "control_type": "Button",
        }
        apply_button = {
            "title_en": "Apply",
            "title_es": "Aplicar",
            "title_ru": "Подтвердить",
            "found_index": 0,
            "control_type": "Button",
        }
        paste_from_clipboard_button = {
            "title_en": "Paste from clipboard",
            "title_es": "Del portapapales",
            "title_ru": "Из буфера обмена",
            "control_type": "Button",
        }
        close_button = "Button5"
        # Заголовок окна
        window_header = {
            "title_en": "DataCenter registration window",
            "title_es": "Entrada de licencia de DataCenter",
            "title_ru": "DataCenter ввод лицензии",
            "control_type": "Window",
        }

    class DistributeAutomaticallyWindow:
        # Кнопки страницы автоматического распределения лицензий
        no_button = {
            "title_en": "No",
            "title_es": "No",
            "title_ru": "Нет",
            "control_type": "Button",
        }
        yes_button = {
            "title_en": "Yes",
            "title_es": "Sí",
            "title_ru": "Да",
            "control_type": "Button",
        }
        close_button = "Button3"
        # Заголовок окна
        window_header = {
            "title_en": "Confirm",
            "title_es": "Confirmación ",
            "title_ru": "Подтверждение",
            "control_type": "Window",
        }

    class StatisticsWindow:
        # Кнопки страницы статистики лицензирования
        export_button = {
            "title_en": "Export",
            "title_es": "Exportar",
            "title_ru": "Экспорт",
            "control_type": "Button",
        }
        licenses_by_users_button = {
            "title_en": "Licenses by users",
            "title_es": "Licencias por usuarios",
            "title_ru": "Лицензии по пользователям",
            "control_type": "Button",
        }
        days_button = {
            "title_en": "days",
            "title_es": "días",
            "title_ru": "дням",
            "control_type": "Button",
        }
        months_button = {
            "title_en": "months",
            "title_es": "meses",
            "title_ru": "месяцам",
            "control_type": "Button",
        }
        by_components_radiobutton = {
            "title_en": "By components",
            "title_es": "Por componentes",
            "title_ru": "По компонентам",
            "control_type": "Button",
        }
        by_dc_agents_radiobutton = {
            "title_en": "By DC agents",
            "title_es": "Por agentes de DC",
            "title_ru": "По агентам DC",
            "control_type": "Button",
        }
        apply_button = {
            "title_en": "Apply",
            "title_es": "Aplicar",
            "title_ru": "Применить",
            "found_index": 0,
            "control_type": "Button",
        }
        close_button = "Button11"
        # Панели страницы статистики лицензирования
        details_by_pane = {
            "title_en": "Details by: ",
            "title_es": "Detalles por: ",
            "title_ru": "Детализация по: ",
            "control_type": "Pane",
        }
        first_calendar_value = "Pane14"
        second_calendar_value = "Pane12"
        till_pane = {
            "title_en": "till",
            "title_es": "a",
            "title_ru": "по",
            "control_type": "Pane",
        }
        from_pane = {
            "title_en": "from",
            "title_es": "desde",
            "title_ru": "c",
            "control_type": "Pane",
        }
        # заголовок окна
        window_header = {
            "title_en": "Statistics of licenses distribution",
            "title_es": "Estadística de distribución de licencias",
            "title_ru": "Статистика распределения лицензий",
            "control_type": "Window",
        }
