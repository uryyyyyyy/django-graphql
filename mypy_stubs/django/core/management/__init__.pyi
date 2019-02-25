# Stubs for django.core.management (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def find_commands(management_dir: Any): ...
def load_command_class(app_name: Any, name: Any): ...
def get_commands(): ...
def call_command(command_name: Any, *args: Any, **options: Any): ...

class ManagementUtility:
    argv: Any = ...
    prog_name: Any = ...
    settings_exception: Any = ...
    def __init__(self, argv: Optional[Any] = ...) -> None: ...
    def main_help_text(self, commands_only: bool = ...): ...
    def fetch_command(self, subcommand: Any): ...
    def autocomplete(self): ...
    def execute(self) -> None: ...

def execute_from_command_line(argv: Optional[Any] = ...) -> None: ...