# Stubs for django.core.cache.backends.dummy (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.cache.backends.base import BaseCache
from typing import Any, Optional

class DummyCache(BaseCache):
    def __init__(self, host: Any, *args: Any, **kwargs: Any) -> None: ...
    def add(self, key: Any, value: Any, timeout: Any = ..., version: Optional[Any] = ...): ...
    def get(self, key: Any, default: Optional[Any] = ..., version: Optional[Any] = ...): ...
    def set(self, key: Any, value: Any, timeout: Any = ..., version: Optional[Any] = ...) -> None: ...
    def touch(self, key: Any, timeout: Any = ..., version: Optional[Any] = ...): ...
    def delete(self, key: Any, version: Optional[Any] = ...) -> None: ...
    def has_key(self, key: Any, version: Optional[Any] = ...): ...
    def clear(self) -> None: ...
