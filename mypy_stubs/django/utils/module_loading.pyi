# Stubs for django.utils.module_loading (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def import_string(dotted_path: Any): ...
def autodiscover_modules(*args: Any, **kwargs: Any) -> None: ...
def module_has_submodule(package: Any, module_name: Any): ...
def module_dir(module: Any): ...