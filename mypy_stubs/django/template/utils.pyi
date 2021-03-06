# Stubs for django.template.utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.exceptions import ImproperlyConfigured
from typing import Any, Optional

class InvalidTemplateEngineError(ImproperlyConfigured): ...

class EngineHandler:
    def __init__(self, templates: Optional[Any] = ...) -> None: ...
    def templates(self): ...
    def __getitem__(self, alias: Any): ...
    def __iter__(self): ...
    def all(self): ...

def get_app_template_dirs(dirname: Any): ...
