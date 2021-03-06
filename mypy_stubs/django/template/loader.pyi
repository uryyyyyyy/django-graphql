# Stubs for django.template.loader (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .exceptions import TemplateDoesNotExist
from typing import Any, Optional

def get_template(template_name: Any, using: Optional[Any] = ...): ...
def select_template(template_name_list: Any, using: Optional[Any] = ...): ...
def render_to_string(template_name: Any, context: Optional[Any] = ..., request: Optional[Any] = ..., using: Optional[Any] = ...): ...
