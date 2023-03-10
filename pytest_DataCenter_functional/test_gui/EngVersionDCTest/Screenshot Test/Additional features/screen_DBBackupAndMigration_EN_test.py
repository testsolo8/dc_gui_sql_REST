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
from DataCenter.locators.path_to_screenshots import PathToScreenshotsEN
from DataCenter.tools.take_screen import make_screenshot_if_error


@pytest.fixture(scope="class")
def new_migration_db_rule_window(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_en"]).click()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_backup_db_rule_window(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(name=DBBackupAndMigrationPage.new_rule["title_en"]).click()
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.fixture(scope="class")
def new_migration_index_rule_window(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page_en
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
def new_backup_index_rule_window(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page_en
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
def new_migration_storage_rule_window(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page_en
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
def new_backup_storage_rule_window(start_screen_test_page_en):
    send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
    app = start_screen_test_page_en
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


@pytest.mark.order(2)
@allure.epic("ENG Screenshot Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestScreensEN
@pytest.mark.testGUI_EngVersionDCTest_ScreensTest_Additionalfeatures
class TestDBBackupAndMigrationPage:
    @allure.story("???????? ???????????????? ???????? ???????????? ???????????????? ?? ??????????????????????????")
    class TestDBBackupAndMigrationMainPage:
        def test_db_backup_and_migration_page_screen(self, start_screen_test_page_en):
            send_keys("{VK_MENU down}Y4Y05{VK_MENU up}")
            time.sleep(2)
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.db_backup_and_migration["path"],
                confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("???????? ???????????? ???????? ?????????????????? ???????????????? ????")
    class TestAddNewMigrationDBRuleWindow:
        def test_new_migration_db_rule_window(self, new_migration_db_rule_window):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.db_backup_and_migration_add_new_migration_db_rule_window[
                    "path"
                ],
                # confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("???????? ???????????? ???????? ?????????????????? ?????????????????????????? ????")
    class TestAddNewBackupDBRuleWindow:
        def test_new_backup_db_rule_window(self, new_backup_db_rule_window):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.db_backup_and_migration_add_new_backup_db_rule_window[
                    "path"
                ],
                # confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("???????? ???????????? ???????? ?????????????????? ???????????????? ??????????????")
    class TestAddNewMigrationIndexRuleWindow:
        def test_new_migration_index_rule_window(self, new_migration_index_rule_window):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.db_backup_and_migration_add_new_migration_index_rule_window[
                    "path"
                ],
                # confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("???????? ???????????? ???????? ?????????????????? ?????????????????????????? ??????????????")
    class TestAddNewBackupIndexRuleWindow:
        def test_new_backup_index_rule_window(self, new_backup_index_rule_window):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.db_backup_and_migration_add_new_backup_index_rule_window[
                    "path"
                ],
                # confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("???????? ???????????? ???????? ?????????????????? ???????????????? ??????????????????")
    class TestAddNewMigrationStorageRuleWindow:
        def test_new_migration_storage_rule_window(
            self, new_migration_storage_rule_window
        ):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.db_backup_and_migration_add_new_migration_storage_rule_window[
                    "path"
                ],
                # confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))

    @allure.story("???????? ???????????? ???????? ?????????????????? ?????????????????????????? ??????????????????")
    class TestAddNewBackupStorageRuleWindow:
        def test_new_backup_storage_rule_window(self, new_backup_storage_rule_window):
            screenshot = pyautogui.locateOnScreen(
                PathToScreenshotsEN.db_backup_and_migration_add_new_backup_storage_rule_window[
                    "path"
                ],
                # confidence=LevelOfConfidence.confidence["confidence"],
            )
            make_screenshot_if_error(check.is_not_none(screenshot))
