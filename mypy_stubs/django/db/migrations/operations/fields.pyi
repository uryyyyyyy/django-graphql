# Stubs for django.db.migrations.operations.fields (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .base import Operation
from .utils import is_referenced_by_foreign_key
from typing import Any, Optional

class FieldOperation(Operation):
    model_name: Any = ...
    name: Any = ...
    def __init__(self, model_name: Any, name: Any) -> None: ...
    def model_name_lower(self): ...
    def name_lower(self): ...
    def is_same_model_operation(self, operation: Any): ...
    def is_same_field_operation(self, operation: Any): ...
    def references_model(self, name: Any, app_label: Optional[Any] = ...): ...
    def references_field(self, model_name: Any, name: Any, app_label: Optional[Any] = ...): ...
    def reduce(self, operation: Any, in_between: Any, app_label: Optional[Any] = ...): ...

class AddField(FieldOperation):
    field: Any = ...
    preserve_default: Any = ...
    def __init__(self, model_name: Any, name: Any, field: Any, preserve_default: bool = ...) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label: Any, state: Any) -> None: ...
    def database_forwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def database_backwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def describe(self): ...
    def reduce(self, operation: Any, in_between: Any, app_label: Optional[Any] = ...): ...

class RemoveField(FieldOperation):
    def deconstruct(self): ...
    def state_forwards(self, app_label: Any, state: Any) -> None: ...
    def database_forwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def database_backwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def describe(self): ...

class AlterField(FieldOperation):
    field: Any = ...
    preserve_default: Any = ...
    def __init__(self, model_name: Any, name: Any, field: Any, preserve_default: bool = ...) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label: Any, state: Any) -> None: ...
    def database_forwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def database_backwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def describe(self): ...
    def reduce(self, operation: Any, in_between: Any, app_label: Optional[Any] = ...): ...

class RenameField(FieldOperation):
    old_name: Any = ...
    new_name: Any = ...
    def __init__(self, model_name: Any, old_name: Any, new_name: Any) -> None: ...
    def old_name_lower(self): ...
    def new_name_lower(self): ...
    def deconstruct(self): ...
    def state_forwards(self, app_label: Any, state: Any) -> None: ...
    def database_forwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def database_backwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def describe(self): ...
    def references_field(self, model_name: Any, name: Any, app_label: Optional[Any] = ...): ...
    def reduce(self, operation: Any, in_between: Any, app_label: Optional[Any] = ...): ...
