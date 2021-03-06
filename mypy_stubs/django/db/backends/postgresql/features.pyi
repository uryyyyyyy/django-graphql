# Stubs for django.db.backends.postgresql.features (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.backends.base.features import BaseDatabaseFeatures
from typing import Any

class DatabaseFeatures(BaseDatabaseFeatures):
    allows_group_by_selected_pks: bool = ...
    can_return_id_from_insert: bool = ...
    can_return_ids_from_bulk_insert: bool = ...
    has_real_datatype: bool = ...
    has_native_uuid_field: bool = ...
    has_native_duration_field: bool = ...
    can_defer_constraint_checks: bool = ...
    has_select_for_update: bool = ...
    has_select_for_update_nowait: bool = ...
    has_select_for_update_of: bool = ...
    uses_savepoints: bool = ...
    can_release_savepoints: bool = ...
    supports_tablespaces: bool = ...
    supports_transactions: bool = ...
    can_introspect_autofield: bool = ...
    can_introspect_ip_address_field: bool = ...
    can_introspect_small_integer_field: bool = ...
    can_distinct_on_fields: bool = ...
    can_rollback_ddl: bool = ...
    supports_combined_alters: bool = ...
    nulls_order_largest: bool = ...
    closed_cursor_error_class: Any = ...
    has_case_insensitive_like: bool = ...
    requires_sqlparse_for_splitting: bool = ...
    greatest_least_ignores_nulls: bool = ...
    can_clone_databases: bool = ...
    supports_temporal_subtraction: bool = ...
    supports_slicing_ordering_in_compound: bool = ...
    create_test_procedure_without_params_sql: str = ...
    create_test_procedure_with_int_param_sql: str = ...
    supports_over_clause: bool = ...
    supports_aggregate_filter_clause: bool = ...
    supported_explain_formats: Any = ...
    validates_explain_options: bool = ...
    def is_postgresql_9_5(self): ...
    has_select_for_update_skip_locked: Any = ...
    has_brin_index_support: Any = ...
    has_jsonb_agg: Any = ...
    has_gin_pending_list_limit: Any = ...
