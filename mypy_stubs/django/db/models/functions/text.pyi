# Stubs for django.db.models.functions.text (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.models import Func, Transform
from typing import Any, Optional

class BytesToCharFieldConversionMixin:
    def convert_value(self, value: Any, expression: Any, connection: Any): ...

class Chr(Transform):
    function: str = ...
    lookup_name: str = ...
    def as_mysql(self, compiler: Any, connection: Any): ...
    def as_oracle(self, compiler: Any, connection: Any): ...
    def as_sqlite(self, compiler: Any, connection: Any, **extra_context: Any): ...

class ConcatPair(Func):
    function: str = ...
    def as_sqlite(self, compiler: Any, connection: Any): ...
    def as_mysql(self, compiler: Any, connection: Any): ...
    def coalesce(self): ...

class Concat(Func):
    function: Any = ...
    template: str = ...
    def __init__(self, *expressions: Any, **extra: Any) -> None: ...

class Left(Func):
    function: str = ...
    arity: int = ...
    def __init__(self, expression: Any, length: Any, **extra: Any) -> None: ...
    def get_substr(self): ...
    def use_substr(self, compiler: Any, connection: Any, **extra_context: Any): ...
    as_oracle: Any = ...
    as_sqlite: Any = ...

class Length(Transform):
    function: str = ...
    lookup_name: str = ...
    output_field: Any = ...
    def as_mysql(self, compiler: Any, connection: Any): ...

class Lower(Transform):
    function: str = ...
    lookup_name: str = ...

class LPad(BytesToCharFieldConversionMixin, Func):
    function: str = ...
    def __init__(self, expression: Any, length: Any, fill_text: Any = ..., **extra: Any) -> None: ...

class LTrim(Transform):
    function: str = ...
    lookup_name: str = ...

class Ord(Transform):
    function: str = ...
    lookup_name: str = ...
    output_field: Any = ...
    def as_mysql(self, compiler: Any, connection: Any, **extra_context: Any): ...
    def as_sqlite(self, compiler: Any, connection: Any, **extra_context: Any): ...

class Repeat(BytesToCharFieldConversionMixin, Func):
    function: str = ...
    def __init__(self, expression: Any, number: Any, **extra: Any) -> None: ...
    def as_oracle(self, compiler: Any, connection: Any, **extra_context: Any): ...

class Replace(Func):
    function: str = ...
    def __init__(self, expression: Any, text: Any, replacement: Any = ..., **extra: Any) -> None: ...

class Right(Left):
    function: str = ...
    def get_substr(self): ...

class RPad(LPad):
    function: str = ...

class RTrim(Transform):
    function: str = ...
    lookup_name: str = ...

class StrIndex(Func):
    function: str = ...
    arity: int = ...
    output_field: Any = ...
    def as_postgresql(self, compiler: Any, connection: Any): ...

class Substr(Func):
    function: str = ...
    def __init__(self, expression: Any, pos: Any, length: Optional[Any] = ..., **extra: Any) -> None: ...
    def as_sqlite(self, compiler: Any, connection: Any): ...
    def as_oracle(self, compiler: Any, connection: Any): ...

class Trim(Transform):
    function: str = ...
    lookup_name: str = ...

class Upper(Transform):
    function: str = ...
    lookup_name: str = ...
