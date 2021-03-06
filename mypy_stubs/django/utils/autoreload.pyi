# Stubs for django.utils.autoreload (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

USE_INOTIFY: bool
fd: Any
RUN_RELOADER: bool
FILE_MODIFIED: int
I18N_MODIFIED: int

def gen_filenames(only_new: bool = ...): ...
def clean_files(filelist: Any): ...
def reset_translations() -> None: ...
def inotify_code_changed(): ...
def code_changed(): ...
def check_errors(fn: Any): ...
def raise_last_exception() -> None: ...
def ensure_echo_on() -> None: ...
def reloader_thread() -> None: ...
def restart_with_reloader(): ...
def python_reloader(main_func: Any, args: Any, kwargs: Any) -> None: ...
def main(main_func: Any, args: Optional[Any] = ..., kwargs: Optional[Any] = ...) -> None: ...
