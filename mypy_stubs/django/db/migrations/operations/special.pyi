# Stubs for django.db.migrations.operations.special (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .base import Operation
from typing import Any, Optional

class SeparateDatabaseAndState(Operation):
    serialization_expand_args: Any = ...
    database_operations: Any = ...
    state_operations: Any = ...
    def __init__(self, database_operations: Optional[Any] = ..., state_operations: Optional[Any] = ...) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label: Any, state: Any) -> None: ...
    def database_forwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def database_backwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def describe(self): ...

class RunSQL(Operation):
    noop: str = ...
    sql: Any = ...
    reverse_sql: Any = ...
    state_operations: Any = ...
    hints: Any = ...
    elidable: Any = ...
    def __init__(self, sql: Any, reverse_sql: Optional[Any] = ..., state_operations: Optional[Any] = ..., hints: Optional[Any] = ..., elidable: bool = ...) -> None: ...
    def deconstruct(self): ...
    @property
    def reversible(self): ...
    def state_forwards(self, app_label: Any, state: Any) -> None: ...
    def database_forwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def database_backwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def describe(self): ...

class RunPython(Operation):
    reduces_to_sql: bool = ...
    atomic: Any = ...
    code: Any = ...
    reverse_code: Any = ...
    hints: Any = ...
    elidable: Any = ...
    def __init__(self, code: Any, reverse_code: Optional[Any] = ..., atomic: Optional[Any] = ..., hints: Optional[Any] = ..., elidable: bool = ...) -> None: ...
    def deconstruct(self): ...
    @property
    def reversible(self): ...
    def state_forwards(self, app_label: Any, state: Any) -> None: ...
    def database_forwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def database_backwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def describe(self): ...
    @staticmethod
    def noop(apps: Any, schema_editor: Any) -> None: ...
