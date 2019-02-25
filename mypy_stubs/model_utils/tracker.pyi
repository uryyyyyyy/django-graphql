# Stubs for model_utils.tracker (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class DescriptorMixin:
    tracker_instance: Any = ...
    def __get__(self, instance: Any, owner: Any): ...

class FieldInstanceTracker:
    instance: Any = ...
    fields: Any = ...
    field_map: Any = ...
    def __init__(self, instance: Any, fields: Any, field_map: Any) -> None: ...
    def get_field_value(self, field: Any): ...
    saved_data: Any = ...
    def set_saved_fields(self, fields: Optional[Any] = ...) -> None: ...
    def current(self, fields: Optional[Any] = ...): ...
    def has_changed(self, field: Any): ...
    def previous(self, field: Any): ...
    def changed(self): ...
    def init_deferred_fields(self): ...

class FieldTracker:
    tracker_class: Any = ...
    fields: Any = ...
    def __init__(self, fields: Optional[Any] = ...) -> None: ...
    def get_field_map(self, cls: Any): ...
    name: Any = ...
    attname: Any = ...
    def contribute_to_class(self, cls: Any, name: Any) -> None: ...
    field_map: Any = ...
    model_class: Any = ...
    def finalize_class(self, sender: Any, **kwargs: Any) -> None: ...
    def initialize_tracker(self, sender: Any, instance: Any, **kwargs: Any) -> None: ...
    def patch_save(self, instance: Any): ...
    def __get__(self, instance: Any, owner: Any): ...

class ModelInstanceTracker(FieldInstanceTracker):
    def has_changed(self, field: Any): ...
    def changed(self): ...

class ModelTracker(FieldTracker):
    tracker_class: Any = ...
    def get_field_map(self, cls: Any): ...