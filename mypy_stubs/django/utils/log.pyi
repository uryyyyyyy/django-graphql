# Stubs for django.utils.log (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import logging.config
from typing import Any, Optional

request_logger: Any
DEFAULT_LOGGING: Any

def configure_logging(logging_config: Any, logging_settings: Any) -> None: ...

class AdminEmailHandler(logging.Handler):
    include_html: Any = ...
    email_backend: Any = ...
    def __init__(self, include_html: bool = ..., email_backend: Optional[Any] = ...) -> None: ...
    def emit(self, record: Any) -> None: ...
    def send_mail(self, subject: Any, message: Any, *args: Any, **kwargs: Any) -> None: ...
    def connection(self): ...
    def format_subject(self, subject: Any): ...

class CallbackFilter(logging.Filter):
    callback: Any = ...
    def __init__(self, callback: Any) -> None: ...
    def filter(self, record: Any): ...

class RequireDebugFalse(logging.Filter):
    def filter(self, record: Any): ...

class RequireDebugTrue(logging.Filter):
    def filter(self, record: Any): ...

class ServerFormatter(logging.Formatter):
    style: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def format(self, record: Any): ...
    def uses_server_time(self): ...

def log_response(message: Any, *args: Any, response: Optional[Any] = ..., request: Optional[Any] = ..., logger: Any = ..., level: Optional[Any] = ..., exc_info: Optional[Any] = ...) -> None: ...
