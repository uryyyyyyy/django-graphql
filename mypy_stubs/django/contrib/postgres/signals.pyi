# Stubs for django.contrib.postgres.signals (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def get_hstore_oids(connection_alias: Any): ...
def get_citext_oids(connection_alias: Any): ...
def register_type_handlers(connection: Any, **kwargs: Any) -> None: ...
