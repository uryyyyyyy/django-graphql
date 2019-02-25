# Stubs for django.utils.jslex (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class Tok:
    num: int = ...
    id: Any = ...
    name: Any = ...
    regex: Any = ...
    next: Any = ...
    def __init__(self, name: Any, regex: Any, next: Optional[Any] = ...) -> None: ...

def literals(choices: Any, prefix: str = ..., suffix: str = ...): ...

class Lexer:
    regexes: Any = ...
    toks: Any = ...
    state: Any = ...
    def __init__(self, states: Any, first: Any) -> None: ...
    def lex(self, text: Any) -> None: ...

class JsLexer(Lexer):
    both_before: Any = ...
    both_after: Any = ...
    states: Any = ...
    def __init__(self) -> None: ...

def prepare_js_for_gettext(js: Any): ...
