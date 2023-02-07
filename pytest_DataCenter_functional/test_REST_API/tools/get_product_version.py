# Standart libraries
from pathlib import Path
from typing import Union

# Third party packages
from win32api import HIWORD, LOWORD, GetFileVersionInfo


def get_file_version(filename: Union[str, Path]) -> str:
    """вернуть версию файла (например, 5.19.1.9)"""
    info = GetFileVersionInfo(str(filename), "\\")
    ms, ls = info["FileVersionMS"], info["FileVersionLS"]
    return f"{HIWORD(ms)}.{LOWORD(ms)}.{HIWORD(ls)}.{LOWORD(ls)}"
