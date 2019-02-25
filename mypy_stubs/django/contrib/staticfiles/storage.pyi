# Stubs for django.contrib.staticfiles.storage (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.files.storage import FileSystemStorage
from django.utils.functional import LazyObject
from typing import Any, Optional

class StaticFilesStorage(FileSystemStorage):
    base_location: Any = ...
    location: Any = ...
    def __init__(self, location: Optional[Any] = ..., base_url: Optional[Any] = ..., *args: Any, **kwargs: Any) -> None: ...
    def path(self, name: Any): ...

class HashedFilesMixin:
    default_template: str = ...
    max_post_process_passes: int = ...
    patterns: Any = ...
    hashed_files: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def file_hash(self, name: Any, content: Optional[Any] = ...): ...
    def hashed_name(self, name: Any, content: Optional[Any] = ..., filename: Optional[Any] = ...): ...
    def url(self, name: Any, force: bool = ...): ...
    def url_converter(self, name: Any, hashed_files: Any, template: Optional[Any] = ...): ...
    def post_process(self, paths: Any, dry_run: bool = ..., **options: Any) -> None: ...
    def clean_name(self, name: Any): ...
    def hash_key(self, name: Any): ...
    def stored_name(self, name: Any): ...

class ManifestFilesMixin(HashedFilesMixin):
    manifest_version: str = ...
    manifest_name: str = ...
    manifest_strict: bool = ...
    hashed_files: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def read_manifest(self): ...
    def load_manifest(self): ...
    def post_process(self, *args: Any, **kwargs: Any) -> None: ...
    def save_manifest(self) -> None: ...
    def stored_name(self, name: Any): ...

class _MappingCache:
    cache: Any = ...
    def __init__(self, cache: Any) -> None: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __getitem__(self, key: Any): ...
    def clear(self) -> None: ...
    def update(self, data: Any) -> None: ...
    def get(self, key: Any, default: Optional[Any] = ...): ...

class CachedFilesMixin(HashedFilesMixin):
    hashed_files: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def hash_key(self, name: Any): ...

class CachedStaticFilesStorage(CachedFilesMixin, StaticFilesStorage): ...
class ManifestStaticFilesStorage(ManifestFilesMixin, StaticFilesStorage): ...
class ConfiguredStorage(LazyObject): ...

staticfiles_storage: Any
