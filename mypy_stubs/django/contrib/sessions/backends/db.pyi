# Stubs for django.contrib.sessions.backends.db (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.contrib.sessions.backends.base import SessionBase
from typing import Any, Optional

class SessionStore(SessionBase):
    def __init__(self, session_key: Optional[Any] = ...) -> None: ...
    @classmethod
    def get_model_class(cls): ...
    def model(self): ...
    def load(self): ...
    def exists(self, session_key: Any): ...
    modified: bool = ...
    def create(self) -> None: ...
    def create_model_instance(self, data: Any): ...
    def save(self, must_create: bool = ...): ...
    def delete(self, session_key: Optional[Any] = ...) -> None: ...
    @classmethod
    def clear_expired(cls) -> None: ...
