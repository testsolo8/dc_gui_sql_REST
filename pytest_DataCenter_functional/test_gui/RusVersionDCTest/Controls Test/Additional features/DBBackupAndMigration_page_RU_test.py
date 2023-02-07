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
def handle(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def new_rule_migration_db_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_ru"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_rule_backup_db_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_ru"]).click()
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_rule_migration_index_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_ru"]).click()
    time.sleep(2)
    send_keys("{TAB}")
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_rule_backup_index_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_ru"]).click()
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
def new_rule_migration_storage_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_ru"]).click()
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
def new_rule_backup_storage_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_ru"]).click()
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
@allure.epic("RUS Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsRU
@pytest.mark.testGUI_RusVersionDCTest_ControlsTest_Additionalfeatures
class TestDBBackupAndMigrationPage:
    @allure.story("тест главного окна правил переноса и архивирования")
    class TestDBBackupAndMigrationMainPage:
        def test_restore(self, handle):
            try:
                restore = (
                    handle.by(name=DBBackupAndMigrationPage.restore["title_ru"])
                    .find()
                    .window_text()
                )
                check.equal(restore, "Восстановить")
            except ElementAmbiguousError:
                print(
                    "!!!В английской версии Windows в полноэкранном режиме на этой странице два элемента с именем Restore!!!"
                )

        def test_new_rule(self, handle):
            new_backup_rule = (
                handle.by(name=DBBackupAndMigrationPage.new_rule["title_ru"])
                .find()
                .window_text()
            )
            check.equal(new_backup_rule, "Новое правило")

        def test_delete(self, handle):
            delete = (
                handle.by(name=DBBackupAndMigrationPage.delete["title_ru"])
                .find()
                .window_text()
            )
            check.equal(delete, "Удалить")

        def test_edit(self, handle):
            edit = (
                handle.by(name=DBBackupAndMigrationPage.edit["title_ru"])
                .find()
                .window_text()
            )
            check.equal(edit, "Редактировать")

        def test_all_objects(self, handle):
            all_objects = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_objects["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(all_objects, "Все объекты")

        def test_last_30_days(self, handle):
            last_30_days = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.last_30_days["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(last_30_days, "Последние 30 дней")

        def test_all_rules(self, handle):
            all_rules = (
                handle.__getattribute__(DBBackupAndMigrationPage.all_rules["title_ru"])
                .find()
                .window_text()
            )
            check.equal(all_rules, "Все правила")

        def test_all_directories(self, handle):
            all_directories = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_directories["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(all_directories, "Все директории")

        def test_all_servers(self, handle):
            all_servers = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_servers["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(all_servers, "Все сервера")

        def test_all_statuses(self, handle):
            all_statuses = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_statuses["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(all_statuses, "Все статусы")

        def test_all_products(self, handle):
            all_products = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_products["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(all_products, "Все продукты")

        def test_all_products2(self, handle):
            all_products2 = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_products2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(all_products2, "Все продукты")

        def test_all_statuses2(self, handle):
            all_statuses2 = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_statuses2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(all_statuses2, "Все статусы")

        def test_all_servers2(self, handle):
            all_servers2 = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_servers2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(all_servers2, "Все сервера")

        def test_all_objects2(self, handle):
            all_objects2 = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_objects2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(all_objects2, "Все объекты")

        def test_all_rules2(self, handle):
            all_rules2 = (
                handle.__getattribute__(DBBackupAndMigrationPage.all_rules2["title_ru"])
                .find()
                .window_text()
            )
            check.equal(all_rules2, "Все правила")

        def test_clear(self, handle):
            clear = (
                handle.__getattribute__(DBBackupAndMigrationPage.clear["title_ru"])
                .find()
                .window_text()
            )
            check.equal(clear, "Очистить")

        def test_clear2(self, handle):
            clear2 = (
                handle.__getattribute__(DBBackupAndMigrationPage.clear2["title_ru"])
                .find()
                .window_text()
            )
            check.equal(clear2, "Очистить")

    @allure.story("тест окна настройки правил переноса БД")
    class TestAddNewRuleMigrationDBWindow:
        def test_new_rule2(self, new_rule_migration_db_window):
            new_rule2 = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.new_rule2["title_ru"],
                    found_index=DBBackupAndMigrationPage.new_rule2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule2, "Новое правило")

        def test_database(self, new_rule_migration_db_window):
            database = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.database["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(database, "БД")

        def test_migration(self, new_rule_migration_db_window):
            migration = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.migration["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(migration, "Перенос")

        def test_months(self, new_rule_migration_db_window):
            months = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.months["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(months, "месяцев")

        def test_create(self, new_rule_migration_db_window):
            create = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.create["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(create, "Создать")

        def test_gb(self, new_rule_migration_db_window):
            gb = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.gb["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(gb, "Гб.")

        def test_add_button(self, new_rule_migration_db_window):
            add_button = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.add_button["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(add_button, "Добавить")

        def test_cancel_button(self, new_rule_migration_db_window):
            cancel_button = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.cancel_button["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Отмена")

    @allure.story("тест окна настройки правил архивации БД")
    class TestAddNewRuleBackupDBWindow:
        def test_new_rule(self, new_rule_backup_db_window):
            new_rule3 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.new_rule3["title_ru"],
                    found_index=DBBackupAndMigrationPage.new_rule3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule3, "Новое правило")

        def test_database2(self, new_rule_backup_db_window):
            database2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.database2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(database2, "БД")

        def test_backup(self, new_rule_backup_db_window):
            backup = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.backup["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(backup, "Архивация")

        def test_back_up_objects(self, new_rule_backup_db_window):
            back_up_objects = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.back_up_objects["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_objects,
                "Архивировать объекты, при наступлении условий (объекты после архивации удаляются)",
            )

        def test_back_up_all_objects(self, new_rule_backup_db_window):
            back_up_all_objects = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.back_up_all_objects["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_all_objects,
                "Архивировать все объекты, кроме активных (объекты после архивации сохраняются)",
            )

        def test_months2(self, new_rule_backup_db_window):
            months2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.months2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(months2, "месяцев")

        def test_create2(self, new_rule_backup_db_window):
            create2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.create2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(create2, "Создать")

        def test_gb2(self, new_rule_backup_db_window):
            gb2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.gb2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(gb2, "Гб.")

        def test_add_button2(self, new_rule_backup_db_window):
            add_button2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.add_button2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(add_button2, "Добавить")

        def test_cancel_button2(self, new_rule_backup_db_window):
            cancel_button2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.cancel_button2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button2, "Отмена")

    @allure.story("тест окна настройки правил переноса индекса")
    class TestAddNewRuleMigrationIndexWindow:
        def test_new_rule4(self, new_rule_migration_index_window):
            new_rule4 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.new_rule2["title_ru"],
                    found_index=DBBackupAndMigrationPage.new_rule4["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule4, "Новое правило")

        def test_index(self, new_rule_migration_index_window):
            index = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.index["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(index, "Индекс")

        def test_migration2(self, new_rule_migration_index_window):
            migration2 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.migration2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(migration2, "Перенос")

        def test_months3(self, new_rule_migration_index_window):
            months3 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.months3["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(months3, "месяцев")

        def test_create3(self, new_rule_migration_index_window):
            create3 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.create3["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(create3, "Создать")

        def test_add_button3(self, new_rule_migration_index_window):
            add_button3 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.add_button3["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(add_button3, "Добавить")

        def test_cancel_button3(self, new_rule_migration_index_window):
            cancel_button3 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.cancel_button3["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button3, "Отмена")

    @allure.story("тест окна настройки правил архивации индекса")
    class TestAddNewRuleBackupIndexWindow:
        def test_new_rule6(self, new_rule_backup_index_window):
            new_rule6 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.new_rule6["title_ru"],
                    found_index=DBBackupAndMigrationPage.new_rule6["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule6, "Новое правило")

        def test_index2(self, new_rule_backup_index_window):
            index2 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.index2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(index2, "Индекс")

        def test_backup2(self, new_rule_backup_index_window):
            backup2 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.backup2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(backup2, "Архивация")

        def test_back_up_objects2(self, new_rule_backup_index_window):
            back_up_objects2 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.back_up_objects2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_objects2, "Архивировать объекты, при наступлении условий"
            )

        def test_back_up_all_objects2(self, new_rule_backup_index_window):
            back_up_all_objects2 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.back_up_all_objects2["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_all_objects2, "Архивировать все объекты, кроме активных"
            )

        def test_months5(self, new_rule_backup_index_window):
            months5 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.months5["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(months5, "месяцев")

        def test_create5(self, new_rule_backup_index_window):
            create5 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.create5["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(create5, "Создать")

        def test_add_button5(self, new_rule_backup_index_window):
            add_button5 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.add_button5["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(add_button5, "Добавить")

        def test_cancel_button5(self, new_rule_backup_index_window):
            cancel_button5 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.cancel_button5["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button5, "Отмена")

    @allure.story("тест окна настройки правил переноса хранилица")
    class TestAddNewRuleMigrationStorageWindow:
        def test_new_rule5(self, new_rule_migration_storage_window):
            new_rule5 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.new_rule5["title_ru"],
                    found_index=DBBackupAndMigrationPage.new_rule5["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule5, "Новое правило")

        def test_storage(self, new_rule_migration_storage_window):
            storage = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.storage["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(storage, "Хранилище")

        def test_migration3(self, new_rule_migration_storage_window):
            migration3 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.migration3["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(migration3, "Перенос")

        def test_months4(self, new_rule_migration_storage_window):
            months4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.months4["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(months4, "месяцев")

        def test_create4(self, new_rule_migration_storage_window):
            create4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.create4["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(create4, "Создать")

        def test_gb3(self, new_rule_migration_storage_window):
            gb3 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.gb3["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(gb3, "Гб.")

        def test_add_button4(self, new_rule_migration_storage_window):
            add_button4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.add_button4["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(add_button4, "Добавить")

        def test_cancel_button4(self, new_rule_migration_storage_window):
            cancel_button4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.cancel_button4["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button4, "Отмена")

    @allure.story("тест окна настройки правил архивации хранилища")
    class TestAddNewRuleBackupStorageWindow:
        def test_new_rule7(self, new_rule_backup_storage_window):
            new_rule7 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.new_rule7["title_ru"],
                    found_index=DBBackupAndMigrationPage.new_rule7["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule7, "Новое правило")

        def test_storage2(self, new_rule_backup_storage_window):
            storage2 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.storage2["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(storage2, "Хранилище")

        def test_backup3(self, new_rule_backup_storage_window):
            backup3 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.backup3["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(backup3, "Архивация")

        def test_back_up_objects3(self, new_rule_backup_storage_window):
            back_up_objects3 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.back_up_objects3["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_objects3,
                "Архивировать объекты, при наступлении условий (объекты после архивации удаляются)",
            )

        def test_back_up_all_objects3(self, new_rule_backup_storage_window):
            back_up_all_objects3 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.back_up_all_objects3["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_all_objects3,
                "Архивировать все объекты, кроме активных (объекты после архивации сохраняются)",
            )

        def test_months6(self, new_rule_backup_storage_window):
            months6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.months6["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(months6, "месяцев")

        def test_create6(self, new_rule_backup_storage_window):
            create6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.create6["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(create6, "Создать")

        def test_gb4(self, new_rule_backup_storage_window):
            gb4 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.gb4["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(gb4, "Гб.")

        def test_add_button6(self, new_rule_backup_storage_window):
            add_button6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.add_button6["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(add_button6, "Добавить")

        def test_cancel_button6(self, new_rule_backup_storage_window):
            cancel_button6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.cancel_button6["title_ru"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button6, "Отмена")
