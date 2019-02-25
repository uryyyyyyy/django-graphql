# Stubs for django.core.cache.backends.base (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.exceptions import ImproperlyConfigured
from typing import Any, Optional

class InvalidCacheBackendError(ImproperlyConfigured): ...
class CacheKeyWarning(RuntimeWarning): ...

DEFAULT_TIMEOUT: Any
MEMCACHE_MAX_KEY_LENGTH: int

def default_key_func(key: Any, key_prefix: Any, version: Any): ...
def get_key_func(key_func: Any): ...

class BaseCache:
    default_timeout: Any = ...
    key_prefix: Any = ...
    version: Any = ...
    key_func: Any = ...
    def __init__(self, params: Any) -> None: ...
    def get_backend_timeout(self, timeout: Any = ...): ...
    def make_key(self, key: Any, version: Optional[Any] = ...): ...
    def add(self, key: Any, value: Any, timeout: Any = ..., version: Optional[Any] = ...) -> None: ...
    def get(self, key: Any, default: Optional[Any] = ..., version: Optional[Any] = ...) -> None: ...
    def set(self, key: Any, value: Any, timeout: Any = ..., version: Optional[Any] = ...) -> None: ...
    def touch(self, key: Any, timeout: Any = ..., version: Optional[Any] = ...) -> None: ...
    def delete(self, key: Any, version: Optional[Any] = ...) -> None: ...
    def get_many(self, keys: Any, version: Optional[Any] = ...): ...
    def get_or_set(self, key: Any, default: Any, timeout: Any = ..., version: Optional[Any] = ...): ...
    def has_key(self, key: Any, version: Optional[Any] = ...): ...
    def incr(self, key: Any, delta: int = ..., version: Optional[Any] = ...): ...
    def decr(self, key: Any, delta: int = ..., version: Optional[Any] = ...): ...
    def __contains__(self, key: Any): ...
    def set_many(self, data: Any, timeout: Any = ..., version: Optional[Any] = ...): ...
    def delete_many(self, keys: Any, version: Optional[Any] = ...) -> None: ...
    def clear(self) -> None: ...
    def validate_key(self, key: Any) -> None: ...
    def incr_version(self, key: Any, delta: int = ..., version: Optional[Any] = ...): ...
    def decr_version(self, key: Any, delta: int = ..., version: Optional[Any] = ...): ...
    def close(self, **kwargs: Any) -> None: ...