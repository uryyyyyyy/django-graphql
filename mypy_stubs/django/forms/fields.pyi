# Stubs for django.forms.fields (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class Field:
    widget: Any = ...
    hidden_widget: Any = ...
    default_validators: Any = ...
    default_error_messages: Any = ...
    empty_values: Any = ...
    show_hidden_initial: Any = ...
    help_text: Any = ...
    disabled: Any = ...
    label_suffix: Any = ...
    localize: Any = ...
    error_messages: Any = ...
    validators: Any = ...
    def __init__(self, *, required: bool = ..., widget: Optional[Any] = ..., label: Optional[Any] = ..., initial: Optional[Any] = ..., help_text: str = ..., error_messages: Optional[Any] = ..., show_hidden_initial: bool = ..., validators: Any = ..., localize: bool = ..., disabled: bool = ..., label_suffix: Optional[Any] = ...) -> None: ...
    def prepare_value(self, value: Any): ...
    def to_python(self, value: Any): ...
    def validate(self, value: Any) -> None: ...
    def run_validators(self, value: Any) -> None: ...
    def clean(self, value: Any): ...
    def bound_data(self, data: Any, initial: Any): ...
    def widget_attrs(self, widget: Any): ...
    def has_changed(self, initial: Any, data: Any): ...
    def get_bound_field(self, form: Any, field_name: Any): ...
    def __deepcopy__(self, memo: Any): ...

class CharField(Field):
    max_length: Any = ...
    min_length: Any = ...
    strip: Any = ...
    empty_value: Any = ...
    def __init__(self, *, max_length: Optional[Any] = ..., min_length: Optional[Any] = ..., strip: bool = ..., empty_value: str = ..., **kwargs: Any) -> None: ...
    def to_python(self, value: Any): ...
    def widget_attrs(self, widget: Any): ...

