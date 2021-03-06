# Stubs for django.db.models.fields (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.exceptions import FieldDoesNotExist as FieldDoesNotExist
from django.db.models.query_utils import RegisterLookupMixin
from typing import Any, Optional

class Empty: ...
class NOT_PROVIDED: ...

BLANK_CHOICE_DASH: Any

class Field(RegisterLookupMixin):
    empty_strings_allowed: bool = ...
    empty_values: Any = ...
    creation_counter: int = ...
    auto_creation_counter: int = ...
    default_validators: Any = ...
    default_error_messages: Any = ...
    system_check_deprecated_details: Any = ...
    system_check_removed_details: Any = ...
    hidden: bool = ...
    many_to_many: Any = ...
    many_to_one: Any = ...
    one_to_many: Any = ...
    one_to_one: Any = ...
    related_model: Any = ...
    description: Any = ...
    name: Any = ...
    verbose_name: Any = ...
    primary_key: Any = ...
    remote_field: Any = ...
    is_relation: Any = ...
    default: Any = ...
    editable: Any = ...
    serialize: Any = ...
    unique_for_date: Any = ...
    unique_for_month: Any = ...
    unique_for_year: Any = ...
    choices: Any = ...
    help_text: Any = ...
    db_index: Any = ...
    db_column: Any = ...
    auto_created: Any = ...
    error_messages: Any = ...
    def __init__(self, verbose_name: Optional[Any] = ..., name: Optional[Any] = ..., primary_key: bool = ..., max_length: Optional[Any] = ..., unique: bool = ..., blank: bool = ..., null: bool = ..., db_index: bool = ..., rel: Optional[Any] = ..., default: Any = ..., editable: bool = ..., serialize: bool = ..., unique_for_date: Optional[Any] = ..., unique_for_month: Optional[Any] = ..., unique_for_year: Optional[Any] = ..., choices: Optional[Any] = ..., help_text: str = ..., db_column: Optional[Any] = ..., db_tablespace: Optional[Any] = ..., auto_created: bool = ..., validators: Any = ..., error_messages: Optional[Any] = ...) -> None: ...
    def check(self, **kwargs: Any): ...
    def get_col(self, alias: Any, output_field: Optional[Any] = ...): ...
    def cached_col(self): ...
    def select_format(self, compiler: Any, sql: Any, params: Any): ...
    def deconstruct(self): ...
    def clone(self): ...
    def __eq__(self, other: Any): ...
    def __lt__(self, other: Any): ...
    def __hash__(self): ...
    def __deepcopy__(self, memodict: Any): ...
    def __copy__(self): ...
    def __reduce__(self): ...
    def get_pk_value_on_save(self, instance: Any): ...
    def to_python(self, value: Any): ...
    def validators(self): ...
    def run_validators(self, value: Any) -> None: ...
    def validate(self, value: Any, model_instance: Any) -> None: ...
    def clean(self, value: Any, model_instance: Any): ...
    def db_type_parameters(self, connection: Any): ...
    def db_check(self, connection: Any): ...
    def db_type(self, connection: Any): ...
    def rel_db_type(self, connection: Any): ...
    def cast_db_type(self, connection: Any): ...
    def db_parameters(self, connection: Any): ...
    def db_type_suffix(self, connection: Any): ...
    def get_db_converters(self, connection: Any): ...
    @property
    def unique(self): ...
    @property
    def db_tablespace(self): ...
    concrete: Any = ...
    def set_attributes_from_name(self, name: Any) -> None: ...
    model: Any = ...
    def contribute_to_class(self, cls: Any, name: Any, private_only: bool = ...) -> None: ...
    def get_filter_kwargs_for_object(self, obj: Any): ...
    def get_attname(self): ...
    def get_attname_column(self): ...
    def get_internal_type(self): ...
    def pre_save(self, model_instance: Any, add: Any): ...
    def get_prep_value(self, value: Any): ...
    def get_db_prep_value(self, value: Any, connection: Any, prepared: bool = ...): ...
    def get_db_prep_save(self, value: Any, connection: Any): ...
    def has_default(self): ...
    def get_default(self): ...
    def get_choices(self, include_blank: bool = ..., blank_choice: Any = ..., limit_choices_to: Optional[Any] = ...): ...
    def value_to_string(self, obj: Any): ...
    flatchoices: Any = ...
    def save_form_data(self, instance: Any, data: Any) -> None: ...
    def formfield(self, **kwargs: Any): ...
    def value_from_object(self, obj: Any): ...

