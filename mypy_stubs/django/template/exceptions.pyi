# Stubs for django.template.exceptions (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class TemplateDoesNotExist(Exception):
    backend: Any = ...
    tried: Any = ...
    chain: Any = ...
    def __init__(self, msg: Any, tried: Optional[Any] = ..., backend: Optional[Any] = ..., chain: Optional[Any] = ...) -> None: ...

class TemplateSyntaxError(Exception): ...