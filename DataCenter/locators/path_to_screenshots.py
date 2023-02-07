from DataCenter.tools.get_project_root import get_project_root
from pathlib import Path

start_path_en = str(Path(get_project_root(), "pytest_DataCenter_functional", "test_gui", "EngVersionDCTest", "Screenshot Test"))
start_path_es = str(Path(get_project_root(), "pytest_DataCenter_functional", "test_gui", "EspVersionDCTest", "Screenshot Test"))
start_path_ru = str(Path(get_project_root(), "pytest_DataCenter_functional", "test_gui", "RusVersionDCTest", "Screenshot Test"))


class PathToScreenshotsEN:
    # Закладка управления
    management_page_synchronization_with_active_directory_window = {
        "path": start_path_en
        + r"\Management\Screenshots\ManagementPage_SynchronizationWithActiveDirectoryWindow.png"
    }

    # Закладка лицензий
    licenses_page = {"path": start_path_en + r"\Licenses\Screenshots\LicensePage.png"}
    license_page_distribute_automatically_window = {
        "path": start_path_en
        + r"\Licenses\Screenshots\LicensePage_DistributeAutomaticallyWindow.png"
    }
    license_page_statistics_window = {
        "path": start_path_en
        + r"\Licenses\Screenshots\LicensePage_StatisticsWindow.png"
    }
    license_page_update_license_window = {
        "path": start_path_en
        + r"\Licenses\Screenshots\LicensePage_UpdateLicenseWindow.png"
    }

    # Закладка настроек
    data_center_server = {
        "path": start_path_en + r"\Settings\Screenshots\DataCenterServer.png"
    }

    default_database = {
        "path": start_path_en + r"\Settings\Screenshots\DefaultDatabase.png"
    }
    default_database_add_server_window = {
        "path": start_path_en
        + r"\Settings\Screenshots\DefaultDatabase_AddServerWindow.png"
    }
    default_database_delete_server_window = {
        "path": start_path_en
        + r"\Settings\Screenshots\DefaultDatabase_DeleteServerWindow.png"
    }
    default_database_edit_server_window = {
        "path": start_path_en
        + r"\Settings\Screenshots\DefaultDatabase_EditServerWindow.png"
    }

    agents_and_components = {
        "path": start_path_en + r"\Settings\Screenshots\AgentsAndComponents.png"
    }
    agents_and_components_change_mail_window = {
        "path": start_path_en
        + r"\Settings\Screenshots\AgentsAndComponents_ChangeMailWindow.png"
    }
    agents_and_components_free_disk_space_monitoring_window = {
        "path": start_path_en
        + r"\Settings\Screenshots\AgentsAndComponents_FreeDiskSpaceMonitoringWindow.png"
    }

    operations_with_indexes_and_db = {
        "path": start_path_en + r"\Settings\Screenshots\OperationsWithIndexesAndDB.png"
    }

    active_directory = {
        "path": start_path_en + r"\Settings\Screenshots\ActiveDirectory.png"
    }
    active_directory_active_directory_add_domain = {
        "path": start_path_en + r"\Settings\Screenshots\ActiveDirectoryAddDomain.png"
    }
    active_directory_active_directory_add_internal_user = {
        "path": start_path_en
        + r"\Settings\Screenshots\ActiveDirectoryAddInternalUser.png"
    }
    active_directory_active_directory_add_workgroup_user = {
        "path": start_path_en
        + r"\Settings\Screenshots\ActiveDirectoryAddWorkgroupUser.png"
    }
    active_directory_active_directory_sql_connection_settings = {
        "path": start_path_en
        + r"\Settings\Screenshots\ActiveDirectorySQLConnectionSettings.png"
    }

    access_rights = {"path": start_path_en + r"\Settings\Screenshots\AccessRights.png"}
    email_notifications = {
        "path": start_path_en + r"\Settings\Screenshots\EmailNotifications.png"
    }
    telegram_notifications = {
        "path": start_path_en + r"\Settings\Screenshots\TelegramNotifications.png"
    }

    # Закладка дополнительных настроек
    operation_logging = {
        "path": start_path_en
        + r"\Additional features\Screenshots\OperationsLoggingPage.png"
    }
    components_update = {
        "path": start_path_en
        + r"\Additional features\Screenshots\ComponentsUpdatePage.png"
    }
    digital_fingerprints = {
        "path": start_path_en
        + r"\Additional features\Screenshots\DigitalFingerprintsPage.png"
    }
    components_settings = {
        "path": start_path_en
        + r"\Additional features\Screenshots\ComponentsSettingsPage.png"
    }

    db_backup_and_migration = {
        "path": start_path_en
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage.png"
    }
    db_backup_and_migration_add_new_migration_db_rule_window = {
        "path": start_path_en
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewMigrationDBRuleWindow.png"
    }

    db_backup_and_migration_add_new_backup_db_rule_window = {
        "path": start_path_en
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewBackupDBRuleWindow.png"
    }

    db_backup_and_migration_add_new_migration_index_rule_window = {
        "path": start_path_en
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewMigrationIndexRuleWindow.png"
    }

    db_backup_and_migration_add_new_backup_index_rule_window = {
        "path": start_path_en
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewBackupIndexRuleWindow.png"
    }

    db_backup_and_migration_add_new_migration_storage_rule_window = {
        "path": start_path_en
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewMigrationStorageRuleWindow.png"
    }

    db_backup_and_migration_add_new_backup_storage_rule_window = {
        "path": start_path_en
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewBackupStorageRuleWindow.png"
    }

    user_cards = {
        "path": start_path_en + r"\Additional features\Screenshots\UserCardsPage.png"
    }
    user_cards_confirm_clear_db = {
        "path": start_path_en
        + r"\Additional features\Screenshots\UserCardsPage_ConfirmClearDB.png"
    }

    task_management = {
        "path": start_path_en
        + r"\Additional features\Screenshots\TaskManagementPage.png"
    }
    task_management_sql_server_connection_setting_window = {
        "path": start_path_en
        + r"\Additional features\Screenshots\TaskManagementPage_SQLServerConnectionSettingWindow.png"
    }

    attributes_storage = {
        "path": start_path_en
        + r"\Additional features\Screenshots\AttributesStoragePage.png"
    }

    RVisionGosSOPKA = {
        "path": start_path_en
        + r"\Additional features\Screenshots\RVisionGosSOPKAPage.png"
    }

    RVisionGosSOPKAPage_add_controlled_information_resources = {
        "path": start_path_en
        + r"\Additional features\Screenshots\RVisionGosSOPKAPage_AddControlledInformationResources.png"
    }

    outlook_calendars = {
        "path": start_path_en
        + r"\Additional features\Screenshots\OutlookCalendarsPage.png"
    }

    profile_center_settings = {
        "path": start_path_en
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage.png"
    }
    profile_center_settings_sql_server_connection_setting_window = {
        "path": start_path_en
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_SQLServerConnectionSettingWindow.png"
    }
    profile_schedule_of_reading_window = {
        "path": start_path_en
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfReadingWindow.png"
    }
    profile_schedule_of_reading_second_window = {
        "path": start_path_en
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfReadingSecondWindow.png"
    }
    profile_schedule_of_reading_third_window = {
        "path": start_path_en
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfReadingThirdWindow.png"
    }
    profile_schedule_of_profiling_window = {
        "path": start_path_en
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfProfilingWindow.png"
    }
    profile_schedule_of_profiling_second_window = {
        "path": start_path_en
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfProfilingSecondWindow.png"
    }
    profile_schedule_of_profiling_third_window = {
        "path": start_path_en
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfProfilingThirdWindow.png"
    }