class AutoField(Field):
    description: Any = ...
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def check(self, **kwargs: Any): ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value: Any): ...
    def rel_db_type(self, connection: Any): ...
    def validate(self, value: Any, model_instance: Any) -> None: ...
    def get_db_prep_value(self, value: Any, connection: Any, prepared: bool = ...): ...
    def get_prep_value(self, value: Any): ...
    def contribute_to_class(self, cls: Any, name: Any, private_only: bool = ...) -> Any: ...
    def formfield(self, **kwargs: Any) -> Any: ...

class BigAutoField(AutoField):
    description: Any = ...
    def get_internal_type(self): ...
    def rel_db_type(self, connection: Any): ...

class BooleanField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def get_internal_type(self): ...
    def to_python(self, value: Any): ...
    def get_prep_value(self, value: Any): ...
    def formfield(self, **kwargs: Any): ...

class CharField(Field):
    description: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def check(self, **kwargs: Any): ...
    def cast_db_type(self, connection: Any): ...
    def get_internal_type(self): ...
    def to_python(self, value: Any): ...
    def get_prep_value(self, value: Any): ...
    def formfield(self, **kwargs: Any): ...

class CommaSeparatedIntegerField(CharField):
    default_validators: Any = ...
    description: Any = ...
    system_check_removed_details: Any = ...

class DateTimeCheckMixin:
    def check(self, **kwargs: Any): ...

class DateField(DateTimeCheckMixin, Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def __init__(self, verbose_name: Optional[Any] = ..., name: Optional[Any] = ..., auto_now: bool = ..., auto_now_add: bool = ..., **kwargs: Any) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value: Any): ...
    def pre_save(self, model_instance: Any, add: Any): ...
    def contribute_to_class(self, cls: Any, name: Any, private_only: bool = ...) -> None: ...
    def get_prep_value(self, value: Any): ...
    def get_db_prep_value(self, value: Any, connection: Any, prepared: bool = ...): ...
    def value_to_string(self, obj: Any): ...
    def formfield(self, **kwargs: Any): ...

class DateTimeField(DateField):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def get_internal_type(self): ...
    def to_python(self, value: Any): ...
    def pre_save(self, model_instance: Any, add: Any): ...
    def get_prep_value(self, value: Any): ...
    def get_db_prep_value(self, value: Any, connection: Any, prepared: bool = ...): ...
    def value_to_string(self, obj: Any): ...
    def formfield(self, **kwargs: Any): ...

class DecimalField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def __init__(self, verbose_name: Optional[Any] = ..., name: Optional[Any] = ..., max_digits: Optional[Any] = ..., decimal_places: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def check(self, **kwargs: Any): ...
    def validators(self): ...
    def context(self): ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value: Any): ...
    def get_db_prep_save(self, value: Any, connection: Any): ...
    def get_prep_value(self, value: Any): ...
    def formfield(self, **kwargs: Any): ...

class DurationField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def get_internal_type(self): ...
    def to_python(self, value: Any): ...
    def get_db_prep_value(self, value: Any, connection: Any, prepared: bool = ...): ...
    def get_db_converters(self, connection: Any): ...
    def value_to_string(self, obj: Any): ...
    def formfield(self, **kwargs: Any): ...

class EmailField(CharField):
    default_validators: Any = ...
    description: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def deconstruct(self): ...
    def formfield(self, **kwargs: Any): ...

class FilePathField(Field):
    description: Any = ...
    def __init__(self, verbose_name: Optional[Any] = ..., name: Optional[Any] = ..., path: str = ..., match: Optional[Any] = ..., recursive: bool = ..., allow_files: bool = ..., allow_folders: bool = ..., **kwargs: Any) -> None: ...
    def check(self, **kwargs: Any): ...
    def deconstruct(self): ...
    def get_prep_value(self, value: Any): ...
    def formfield(self, **kwargs: Any): ...
    def get_internal_type(self): ...