class IntegerField(Field):
    widget: Any = ...
    default_error_messages: Any = ...
    re_decimal: Any = ...
    def __init__(self, *, max_value: Optional[Any] = ..., min_value: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def to_python(self, value: Any): ...
    def widget_attrs(self, widget: Any): ...

class FloatField(IntegerField):
    default_error_messages: Any = ...
    def to_python(self, value: Any): ...
    def validate(self, value: Any) -> None: ...
    def widget_attrs(self, widget: Any): ...

class DecimalField(IntegerField):
    default_error_messages: Any = ...
    def __init__(self, *, max_value: Optional[Any] = ..., min_value: Optional[Any] = ..., max_digits: Optional[Any] = ..., decimal_places: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def to_python(self, value: Any): ...
    def validate(self, value: Any) -> None: ...
    def widget_attrs(self, widget: Any): ...

class BaseTemporalField(Field):
    input_formats: Any = ...
    def __init__(self, *, input_formats: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def to_python(self, value: Any): ...
    def strptime(self, value: Any, format: Any) -> None: ...

class DateField(BaseTemporalField):
    widget: Any = ...
    input_formats: Any = ...
    default_error_messages: Any = ...
    def to_python(self, value: Any): ...
    def strptime(self, value: Any, format: Any): ...

class TimeField(BaseTemporalField):
    widget: Any = ...
    input_formats: Any = ...
    default_error_messages: Any = ...
    def to_python(self, value: Any): ...
    def strptime(self, value: Any, format: Any): ...

class DateTimeField(BaseTemporalField):
    widget: Any = ...
    input_formats: Any = ...
    default_error_messages: Any = ...
    def prepare_value(self, value: Any): ...
    def to_python(self, value: Any): ...
    def strptime(self, value: Any, format: Any): ...

class DurationField(Field):
    default_error_messages: Any = ...
    def prepare_value(self, value: Any): ...
    def to_python(self, value: Any): ...

class RegexField(CharField):
    def __init__(self, regex: Any, **kwargs: Any) -> None: ...
    regex: Any = ...

class EmailField(CharField):
    widget: Any = ...
    default_validators: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...

class FileField(Field):
    widget: Any = ...
    default_error_messages: Any = ...
    max_length: Any = ...
    allow_empty_file: Any = ...
    def __init__(self, *, max_length: Optional[Any] = ..., allow_empty_file: bool = ..., **kwargs: Any) -> None: ...
    def to_python(self, data: Any): ...
    def clean(self, data: Any, initial: Optional[Any] = ...): ...
    def bound_data(self, data: Any, initial: Any): ...
    def has_changed(self, initial: Any, data: Any): ...

class ImageField(FileField):
    default_validators: Any = ...
    default_error_messages: Any = ...
    def to_python(self, data: Any): ...
    def widget_attrs(self, widget: Any): ...

class URLField(CharField):
    widget: Any = ...
    default_error_messages: Any = ...
    default_validators: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def to_python(self, value: Any): ...

class BooleanField(Field):
    widget: Any = ...
    def to_python(self, value: Any): ...
    def validate(self, value: Any) -> None: ...
    def has_changed(self, initial: Any, data: Any): ...

class NullBooleanField(BooleanField):
    widget: Any = ...
    def to_python(self, value: Any): ...
    def validate(self, value: Any) -> None: ...

class CallableChoiceIterator:
    choices_func: Any = ...
    def __init__(self, choices_func: Any) -> None: ...
    def __iter__(self) -> None: ...

class ChoiceField(Field):
    widget: Any = ...
    default_error_messages: Any = ...
    choices: Any = ...
    def __init__(self, *, choices: Any = ..., **kwargs: Any) -> None: ...
    def __deepcopy__(self, memo: Any): ...
    def to_python(self, value: Any): ...
    def validate(self, value: Any) -> None: ...
    def valid_value(self, value: Any): ...

class TypedChoiceField(ChoiceField):
    coerce: Any = ...
    empty_value: Any = ...
    def __init__(self, *, coerce: Any = ..., empty_value: str = ..., **kwargs: Any) -> None: ...
    def clean(self, value: Any): ...

class MultipleChoiceField(ChoiceField):
    hidden_widget: Any = ...
    widget: Any = ...
    default_error_messages: Any = ...
    def to_python(self, value: Any): ...
    def validate(self, value: Any) -> None: ...
    def has_changed(self, initial: Any, data: Any): ...

class TypedMultipleChoiceField(MultipleChoiceField):
    coerce: Any = ...
    empty_value: Any = ...
    def __init__(self, *, coerce: Any = ..., **kwargs: Any) -> None: ...
    def clean(self, value: Any): ...
    def validate(self, value: Any) -> None: ...

class ComboField(Field):
    fields: Any = ...
    def __init__(self, fields: Any, **kwargs: Any) -> None: ...
    def clean(self, value: Any): ...

class MultiValueField(Field):
    default_error_messages: Any = ...
    require_all_fields: Any = ...
    fields: Any = ...
    def __init__(self, fields: Any, *, require_all_fields: bool = ..., **kwargs: Any) -> None: ...
    def __deepcopy__(self, memo: Any): ...
    def validate(self, value: Any) -> None: ...
    def clean(self, value: Any): ...
    def compress(self, data_list: Any) -> None: ...
    def has_changed(self, initial: Any, data: Any): ...

class FilePathField(ChoiceField):
    choices: Any = ...
    match_re: Any = ...
    def __init__(self, path: Any, *, match: Optional[Any] = ..., recursive: bool = ..., allow_files: bool = ..., allow_folders: bool = ..., **kwargs: Any) -> None: ...

class SplitDateTimeField(MultiValueField):
    widget: Any = ...
    hidden_widget: Any = ...
    default_error_messages: Any = ...
    def __init__(self, *, input_date_formats: Optional[Any] = ..., input_time_formats: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def compress(self, data_list: Any): ...

class GenericIPAddressField(CharField):
    unpack_ipv4: Any = ...
    default_validators: Any = ...
    def __init__(self, *, protocol: str = ..., unpack_ipv4: bool = ..., **kwargs: Any) -> None: ...
    def to_python(self, value: Any): ...

class SlugField(CharField):
    default_validators: Any = ...
    allow_unicode: Any = ...
    def __init__(self, *, allow_unicode: bool = ..., **kwargs: Any) -> None: ...

class UUIDField(CharField):
    default_error_messages: Any = ...
    def prepare_value(self, value: Any): ...
    def to_python(self, value: Any): ...
