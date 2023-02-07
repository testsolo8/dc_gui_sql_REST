# Standart libraries
import time

# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.findwindows import ElementAmbiguousError
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import DBBackupAndMigrationPage


@pytest.fixture(scope="class")
def handle(start_test_page_en):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def new_rule_migration_db_window(start_test_page_en):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_en"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_rule_backup_db_window(start_test_page_en):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_en"]).click()
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_rule_migration_index_window(start_test_page_en):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_en"]).click()
    time.sleep(2)
    send_keys("{TAB}")
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_rule_backup_index_window(start_test_page_en):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_en"]).click()
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(1)
    send_keys("{TAB}")
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_rule_migration_storage_window(start_test_page_en):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_en"]).click()
    time.sleep(2)
    send_keys("{TAB}")
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_rule_backup_storage_window(start_test_page_en):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_en"]).click()
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(1)
    send_keys("{TAB}")
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("ENG Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsEN
@pytest.mark.testGUI_EngVersionDCTest_ControlsTest_Additionalfeatures
class TestDBBackupAndMigrationPage:
    @allure.story("тест главного окна правил переноса и архивирования")
    class TestDBBackupAndMigrationMainPage:
        def test_restore(self, handle):
            try:
                restore = (
                    handle.by(name=DBBackupAndMigrationPage.restore["title_en"])
                    .find()
                    .window_text()
                )
                check.equal(restore, "Restore")
            except ElementAmbiguousError:
                print(
                    "!!!В английской версии Windows в полноэкранном режиме на этой странице два элемента с именем Restore!!!"
                )

        def test_new_rule(self, handle):
            new_backup_rule = (
                handle.by(name=DBBackupAndMigrationPage.new_rule["title_en"])
                .find()
                .window_text()
            )
            check.equal(new_backup_rule, "New rule")

        def test_delete(self, handle):
            delete = (
                handle.by(name=DBBackupAndMigrationPage.delete["title_en"])
                .find()
                .window_text()
            )
            check.equal(delete, "Delete")

        def test_edit(self, handle):
            edit = (
                handle.by(name=DBBackupAndMigrationPage.edit["title_en"])
                .find()
                .window_text()
            )
            check.equal(edit, "Edit")

        def test_all_objects(self, handle):
            all_objects = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_objects["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(all_objects, "All objects")

        def test_last_30_days(self, handle):
            last_30_days = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.last_30_days["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(last_30_days, "Last 30 days")

        def test_all_rules(self, handle):
            all_rules = (
                handle.__getattribute__(DBBackupAndMigrationPage.all_rules["title_en"])
                .find()
                .window_text()
            )
            check.equal(all_rules, "All rules")

        def test_all_directories(self, handle):
            all_directories = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_directories["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(all_directories, "All directories")

        def test_all_servers(self, handle):
            all_servers = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_servers["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(all_servers, "All Servers")

        def test_all_statuses(self, handle):
            all_statuses = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_statuses["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(all_statuses, "All statuses")

        def test_all_products(self, handle):
            all_products = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_products["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(all_products, "All products")

        def test_all_products2(self, handle):
            all_products2 = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_products2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(all_products2, "All products")

        def test_all_statuses2(self, handle):
            all_statuses2 = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_statuses2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(all_statuses2, "All statuses")

        def test_all_servers2(self, handle):
            all_servers2 = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_servers2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(all_servers2, "All Servers")

        def test_all_objects2(self, handle):
            all_objects2 = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_objects2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(all_objects2, "All objects")

        def test_all_rules2(self, handle):
            all_rules2 = (
                handle.__getattribute__(DBBackupAndMigrationPage.all_rules2["title_en"])
                .find()
                .window_text()
            )
            check.equal(all_rules2, "All rules")

        def test_clear(self, handle):
            clear = (
                handle.__getattribute__(DBBackupAndMigrationPage.clear["title_en"])
                .find()
                .window_text()
            )
            check.equal(clear, "Clear")

        def test_clear2(self, handle):
            clear2 = (
                handle.__getattribute__(DBBackupAndMigrationPage.clear2["title_en"])
                .find()
                .window_text()
            )
            check.equal(clear2, "Clear")

    @allure.story("тест окна настройки правил переноса БД")
    class TestAddNewRuleMigrationDBWindow:
        def test_new_rule2(self, new_rule_migration_db_window):
            new_rule2 = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.new_rule2["title_en"],
                    found_index=DBBackupAndMigrationPage.new_rule2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule2, "New rule")

        def test_database(self, new_rule_migration_db_window):
            database = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.database["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(database, "Database")

        def test_migration(self, new_rule_migration_db_window):
            migration = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.migration["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(migration, "Migration")

        def test_months(self, new_rule_migration_db_window):
            months = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.months["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(months, "months")

        def test_create(self, new_rule_migration_db_window):
            create = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.create["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(create, "Create")

        def test_gb(self, new_rule_migration_db_window):
            gb = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.gb["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(gb, "GB.")

        def test_add_button(self, new_rule_migration_db_window):
            add_button = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.add_button["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(add_button, "Add")

        def test_cancel_button(self, new_rule_migration_db_window):
            cancel_button = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.cancel_button["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Cancel")

    @allure.story("тест окна настройки правил архивации БД")
    class TestAddNewRuleBackupDBWindow:
        def test_new_rule(self, new_rule_backup_db_window):
            new_rule3 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.new_rule3["title_en"],
                    found_index=DBBackupAndMigrationPage.new_rule3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule3, "New rule")

        def test_database2(self, new_rule_backup_db_window):
            database2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.database2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(database2, "Database")

        def test_backup(self, new_rule_backup_db_window):
            backup = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.backup["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(backup, "Backup")

        def test_back_up_objects(self, new_rule_backup_db_window):
            back_up_objects = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.back_up_objects["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_objects,
                "Back up objects when the conditions are met (the databases are deleted after backup)",
            )

        def test_back_up_all_objects(self, new_rule_backup_db_window):
            back_up_all_objects = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.back_up_all_objects["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_all_objects,
                "Back up all objects, except for active ones (the databases remain after backup)",
            )

        def test_months2(self, new_rule_backup_db_window):
            months2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.months2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(months2, "months")

        def test_create2(self, new_rule_backup_db_window):
            create2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.create2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(create2, "Create")

        def test_gb2(self, new_rule_backup_db_window):
            gb2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.gb2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(gb2, "GB.")

        def test_add_button2(self, new_rule_backup_db_window):
            add_button2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.add_button2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(add_button2, "Add")

        def test_cancel_button2(self, new_rule_backup_db_window):
            cancel_button2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.cancel_button2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button2, "Cancel")

    @allure.story("тест окна настройки правил переноса индекса")
    class TestAddNewRuleMigrationIndexWindow:
        def test_new_rule4(self, new_rule_migration_index_window):
            new_rule4 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.new_rule4["title_en"],
                    found_index=DBBackupAndMigrationPage.new_rule4["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule4, "New rule")

        def test_index(self, new_rule_migration_index_window):
            index = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.index["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(index, "Index")

        def test_migration2(self, new_rule_migration_index_window):
            migration2 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.migration2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(migration2, "Migration")

        def test_months3(self, new_rule_migration_index_window):
            months3 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.months3["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(months3, "months")

        def test_create3(self, new_rule_migration_index_window):
            create3 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.create3["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(create3, "Create")

        def test_add_button3(self, new_rule_migration_index_window):
            add_button3 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.add_button3["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(add_button3, "Add")

        def test_cancel_button3(self, new_rule_migration_index_window):
            cancel_button3 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.cancel_button3["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button3, "Cancel")

    @allure.story("тест окна настройки правил архивации индекса")
    class TestAddNewRuleBackupIndexWindow:
        def test_new_rule6(self, new_rule_backup_index_window):
            new_rule6 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.new_rule6["title_en"],
                    found_index=DBBackupAndMigrationPage.new_rule6["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule6, "New rule")

        def test_index2(self, new_rule_backup_index_window):
            index2 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.index2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(index2, "Index")

        def test_backup2(self, new_rule_backup_index_window):
            backup2 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.backup2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(backup2, "Backup")

        def test_back_up_objects2(self, new_rule_backup_index_window):
            back_up_objects2 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.back_up_objects2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(back_up_objects2, "Back up objects when the conditions are met")

        def test_back_up_all_objects2(self, new_rule_backup_index_window):
            back_up_all_objects2 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.back_up_all_objects2["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_all_objects2, "Back up all objects, except for active ones"
            )

        def test_months5(self, new_rule_backup_index_window):
            months5 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.months5["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(months5, "months")

        def test_create5(self, new_rule_backup_index_window):
            create5 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.create5["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(create5, "Create")

        def test_add_button5(self, new_rule_backup_index_window):
            add_button5 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.add_button5["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(add_button5, "Add")

        def test_cancel_button5(self, new_rule_backup_index_window):
            cancel_button5 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.cancel_button5["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button5, "Cancel")

    @allure.story("тест окна настройки правил переноса хранилица")
    class TestAddNewRuleMigrationStorageWindow:
        def test_new_rule5(self, new_rule_migration_storage_window):
            new_rule5 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.new_rule5["title_en"],
                    found_index=DBBackupAndMigrationPage.new_rule5["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule5, "New rule")

        def test_storage(self, new_rule_migration_storage_window):
            storage = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.storage["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(storage, "Storage")

        def test_migration3(self, new_rule_migration_storage_window):
            migration3 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.migration3["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(migration3, "Migration")

        def test_months4(self, new_rule_migration_storage_window):
            months4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.months4["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(months4, "months")

        def test_create4(self, new_rule_migration_storage_window):
            create4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.create4["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(create4, "Create")

        def test_gb3(self, new_rule_migration_storage_window):
            gb3 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.gb3["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(gb3, "GB.")

        def test_add_button4(self, new_rule_migration_storage_window):
            add_button4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.add_button4["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(add_button4, "Add")

        def test_cancel_button4(self, new_rule_migration_storage_window):
            cancel_button4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.cancel_button4["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button4, "Cancel")

    @allure.story("тест окна настройки правил архивации хранилища")
    class TestAddNewRuleBackupStorageWindow:
        def test_new_rule7(self, new_rule_backup_storage_window):
            new_rule7 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.new_rule7["title_en"],
                    found_index=DBBackupAndMigrationPage.new_rule7["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule7, "New rule")

        def test_storage2(self, new_rule_backup_storage_window):
            storage2 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.storage2["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(storage2, "Storage")

        def test_backup3(self, new_rule_backup_storage_window):
            backup3 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.backup3["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(backup3, "Backup")

        def test_back_up_objects3(self, new_rule_backup_storage_window):
            back_up_objects3 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.back_up_objects3["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_objects3,
                "Back up objects when the conditions are met (the databases are deleted after backup)",
            )

        def test_back_up_all_objects3(self, new_rule_backup_storage_window):
            back_up_all_objects3 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.back_up_all_objects3["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_all_objects3,
                "Back up all objects, except for active ones (the databases remain after backup)",
            )

        def test_months6(self, new_rule_backup_storage_window):
            months6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.months6["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(months6, "months")

        def test_create6(self, new_rule_backup_storage_window):
            create6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.create6["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(create6, "Create")

        def test_gb4(self, new_rule_backup_storage_window):
            gb4 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.gb4["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(gb4, "GB.")

        def test_add_button6(self, new_rule_backup_storage_window):
            add_button6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.add_button6["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(add_button6, "Add")

        def test_cancel_button6(self, new_rule_backup_storage_window):
            cancel_button6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.cancel_button6["title_en"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button6, "Cancel")