class FloatField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def get_prep_value(self, value: Any): ...
    def get_internal_type(self): ...
    def to_python(self, value: Any): ...
    def formfield(self, **kwargs: Any): ...

class IntegerField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def check(self, **kwargs: Any): ...
    def validators(self): ...
    def get_prep_value(self, value: Any): ...
    def get_internal_type(self): ...
    def to_python(self, value: Any): ...
    def formfield(self, **kwargs: Any): ...

class BigIntegerField(IntegerField):
    empty_strings_allowed: bool = ...
    description: Any = ...
    MAX_BIGINT: int = ...
    def get_internal_type(self): ...
    def formfield(self, **kwargs: Any): ...

class IPAddressField(Field):
    empty_strings_allowed: bool = ...
    description: Any = ...
    system_check_removed_details: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def deconstruct(self): ...
    def get_prep_value(self, value: Any): ...
    def get_internal_type(self): ...

class GenericIPAddressField(Field):
    empty_strings_allowed: bool = ...
    description: Any = ...
    default_error_messages: Any = ...
    unpack_ipv4: Any = ...
    protocol: Any = ...
    def __init__(self, verbose_name: Optional[Any] = ..., name: Optional[Any] = ..., protocol: str = ..., unpack_ipv4: bool = ..., *args: Any, **kwargs: Any) -> None: ...
    def check(self, **kwargs: Any): ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value: Any): ...
    def get_db_prep_value(self, value: Any, connection: Any, prepared: bool = ...): ...
    def get_prep_value(self, value: Any): ...
    def formfield(self, **kwargs: Any): ...

class NullBooleanField(BooleanField):
    default_error_messages: Any = ...
    description: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...

class PositiveIntegerRelDbTypeMixin:
    def rel_db_type(self, connection: Any): ...

class PositiveIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField):
    description: Any = ...
    def get_internal_type(self): ...
    def formfield(self, **kwargs: Any): ...

class PositiveSmallIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField):
    description: Any = ...
    def get_internal_type(self): ...
    def formfield(self, **kwargs: Any): ...

class SlugField(CharField):
    default_validators: Any = ...
    description: Any = ...
    allow_unicode: Any = ...
    def __init__(self, *args: Any, max_length: int = ..., db_index: bool = ..., allow_unicode: bool = ..., **kwargs: Any) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def formfield(self, **kwargs: Any): ...

class SmallIntegerField(IntegerField):
    description: Any = ...
    def get_internal_type(self): ...

class TextField(Field):
    description: Any = ...
    def get_internal_type(self): ...
    def to_python(self, value: Any): ...
    def get_prep_value(self, value: Any): ...
    def formfield(self, **kwargs: Any): ...

class TimeField(DateTimeCheckMixin, Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def __init__(self, verbose_name: Optional[Any] = ..., name: Optional[Any] = ..., auto_now: bool = ..., auto_now_add: bool = ..., **kwargs: Any) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value: Any): ...
    def pre_save(self, model_instance: Any, add: Any): ...
    def get_prep_value(self, value: Any): ...
    def get_db_prep_value(self, value: Any, connection: Any, prepared: bool = ...): ...
    def value_to_string(self, obj: Any): ...
    def formfield(self, **kwargs: Any): ...

class URLField(CharField):
    default_validators: Any = ...
    description: Any = ...
    def __init__(self, verbose_name: Optional[Any] = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def deconstruct(self): ...
    def formfield(self, **kwargs: Any): ...

class BinaryField(Field):
    description: Any = ...
    empty_values: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def get_placeholder(self, value: Any, compiler: Any, connection: Any): ...
    def get_default(self): ...
    def get_db_prep_value(self, value: Any, connection: Any, prepared: bool = ...): ...
    def value_to_string(self, obj: Any): ...
    def to_python(self, value: Any): ...

class UUIDField(Field):
    default_error_messages: Any = ...
    description: str = ...
    empty_strings_allowed: bool = ...
    def __init__(self, verbose_name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def get_db_prep_value(self, value: Any, connection: Any, prepared: bool = ...): ...
    def to_python(self, value: Any): ...
    def formfield(self, **kwargs: Any): ...
