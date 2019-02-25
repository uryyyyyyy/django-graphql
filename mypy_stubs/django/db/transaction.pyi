# Stubs for django.db.transaction (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from contextlib import ContextDecorator
from django.db import ProgrammingError
from typing import Any, Optional

class TransactionManagementError(ProgrammingError): ...

def get_connection(using: Optional[Any] = ...): ...
def get_autocommit(using: Optional[Any] = ...): ...
def set_autocommit(autocommit: Any, using: Optional[Any] = ...): ...
def commit(using: Optional[Any] = ...) -> None: ...
def rollback(using: Optional[Any] = ...) -> None: ...
def savepoint(using: Optional[Any] = ...): ...
def savepoint_rollback(sid: Any, using: Optional[Any] = ...) -> None: ...
def savepoint_commit(sid: Any, using: Optional[Any] = ...) -> None: ...
def clean_savepoints(using: Optional[Any] = ...) -> None: ...
def get_rollback(using: Optional[Any] = ...): ...
def set_rollback(rollback: Any, using: Optional[Any] = ...): ...
def on_commit(func: Any, using: Optional[Any] = ...) -> None: ...

class Atomic(ContextDecorator):
    using: Any = ...
    savepoint: Any = ...
    def __init__(self, using: Any, savepoint: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...

def atomic(using: Optional[Any] = ..., savepoint: bool = ...): ...
def non_atomic_requests(using: Optional[Any] = ...): ...