# Standart libraries
import logging
import os
import shutil
from io import BytesIO
from pathlib import Path
from typing import Any
import time

# Third party packages
import psutil
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch
from pywinauto import Application

# Third party packages
import allure
import pytest


@pytest.fixture(scope="session", params=["eng", "es", "rus"], ids=["english version", "spanish version", "russian version"])
def lang_parametrize(request):
    return request.param


@pytest.fixture(scope="session")
def title_key(lang_parametrize):
    return f"title_{lang_parametrize}"


@pytest.fixture(scope="function")
def assert_snapshot(request: Any):
    test_name = f"{str(Path(request.node.name))}"
    test_dir = str(Path(request.node.name)).split("[", 1)[0]

    def compare(img: bytes, *, threshold: float = 0.1, name=f"{test_name}.png", fail_fast=False):
        test_file_name = str(os.path.basename(Path(request.node.fspath))).strip(".py")
        filepath = Path(request.node.fspath).parent.resolve() / "screenshots" / test_file_name / test_dir
        filepath.mkdir(parents=True, exist_ok=True)
        file = filepath / name
        # Create a dir where all screenshot test failures will go
        results_dir_name = Path(request.node.fspath).parent.resolve() / "screenshot_tests_failures"
        test_results_dir = results_dir_name / test_file_name / test_name
        # Remove a single test's past run dir with actual, diff and expected images
        if test_results_dir.exists():
            shutil.rmtree(test_results_dir)
        if not file.exists():
            file.write_bytes(img)
            pytest.fail("--> New screenshot(s) created. Please review images")
        img_a = Image.open(BytesIO(img))
        img_b = Image.open(file)
        img_diff = Image.new("RGBA", img_a.size)
        mismatch = pixelmatch(img_a, img_b, img_diff, threshold=threshold, fail_fast=fail_fast)
        if mismatch == 0:
            return
        else:
            with allure.step("ERROR Screenshot"):
                # Create new test_results folder
                test_results_dir.mkdir(parents=True, exist_ok=True)
                img_diff.save(test_results_dir / f"Diff_{name}")
                img_a.save(test_results_dir / f"Actual_{name}")
                img_b.save(test_results_dir / f"Expected_{name}")
                if os.path.isdir(test_results_dir):
                    for file_name in os.listdir(test_results_dir):
                        if file_name.endswith(".png"):
                            file_path = os.path.join(test_results_dir, file_name)
                            with open(file_path, "rb") as file:
                                allure.attach(file.read(), name=file_name, attachment_type=allure.attachment_type.PNG)
                pytest.fail("--> Screenshots DO NOT match!")

    return compare


@pytest.fixture(scope="module")
def start_screen_test_page(lang_parametrize):
    # Check if DCClient.exe is open
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            if proc.name() == "DCClient.exe":
                proc.kill()
        except Exception as ex:
            logging.debug(ex)
    # Start DCClient.exe
    app = Application().start(
        cmd_line=f"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe -L={lang_parametrize}",
        timeout=5,
    )
    app = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    main_dlg = app.window(name_re=".*Dcclient.*", found_index=0)
    main_dlg.find(timeout=120, retry_interval=2).wait_visible(timeout=120, retry_interval=2)
    time.sleep(2)
    main_dlg.OK.click()
    main_win = app.window(name_re="DataCenter*")
    main_win.find(timeout=120, retry_interval=2).wait_visible(timeout=120, retry_interval=2)
    # # Выставляем минимальный размер окна
    main_win.move_window(x=50, y=20, width=800, height=600)
    app = Application(backend="uia").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    yield app
    # Закрытие клиента DC
    app.kill()


