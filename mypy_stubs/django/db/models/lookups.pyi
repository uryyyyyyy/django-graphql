# Stubs for django.db.models.lookups (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.models.expressions import Func
from django.db.models.query_utils import RegisterLookupMixin
from typing import Any, Optional

class Lookup:
    lookup_name: Any = ...
    prepare_rhs: bool = ...
    can_use_none_as_rhs: bool = ...
    rhs: Any = ...
    bilateral_transforms: Any = ...
    def __init__(self, lhs: Any, rhs: Any) -> None: ...
    def apply_bilateral_transforms(self, value: Any): ...
    def batch_process_rhs(self, compiler: Any, connection: Any, rhs: Optional[Any] = ...): ...
    def get_source_expressions(self): ...
    lhs: Any = ...
    def set_source_expressions(self, new_exprs: Any) -> None: ...
    def get_prep_lookup(self): ...
    def get_db_prep_lookup(self, value: Any, connection: Any): ...
    def process_lhs(self, compiler: Any, connection: Any, lhs: Optional[Any] = ...): ...
    def process_rhs(self, compiler: Any, connection: Any): ...
    def rhs_is_direct_value(self): ...
    def relabeled_clone(self, relabels: Any): ...
    def get_group_by_cols(self): ...
    def as_sql(self, compiler: Any, connection: Any) -> None: ...
    def contains_aggregate(self): ...
    def contains_over_clause(self): ...
    @property
    def is_summary(self): ...

class Transform(RegisterLookupMixin, Func):
    bilateral: bool = ...
    arity: int = ...
    @property
    def lhs(self): ...
    def get_bilateral_transforms(self): ...

class BuiltinLookup(Lookup):
    def process_lhs(self, compiler: Any, connection: Any, lhs: Optional[Any] = ...): ...
    def as_sql(self, compiler: Any, connection: Any): ...
    def get_rhs_op(self, connection: Any, rhs: Any): ...

class FieldGetDbPrepValueMixin:
    get_db_prep_lookup_value_is_iterable: bool = ...
    def get_db_prep_lookup(self, value: Any, connection: Any): ...

class FieldGetDbPrepValueIterableMixin(FieldGetDbPrepValueMixin):
    get_db_prep_lookup_value_is_iterable: bool = ...
    def get_prep_lookup(self): ...
    def process_rhs(self, compiler: Any, connection: Any): ...
    def resolve_expression_parameter(self, compiler: Any, connection: Any, sql: Any, param: Any): ...
    def batch_process_rhs(self, compiler: Any, connection: Any, rhs: Optional[Any] = ...): ...

class Exact(FieldGetDbPrepValueMixin, BuiltinLookup):
    lookup_name: str = ...
    def process_rhs(self, compiler: Any, connection: Any): ...

class IExact(BuiltinLookup):
    lookup_name: str = ...
    prepare_rhs: bool = ...
    def process_rhs(self, qn: Any, connection: Any): ...

class GreaterThan(FieldGetDbPrepValueMixin, BuiltinLookup):
    lookup_name: str = ...

class GreaterThanOrEqual(FieldGetDbPrepValueMixin, BuiltinLookup):
    lookup_name: str = ...

class LessThan(FieldGetDbPrepValueMixin, BuiltinLookup):
    lookup_name: str = ...

class LessThanOrEqual(FieldGetDbPrepValueMixin, BuiltinLookup):
    lookup_name: str = ...

class IntegerFieldFloatRounding:
    rhs: Any = ...
    def get_prep_lookup(self): ...

class IntegerGreaterThanOrEqual(IntegerFieldFloatRounding, GreaterThanOrEqual): ...
class IntegerLessThan(IntegerFieldFloatRounding, LessThan): ...

class In(FieldGetDbPrepValueIterableMixin, BuiltinLookup):
    lookup_name: str = ...
    def process_rhs(self, compiler: Any, connection: Any): ...
    def get_rhs_op(self, connection: Any, rhs: Any): ...
    def as_sql(self, compiler: Any, connection: Any): ...
    def split_parameter_list_as_sql(self, compiler: Any, connection: Any): ...

class PatternLookup(BuiltinLookup):
    param_pattern: str = ...
    prepare_rhs: bool = ...
    def get_rhs_op(self, connection: Any, rhs: Any): ...
    def process_rhs(self, qn: Any, connection: Any): ...

class Contains(PatternLookup):
    lookup_name: str = ...

class IContains(Contains):
    lookup_name: str = ...

class StartsWith(PatternLookup):
    lookup_name: str = ...
    param_pattern: str = ...

class IStartsWith(StartsWith):
    lookup_name: str = ...

class EndsWith(PatternLookup):
    lookup_name: str = ...
    param_pattern: str = ...

class IEndsWith(EndsWith):
    lookup_name: str = ...

class Range(FieldGetDbPrepValueIterableMixin, BuiltinLookup):
    lookup_name: str = ...
    def get_rhs_op(self, connection: Any, rhs: Any): ...

class IsNull(BuiltinLookup):
    lookup_name: str = ...
    prepare_rhs: bool = ...
    def as_sql(self, compiler: Any, connection: Any): ...

class Regex(BuiltinLookup):
    lookup_name: str = ...
    prepare_rhs: bool = ...
    def as_sql(self, compiler: Any, connection: Any): ...

class IRegex(Regex):
    lookup_name: str = ...

class YearLookup(Lookup):
    def year_lookup_bounds(self, connection: Any, year: Any): ...

class YearComparisonLookup(YearLookup):
    def as_sql(self, compiler: Any, connection: Any): ...
    def get_rhs_op(self, connection: Any, rhs: Any): ...
    def get_bound(self, start: Any, finish: Any) -> None: ...

class YearExact(YearLookup, Exact):
    lookup_name: str = ...
    def as_sql(self, compiler: Any, connection: Any): ...

class YearGt(YearComparisonLookup):
    lookup_name: str = ...
    def get_bound(self, start: Any, finish: Any): ...

class YearGte(YearComparisonLookup):
    lookup_name: str = ...
    def get_bound(self, start: Any, finish: Any): ...

class YearLt(YearComparisonLookup):
    lookup_name: str = ...
    def get_bound(self, start: Any, finish: Any): ...

class YearLte(YearComparisonLookup):
    lookup_name: str = ...
    def get_bound(self, start: Any, finish: Any): ...
