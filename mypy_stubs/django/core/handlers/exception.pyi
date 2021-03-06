# Stubs for django.core.handlers.exception (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def convert_exception_to_response(get_response: Any): ...
def response_for_exception(request: Any, exc: Any): ...
def get_exception_response(request: Any, resolver: Any, status_code: Any, exception: Any, sender: Optional[Any] = ...): ...
def handle_uncaught_exception(request: Any, resolver: Any, exc_info: Any): ...
