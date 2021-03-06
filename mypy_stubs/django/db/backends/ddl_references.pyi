# Stubs for django.db.backends.ddl_references (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class Reference:
    def references_table(self, table: Any): ...
    def references_column(self, table: Any, column: Any): ...
    def rename_table_references(self, old_table: Any, new_table: Any) -> None: ...
    def rename_column_references(self, table: Any, old_column: Any, new_column: Any) -> None: ...

class Table(Reference):
    table: Any = ...
    quote_name: Any = ...
    def __init__(self, table: Any, quote_name: Any) -> None: ...
    def references_table(self, table: Any): ...
    def rename_table_references(self, old_table: Any, new_table: Any) -> None: ...

class TableColumns(Table):
    table: Any = ...
    columns: Any = ...
    def __init__(self, table: Any, columns: Any) -> None: ...
    def references_column(self, table: Any, column: Any): ...
    def rename_column_references(self, table: Any, old_column: Any, new_column: Any) -> None: ...

class Columns(TableColumns):
    quote_name: Any = ...
    col_suffixes: Any = ...
    def __init__(self, table: Any, columns: Any, quote_name: Any, col_suffixes: Any = ...) -> None: ...

class IndexName(TableColumns):
    suffix: Any = ...
    create_index_name: Any = ...
    def __init__(self, table: Any, columns: Any, suffix: Any, create_index_name: Any) -> None: ...

class ForeignKeyName(TableColumns):
    to_reference: Any = ...
    suffix_template: Any = ...
    create_fk_name: Any = ...
    def __init__(self, from_table: Any, from_columns: Any, to_table: Any, to_columns: Any, suffix_template: Any, create_fk_name: Any) -> None: ...
    def references_table(self, table: Any): ...
    def references_column(self, table: Any, column: Any): ...
    def rename_table_references(self, old_table: Any, new_table: Any) -> None: ...
    def rename_column_references(self, table: Any, old_column: Any, new_column: Any) -> None: ...

class Statement(Reference):
    template: Any = ...
    parts: Any = ...
    def __init__(self, template: Any, **parts: Any) -> None: ...
    def references_table(self, table: Any): ...
    def references_column(self, table: Any, column: Any): ...
    def rename_table_references(self, old_table: Any, new_table: Any) -> None: ...
    def rename_column_references(self, table: Any, old_column: Any, new_column: Any) -> None: ...
