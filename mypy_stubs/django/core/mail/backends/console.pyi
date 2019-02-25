# Stubs for django.core.mail.backends.console (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.mail.backends.base import BaseEmailBackend
from typing import Any

class EmailBackend(BaseEmailBackend):
    stream: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def write_message(self, message: Any) -> None: ...
    def send_messages(self, email_messages: Any): ...
