# Stubs for django.db.backends.mysql.creation (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .client import DatabaseClient
from django.db.backends.base.creation import BaseDatabaseCreation

class DatabaseCreation(BaseDatabaseCreation):
    def sql_table_creation_suffix(self): ...
