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
def handle(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def new_rule_migration_db_window(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_es"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_rule_backup_db_window(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_es"]).click()
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_rule_migration_index_window(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_es"]).click()
    time.sleep(2)
    send_keys("{TAB}")
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_rule_backup_index_window(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_es"]).click()
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
def new_rule_migration_storage_window(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_es"]).click()
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
def new_rule_backup_storage_window(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_es"]).click()
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
@allure.epic("ESP Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsES
@pytest.mark.testGUI_EspVersionDCTest_ControlsTest_Additionalfeatures
class TestDBBackupAndMigrationPage:
    @allure.story("тест главного окна правил переноса и архивирования")
    class TestDBBackupAndMigrationMainPage:
        def test_restore(self, handle):
            try:
                restore = (
                    handle.by(name=DBBackupAndMigrationPage.restore["title_es"])
                    .find()
                    .window_text()
                )
                check.equal(restore, "Restaurar")
            except ElementAmbiguousError:
                print(
                    "!!!В английской версии Windows в полноэкранном режиме на этой странице два элемента с именем Restore!!!"
                )

        def test_new_rule(self, handle):
            new_backup_rule = (
                handle.by(name=DBBackupAndMigrationPage.new_rule["title_es"])
                .find()
                .window_text()
            )
            check.equal(new_backup_rule, "Nueva regla")

        def test_delete(self, handle):
            delete = (
                handle.by(name=DBBackupAndMigrationPage.delete["title_es"])
                .find()
                .window_text()
            )
            check.equal(delete, "Borrar")

        def test_edit(self, handle):
            edit = (
                handle.by(name=DBBackupAndMigrationPage.edit["title_es"])
                .find()
                .window_text()
            )
            check.equal(edit, "Editar")

        def test_all_objects(self, handle):
            all_objects = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_objects["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(all_objects, "Todos los objetos")

        def test_last_30_days(self, handle):
            last_30_days = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.last_30_days["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(last_30_days, "30 días últimos")

        def test_all_rules(self, handle):
            all_rules = (
                handle.__getattribute__(DBBackupAndMigrationPage.all_rules["title_es"])
                .find()
                .window_text()
            )
            check.equal(all_rules, "Todas las reglas")

        def test_all_directories(self, handle):
            all_directories = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_directories["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(all_directories, "Todos los directorios")

        def test_all_servers(self, handle):
            all_servers = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_servers["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(all_servers, "Todos los servidores")

        def test_all_statuses(self, handle):
            all_statuses = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_statuses["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(all_statuses, "Todos los estados")

        def test_all_products(self, handle):
            all_products = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_products["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(all_products, "Todos los productos")

        def test_all_products2(self, handle):
            all_products2 = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_products2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(all_products2, "Todos los productos")

        def test_all_statuses2(self, handle):
            all_statuses2 = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_statuses2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(all_statuses2, "Todos los estados")

        def test_all_servers2(self, handle):
            all_servers2 = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_servers2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(all_servers2, "Todos los servidores")

        def test_all_objects2(self, handle):
            all_objects2 = (
                handle.__getattribute__(
                    DBBackupAndMigrationPage.all_objects2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(all_objects2, "Todos los objetos")

        def test_all_rules2(self, handle):
            all_rules2 = (
                handle.__getattribute__(DBBackupAndMigrationPage.all_rules2["title_es"])
                .find()
                .window_text()
            )
            check.equal(all_rules2, "Todas las reglas")

        def test_clear(self, handle):
            clear = (
                handle.__getattribute__(DBBackupAndMigrationPage.clear["title_es"])
                .find()
                .window_text()
            )
            check.equal(clear, "Eliminar")

        def test_clear2(self, handle):
            clear2 = (
                handle.__getattribute__(DBBackupAndMigrationPage.clear2["title_es"])
                .find()
                .window_text()
            )
            check.equal(clear2, "Eliminar")

    @allure.story("тест окна настройки правил переноса БД")
    class TestAddNewRuleMigrationDBWindow:
        def test_new_rule2(self, new_rule_migration_db_window):
            new_rule2 = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.new_rule2["title_es"],
                    found_index=DBBackupAndMigrationPage.new_rule2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule2, "Nueva regla")

        def test_database(self, new_rule_migration_db_window):
            database = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.database["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(database, "Base de datos")

        def test_migration(self, new_rule_migration_db_window):
            migration = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.migration["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(migration, "Migración")

        def test_months(self, new_rule_migration_db_window):
            months = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.months["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(months, "meses")

        def test_create(self, new_rule_migration_db_window):
            create = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.create["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(create, "Crear")

        def test_gb(self, new_rule_migration_db_window):
            gb = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.gb["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(gb, "GB.")

        def test_add_button(self, new_rule_migration_db_window):
            add_button = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.add_button["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(add_button, "Añadir")

        def test_cancel_button(self, new_rule_migration_db_window):
            cancel_button = (
                new_rule_migration_db_window.by(
                    name=DBBackupAndMigrationPage.cancel_button["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Cancelar")

    @allure.story("тест окна настройки правил архивации БД")
    class TestAddNewRuleBackupDBWindow:
        def test_new_rule(self, new_rule_backup_db_window):
            new_rule3 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.new_rule3["title_es"],
                    found_index=DBBackupAndMigrationPage.new_rule3["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule3, "Nueva regla")

        def test_database2(self, new_rule_backup_db_window):
            database2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.database2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(database2, "Base de datos")

        def test_backup(self, new_rule_backup_db_window):
            backup = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.backup["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(backup, "Copia de seguridad")

        def test_back_up_objects(self, new_rule_backup_db_window):
            back_up_objects = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.back_up_objects["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_objects,
                "Archivar los objetos, cuando se cumplan las condiciones (los objetos se borran después de archivar)",
            )

        def test_back_up_all_objects(self, new_rule_backup_db_window):
            back_up_all_objects = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.back_up_all_objects["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_all_objects,
                "Archivar todas los objetos, excepto las activas (los objetos se guardan después de archivar)",
            )

        def test_months2(self, new_rule_backup_db_window):
            months2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.months2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(months2, "meses")

        def test_create2(self, new_rule_backup_db_window):
            create2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.create2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(create2, "Crear")

        def test_gb2(self, new_rule_backup_db_window):
            gb2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.gb2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(gb2, "GB.")

        def test_add_button2(self, new_rule_backup_db_window):
            add_button2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.add_button2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(add_button2, "Añadir")

        def test_cancel_button2(self, new_rule_backup_db_window):
            cancel_button2 = (
                new_rule_backup_db_window.by(
                    name=DBBackupAndMigrationPage.cancel_button2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button2, "Cancelar")

    @allure.story("тест окна настройки правил переноса индекса")
    class TestAddNewRuleMigrationIndexWindow:
        def test_new_rule4(self, new_rule_migration_index_window):
            new_rule4 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.new_rule2["title_es"],
                    found_index=DBBackupAndMigrationPage.new_rule4["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule4, "Nueva regla")

        def test_index(self, new_rule_migration_index_window):
            index = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.index["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(index, "Índice")

        def test_migration2(self, new_rule_migration_index_window):
            migration2 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.migration2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(migration2, "Migración")

        def test_months3(self, new_rule_migration_index_window):
            months3 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.months3["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(months3, "meses")

        def test_create3(self, new_rule_migration_index_window):
            create3 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.create3["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(create3, "Crear")

        def test_add_button3(self, new_rule_migration_index_window):
            add_button3 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.add_button3["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(add_button3, "Añadir")

        def test_cancel_button3(self, new_rule_migration_index_window):
            cancel_button3 = (
                new_rule_migration_index_window.by(
                    name=DBBackupAndMigrationPage.cancel_button3["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button3, "Cancelar")

    @allure.story("тест окна настройки правил архивации индекса")
    class TestAddNewRuleBackupIndexWindow:
        def test_new_rule6(self, new_rule_backup_index_window):
            new_rule6 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.new_rule6["title_es"],
                    found_index=DBBackupAndMigrationPage.new_rule6["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule6, "Nueva regla")

        def test_index2(self, new_rule_backup_index_window):
            index2 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.index2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(index2, "Índice")

        def test_backup2(self, new_rule_backup_index_window):
            backup2 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.backup2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(backup2, "Copia de seguridad")

        def test_back_up_objects2(self, new_rule_backup_index_window):
            back_up_objects2 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.back_up_objects2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_objects2,
                "Archivar los objetos, cuando se cumplan las condiciones",
            )

        def test_back_up_all_objects2(self, new_rule_backup_index_window):
            back_up_all_objects2 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.back_up_all_objects2["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_all_objects2, "Archivar todas los objetos, excepto las activas"
            )

        def test_months5(self, new_rule_backup_index_window):
            months5 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.months5["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(months5, "meses")

        def test_create5(self, new_rule_backup_index_window):
            create5 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.create5["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(create5, "Crear")

        def test_add_button5(self, new_rule_backup_index_window):
            add_button5 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.add_button5["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(add_button5, "Añadir")

        def test_cancel_button5(self, new_rule_backup_index_window):
            cancel_button5 = (
                new_rule_backup_index_window.by(
                    name=DBBackupAndMigrationPage.cancel_button5["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button5, "Cancelar")

    @allure.story("тест окна настройки правил переноса хранилица")
    class TestAddNewRuleMigrationStorageWindow:
        def test_new_rule5(self, new_rule_migration_storage_window):
            new_rule5 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.new_rule5["title_es"],
                    found_index=DBBackupAndMigrationPage.new_rule5["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule5, "Nueva regla")

        def test_storage(self, new_rule_migration_storage_window):
            storage = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.storage["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(storage, "Almacenamiento")

        def test_migration3(self, new_rule_migration_storage_window):
            migration3 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.migration3["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(migration3, "Migración")

        def test_months4(self, new_rule_migration_storage_window):
            months4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.months4["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(months4, "meses")

        def test_create4(self, new_rule_migration_storage_window):
            create4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.create4["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(create4, "Crear")

        def test_gb3(self, new_rule_migration_storage_window):
            gb3 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.gb3["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(gb3, "GB.")

        def test_add_button4(self, new_rule_migration_storage_window):
            add_button4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.add_button4["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(add_button4, "Añadir")

        def test_cancel_button4(self, new_rule_migration_storage_window):
            cancel_button4 = (
                new_rule_migration_storage_window.by(
                    name=DBBackupAndMigrationPage.cancel_button4["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button4, "Cancelar")

    @allure.story("тест окна настройки правил архивации хранилища")
    class TestAddNewRuleBackupStorageWindow:
        def test_new_rule7(self, new_rule_backup_storage_window):
            new_rule7 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.new_rule7["title_es"],
                    found_index=DBBackupAndMigrationPage.new_rule7["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(new_rule7, "Nueva regla")

        def test_storage2(self, new_rule_backup_storage_window):
            storage2 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.storage2["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(storage2, "Almacenamiento")

        def test_backup3(self, new_rule_backup_storage_window):
            backup3 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.backup3["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(backup3, "Copia de seguridad")

        def test_back_up_objects3(self, new_rule_backup_storage_window):
            back_up_objects3 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.back_up_objects3["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_objects3,
                "Archivar los objetos, cuando se cumplan las condiciones (los objetos se borran después de archivar)",
            )

        def test_back_up_all_objects3(self, new_rule_backup_storage_window):
            back_up_all_objects3 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.back_up_all_objects3["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(
                back_up_all_objects3,
                "Archivar todas los objetos, excepto las activas (los objetos se guardan después de archivar)",
            )

        def test_months6(self, new_rule_backup_storage_window):
            months6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.months6["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(months6, "meses")

        def test_create6(self, new_rule_backup_storage_window):
            create6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.create6["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(create6, "Crear")

        def test_gb4(self, new_rule_backup_storage_window):
            gb4 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.gb4["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(gb4, "GB.")

        def test_add_button6(self, new_rule_backup_storage_window):
            add_button6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.add_button6["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(add_button6, "Añadir")

        def test_cancel_button6(self, new_rule_backup_storage_window):
            cancel_button6 = (
                new_rule_backup_storage_window.by(
                    name=DBBackupAndMigrationPage.cancel_button6["title_es"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel_button6, "Cancelar")
