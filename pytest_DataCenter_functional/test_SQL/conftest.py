# Standart libraries
import logging
import time
from threading import Event, Thread

# Third party packages
import psutil
import pytest
from common.autotestAPI import autotestAPI
from pywinauto import Application

# My packages
from pytest_DataCenter_functional.test_SQL.sql_tools import Docker


class TaskNeedTerminateWatcher(Thread):
    def __init__(self, need_terminate_watcher):
        super().__init__()
        # Third party packages
        from common.config import task_config

        task_cfg = task_config()
        self.at_api = autotestAPI(
            task_cfg.server, task_cfg.taskID, task_cfg.taskGUID, task_cfg.destination
        )
        self.need_terminate_watcher = need_terminate_watcher

    def run(self):
        while not self.need_terminate_watcher.is_set():
            # logging.debug(f'pytest.need_skip_tests={pytest.need_skip_tests}')
            if not pytest.need_skip_tests:
                # если флаг уже был установлен, то смысла проверять нет
                is_task_need_kill = self.at_api.isTaskNeedKill()
                if is_task_need_kill:
                    logging.warning(
                        "The flag of the need to complete the task for testing is set"
                    )
                    pytest.need_skip_tests = is_task_need_kill
            time.sleep(30)


def pytest_configure(config):
    pytest.need_skip_tests = False


def pytest_runtest_setup(item):
    """если был поднят флаг необходимости терминирования задачи, то невыполненные тесты буду скипаться"""
    if pytest.need_skip_tests:
        logging.debug('Test is skipped (flag "need_skip_tests" is set)')
        pytest.skip("Задача на тестирование была прервана")


@pytest.fixture(scope="session", autouse=True)
def task_need_terminate():
    """запуск вотчера, определяющего необходимость завершения задачи"""
    need_terminate_watcher = Event()

    task_need_terminate_watcher = TaskNeedTerminateWatcher(need_terminate_watcher)
    task_need_terminate_watcher.start()

    yield

    need_terminate_watcher.set()
    task_need_terminate_watcher.join()  # FIXME возможен дедлок???


@pytest.fixture(scope="module")
def sql_test_page_ru():
    # Check if DCClient.exe is open
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            if proc.name() == "DCClient.exe":
                proc.kill()
        except Exception as ex:
            logging.debug(ex)
    # Start DCClient.exe
    app = Application().start(
        cmd_line=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe -L=RUS",
        timeout=5,
    )
    app = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    main_dlg = app.window(name_re=".*Dcclient.*", found_index=0)
    main_dlg.find(timeout=240, retry_interval=5).wait_visible(
        timeout=240, retry_interval=5
    )
    time.sleep(2)
    main_dlg.OK.click()
    main_win = app.window(name_re="DataCenter*")
    main_win.find(timeout=240, retry_interval=5).wait_visible(
        timeout=240, retry_interval=5
    )
    # # Максимизация окна (занимает время)
    main_win.maximize()
    time.sleep(2)
    app = Application(backend="uia").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    yield app
    # Закрытие клиента DC
    app.kill()


@pytest.fixture(scope="session", autouse=True)
def start_stop_docker():
    Docker().start_mssql()
    Docker().start_mssql_spec()
    Docker().start_postgresql()
    Docker().start_postgresql_spec()
    yield
    Docker().stop_mssql()
    Docker().stop_mssql_spec()
    Docker().stop_postgresql()
    Docker().stop_postgresql_spec()
