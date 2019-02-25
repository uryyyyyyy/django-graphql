# Stubs for django.contrib.sessions.middleware (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.utils.deprecation import MiddlewareMixin
from typing import Any, Optional

class SessionMiddleware(MiddlewareMixin):
    get_response: Any = ...
    SessionStore: Any = ...
    def __init__(self, get_response: Optional[Any] = ...) -> None: ...
    def process_request(self, request: Any) -> None: ...
    def process_response(self, request: Any, response: Any): ...