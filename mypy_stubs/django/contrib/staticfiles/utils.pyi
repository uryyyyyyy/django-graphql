# Stubs for django.contrib.staticfiles.utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def matches_patterns(path: Any, patterns: Optional[Any] = ...): ...
def get_files(storage: Any, ignore_patterns: Optional[Any] = ..., location: str = ...) -> None: ...
def check_settings(base_url: Optional[Any] = ...) -> None: ...
