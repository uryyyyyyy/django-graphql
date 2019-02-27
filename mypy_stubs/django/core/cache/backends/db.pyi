# Stubs for django.core.cache.backends.db (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.cache.backends.base import BaseCache
from typing import Any, Optional

class Options:
    db_table: Any = ...
    app_label: str = ...
    model_name: str = ...
    verbose_name: str = ...
    verbose_name_plural: str = ...
    object_name: str = ...
    abstract: bool = ...
    managed: bool = ...
    proxy: bool = ...
    swapped: bool = ...
    def __init__(self, table: Any) -> None: ...

class BaseDatabaseCache(BaseCache):
    cache_model_class: Any = ...
    def __init__(self, table: Any, params: Any) -> None: ...

class DatabaseCache(BaseDatabaseCache):
    def get(self, key: Any, default: Optional[Any] = ..., version: Optional[Any] = ...): ...
    def set(self, key: Any, value: Any, timeout: Any = ..., version: Optional[Any] = ...) -> None: ...
    def add(self, key: Any, value: Any, timeout: Any = ..., version: Optional[Any] = ...): ...
    def touch(self, key: Any, timeout: Any = ..., version: Optional[Any] = ...): ...
    def delete(self, key: Any, version: Optional[Any] = ...) -> None: ...
    def has_key(self, key: Any, version: Optional[Any] = ...): ...
    def clear(self) -> None: ...
