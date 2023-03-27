# Standart libraries
import time

# Third party packages
import allure
import pytest
import pywinauto.mouse as mouse
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import DBBackupAndMigrationPage
from DataCenter.tools.take_screen import take_screenshot_with_elements


@pytest.fixture(scope="class")
def new_migration_db_rule_window(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule[title_key]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_backup_db_rule_window(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule[title_key]).click()
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_migration_index_rule_window(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page
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
def new_backup_index_rule_window(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page
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
def new_migration_storage_rule_window(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page
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
def new_backup_storage_rule_window(start_screen_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page
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


@pytest.mark.order(2)
@allure.epic("Screenshot Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestScreens
@pytest.mark.testGUI_DCTest_ScreensTest_Additionalfeatures
class TestDBBackupAndMigrationPage:
    @allure.story("тест главного окна правил переноса и архивирования")
    class TestDBBackupAndMigrationMainPage:
        def test_db_backup_and_migration_screen(self, start_screen_test_page, assert_snapshot, lang_parametrize):
            send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
            time.sleep(2)
            mouse.move(coords=(0, 0))
            app = start_screen_test_page
            window = app.window(name_re="DataCenter*")
            time.sleep(1)
            elements = [
                {"name": "TitleBar", "element": window.TitleBar},
            ]
            screenshot = take_screenshot_with_elements(window, elements=elements)
            assert_snapshot(screenshot)

    @allure.story("тест скрина окна настройки переноса БД")
    class TestAddNewMigrationDBRuleWindow:
        def test_new_migration_db_rule_window(self, new_migration_db_rule_window, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = new_migration_db_rule_window
            window = handle.by(
                name=DBBackupAndMigrationPage.new_rule2[title_key],
                found_index=DBBackupAndMigrationPage.new_rule2["found_index"],
            )
            time.sleep(1)
            elements = [
                {
                    "name": "DateEdit",
                    "element": window.Pane1.by(class_name="TcxDateEdit", control_type="Pane", found_index=0),
                }
            ]
            screenshot = take_screenshot_with_elements(window, elements=elements)
            assert_snapshot(screenshot)

    @allure.story("тест скрина окна настройки архивирования БД")
    class TestAddNewBackupDBRuleWindow:
        def test_new_backup_db_rule_window(self, new_backup_db_rule_window, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = new_backup_db_rule_window
            window = handle.by(
                name=DBBackupAndMigrationPage.new_rule3[title_key],
                found_index=DBBackupAndMigrationPage.new_rule3["found_index"],
            )
            time.sleep(1)
            elements = [
                {
                    "name": "DateEdit",
                    "element": window.Pane1.by(class_name="TcxDateEdit", control_type="Pane", found_index=0),
                }
            ]
            screenshot = take_screenshot_with_elements(window, elements=elements)
            assert_snapshot(screenshot)

    @allure.story("тест скрина окна настройки переноса индекса")
    class TestAddNewMigrationIndexRuleWindow:
        def test_new_migration_index_rule_window(self, new_migration_index_rule_window, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = new_migration_index_rule_window
            window = handle.by(
                name=DBBackupAndMigrationPage.new_rule4[title_key],
                found_index=DBBackupAndMigrationPage.new_rule4["found_index"],
            )
            time.sleep(1)
            elements = [
                {
                    "name": "DateEdit",
                    "element": window.Pane1.by(class_name="TcxDateEdit", control_type="Pane", found_index=0),
                }
            ]
            screenshot = take_screenshot_with_elements(window, elements=elements)
            assert_snapshot(screenshot)

    @allure.story("тест скрина окна настройки архивирования индекса")
    class TestAddNewBackupIndexRuleWindow:
        def test_new_backup_index_rule_window(self, new_backup_index_rule_window, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = new_backup_index_rule_window
            window = handle.by(
                name=DBBackupAndMigrationPage.new_rule6[title_key],
                found_index=DBBackupAndMigrationPage.new_rule6["found_index"],
            )
            time.sleep(1)
            elements = [
                {
                    "name": "DateEdit",
                    "element": window.Pane1.by(class_name="TcxDateEdit", control_type="Pane", found_index=0),
                }
            ]
            screenshot = take_screenshot_with_elements(window, elements=elements)
            assert_snapshot(screenshot)

    @allure.story("тест скрина окна настройки переноса хранилища")
    class TestAddNewMigrationStorageRuleWindow:
        def test_new_migration_storage_rule_window(self, new_migration_storage_rule_window, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = new_migration_storage_rule_window
            window = handle.by(
                name=DBBackupAndMigrationPage.new_rule5[title_key],
                found_index=DBBackupAndMigrationPage.new_rule5["found_index"],
            )
            time.sleep(1)
            elements = [
                {
                    "name": "DateEdit",
                    "element": window.Pane1.by(class_name="TcxDateEdit", control_type="Pane", found_index=0),
                }
            ]
            screenshot = take_screenshot_with_elements(window, elements=elements)
            assert_snapshot(screenshot)

    @allure.story("тест скрина окна настройки архивирования хранилища")
    class TestAddNewBackupStorageRuleWindow:
        def test_new_backup_storage_rule_window(self, new_backup_storage_rule_window, assert_snapshot, title_key):
            mouse.move(coords=(0, 0))
            handle = new_backup_storage_rule_window
            window = handle.by(
                name=DBBackupAndMigrationPage.new_rule7[title_key],
                found_index=DBBackupAndMigrationPage.new_rule7["found_index"],
            )
            time.sleep(1)
            elements = [
                {
                    "name": "DateEdit",
                    "element": window.Pane1.by(class_name="TcxDateEdit", control_type="Pane", found_index=0),
                }
            ]
            screenshot = take_screenshot_with_elements(window, elements=elements)
            assert_snapshot(screenshot)
