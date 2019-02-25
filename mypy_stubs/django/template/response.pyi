# Stubs for django.template.response (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .loader import get_template, select_template
from django.http import HttpResponse
from typing import Any, Optional

class ContentNotRenderedError(Exception): ...

class SimpleTemplateResponse(HttpResponse):
    rendering_attrs: Any = ...
    template_name: Any = ...
    context_data: Any = ...
    using: Any = ...
    def __init__(self, template: Any, context: Optional[Any] = ..., content_type: Optional[Any] = ..., status: Optional[Any] = ..., charset: Optional[Any] = ..., using: Optional[Any] = ...) -> None: ...
    def resolve_template(self, template: Any): ...
    def resolve_context(self, context: Any): ...
    @property
    def rendered_content(self): ...
    def add_post_render_callback(self, callback: Any) -> None: ...
    content: Any = ...
    def render(self): ...
    @property
    def is_rendered(self): ...
    def __iter__(self): ...
    @property
    def content(self): ...
    @content.setter
    def content(self, value: Any) -> None: ...

class TemplateResponse(SimpleTemplateResponse):
    rendering_attrs: Any = ...
    def __init__(self, request: Any, template: Any, context: Optional[Any] = ..., content_type: Optional[Any] = ..., status: Optional[Any] = ..., charset: Optional[Any] = ..., using: Optional[Any] = ...) -> None: ...