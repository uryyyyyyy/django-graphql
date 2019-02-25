# Stubs for django.urls.converters (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class IntConverter:
    regex: str = ...
    def to_python(self, value: Any): ...
    def to_url(self, value: Any): ...

class StringConverter:
    regex: str = ...
    def to_python(self, value: Any): ...
    def to_url(self, value: Any): ...

class UUIDConverter:
    regex: str = ...
    def to_python(self, value: Any): ...
    def to_url(self, value: Any): ...

class SlugConverter(StringConverter):
    regex: str = ...

class PathConverter(StringConverter):
    regex: str = ...

DEFAULT_CONVERTERS: Any
REGISTERED_CONVERTERS: Any

def register_converter(converter: Any, type_name: Any) -> None: ...
def get_converters(): ...
def get_converter(raw_converter: Any): ...