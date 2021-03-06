# Stubs for django.db.backends.sqlite3.introspection (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.backends.base.introspection import BaseDatabaseIntrospection
from typing import Any

field_size_re: Any

def get_field_size(name: Any): ...

class FlexibleFieldLookupDict:
    base_data_types_reverse: Any = ...
    def __getitem__(self, key: Any): ...

class DatabaseIntrospection(BaseDatabaseIntrospection):
    data_types_reverse: Any = ...
    def get_table_list(self, cursor: Any): ...
    def get_table_description(self, cursor: Any, table_name: Any): ...
    def get_sequences(self, cursor: Any, table_name: Any, table_fields: Any = ...): ...
    def get_relations(self, cursor: Any, table_name: Any): ...
    def get_key_columns(self, cursor: Any, table_name: Any): ...
    def get_primary_key_column(self, cursor: Any, table_name: Any): ...
    def get_constraints(self, cursor: Any, table_name: Any): ...
