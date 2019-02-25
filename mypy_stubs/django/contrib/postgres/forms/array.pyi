# Stubs for django.contrib.postgres.forms.array (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..utils import prefix_validation_error
from django import forms
from typing import Any, Optional

class SimpleArrayField(forms.CharField):
    default_error_messages: Any = ...
    base_field: Any = ...
    delimiter: Any = ...
    min_length: Any = ...
    max_length: Any = ...
    def __init__(self, base_field: Any, *, delimiter: str = ..., max_length: Optional[Any] = ..., min_length: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def clean(self, value: Any): ...
    def prepare_value(self, value: Any): ...
    def to_python(self, value: Any): ...
    def validate(self, value: Any) -> None: ...
    def run_validators(self, value: Any) -> None: ...
    def has_changed(self, initial: Any, data: Any): ...

class SplitArrayWidget(forms.Widget):
    template_name: str = ...
    widget: Any = ...
    size: Any = ...
    def __init__(self, widget: Any, size: Any, **kwargs: Any) -> None: ...
    @property
    def is_hidden(self): ...
    def value_from_datadict(self, data: Any, files: Any, name: Any): ...
    def value_omitted_from_data(self, data: Any, files: Any, name: Any): ...
    def id_for_label(self, id_: Any): ...
    def get_context(self, name: Any, value: Any, attrs: Optional[Any] = ...): ...
    @property
    def media(self): ...
    def __deepcopy__(self, memo: Any): ...
    @property
    def needs_multipart_form(self): ...

class SplitArrayField(forms.Field):
    default_error_messages: Any = ...
    base_field: Any = ...
    size: Any = ...
    remove_trailing_nulls: Any = ...
    def __init__(self, base_field: Any, size: Any, *, remove_trailing_nulls: bool = ..., **kwargs: Any) -> None: ...
    def clean(self, value: Any): ...
