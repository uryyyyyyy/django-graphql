# Stubs for django.contrib.sites.requests (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class RequestSite:
    domain: Any = ...
    def __init__(self, request: Any) -> None: ...
    def save(self, force_insert: bool = ..., force_update: bool = ...) -> None: ...
    def delete(self) -> None: ...