# Stubs for django.core.files.base (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.files.utils import FileProxyMixin
from typing import Any, Optional

class File(FileProxyMixin):
    DEFAULT_CHUNK_SIZE: Any = ...
    file: Any = ...
    name: Any = ...
    mode: Any = ...
    def __init__(self, file: Any, name: Optional[Any] = ...) -> None: ...
    def __bool__(self): ...
    def __len__(self): ...
    def size(self): ...
    def chunks(self, chunk_size: Optional[Any] = ...) -> None: ...
    def multiple_chunks(self, chunk_size: Optional[Any] = ...): ...
    def __iter__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_value: Any, tb: Any) -> None: ...
    def open(self, mode: Optional[Any] = ...): ...
    def close(self) -> None: ...

class ContentFile(File):
    size: Any = ...
    def __init__(self, content: Any, name: Optional[Any] = ...) -> None: ...
    def __bool__(self): ...
    def open(self, mode: Optional[Any] = ...): ...
    def close(self) -> None: ...
    def write(self, data: Any): ...

def endswith_cr(line: Any): ...
def endswith_lf(line: Any): ...
def equals_lf(line: Any): ...
