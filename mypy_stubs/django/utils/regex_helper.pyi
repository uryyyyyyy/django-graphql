# Stubs for django.utils.regex_helper (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

ESCAPE_MAPPINGS: Any

class Choice(list): ...
class Group(list): ...
class NonCapture(list): ...

def normalize(pattern: Any): ...
def next_char(input_iter: Any) -> None: ...
def walk_to_end(ch: Any, input_iter: Any) -> None: ...
def get_quantifier(ch: Any, input_iter: Any): ...
def contains(source: Any, inst: Any): ...
def flatten_result(source: Any): ...