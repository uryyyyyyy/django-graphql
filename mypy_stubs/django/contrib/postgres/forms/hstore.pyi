# Stubs for django.contrib.postgres.forms.hstore (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django import forms
from typing import Any

class HStoreField(forms.CharField):
    widget: Any = ...
    default_error_messages: Any = ...
    def prepare_value(self, value: Any): ...
    def to_python(self, value: Any): ...
    def has_changed(self, initial: Any, data: Any): ...
