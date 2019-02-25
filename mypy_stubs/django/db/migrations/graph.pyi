# Stubs for django.db.migrations.graph (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .exceptions import CircularDependencyError, NodeNotFoundError
from typing import Any, Optional

RECURSION_DEPTH_WARNING: str

class Node:
    key: Any = ...
    children: Any = ...
    parents: Any = ...
    def __init__(self, key: Any) -> None: ...
    def __eq__(self, other: Any): ...
    def __lt__(self, other: Any): ...
    def __hash__(self): ...
    def __getitem__(self, item: Any): ...
    def add_child(self, child: Any) -> None: ...
    def add_parent(self, parent: Any) -> None: ...
    def ancestors(self): ...
    def descendants(self): ...

class DummyNode(Node):
    origin: Any = ...
    error_message: Any = ...
    def __init__(self, key: Any, origin: Any, error_message: Any) -> None: ...
    __class__: Any = ...
    def promote(self) -> None: ...
    def raise_error(self) -> None: ...

class MigrationGraph:
    node_map: Any = ...
    nodes: Any = ...
    cached: bool = ...
    def __init__(self) -> None: ...
    def add_node(self, key: Any, migration: Any) -> None: ...
    def add_dummy_node(self, key: Any, origin: Any, error_message: Any) -> None: ...
    def add_dependency(self, migration: Any, child: Any, parent: Any, skip_validation: bool = ...) -> None: ...
    def remove_replaced_nodes(self, replacement: Any, replaced: Any) -> None: ...
    def remove_replacement_node(self, replacement: Any, replaced: Any) -> None: ...
    def validate_consistency(self) -> None: ...
    def clear_cache(self) -> None: ...
    def forwards_plan(self, target: Any): ...
    def backwards_plan(self, target: Any): ...
    def iterative_dfs(self, start: Any, forwards: bool = ...): ...
    def root_nodes(self, app: Optional[Any] = ...): ...
    def leaf_nodes(self, app: Optional[Any] = ...): ...
    def ensure_not_cyclic(self, start: Any, get_children: Any) -> None: ...
    def make_state(self, nodes: Optional[Any] = ..., at_end: bool = ..., real_apps: Optional[Any] = ...): ...
    def __contains__(self, node: Any): ...