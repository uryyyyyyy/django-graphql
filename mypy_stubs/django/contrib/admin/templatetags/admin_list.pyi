# Stubs for django.contrib.admin.templatetags.admin_list (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .base import InclusionAdminNode
from typing import Any

register: Any
DOT: str

def paginator_number(cl: Any, i: Any): ...
def pagination(cl: Any): ...
def pagination_tag(parser: Any, token: Any): ...
def result_headers(cl: Any): ...
def items_for_result(cl: Any, result: Any, form: Any): ...

class ResultList(list):
    form: Any = ...
    def __init__(self, form: Any, *items: Any) -> None: ...

def results(cl: Any) -> None: ...
def result_hidden_fields(cl: Any) -> None: ...
def result_list(cl: Any): ...
def result_list_tag(parser: Any, token: Any): ...
def date_hierarchy(cl: Any): ...
def date_hierarchy_tag(parser: Any, token: Any): ...
def search_form(cl: Any): ...
def search_form_tag(parser: Any, token: Any): ...
def admin_list_filter(cl: Any, spec: Any): ...
def admin_actions(context: Any): ...
def admin_actions_tag(parser: Any, token: Any): ...
def change_list_object_tools_tag(parser: Any, token: Any): ...