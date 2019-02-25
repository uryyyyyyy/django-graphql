# Stubs for django.contrib.messages.middleware (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.utils.deprecation import MiddlewareMixin
from typing import Any

class MessageMiddleware(MiddlewareMixin):
    def process_request(self, request: Any) -> None: ...
    def process_response(self, request: Any, response: Any): ...