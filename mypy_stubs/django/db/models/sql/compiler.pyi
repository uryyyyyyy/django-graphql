# Stubs for django.db.models.sql.compiler (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

FORCE: Any

class SQLCompiler:
    query: Any = ...
    connection: Any = ...
    using: Any = ...
    quote_cache: Any = ...
    select: Any = ...
    annotation_col_map: Any = ...
    klass_info: Any = ...
    ordering_parts: Any = ...
    def __init__(self, query: Any, connection: Any, using: Any) -> None: ...
    col_count: Any = ...
    def setup_query(self) -> None: ...
    has_extra_select: Any = ...
    def pre_sql_setup(self): ...
    def get_group_by(self, select: Any, order_by: Any): ...
    def collapse_group_by(self, expressions: Any, having: Any): ...
    def get_select(self): ...
    def get_order_by(self): ...
    def get_extra_select(self, order_by: Any, select: Any): ...
    def quote_name_unless_alias(self, name: Any): ...
    def compile(self, node: Any, select_format: bool = ...): ...
    def get_combinator_sql(self, combinator: Any, all: Any): ...
    def as_sql(self, with_limits: bool = ..., with_col_aliases: bool = ...): ...
    def get_default_columns(self, start_alias: Optional[Any] = ..., opts: Optional[Any] = ..., from_parent: Optional[Any] = ...): ...
    def get_distinct(self): ...
    def find_ordering_name(self, name: Any, opts: Any, alias: Optional[Any] = ..., default_order: str = ..., already_seen: Optional[Any] = ...): ...
    def get_from_clause(self): ...
    def get_related_selections(self, select: Any, opts: Optional[Any] = ..., root_alias: Optional[Any] = ..., cur_depth: int = ..., requested: Optional[Any] = ..., restricted: Optional[Any] = ...): ...
    def get_select_for_update_of_arguments(self): ...
    def deferred_to_columns(self): ...
    def get_converters(self, expressions: Any): ...
    def apply_converters(self, rows: Any, converters: Any) -> None: ...
    def results_iter(self, results: Optional[Any] = ..., tuple_expected: bool = ..., chunked_fetch: bool = ..., chunk_size: Any = ...): ...
    def has_results(self): ...
    def execute_sql(self, result_type: Any = ..., chunked_fetch: bool = ..., chunk_size: Any = ...): ...
    def as_subquery_condition(self, alias: Any, columns: Any, compiler: Any): ...
    def explain_query(self) -> None: ...

class SQLInsertCompiler(SQLCompiler):
    return_id: bool = ...
    def field_as_sql(self, field: Any, val: Any): ...
    def prepare_value(self, field: Any, value: Any): ...
    def pre_save_val(self, field: Any, obj: Any): ...
    def assemble_as_sql(self, fields: Any, value_rows: Any): ...
    def as_sql(self): ...
    def execute_sql(self, return_id: bool = ...): ...

class SQLDeleteCompiler(SQLCompiler):
    def as_sql(self): ...

class SQLUpdateCompiler(SQLCompiler):
    def as_sql(self): ...
    def execute_sql(self, result_type: Any): ...
    def pre_sql_setup(self) -> None: ...

class SQLAggregateCompiler(SQLCompiler):
    col_count: Any = ...
    def as_sql(self): ...

def cursor_iter(cursor: Any, sentinel: Any, col_count: Any, itersize: Any): ...
