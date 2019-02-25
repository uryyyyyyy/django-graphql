# Stubs for django.utils.datastructures (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class OrderedSet:
    dict: Any = ...
    def __init__(self, iterable: Optional[Any] = ...) -> None: ...
    def add(self, item: Any) -> None: ...
    def remove(self, item: Any) -> None: ...
    def discard(self, item: Any) -> None: ...
    def __iter__(self): ...
    def __contains__(self, item: Any): ...
    def __bool__(self): ...
    def __len__(self): ...

class MultiValueDictKeyError(KeyError): ...

class MultiValueDict(dict):
    def __init__(self, key_to_list_mapping: Any = ...) -> None: ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __copy__(self): ...
    def __deepcopy__(self, memo: Any): ...
    def get(self, key: Any, default: Optional[Any] = ...): ...
    def getlist(self, key: Any, default: Optional[Any] = ...): ...
    def setlist(self, key: Any, list_: Any) -> None: ...
    def setdefault(self, key: Any, default: Optional[Any] = ...): ...
    def setlistdefault(self, key: Any, default_list: Optional[Any] = ...): ...
    def appendlist(self, key: Any, value: Any) -> None: ...
    def items(self) -> Any: ...
    def lists(self): ...
    def values(self) -> Any: ...
    def copy(self): ...
    def update(self, *args: Any, **kwargs: Any) -> None: ...
    def dict(self): ...

class ImmutableList(tuple):
    warning: Any = ...
    def __new__(cls, *args: Any, warning: str = ..., **kwargs: Any): ...
    def complain(self, *wargs: Any, **kwargs: Any) -> None: ...
    __delitem__: Any = ...
    __delslice__: Any = ...
    __iadd__: Any = ...
    __imul__: Any = ...
    __setitem__: Any = ...
    __setslice__: Any = ...
    append: Any = ...
    extend: Any = ...
    insert: Any = ...
    pop: Any = ...
    remove: Any = ...
    sort: Any = ...
    reverse: Any = ...

class DictWrapper(dict):
    func: Any = ...
    prefix: Any = ...
    def __init__(self, data: Any, func: Any, prefix: Any) -> None: ...
    def __getitem__(self, key: Any): ...