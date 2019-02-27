# Stubs for django.urls.base (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .exceptions import NoReverseMatch, Resolver404
from .resolvers import get_ns_resolver, get_resolver
from .utils import get_callable
from typing import Any, Optional

def resolve(path: Any, urlconf: Optional[Any] = ...): ...
def reverse(viewname: Any, urlconf: Optional[Any] = ..., args: Optional[Any] = ..., kwargs: Optional[Any] = ..., current_app: Optional[Any] = ...): ...

reverse_lazy: Any

def clear_url_caches() -> None: ...
def set_script_prefix(prefix: Any) -> None: ...
def get_script_prefix(): ...
def clear_script_prefix() -> None: ...
def set_urlconf(urlconf_name: Any) -> None: ...
def get_urlconf(default: Optional[Any] = ...): ...
def is_valid_path(path: Any, urlconf: Optional[Any] = ...): ...
def translate_url(url: Any, lang_code: Any): ...
