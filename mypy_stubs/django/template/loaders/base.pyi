# Stubs for django.template.loaders.base (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class Loader:
    engine: Any = ...
    def __init__(self, engine: Any) -> None: ...
    def get_template(self, template_name: Any, skip: Optional[Any] = ...): ...
    def get_template_sources(self, template_name: Any) -> None: ...
    def reset(self) -> None: ...
