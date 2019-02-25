# Stubs for django.utils._os (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from os.path import abspath
from typing import Any

abspathu = abspath

def upath(path: Any): ...
def npath(path: Any): ...
def safe_join(base: Any, *paths: Any): ...
def symlinks_supported(): ...