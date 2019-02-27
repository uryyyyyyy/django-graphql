# Stubs for django.db.backends.sqlite3.schema (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from typing import Any

class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    sql_delete_table: str = ...
    sql_create_fk: Any = ...
    sql_create_inline_fk: str = ...
    sql_create_unique: str = ...
    sql_delete_unique: str = ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
    def quote_value(self, value: Any): ...
    def alter_db_table(self, model: Any, old_db_table: Any, new_db_table: Any, disable_constraints: bool = ...) -> None: ...
    def alter_field(self, model: Any, old_field: Any, new_field: Any, strict: bool = ...) -> None: ...
    def delete_model(self, model: Any, handle_autom2m: bool = ...) -> None: ...
    def add_field(self, model: Any, field: Any): ...
    def remove_field(self, model: Any, field: Any) -> None: ...
