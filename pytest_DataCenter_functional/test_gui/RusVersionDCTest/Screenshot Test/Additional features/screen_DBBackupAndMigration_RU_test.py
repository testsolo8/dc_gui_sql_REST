# Standart libraries
import time

# Third party packages
import allure
import pyautogui
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import DBBackupAndMigrationPage
from DataCenter.locators.confidence import LevelOfConfidence
from DataCenter.locators.path_to_screenshots import PathToScreenshotsRU
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.fixture(scope="class")
def new_migration_db_rule_window(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_ru"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_backup_db_rule_window(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_ru"]).click()
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_migration_index_rule_window(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page_ru
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
def new_backup_index_rule_window(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page_ru
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
def new_migration_storage_rule_window(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page_ru
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
def new_backup_storage_rule_window(start_screen_test_page_ru):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page_ru
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


@pytest.mark.order(2)
@allure.epic("RUS Screenshot Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestScreensRU
@pytest.mark.testGUI_RusVersionDCTest_ScreensTest_Additionalfeatures
class TestDBBackupAndMigrationPage:
    @allure.story("тест главного окна правил переноса и архивирования")
    class TestDBBackupAndMigrationMainPage:
        def test_db_backup_and_migration_page_screen(self, start_screen_test_page_ru):
            send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
            time.sleep(2)
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.db_backup_and_migration["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест скрина окна настройки нового правила переноса БД")
    class TestAddNewMigrationDBRuleWindow:
        def test_new_migration_db_rule_window(self, new_migration_db_rule_window):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.db_backup_and_migration_add_new_migration_db_rule_window[
                    "path"
                ],
                # confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест скрина окна настройки архивирования БД")
    class TestAddNewBackupDBRuleWindow:
        def test_new_backup_db_rule_window(self, new_backup_db_rule_window):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.db_backup_and_migration_add_new_backup_db_rule_window[
                    "path"
                ],
                # confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест скрина окна настройки переноса индекса")
    class TestAddNewMigrationIndexRuleWindow:
        def test_new_migration_index_rule_window(self, new_migration_index_rule_window):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.db_backup_and_migration_add_new_migration_index_rule_window[
                    "path"
                ],
                # confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест скрина окна настройки архивирования индекса")
    class TestAddNewBackupIndexRuleWindow:
        def test_new_backup_index_rule_window(self, new_backup_index_rule_window):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.db_backup_and_migration_add_new_backup_index_rule_window[
                    "path"
                ],
                # confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест скрина окна настройки переноса хранилища")
    class TestAddNewMigrationStorageRuleWindow:
        def test_new_migration_storage_rule_window(
            self, new_migration_storage_rule_window
        ):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.db_backup_and_migration_add_new_migration_storage_rule_window[
                    "path"
                ],
                # confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("тест скрина окна настройки архивирования хранилища")
    class TestAddNewBackupStorageRuleWindow:
        def test_new_backup_storage_rule_window(self, new_backup_storage_rule_window):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsRU.db_backup_and_migration_add_new_backup_storage_rule_window[
                    "path"
                ],
                # confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))
