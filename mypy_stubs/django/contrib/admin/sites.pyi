# Stubs for django.contrib.admin.sites (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.utils.functional import LazyObject
from typing import Any, Optional

all_sites: Any

class AlreadyRegistered(Exception): ...
class NotRegistered(Exception): ...

class AdminSite:
    site_title: Any = ...
    site_header: Any = ...
    index_title: Any = ...
    site_url: str = ...
    login_form: Any = ...
    index_template: Any = ...
    app_index_template: Any = ...
    login_template: Any = ...
    logout_template: Any = ...
    password_change_template: Any = ...
    password_change_done_template: Any = ...
    name: Any = ...
    def __init__(self, name: str = ...) -> None: ...
    def check(self, app_configs: Any): ...
    def register(self, model_or_iterable: Any, admin_class: Optional[Any] = ..., **options: Any) -> None: ...
    def unregister(self, model_or_iterable: Any) -> None: ...
    def is_registered(self, model: Any): ...
    def add_action(self, action: Any, name: Optional[Any] = ...) -> None: ...
    def disable_action(self, name: Any) -> None: ...
    def get_action(self, name: Any): ...
    @property
    def actions(self): ...
    @property
    def empty_value_display(self): ...
    @empty_value_display.setter
    def empty_value_display(self, empty_value_display: Any) -> None: ...
    def has_permission(self, request: Any): ...
    def admin_view(self, view: Any, cacheable: bool = ...): ...
    def get_urls(self): ...
    @property
    def urls(self): ...
    def each_context(self, request: Any): ...
    def password_change(self, request: Any, extra_context: Optional[Any] = ...): ...
    def password_change_done(self, request: Any, extra_context: Optional[Any] = ...): ...
    def i18n_javascript(self, request: Any, extra_context: Optional[Any] = ...): ...
    def logout(self, request: Any, extra_context: Optional[Any] = ...): ...
    def login(self, request: Any, extra_context: Optional[Any] = ...): ...
    def get_app_list(self, request: Any): ...
    def index(self, request: Any, extra_context: Optional[Any] = ...): ...
    def app_index(self, request: Any, app_label: Any, extra_context: Optional[Any] = ...): ...

class DefaultAdminSite(LazyObject): ...

site: Any