class PathToScreenshotsES:
    # Закладка управления
    management_page_synchronization_with_active_directory_window = {
        "path": start_path_es
        + r"\Management\Screenshots\ManagementPage_SynchronizationWithActiveDirectoryWindow.png"
    }

    # Закладка лицензий
    licenses_page = {"path": start_path_es + r"\Licenses\Screenshots\LicensePage.png"}
    license_page_distribute_automatically_window = {
        "path": start_path_es
        + r"\Licenses\Screenshots\LicensePage_DistributeAutomaticallyWindow.png"
    }
    license_page_statistics_window = {
        "path": start_path_es
        + r"\Licenses\Screenshots\LicensePage_StatisticsWindow.png"
    }
    license_page_update_license_window = {
        "path": start_path_es
        + r"\Licenses\Screenshots\LicensePage_UpdateLicenseWindow.png"
    }

    # Закладка настроек
    data_center_server = {
        "path": start_path_es + r"\Settings\Screenshots\DataCenterServer.png"
    }

    default_database = {
        "path": start_path_es + r"\Settings\Screenshots\DefaultDatabase.png"
    }
    default_database_add_server_window = {
        "path": start_path_es
        + r"\Settings\Screenshots\DefaultDatabase_AddServerWindow.png"
    }
    default_database_delete_server_window = {
        "path": start_path_es
        + r"\Settings\Screenshots\DefaultDatabase_DeleteServerWindow.png"
    }
    default_database_edit_server_window = {
        "path": start_path_es
        + r"\Settings\Screenshots\DefaultDatabase_EditServerWindow.png"
    }

    agents_and_components = {
        "path": start_path_es + r"\Settings\Screenshots\AgentsAndComponents.png"
    }
    agents_and_components_change_mail_window = {
        "path": start_path_es
        + r"\Settings\Screenshots\AgentsAndComponents_ChangeMailWindow.png"
    }
    agents_and_components_free_disk_space_monitoring_window = {
        "path": start_path_es
        + r"\Settings\Screenshots\AgentsAndComponents_FreeDiskSpaceMonitoringWindow.png"
    }

    operations_with_indexes_and_db = {
        "path": start_path_es + r"\Settings\Screenshots\OperationsWithIndexesAndDB.png"
    }

    active_directory = {
        "path": start_path_es + r"\Settings\Screenshots\ActiveDirectory.png"
    }
    active_directory_active_directory_add_domain = {
        "path": start_path_es + r"\Settings\Screenshots\ActiveDirectoryAddDomain.png"
    }
    active_directory_active_directory_add_internal_user = {
        "path": start_path_es
        + r"\Settings\Screenshots\ActiveDirectoryAddInternalUser.png"
    }
    active_directory_active_directory_add_workgroup_user = {
        "path": start_path_es
        + r"\Settings\Screenshots\ActiveDirectoryAddWorkgroupUser.png"
    }
    active_directory_active_directory_sql_connection_settings = {
        "path": start_path_es
        + r"\Settings\Screenshots\ActiveDirectorySQLConnectionSettings.png"
    }

    access_rights = {"path": start_path_es + r"\Settings\Screenshots\AccessRights.png"}
    email_notifications = {
        "path": start_path_es + r"\Settings\Screenshots\EmailNotifications.png"
    }
    telegram_notifications = {
        "path": start_path_es + r"\Settings\Screenshots\TelegramNotifications.png"
    }

    # Закладка дополнительных настроек
    operation_logging = {
        "path": start_path_es
        + r"\Additional features\Screenshots\OperationsLoggingPage.png"
    }
    components_update = {
        "path": start_path_es
        + r"\Additional features\Screenshots\ComponentsUpdatePage.png"
    }
    digital_fingerprints = {
        "path": start_path_es
        + r"\Additional features\Screenshots\DigitalFingerprintsPage.png"
    }
    components_settings = {
        "path": start_path_es
        + r"\Additional features\Screenshots\ComponentsSettingsPage.png"
    }
    db_backup_and_migration = {
        "path": start_path_es
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage.png"
    }
    db_backup_and_migration_add_new_migration_db_rule_window = {
        "path": start_path_es
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewMigrationDBRuleWindow.png"
    }

    db_backup_and_migration_add_new_backup_db_rule_window = {
        "path": start_path_es
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewBackupDBRuleWindow.png"
    }

    db_backup_and_migration_add_new_migration_index_rule_window = {
        "path": start_path_es
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewMigrationIndexRuleWindow.png"
    }

    db_backup_and_migration_add_new_backup_index_rule_window = {
        "path": start_path_es
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewBackupIndexRuleWindow.png"
    }

    db_backup_and_migration_add_new_migration_storage_rule_window = {
        "path": start_path_es
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewMigrationStorageRuleWindow.png"
    }

    db_backup_and_migration_add_new_backup_storage_rule_window = {
        "path": start_path_es
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewBackupStorageRuleWindow.png"
    }

    user_cards = {
        "path": start_path_es + r"\Additional features\Screenshots\UserCardsPage.png"
    }
    user_cards_confirm_clear_db = {
        "path": start_path_es
        + r"\Additional features\Screenshots\UserCardsPage_ConfirmClearDB.png"
    }

    task_management = {
        "path": start_path_es
        + r"\Additional features\Screenshots\TaskManagementPage.png"
    }
    task_management_sql_server_connection_setting_window = {
        "path": start_path_es
        + r"\Additional features\Screenshots\TaskManagementPage_SQLServerConnectionSettingWindow.png"
    }
    attributes_storage = {
        "path": start_path_es
        + r"\Additional features\Screenshots\AttributesStoragePage.png"
    }

    RVisionGosSOPKA = {
        "path": start_path_es
        + r"\Additional features\Screenshots\RVisionGosSOPKAPage.png"
    }

    RVisionGosSOPKAPage_add_controlled_information_resources = {
        "path": start_path_es
        + r"\Additional features\Screenshots\RVisionGosSOPKAPage_AddControlledInformationResources.png"
    }

    outlook_calendars = {
        "path": start_path_es
        + r"\Additional features\Screenshots\OutlookCalendarsPage.png"
    }

    profile_center_settings = {
        "path": start_path_es
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage.png"
    }
    profile_center_settings_sql_server_connection_setting_window = {
        "path": start_path_es
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_SQLServerConnectionSettingWindow.png"
    }
    profile_schedule_of_reading_window = {
        "path": start_path_es
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfReadingWindow.png"
    }
    profile_schedule_of_reading_second_window = {
        "path": start_path_es
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfReadingSecondWindow.png"
    }
    profile_schedule_of_reading_third_window = {
        "path": start_path_es
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfReadingThirdWindow.png"
    }
    profile_schedule_of_profiling_window = {
        "path": start_path_es
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfProfilingWindow.png"
    }
    profile_schedule_of_profiling_second_window = {
        "path": start_path_es
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfProfilingSecondWindow.png"
    }
    profile_schedule_of_profiling_third_window = {
        "path": start_path_es
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfProfilingThirdWindow.png"
    }


