# Stubs for django.db.models.fields.mixins (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

NOT_PROVIDED: Any

class FieldCacheMixin:
    def get_cache_name(self) -> None: ...
    def get_cached_value(self, instance: Any, default: Any = ...): ...
    def is_cached(self, instance: Any): ...
    def set_cached_value(self, instance: Any, value: Any) -> None: ...
    def delete_cached_value(self, instance: Any) -> None: ...