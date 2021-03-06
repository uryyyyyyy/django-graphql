# Stubs for django.contrib.auth.apps (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .checks import check_models_permissions, check_user_model
from .management import create_permissions
from .signals import user_logged_in
from django.apps import AppConfig
from typing import Any

class AuthConfig(AppConfig):
    name: str = ...
    verbose_name: Any = ...
    def ready(self) -> None: ...
