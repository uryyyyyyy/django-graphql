# Stubs for django.template.backends.base (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class BaseEngine:
    name: Any = ...
    dirs: Any = ...
    app_dirs: Any = ...
    def __init__(self, params: Any) -> None: ...
    @property
    def app_dirname(self) -> None: ...
    def from_string(self, template_code: Any) -> None: ...
    def get_template(self, template_name: Any) -> None: ...
    def template_dirs(self): ...
    def iter_template_filenames(self, template_name: Any) -> None: ...
