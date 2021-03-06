# Stubs for django.db.backends.oracle.compiler (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.models.sql import compiler

class SQLCompiler(compiler.SQLCompiler):
    def as_sql(self, with_limits: bool = ..., with_col_aliases: bool = ...): ...

class SQLInsertCompiler(compiler.SQLInsertCompiler, SQLCompiler): ...
class SQLDeleteCompiler(compiler.SQLDeleteCompiler, SQLCompiler): ...
class SQLUpdateCompiler(compiler.SQLUpdateCompiler, SQLCompiler): ...
class SQLAggregateCompiler(compiler.SQLAggregateCompiler, SQLCompiler): ...
