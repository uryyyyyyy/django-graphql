# Stubs for django.forms.utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import UserList
from typing import Any, Optional

def pretty_name(name: Any): ...
def flatatt(attrs: Any): ...

class ErrorDict(dict):
    def as_data(self): ...
    def get_json_data(self, escape_html: bool = ...): ...
    def as_json(self, escape_html: bool = ...): ...
    def as_ul(self): ...
    def as_text(self): ...

class ErrorList(UserList, list): # type: ignore
    error_class: str = ...
    def __init__(self, initlist: Optional[Any] = ..., error_class: Optional[Any] = ...) -> None: ...
    def as_data(self): ...
    def get_json_data(self, escape_html: bool = ...): ...
    def as_json(self, escape_html: bool = ...): ...
    def as_ul(self): ...
    def as_text(self): ...
    def __contains__(self, item: Any): ...
    def __eq__(self, other: Any): ...
    def __getitem__(self, i: Any): ...
    def __reduce_ex__(self, *args: Any, **kwargs: Any): ...

def from_current_timezone(value: Any): ...
def to_current_timezone(value: Any): ...
