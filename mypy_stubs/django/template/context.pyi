# Stubs for django.template.context (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class ContextPopException(Exception): ...

class ContextDict(dict):
    context: Any = ...
    def __init__(self, context: Any, *args: Any, **kwargs: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args: Any, **kwargs: Any) -> None: ...

class BaseContext:
    def __init__(self, dict_: Optional[Any] = ...) -> None: ...
    def __copy__(self): ...
    def __iter__(self) -> None: ...
    def push(self, *args: Any, **kwargs: Any): ...
    def pop(self): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def set_upward(self, key: Any, value: Any) -> None: ...
    def __getitem__(self, key: Any): ...
    def __delitem__(self, key: Any) -> None: ...
    def __contains__(self, key: Any): ...
    def get(self, key: Any, otherwise: Optional[Any] = ...): ...
    def setdefault(self, key: Any, default: Optional[Any] = ...): ...
    def new(self, values: Optional[Any] = ...): ...
    def flatten(self): ...
    def __eq__(self, other: Any): ...

class Context(BaseContext):
    autoescape: Any = ...
    use_l10n: Any = ...
    use_tz: Any = ...
    template_name: str = ...
    render_context: Any = ...
    template: Any = ...
    def __init__(self, dict_: Optional[Any] = ..., autoescape: bool = ..., use_l10n: Optional[Any] = ..., use_tz: Optional[Any] = ...) -> None: ...
    def bind_template(self, template: Any) -> None: ...
    def __copy__(self): ...
    def update(self, other_dict: Any): ...

class RenderContext(BaseContext):
    template: Any = ...
    def __iter__(self) -> None: ...
    def __contains__(self, key: Any): ...
    def get(self, key: Any, otherwise: Optional[Any] = ...): ...
    def __getitem__(self, key: Any): ...
    def push_state(self, template: Any, isolated_context: bool = ...) -> None: ...

class RequestContext(Context):
    request: Any = ...
    def __init__(self, request: Any, dict_: Optional[Any] = ..., processors: Optional[Any] = ..., use_l10n: Optional[Any] = ..., use_tz: Optional[Any] = ..., autoescape: bool = ...) -> None: ...
    template: Any = ...
    def bind_template(self, template: Any) -> None: ...
    def new(self, values: Optional[Any] = ...): ...

def make_context(context: Any, request: Optional[Any] = ..., **kwargs: Any): ...