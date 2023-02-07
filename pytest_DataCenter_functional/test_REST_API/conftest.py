# Standart libraries
import logging
import time
from threading import Event, Thread

# Third party packages
import pytest
from common.autotestAPI import autotestAPI

# My packages
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import DcApiWithToken
from tools.dc_base_url import DcApiWithToken


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


@pytest.fixture(scope="session")
def dc_api():
    return DcApiWithToken()
