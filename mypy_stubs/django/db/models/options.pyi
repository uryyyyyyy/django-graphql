# Stubs for django.db.models.options (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

PROXY_PARENTS: Any
EMPTY_RELATION_TREE: Any
IMMUTABLE_WARNING: str
DEFAULT_NAMES: Any

def normalize_together(option_together: Any): ...
def make_immutable_fields_list(name: Any, data: Any): ...

class Options:
    FORWARD_PROPERTIES: Any = ...
    REVERSE_PROPERTIES: Any = ...
    default_apps: Any = ...
    local_fields: Any = ...
    local_many_to_many: Any = ...
    private_fields: Any = ...
    local_managers: Any = ...
    base_manager_name: Any = ...
    default_manager_name: Any = ...
    model_name: Any = ...
    verbose_name: Any = ...
    verbose_name_plural: Any = ...
    db_table: str = ...
    ordering: Any = ...
    indexes: Any = ...
    unique_together: Any = ...
    index_together: Any = ...
    select_on_save: bool = ...
    default_permissions: Any = ...
    permissions: Any = ...
    object_name: Any = ...
    app_label: Any = ...
    get_latest_by: Any = ...
    order_with_respect_to: Any = ...
    db_tablespace: Any = ...
    required_db_features: Any = ...
    required_db_vendor: Any = ...
    meta: Any = ...
    pk: Any = ...
    auto_field: Any = ...
    abstract: bool = ...
    managed: bool = ...
    proxy: bool = ...
    proxy_for_model: Any = ...
    concrete_model: Any = ...
    swappable: Any = ...
    parents: Any = ...
    auto_created: bool = ...
    related_fkey_lookups: Any = ...
    apps: Any = ...
    default_related_name: Any = ...
    def __init__(self, meta: Any, app_label: Optional[Any] = ...) -> None: ...
    @property
    def label(self): ...
    @property
    def label_lower(self): ...
    @property
    def app_config(self): ...
    @property
    def installed(self): ...
    model: Any = ...
    original_attrs: Any = ...
    def contribute_to_class(self, cls: Any, name: Any) -> None: ...
    def add_manager(self, manager: Any) -> None: ...
    def add_field(self, field: Any, private: bool = ...) -> None: ...
    def setup_pk(self, field: Any) -> None: ...
    def setup_proxy(self, target: Any) -> None: ...
    def can_migrate(self, connection: Any): ...
    @property
    def verbose_name_raw(self): ...
    @property
    def swapped(self): ...
    def managers(self): ...
    def managers_map(self): ...
    def base_manager(self): ...
    def default_manager(self): ...
    def fields(self): ...
    def concrete_fields(self): ...
    def local_concrete_fields(self): ...
    def many_to_many(self): ...
    def related_objects(self): ...
    def fields_map(self): ...
    def get_field(self, field_name: Any): ...
    def get_base_chain(self, model: Any): ...
    def get_parent_list(self): ...
    def get_ancestor_link(self, ancestor: Any): ...
    def get_path_to_parent(self, parent: Any): ...
    def get_path_from_parent(self, parent: Any): ...
    def get_fields(self, include_parents: bool = ..., include_hidden: bool = ...): ...