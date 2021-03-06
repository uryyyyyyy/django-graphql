# Stubs for django.template.library (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .base import Node, Template, token_kwargs
from .exceptions import TemplateSyntaxError
from typing import Any, Optional

class InvalidTemplateLibrary(Exception): ...

class Library:
    filters: Any = ...
    tags: Any = ...
    def __init__(self) -> None: ...
    def tag(self, name: Optional[Any] = ..., compile_function: Optional[Any] = ...): ...
    def tag_function(self, func: Any): ...
    def filter(self, name: Optional[Any] = ..., filter_func: Optional[Any] = ..., **flags: Any): ...
    def filter_function(self, func: Any, **flags: Any): ...
    def simple_tag(self, func: Optional[Any] = ..., takes_context: Optional[Any] = ..., name: Optional[Any] = ...): ...
    def inclusion_tag(self, filename: Any, func: Optional[Any] = ..., takes_context: Optional[Any] = ..., name: Optional[Any] = ...): ...

class TagHelperNode(Node):
    func: Any = ...
    takes_context: Any = ...
    args: Any = ...
    kwargs: Any = ...
    def __init__(self, func: Any, takes_context: Any, args: Any, kwargs: Any) -> None: ...
    def get_resolved_arguments(self, context: Any): ...

class SimpleNode(TagHelperNode):
    target_var: Any = ...
    def __init__(self, func: Any, takes_context: Any, args: Any, kwargs: Any, target_var: Any) -> None: ...
    def render(self, context: Any): ...

class InclusionNode(TagHelperNode):
    filename: Any = ...
    def __init__(self, func: Any, takes_context: Any, args: Any, kwargs: Any, filename: Any) -> None: ...
    def render(self, context: Any): ...

def parse_bits(parser: Any, bits: Any, params: Any, varargs: Any, varkw: Any, defaults: Any, kwonly: Any, kwonly_defaults: Any, takes_context: Any, name: Any): ...
def import_library(name: Any): ...
