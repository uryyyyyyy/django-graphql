# Stubs for django.core.mail.backends.smtp (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.mail.backends.base import BaseEmailBackend
from typing import Any, Optional

class EmailBackend(BaseEmailBackend):
    host: Any = ...
    port: Any = ...
    username: Any = ...
    password: Any = ...
    use_tls: Any = ...
    use_ssl: Any = ...
    timeout: Any = ...
    ssl_keyfile: Any = ...
    ssl_certfile: Any = ...
    connection: Any = ...
    def __init__(self, host: Optional[Any] = ..., port: Optional[Any] = ..., username: Optional[Any] = ..., password: Optional[Any] = ..., use_tls: Optional[Any] = ..., fail_silently: bool = ..., use_ssl: Optional[Any] = ..., timeout: Optional[Any] = ..., ssl_keyfile: Optional[Any] = ..., ssl_certfile: Optional[Any] = ..., **kwargs: Any) -> None: ...
    @property
    def connection_class(self): ...
    def open(self): ...
    def close(self) -> None: ...
    def send_messages(self, email_messages: Any): ...
