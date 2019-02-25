# Stubs for django.db.backends.oracle.features (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.backends.base.features import BaseDatabaseFeatures
from typing import Any

class DatabaseFeatures(BaseDatabaseFeatures):
    empty_fetchmany_value: Any = ...
    interprets_empty_strings_as_nulls: bool = ...
    uses_savepoints: bool = ...
    has_select_for_update: bool = ...
    has_select_for_update_nowait: bool = ...
    has_select_for_update_skip_locked: bool = ...
    has_select_for_update_of: bool = ...
    select_for_update_of_column: bool = ...
    can_return_id_from_insert: bool = ...
    can_introspect_autofield: bool = ...
    supports_subqueries_in_group_by: bool = ...
    supports_transactions: bool = ...
    supports_timezones: bool = ...
    has_native_duration_field: bool = ...
    can_defer_constraint_checks: bool = ...
    supports_partially_nullable_unique_constraints: bool = ...
    truncates_names: bool = ...
    supports_tablespaces: bool = ...
    supports_sequence_reset: bool = ...
    can_introspect_time_field: bool = ...
    atomic_transactions: bool = ...
    supports_combined_alters: bool = ...
    nulls_order_largest: bool = ...
    requires_literal_defaults: bool = ...
    closed_cursor_error_class: Any = ...
    bare_select_suffix: str = ...
    uppercases_column_names: bool = ...
    supports_select_for_update_with_limit: bool = ...
    supports_temporal_subtraction: bool = ...
    ignores_table_name_case: bool = ...
    supports_index_on_text_field: bool = ...
    has_case_insensitive_like: bool = ...
    create_test_procedure_without_params_sql: str = ...
    create_test_procedure_with_int_param_sql: str = ...
    supports_callproc_kwargs: bool = ...
    supports_over_clause: bool = ...
    max_query_params: Any = ...
    def has_fetch_offset_support(self): ...
    def allow_sliced_subqueries_with_in(self): ...