class PathToScreenshotsRU:
    # Закладка управления
    management_page_synchronization_with_active_directory_window = {
        "path": start_path_ru
        + r"\Management\Screenshots\ManagementPage_SynchronizationWithActiveDirectoryWindow.png"
    }

    # Закладка лицензий
    licenses_page = {"path": start_path_ru + r"\Licenses\Screenshots\LicensePage.png"}
    license_page_distribute_automatically_window = {
        "path": start_path_ru
        + r"\Licenses\Screenshots\LicensePage_DistributeAutomaticallyWindow.png"
    }
    license_page_statistics_window = {
        "path": start_path_ru
        + r"\Licenses\Screenshots\LicensePage_StatisticsWindow.png"
    }
    license_page_update_license_window = {
        "path": start_path_ru
        + r"\Licenses\Screenshots\LicensePage_UpdateLicenseWindow.png"
    }

    # Закладка настроек
    data_center_server = {
        "path": start_path_ru + r"\Settings\Screenshots\DataCenterServer.png"
    }

    default_database = {
        "path": start_path_ru + r"\Settings\Screenshots\DefaultDatabase.png"
    }
    default_database_add_server_window = {
        "path": start_path_ru
        + r"\Settings\Screenshots\DefaultDatabase_AddServerWindow.png"
    }
    default_database_delete_server_window = {
        "path": start_path_ru
        + r"\Settings\Screenshots\DefaultDatabase_DeleteServerWindow.png"
    }
    default_database_edit_server_window = {
        "path": start_path_ru
        + r"\Settings\Screenshots\DefaultDatabase_EditServerWindow.png"
    }

    agents_and_components = {
        "path": start_path_ru + r"\Settings\Screenshots\AgentsAndComponents.png"
    }
    agents_and_components_change_mail_window = {
        "path": start_path_ru
        + r"\Settings\Screenshots\AgentsAndComponents_ChangeMailWindow.png"
    }
    agents_and_components_free_disk_space_monitoring_window = {
        "path": start_path_ru
        + r"\Settings\Screenshots\AgentsAndComponents_FreeDiskSpaceMonitoringWindow.png"
    }

    operations_with_indexes_and_db = {
        "path": start_path_ru + r"\Settings\Screenshots\OperationsWithIndexesAndDB.png"
    }

    active_directory = {
        "path": start_path_ru + r"\Settings\Screenshots\ActiveDirectory.png"
    }
    active_directory_active_directory_add_domain = {
        "path": start_path_ru + r"\Settings\Screenshots\ActiveDirectoryAddDomain.png"
    }
    active_directory_active_directory_add_internal_user = {
        "path": start_path_ru
        + r"\Settings\Screenshots\ActiveDirectoryAddInternalUser.png"
    }
    active_directory_active_directory_add_workgroup_user = {
        "path": start_path_ru
        + r"\Settings\Screenshots\ActiveDirectoryAddWorkgroupUser.png"
    }
    active_directory_active_directory_sql_connection_settings = {
        "path": start_path_ru
        + r"\Settings\Screenshots\ActiveDirectorySQLConnectionSettings.png"
    }

    access_rights = {"path": start_path_ru + r"\Settings\Screenshots\AccessRights.png"}
    email_notifications = {
        "path": start_path_ru + r"\Settings\Screenshots\EmailNotifications.png"
    }
    telegram_notifications = {
        "path": start_path_ru + r"\Settings\Screenshots\TelegramNotifications.png"
    }

    # Закладка дополнительных настроек
    operation_logging = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\OperationsLoggingPage.png"
    }
    components_update = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\ComponentsUpdatePage.png"
    }
    digital_fingerprints = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\DigitalFingerprintsPage.png"
    }
    components_settings = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\ComponentsSettingsPage.png"
    }
    db_backup_and_migration = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage.png"
    }
    db_backup_and_migration_add_new_migration_db_rule_window = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewMigrationDBRuleWindow.png"
    }

    db_backup_and_migration_add_new_backup_db_rule_window = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewBackupDBRuleWindow.png"
    }

    db_backup_and_migration_add_new_migration_index_rule_window = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewMigrationIndexRuleWindow.png"
    }

    db_backup_and_migration_add_new_backup_index_rule_window = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewBackupIndexRuleWindow.png"
    }

    db_backup_and_migration_add_new_migration_storage_rule_window = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewMigrationStorageRuleWindow.png"
    }

    db_backup_and_migration_add_new_backup_storage_rule_window = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\DBBackupAndMigrationPage_AddNewBackupStorageRuleWindow.png"
    }

    user_cards = {
        "path": start_path_ru + r"\Additional features\Screenshots\UserCardsPage.png"
    }
    user_cards_confirm_clear_db = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\UserCardsPage_ConfirmClearDB.png"
    }

    task_management = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\TaskManagementPage.png"
    }
    task_management_sql_server_connection_setting_window = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\TaskManagementPage_SQLServerConnectionSettingWindow.png"
    }
    attributes_storage = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\AttributesStoragePage.png"
    }

    RVisionGosSOPKA = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\RVisionGosSOPKAPage.png"
    }

    RVisionGosSOPKAPage_add_controlled_information_resources = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\RVisionGosSOPKAPage_AddControlledInformationResources.png"
    }

    outlook_calendars = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\OutlookCalendarsPage.png"
    }

    profile_center_settings = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage.png"
    }
    profile_center_settings_sql_server_connection_setting_window = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_SQLServerConnectionSettingWindow.png"
    }
    profile_schedule_of_reading_window = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfReadingWindow.png"
    }
    profile_schedule_of_reading_second_window = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfReadingSecondWindow.png"
    }
    profile_schedule_of_reading_third_window = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfReadingThirdWindow.png"
    }
    profile_schedule_of_profiling_window = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfProfilingWindow.png"
    }
    profile_schedule_of_profiling_second_window = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfProfilingSecondWindow.png"
    }
    profile_schedule_of_profiling_third_window = {
        "path": start_path_ru
        + r"\Additional features\Screenshots\ProfileCenterSettingsPage_ScheduleOfProfilingThirdWindow.png"
    }
