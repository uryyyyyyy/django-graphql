# Stubs for django.template.base (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .exceptions import TemplateSyntaxError
from enum import Enum
from typing import Any, Optional

FILTER_SEPARATOR: str
FILTER_ARGUMENT_SEPARATOR: str
VARIABLE_ATTRIBUTE_SEPARATOR: str
BLOCK_TAG_START: str
BLOCK_TAG_END: str
VARIABLE_TAG_START: str
VARIABLE_TAG_END: str
COMMENT_TAG_START: str
COMMENT_TAG_END: str
TRANSLATOR_COMMENT_MARK: str
SINGLE_BRACE_START: str
SINGLE_BRACE_END: str
UNKNOWN_SOURCE: str
tag_re: Any
logger: Any

class TokenType(Enum):
    TEXT: int = ...
    VAR: int = ...
    BLOCK: int = ...
    COMMENT: int = ...

class VariableDoesNotExist(Exception):
    msg: Any = ...
    params: Any = ...
    def __init__(self, msg: Any, params: Any = ...) -> None: ...

class Origin:
    name: Any = ...
    template_name: Any = ...
    loader: Any = ...
    def __init__(self, name: Any, template_name: Optional[Any] = ..., loader: Optional[Any] = ...) -> None: ...
    def __eq__(self, other: Any): ...
    @property
    def loader_name(self): ...

class Template:
    name: Any = ...
    origin: Any = ...
    engine: Any = ...
    source: Any = ...
    nodelist: Any = ...
    def __init__(self, template_string: Any, origin: Optional[Any] = ..., name: Optional[Any] = ..., engine: Optional[Any] = ...) -> None: ...
    def __iter__(self) -> None: ...
    def render(self, context: Any): ...
    def compile_nodelist(self): ...
    def get_exception_info(self, exception: Any, token: Any): ...

def linebreak_iter(template_source: Any) -> None: ...

class Token:
    lineno: Any = ...
    position: Any = ...
    def __init__(self, token_type: Any, contents: Any, position: Optional[Any] = ..., lineno: Optional[Any] = ...) -> None: ...
    def split_contents(self): ...

class Lexer:
    template_string: Any = ...
    verbatim: bool = ...
    def __init__(self, template_string: Any) -> None: ...
    def tokenize(self): ...
    def create_token(self, token_string: Any, position: Any, lineno: Any, in_tag: Any): ...

class DebugLexer(Lexer):
    def tokenize(self): ...

class Parser:
    tokens: Any = ...
    tags: Any = ...
    filters: Any = ...
    command_stack: Any = ...
    libraries: Any = ...
    origin: Any = ...
    def __init__(self, tokens: Any, libraries: Optional[Any] = ..., builtins: Optional[Any] = ..., origin: Optional[Any] = ...) -> None: ...
    def parse(self, parse_until: Optional[Any] = ...): ...
    def skip_past(self, endtag: Any) -> None: ...
    def extend_nodelist(self, nodelist: Any, node: Any, token: Any) -> None: ...
    def error(self, token: Any, e: Any): ...
    def invalid_block_tag(self, token: Any, command: Any, parse_until: Optional[Any] = ...) -> None: ...
    def unclosed_block_tag(self, parse_until: Any) -> None: ...
    def next_token(self): ...
    def prepend_token(self, token: Any) -> None: ...
    def delete_first_token(self) -> None: ...
    def add_library(self, lib: Any) -> None: ...
    def compile_filter(self, token: Any): ...
    def find_filter(self, filter_name: Any): ...

constant_string: Any
filter_raw_string: Any
filter_re: Any

class FilterExpression:
    token: Any = ...
    filters: Any = ...
    var: Any = ...
    def __init__(self, token: Any, parser: Any) -> None: ...
    def resolve(self, context: Any, ignore_failures: bool = ...): ...
    def args_check(name: Any, func: Any, provided: Any): ...
    args_check: Any = ...

class Variable:
    var: Any = ...
    literal: Any = ...
    lookups: Any = ...
    translate: bool = ...
    message_context: Any = ...
    def __init__(self, var: Any) -> None: ...
    def resolve(self, context: Any): ...

class Node:
    must_be_first: bool = ...
    child_nodelists: Any = ...
    token: Any = ...
    def render(self, context: Any) -> None: ...
    def render_annotated(self, context: Any): ...
    def __iter__(self) -> None: ...
    def get_nodes_by_type(self, nodetype: Any): ...

class NodeList(list):
    contains_nontext: bool = ...
    def render(self, context: Any): ...
    def get_nodes_by_type(self, nodetype: Any): ...

class TextNode(Node):
    s: Any = ...
    def __init__(self, s: Any) -> None: ...
    def render(self, context: Any): ...

def render_value_in_context(value: Any, context: Any): ...

class VariableNode(Node):
    filter_expression: Any = ...
    def __init__(self, filter_expression: Any) -> None: ...
    def render(self, context: Any): ...

kwarg_re: Any

def token_kwargs(bits: Any, parser: Any, support_legacy: bool = ...): ...