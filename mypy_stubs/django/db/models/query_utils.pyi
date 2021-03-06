# Stubs for django.db.models.query_utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple
from django.utils import tree
from typing import Any, Optional

PathInfo = namedtuple('PathInfo', 'from_opts to_opts target_fields join_field m2m direct filtered_relation')

class InvalidQuery(Exception): ...

def subclasses(cls) -> None: ...

class QueryWrapper:
    contains_aggregate: bool = ...
    data: Any = ...
    def __init__(self, sql: Any, params: Any) -> None: ...
    def as_sql(self, compiler: Optional[Any] = ..., connection: Optional[Any] = ...): ...

class Q(tree.Node):
    AND: str = ...
    OR: str = ...
    default: Any = ...
    conditional: bool = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __or__(self, other: Any): ...
    def __and__(self, other: Any): ...
    def __invert__(self): ...
    def resolve_expression(self, query: Optional[Any] = ..., allow_joins: bool = ..., reuse: Optional[Any] = ..., summarize: bool = ..., for_save: bool = ...): ...
    def deconstruct(self): ...

class DeferredAttribute:
    field_name: Any = ...
    def __init__(self, field_name: Any) -> None: ...
    def __get__(self, instance: Any, cls: Optional[Any] = ...): ...

class RegisterLookupMixin:
    @classmethod
    def get_lookups(cls): ...
    def get_lookup(self, lookup_name: Any): ...
    def get_transform(self, lookup_name: Any): ...
    @staticmethod
    def merge_dicts(dicts: Any): ...
    @classmethod
    def register_lookup(cls, lookup: Any, lookup_name: Optional[Any] = ...): ...

def select_related_descend(field: Any, restricted: Any, requested: Any, load_fields: Any, reverse: bool = ...): ...
def refs_expression(lookup_parts: Any, annotations: Any): ...
def check_rel_lookup_compatibility(model: Any, target_opts: Any, field: Any): ...

class FilteredRelation:
    relation_name: Any = ...
    alias: Any = ...
    condition: Any = ...
    path: Any = ...
    def __init__(self, relation_name: Any, *, condition: Any = ...) -> None: ...
    def __eq__(self, other: Any): ...
    def clone(self): ...
    def resolve_expression(self, *args: Any, **kwargs: Any) -> None: ...
    def as_sql(self, compiler: Any, connection: Any): ...
