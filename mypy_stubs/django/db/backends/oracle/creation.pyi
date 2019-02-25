# Stubs for django.db.backends.oracle.creation (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.backends.base.creation import BaseDatabaseCreation
from typing import Any

TEST_DATABASE_PREFIX: str

class DatabaseCreation(BaseDatabaseCreation):
    def set_as_test_mirror(self, primary_settings_dict: Any) -> None: ...
    def test_db_signature(self): ...
