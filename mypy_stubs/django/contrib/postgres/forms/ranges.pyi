# Stubs for django.contrib.postgres.forms.ranges (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django import forms
from django.forms.widgets import MultiWidget
from typing import Any, Optional

class BaseRangeField(forms.MultiValueField):
    default_error_messages: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def prepare_value(self, value: Any): ...
    def compress(self, values: Any): ...

class IntegerRangeField(BaseRangeField):
    default_error_messages: Any = ...
    base_field: Any = ...
    range_type: Any = ...

class FloatRangeField(BaseRangeField):
    default_error_messages: Any = ...
    base_field: Any = ...
    range_type: Any = ...

class DateTimeRangeField(BaseRangeField):
    default_error_messages: Any = ...
    base_field: Any = ...
    range_type: Any = ...

class DateRangeField(BaseRangeField):
    default_error_messages: Any = ...
    base_field: Any = ...
    range_type: Any = ...

class RangeWidget(MultiWidget):
    def __init__(self, base_widget: Any, attrs: Optional[Any] = ...) -> None: ...
    def decompress(self, value: Any): ...
