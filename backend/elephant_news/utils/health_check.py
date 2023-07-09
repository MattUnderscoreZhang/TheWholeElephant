import os
from rich.console import Console
from typing import Any

from elephant_news.root import ROOT_DIR


def compare_test_log(filename: str, contents: str, overwrite: bool = False) -> bool:
    filepath = os.path.join(ROOT_DIR, 'tests', 'logs', f'{filename}.log')
    if overwrite:
        with open(filepath, 'w') as f:
            f.write(contents)
        return True
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return f.read() == contents
    return False


def save_test_log(filename: str, contents: str) -> None:
    compare_test_log(filename, contents, overwrite=True)


def get_rich_print(contents: Any) -> str:
    console = Console()
    with console.capture() as capture:
        console.print(contents)
    return capture.get()
