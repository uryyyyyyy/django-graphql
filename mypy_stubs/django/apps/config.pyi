# Stubs for django.apps.config (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

MODELS_MODULE_NAME: str

class AppConfig:
    name: Any = ...
    module: Any = ...
    apps: Any = ...
    label: Any = ...
    verbose_name: Any = ...
    path: Any = ...
    models_module: Any = ...
    models: Any = ...
    def __init__(self, app_name: Any, app_module: Any) -> None: ...
    @classmethod
    def create(cls, entry: Any): ...
    def get_model(self, model_name: Any, require_ready: bool = ...): ...
    def get_models(self, include_auto_created: bool = ..., include_swapped: bool = ...) -> None: ...
    def import_models(self) -> None: ...
    def ready(self) -> None: ...