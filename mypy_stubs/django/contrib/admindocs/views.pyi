# Stubs for django.contrib.admindocs.views (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .utils import get_view_name
from django.views.generic import TemplateView
from typing import Any, Optional

MODEL_METHODS_EXCLUDE: Any

class BaseAdminDocsView(TemplateView):
    template_name: str = ...
    def dispatch(self, request: Any, *args: Any, **kwargs: Any): ...
    def get_context_data(self, **kwargs: Any): ...

class BookmarkletsView(BaseAdminDocsView):
    template_name: str = ...
    def get_context_data(self, **kwargs: Any): ...

class TemplateTagIndexView(BaseAdminDocsView):
    template_name: str = ...
    def get_context_data(self, **kwargs: Any): ...

class TemplateFilterIndexView(BaseAdminDocsView):
    template_name: str = ...
    def get_context_data(self, **kwargs: Any): ...

class ViewIndexView(BaseAdminDocsView):
    template_name: str = ...
    def get_context_data(self, **kwargs: Any): ...

class ViewDetailView(BaseAdminDocsView):
    template_name: str = ...
    def get_context_data(self, **kwargs: Any): ...

class ModelIndexView(BaseAdminDocsView):
    template_name: str = ...
    def get_context_data(self, **kwargs: Any): ...

class ModelDetailView(BaseAdminDocsView):
    template_name: str = ...
    def get_context_data(self, **kwargs: Any): ...

class TemplateDetailView(BaseAdminDocsView):
    template_name: str = ...
    def get_context_data(self, **kwargs: Any): ...

def get_return_data_type(func_name: Any): ...
def get_readable_field_data_type(field: Any): ...
def extract_views_from_urlpatterns(urlpatterns: Any, base: str = ..., namespace: Optional[Any] = ...): ...
def simplify_regex(pattern: Any): ...
