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
def handle(start_test_page):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def new_rule_migration_db_window(start_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule[title_key]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_rule_backup_db_window(start_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule[title_key]).click()
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_rule_migration_index_window(start_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule[title_key]).click()
    time.sleep(2)
    send_keys("{TAB}")
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_rule_backup_index_window(start_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule[title_key]).click()
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
def new_rule_migration_storage_window(start_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule[title_key]).click()
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
def new_rule_backup_storage_window(start_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule[title_key]).click()
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
@allure.epic("Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Additionalfeatures
class TestDBBackupAndMigrationPage:
    @allure.story("тест главного окна правил переноса и архивирования")
    class TestDBBackupAndMigrationMainPage:
        def test_restore(self, handle, title_key):
            restore = handle.by(name=DBBackupAndMigrationPage.restore[title_key],
                                found_index=DBBackupAndMigrationPage.restore["found_index"]).find().window_text()
            check.equal(restore, DBBackupAndMigrationPage.restore[title_key])

        def test_new_rule(self, handle, title_key):
            new_backup_rule = handle.by(name=DBBackupAndMigrationPage.new_rule[title_key]).find().window_text()
            check.equal(new_backup_rule, DBBackupAndMigrationPage.new_rule[title_key])

        def test_delete(self, handle, title_key):
            delete = handle.by(name=DBBackupAndMigrationPage.delete[title_key]).find().window_text()
            check.equal(delete, DBBackupAndMigrationPage.delete[title_key])

        def test_edit(self, handle, title_key):
            edit = handle.by(name=DBBackupAndMigrationPage.edit[title_key]).find().window_text()
            check.equal(edit, DBBackupAndMigrationPage.edit[title_key])

        def test_all_objects(self, handle, title_key):
            all_objects = handle.__getattribute__(DBBackupAndMigrationPage.all_objects[title_key]).find().window_text()
            check.equal(all_objects, DBBackupAndMigrationPage.all_objects[title_key])

        def test_last_30_days(self, handle, title_key):
            last_30_days = (
                handle.__getattribute__(DBBackupAndMigrationPage.last_30_days[title_key]).find().window_text()
            )
            check.equal(last_30_days, DBBackupAndMigrationPage.last_30_days[title_key])

        def test_all_rules(self, handle, title_key):
            all_rules = handle.__getattribute__(DBBackupAndMigrationPage.all_rules[title_key]).find().window_text()
            check.equal(all_rules, DBBackupAndMigrationPage.all_rules[title_key])

        def test_all_directories(self, handle, title_key):
            all_directories = (
                handle.__getattribute__(DBBackupAndMigrationPage.all_directories[title_key]).find().window_text()
            )
            check.equal(all_directories, DBBackupAndMigrationPage.all_directories[title_key])

        def test_all_servers(self, handle, title_key):
            all_servers = handle.__getattribute__(DBBackupAndMigrationPage.all_servers[title_key]).find().window_text()
            check.equal(all_servers, DBBackupAndMigrationPage.all_servers[title_key])

        def test_all_statuses(self, handle, title_key):
            all_statuses = (
                handle.__getattribute__(DBBackupAndMigrationPage.all_statuses[title_key]).find().window_text()
            )
            check.equal(all_statuses, DBBackupAndMigrationPage.all_statuses[title_key])

        def test_all_products(self, handle, title_key):
            all_products = (
                handle.__getattribute__(DBBackupAndMigrationPage.all_products[title_key]).find().window_text()
            )
            check.equal(all_products, DBBackupAndMigrationPage.all_products[title_key])

        def test_all_products2(self, handle, title_key):
            all_products2 = (
                handle.__getattribute__(DBBackupAndMigrationPage.all_products2[title_key]).find().window_text()
            )
            check.equal(all_products2, DBBackupAndMigrationPage.all_products2[title_key])

        def test_all_statuses2(self, handle, title_key):
            all_statuses2 = (
                handle.__getattribute__(DBBackupAndMigrationPage.all_statuses2[title_key]).find().window_text()
            )
            check.equal(all_statuses2, DBBackupAndMigrationPage.all_statuses2[title_key])

        def test_all_servers2(self, handle, title_key):
            all_servers2 = (
                handle.__getattribute__(DBBackupAndMigrationPage.all_servers2[title_key]).find().window_text()
            )
            check.equal(all_servers2, DBBackupAndMigrationPage.all_servers2[title_key])

        def test_all_objects2(self, handle, title_key):
            all_objects2 = (
                handle.__getattribute__(DBBackupAndMigrationPage.all_objects2[title_key]).find().window_text()
            )
            check.equal(all_objects2, DBBackupAndMigrationPage.all_objects2[title_key])

        def test_all_rules2(self, handle, title_key):
            all_rules2 = handle.__getattribute__(DBBackupAndMigrationPage.all_rules2[title_key]).find().window_text()
            check.equal(all_rules2, DBBackupAndMigrationPage.all_rules2[title_key])

        def test_clear(self, handle, title_key):
            clear = handle.Button0.find().window_text()
            check.equal(clear, DBBackupAndMigrationPage.clear[title_key])

        def test_clear2(self, handle, title_key):
            clear2 = handle.Button3.find().window_text()
            check.equal(clear2, DBBackupAndMigrationPage.clear2[title_key])

    @allure.story("тест окна настройки правил переноса БД")
    class TestAddNewRuleMigrationDBWindow:
        def test_new_rule2(self, new_rule_migration_db_window, title_key):
            new_rule2 = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.new_rule2[title_key],
                    found_index=DBBackupAndMigrationPage.new_rule2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule2, DBBackupAndMigrationPage.new_rule2[title_key])

        def test_database(self, new_rule_migration_db_window, title_key):
            database = (
                new_rule_migration_db_window.by(name=DBBackupAndMigrationPage.database[title_key]).find().window_text()
            )
            check.equal(database, DBBackupAndMigrationPage.database[title_key])

        def test_migration(self, new_rule_migration_db_window, title_key):
            migration = (
                new_rule_migration_db_window.by(name=DBBackupAndMigrationPage.migration[title_key])
                .find()
                .window_text()
            )
            check.equal(migration, DBBackupAndMigrationPage.migration[title_key])

        def test_months(self, new_rule_migration_db_window, title_key):
            months = (
                new_rule_migration_db_window.by(name=DBBackupAndMigrationPage.months[title_key]).find().window_text()
            )
            check.equal(months, DBBackupAndMigrationPage.months[title_key])

        def test_create(self, new_rule_migration_db_window, title_key):
            create = (
                new_rule_migration_db_window.by(name=DBBackupAndMigrationPage.create[title_key]).find().window_text()
            )
            check.equal(create, DBBackupAndMigrationPage.create[title_key])

        def test_gb(self, new_rule_migration_db_window, title_key):
            gb = new_rule_migration_db_window.by(name=DBBackupAndMigrationPage.gb[title_key]).find().window_text()
            check.equal(gb, DBBackupAndMigrationPage.gb[title_key])

        def test_add_button(self, new_rule_migration_db_window, title_key):
            add_button = (
                new_rule_migration_db_window.by(name=DBBackupAndMigrationPage.add_button[title_key])
                .find()
                .window_text()
            )
            check.equal(add_button, DBBackupAndMigrationPage.add_button[title_key])

        def test_cancel_button(self, new_rule_migration_db_window, title_key):
            cancel_button = (
                new_rule_migration_db_window.by(name=DBBackupAndMigrationPage.cancel_button[title_key])
                .find()
                .window_text()
            )
            check.equal(cancel_button, DBBackupAndMigrationPage.cancel_button[title_key])

    @allure.story("тест окна настройки правил архивации БД")
    class TestAddNewRuleBackupDBWindow:
        def test_new_rule(self, new_rule_backup_db_window, title_key):
            new_rule3 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.new_rule3[title_key],
                    found_index=DBBackupAndMigrationPage.new_rule3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule3, DBBackupAndMigrationPage.new_rule3[title_key])

        def test_database2(self, new_rule_backup_db_window, title_key):
            database2 = (
                new_rule_backup_db_window.by(name=DBBackupAndMigrationPage.database2[title_key]).find().window_text()
            )
            check.equal(database2, DBBackupAndMigrationPage.database2[title_key])

        def test_backup(self, new_rule_backup_db_window, title_key):
            backup = new_rule_backup_db_window.by(name=DBBackupAndMigrationPage.backup[title_key]).find().window_text()
            check.equal(backup, DBBackupAndMigrationPage.backup[title_key])

        def test_back_up_objects(self, new_rule_backup_db_window, title_key):
            back_up_objects = (
                new_rule_backup_db_window.by(name=DBBackupAndMigrationPage.back_up_objects[title_key])
                .find()
                .window_text()
            )
            check.equal(
                back_up_objects,
                DBBackupAndMigrationPage.back_up_objects[title_key],
            )

        def test_back_up_all_objects(self, new_rule_backup_db_window, title_key):
            back_up_all_objects = (
                new_rule_backup_db_window.by(name=DBBackupAndMigrationPage.back_up_all_objects[title_key])
                .find()
                .window_text()
            )
            check.equal(
                back_up_all_objects,
                DBBackupAndMigrationPage.back_up_all_objects[title_key],
            )

        def test_months2(self, new_rule_backup_db_window, title_key):
            months2 = (
                new_rule_backup_db_window.by(name=DBBackupAndMigrationPage.months2[title_key]).find().window_text()
            )
            check.equal(months2, DBBackupAndMigrationPage.months2[title_key])

        def test_create2(self, new_rule_backup_db_window, title_key):
            create2 = (
                new_rule_backup_db_window.by(name=DBBackupAndMigrationPage.create2[title_key]).find().window_text()
            )
            check.equal(create2, DBBackupAndMigrationPage.create2[title_key])

        def test_gb2(self, new_rule_backup_db_window, title_key):
            gb2 = new_rule_backup_db_window.by(name=DBBackupAndMigrationPage.gb2[title_key]).find().window_text()
            check.equal(gb2, DBBackupAndMigrationPage.gb2[title_key])

        def test_add_button2(self, new_rule_backup_db_window, title_key):
            add_button2 = (
                new_rule_backup_db_window.by(name=DBBackupAndMigrationPage.add_button2[title_key]).find().window_text()
            )
            check.equal(add_button2, DBBackupAndMigrationPage.add_button2[title_key])

        def test_cancel_button2(self, new_rule_backup_db_window, title_key):
            cancel_button2 = (
                new_rule_backup_db_window.by(name=DBBackupAndMigrationPage.cancel_button2[title_key])
                .find()
                .window_text()
            )
            check.equal(cancel_button2, DBBackupAndMigrationPage.cancel_button2[title_key])

    @allure.story("тест окна настройки правил переноса индекса")
    class TestAddNewRuleMigrationIndexWindow:
        def test_new_rule4(self, new_rule_migration_index_window, title_key):
            new_rule4 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.new_rule4[title_key],
                    found_index=DBBackupAndMigrationPage.new_rule4["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule4, DBBackupAndMigrationPage.new_rule4[title_key])

        def test_index(self, new_rule_migration_index_window, title_key):
            index = (
                new_rule_migration_index_window.by(name=DBBackupAndMigrationPage.index[title_key]).find().window_text()
            )
            check.equal(index, DBBackupAndMigrationPage.index[title_key])

        def test_migration2(self, new_rule_migration_index_window, title_key):
            migration2 = (
                new_rule_migration_index_window.by(name=DBBackupAndMigrationPage.migration2[title_key])
                .find()
                .window_text()
            )
            check.equal(migration2, DBBackupAndMigrationPage.migration2[title_key])

        def test_months3(self, new_rule_migration_index_window, title_key):
            months3 = (
                new_rule_migration_index_window.by(name=DBBackupAndMigrationPage.months3[title_key])
                .find()
                .window_text()
            )
            check.equal(months3, DBBackupAndMigrationPage.months3[title_key])

        def test_create3(self, new_rule_migration_index_window, title_key):
            create3 = (
                new_rule_migration_index_window.by(name=DBBackupAndMigrationPage.create3[title_key])
                .find()
                .window_text()
            )
            check.equal(create3, DBBackupAndMigrationPage.create3[title_key])

        def test_add_button3(self, new_rule_migration_index_window, title_key):
            add_button3 = (
                new_rule_migration_index_window.by(name=DBBackupAndMigrationPage.add_button3[title_key])
                .find()
                .window_text()
            )
            check.equal(add_button3, DBBackupAndMigrationPage.add_button3[title_key])

        def test_cancel_button3(self, new_rule_migration_index_window, title_key):
            cancel_button3 = (
                new_rule_migration_index_window.by(name=DBBackupAndMigrationPage.cancel_button3[title_key])
                .find()
                .window_text()
            )
            check.equal(cancel_button3, DBBackupAndMigrationPage.cancel_button3[title_key])

    @allure.story("тест окна настройки правил архивации индекса")
    class TestAddNewRuleBackupIndexWindow:
        def test_new_rule6(self, new_rule_backup_index_window, title_key):
            new_rule6 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.new_rule6[title_key],
                    found_index=DBBackupAndMigrationPage.new_rule6["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule6, DBBackupAndMigrationPage.new_rule6[title_key])

        def test_index2(self, new_rule_backup_index_window, title_key):
            index2 = (
                new_rule_backup_index_window.by(name=DBBackupAndMigrationPage.index2[title_key]).find().window_text()
            )
            check.equal(index2, DBBackupAndMigrationPage.index2[title_key])

        def test_backup2(self, new_rule_backup_index_window, title_key):
            backup2 = (
                new_rule_backup_index_window.by(name=DBBackupAndMigrationPage.backup2[title_key]).find().window_text()
            )
            check.equal(backup2, DBBackupAndMigrationPage.backup2[title_key])

        def test_back_up_objects2(self, new_rule_backup_index_window, title_key):
            back_up_objects2 = (
                new_rule_backup_index_window.by(name=DBBackupAndMigrationPage.back_up_objects2[title_key])
                .find()
                .window_text()
            )
            check.equal(back_up_objects2, DBBackupAndMigrationPage.back_up_objects2[title_key])

        def test_back_up_all_objects2(self, new_rule_backup_index_window, title_key):
            back_up_all_objects2 = (
                new_rule_backup_index_window.by(name=DBBackupAndMigrationPage.back_up_all_objects2[title_key])
                .find()
                .window_text()
            )
            check.equal(back_up_all_objects2, DBBackupAndMigrationPage.back_up_all_objects2[title_key])

        def test_months5(self, new_rule_backup_index_window, title_key):
            months5 = (
                new_rule_backup_index_window.by(name=DBBackupAndMigrationPage.months5[title_key]).find().window_text()
            )
            check.equal(months5, DBBackupAndMigrationPage.months5[title_key])

        def test_create5(self, new_rule_backup_index_window, title_key):
            create5 = (
                new_rule_backup_index_window.by(name=DBBackupAndMigrationPage.create5[title_key]).find().window_text()
            )
            check.equal(create5, DBBackupAndMigrationPage.create5[title_key])

        def test_add_button5(self, new_rule_backup_index_window, title_key):
            add_button5 = (
                new_rule_backup_index_window.by(name=DBBackupAndMigrationPage.add_button5[title_key])
                .find()
                .window_text()
            )
            check.equal(add_button5, DBBackupAndMigrationPage.add_button5[title_key])

        def test_cancel_button5(self, new_rule_backup_index_window, title_key):
            cancel_button5 = (
                new_rule_backup_index_window.by(name=DBBackupAndMigrationPage.cancel_button5[title_key])
                .find()
                .window_text()
            )
            check.equal(cancel_button5, DBBackupAndMigrationPage.cancel_button5[title_key])

    @allure.story("тест окна настройки правил переноса хранилица")
    class TestAddNewRuleMigrationStorageWindow:
        def test_new_rule5(self, new_rule_migration_storage_window, title_key):
            new_rule5 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.new_rule5[title_key],
                    found_index=DBBackupAndMigrationPage.new_rule5["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule5, DBBackupAndMigrationPage.new_rule5[title_key])

        def test_storage(self, new_rule_migration_storage_window, title_key):
            storage = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.storage[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(storage, DBBackupAndMigrationPage.storage[title_key])

        def test_migration3(self, new_rule_migration_storage_window, title_key):
            migration3 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.migration3[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(migration3, DBBackupAndMigrationPage.migration3[title_key])

        def test_months4(self, new_rule_migration_storage_window, title_key):
            months4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.months4[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(months4, DBBackupAndMigrationPage.months4[title_key])

        def test_create4(self, new_rule_migration_storage_window, title_key):
            create4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.create4[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(create4, DBBackupAndMigrationPage.create4[title_key])

        def test_gb3(self, new_rule_migration_storage_window, title_key):
            gb3 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.gb3[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(gb3, DBBackupAndMigrationPage.gb3[title_key])

        def test_add_button4(self, new_rule_migration_storage_window, title_key):
            add_button4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.add_button4[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(add_button4, DBBackupAndMigrationPage.add_button4[title_key])

        def test_cancel_button4(self, new_rule_migration_storage_window, title_key):
            cancel_button4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.cancel_button4[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button4, DBBackupAndMigrationPage.cancel_button4[title_key])

    @allure.story("тест окна настройки правил архивации хранилища")
    class TestAddNewRuleBackupStorageWindow:
        def test_new_rule7(self, new_rule_backup_storage_window, title_key):
            new_rule7 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.new_rule7[title_key],
                    found_index=DBBackupAndMigrationPage.new_rule7["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule7, DBBackupAndMigrationPage.new_rule7[title_key])

        def test_storage2(self, new_rule_backup_storage_window, title_key):
            storage2 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.storage2[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(storage2, DBBackupAndMigrationPage.storage2[title_key])

        def test_backup3(self, new_rule_backup_storage_window, title_key):
            backup3 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.backup3[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(backup3, DBBackupAndMigrationPage.backup3[title_key])

        def test_back_up_objects3(self, new_rule_backup_storage_window, title_key):
            back_up_objects3 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.back_up_objects3[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_objects3,
                DBBackupAndMigrationPage.back_up_objects3[title_key],
            )

        def test_back_up_all_objects3(self, new_rule_backup_storage_window, title_key):
            back_up_all_objects3 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.back_up_all_objects3[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_all_objects3,
                DBBackupAndMigrationPage.back_up_all_objects3[title_key],
            )

        def test_months6(self, new_rule_backup_storage_window, title_key):
            months6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.months6[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(months6, DBBackupAndMigrationPage.months6[title_key])

        def test_create6(self, new_rule_backup_storage_window, title_key):
            create6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.create6[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(create6, DBBackupAndMigrationPage.create6[title_key])

        def test_gb4(self, new_rule_backup_storage_window, title_key):
            gb4 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.gb4[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(gb4, DBBackupAndMigrationPage.gb4[title_key])

        def test_add_button6(self, new_rule_backup_storage_window, title_key):
            add_button6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.add_button6[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(add_button6, DBBackupAndMigrationPage.add_button6[title_key])

        def test_cancel_button6(self, new_rule_backup_storage_window, title_key):
            cancel_button6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.cancel_button6[title_key],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button6, DBBackupAndMigrationPage.cancel_button6[title_key])
