# Stubs for django.core.files.uploadedfile (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.files.base import File
from typing import Any, Optional

class UploadedFile(File):
    size: Any = ...
    content_type: Any = ...
    charset: Any = ...
    content_type_extra: Any = ...
    def __init__(self, file: Optional[Any] = ..., name: Optional[Any] = ..., content_type: Optional[Any] = ..., size: Optional[Any] = ..., charset: Optional[Any] = ..., content_type_extra: Optional[Any] = ...) -> None: ...
    name: Any = ...

class TemporaryUploadedFile(UploadedFile):
    def __init__(self, name: Any, content_type: Any, size: Any, charset: Any, content_type_extra: Optional[Any] = ...) -> None: ...
    def temporary_file_path(self): ...
    def close(self): ...

class InMemoryUploadedFile(UploadedFile):
    field_name: Any = ...
    def __init__(self, file: Any, field_name: Any, name: Any, content_type: Any, size: Any, charset: Any, content_type_extra: Optional[Any] = ...) -> None: ...
    def open(self, mode: Optional[Any] = ...): ...
    def chunks(self, chunk_size: Optional[Any] = ...) -> None: ...
    def multiple_chunks(self, chunk_size: Optional[Any] = ...): ...

class SimpleUploadedFile(InMemoryUploadedFile):
    def __init__(self, name: Any, content: Any, content_type: str = ...) -> None: ...
    @classmethod
    def from_dict(cls, file_dict: Any): ...