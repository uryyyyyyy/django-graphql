# Stubs for django.db.models.functions.comparison (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.models import Func
from typing import Any

class Cast(Func):
    function: str = ...
    template: str = ...
    def __init__(self, expression: Any, output_field: Any) -> None: ...
    def as_sql(self, compiler: Any, connection: Any, **extra_context: Any): ...
    def as_mysql(self, compiler: Any, connection: Any): ...
    def as_postgresql(self, compiler: Any, connection: Any): ...

class Coalesce(Func):
    function: str = ...
    def __init__(self, *expressions: Any, **extra: Any) -> None: ...
    def as_oracle(self, compiler: Any, connection: Any): ...

class Greatest(Func):
    function: str = ...
    def __init__(self, *expressions: Any, **extra: Any) -> None: ...
    def as_sqlite(self, compiler: Any, connection: Any): ...

class Least(Func):
    function: str = ...
    def __init__(self, *expressions: Any, **extra: Any) -> None: ...
    def as_sqlite(self, compiler: Any, connection: Any): ...
