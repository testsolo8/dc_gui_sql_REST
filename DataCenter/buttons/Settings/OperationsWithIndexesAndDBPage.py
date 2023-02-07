class OperationsWithIndexesAndDBPage:
    # Кнопки
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
    export_button = {
        "title_en": "Export",
        "title_es": "Exportar",
        "title_ru": "Экспорт",
        "control_type": "Button",
    }
    import_button = {
        "title_en": "Import",
        "title_es": "Importar",
        "title_ru": "Импорт",
        "control_type": "Button",
    }

    # Панель места хранения бд
    location_of_databases = {
        "title_en": "Location of databases",
        "title_es": "Ubicación de bases de datos",
        "title_ru": "Место хранения баз данных",
        "control_type": "Pane",
    }

    # Кнопки места хранения бд
    inherit_databases_original = {
        "title_en": "Inherit databases creation paths from the original (split) database",
        "title_es": "Heredar rutas de creación de bases de datos desde la BD original (dividida)",
        "title_ru": "использовать пути создания баз данных от исходной (разбиваемой) базы данных",
        "control_type": "Button",
    }
    inherit_databases_mssql = {
        "title_en": "Inherit databases creation paths from the MS SQL Server settings",
        "title_es": "Heredar rutas de creación de bases de datos desde los ajustes del MS SQL Server",
        "title_ru": "наследовать пути создания баз данных из настроек MS SQL сервера",
        "control_type": "Button",
    }

    # Панель параметров контроля индекса
    weekdays_only = {
        "title_en": "weekdays only",
        "title_es": "solo días de trabajo",
        "title_ru": "кроме выходных",
        "control_type": "Pane",
    }
    control_new_data = {
        "title_en": "Control new data received in index in the time period from ",
        "title_es": "Controlar datos nuevos recibidos en índice en el período de tiempo de",
        "title_ru": "Контролировать поступление информации в индексы в промежутке времени с",
        "control_type": "Pane",
    }
    delete_indexes_available_for_search = {
        "title_en": "Delete indexes available for search",
        "title_es": "Borrar índices disponibles para búsqueda",
        "title_ru": "Разрешить удалять доступные для поиска индексы",
        "control_type": "Pane",
    }
    automatically_delete_indexes = {
        "title_en": "Automatically delete indexes unavailable for search if the following conditions are met:",
        "title_es": "Automáticamente borrar índices no disponibles para búsqueda al cumplir algunas de condiciones",
        "title_ru": "Автоматически удалять недоступные для поиска индексы по достижении условий:",
        "control_type": "Pane",
    }
    add_suffix_index_filename = {
        "title_en": "Add a suffix to index file name",
        "title_es": "Añadir sufijo a nombre de índice",
        "title_ru": "Добавлять суффикс к имени индекса",
        "control_type": "Pane",
    }
    create_index_in_new_folder = {
        "title_en": "Create index in a new folder",
        "title_es": "Crear índice en carpeta nueva",
        "title_ru": "Создавать новую  папку для индекса",
        "control_type": "Pane",
    }
    index_size_over = {
        "title_en": "Index size over (GB)",
        "title_es": "Tamaño de índice es más de (GB)",
        "title_ru": "Размер индекса более (Гб)",
        "control_type": "Pane",
    }
    text_size = {
        "title_en": "Text size (GB)",
        "title_es": "Tamaño de texto en índice (GB)",
        "title_ru": "Размер текстов в индексе (Гб)",
        "control_type": "Pane",
    }
    on_schedule = {
        "title_en": "On schedule",
        "title_es": "Dividir según horario",
        "title_ru": "Разбивать по расписанию",
        "control_type": "Pane",
    }
    scheduler = {
        "title_en": "Scheduler...",
        "title_es": "Configurar...",
        "title_ru": "Настроить...",
        "control_type": "Pane",
    }
    number_of_documents = {
        "title_en": "Number of documents (MIO)",
        "title_es": "Número de documentos (millón)",
        "title_ru": "Кол-во документов (млн. шт.)",
        "control_type": "Pane",
    }
    documents_size = {
        "title_en": "Documents size (GB)",
        "title_es": "Tamaño de documentos (GB)",
        "title_ru": "Размер документов (Гб)",
        "control_type": "Pane",
    }
    index_older_than = {
        "title_en": "Index older than (days)",
        "title_es": "Índice es más antiguo de (días)",
        "title_ru": "Индекс старше (дней)",
        "control_type": "Pane",
    }
    number_of_db_records = {
        "title_en": "Number of DB records (MIO)",
        "title_es": "Número de registros en BD (millón)",
        "title_ru": "Кол-во записей в БД (млн. шт.)",
        "control_type": "Pane",
    }
    db_data_size = {
        "title_en": "DB data size (GB)",
        "title_es": "Tamaño de datos en BD (GB)",
        "title_ru": "Размер данных в БД (Гб)",
        "control_type": "Pane",
    }
    number_of_unique_words = {
        "title_en": "Number of unique words (MIO)",
        "title_es": "Número de palabras únicas (millón)",
        "title_ru": "Кол-во уникальных слов (млн. шт.)",
        "control_type": "Pane",
    }
    only_in_time_period = {
        "title_en": "only in the time period from ",
        "title_es": "solo en el período de tiempo desde",
        "title_ru": "только в промежутке времени с",
        "control_type": "Pane",
    }
    automatically_create_indexes = {
        "title_en": "Automatically create indexes if any of the following conditions are met:",
        "title_es": "Automáticamente crear índices al cumplir algunas de condiciones ",
        "title_ru": "Автоматически создавать индексы по достижении условий:",
        "control_type": "Pane",
    }
