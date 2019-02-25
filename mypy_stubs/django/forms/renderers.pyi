# Stubs for django.forms.renderers (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

ROOT: Any

def get_default_renderer(): ...

class BaseRenderer:
    def get_template(self, template_name: Any) -> None: ...
    def render(self, template_name: Any, context: Any, request: Optional[Any] = ...): ...

class EngineMixin:
    def get_template(self, template_name: Any): ...
    def engine(self): ...

class DjangoTemplates(EngineMixin, BaseRenderer):
    backend: Any = ...

class Jinja2(EngineMixin, BaseRenderer):
    backend: Any = ...

class TemplatesSetting(BaseRenderer):
    def get_template(self, template_name: Any): ...