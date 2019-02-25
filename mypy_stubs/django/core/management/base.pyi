# Stubs for django.core.management.base (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from argparse import ArgumentParser, HelpFormatter
from io import TextIOBase
from typing import Any, Optional

class CommandError(Exception): ...
class SystemCheckError(CommandError): ...

class CommandParser(ArgumentParser):
    missing_args_message: Any = ...
    called_from_command_line: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def parse_args(self, args: Optional[Any] = ..., namespace: Optional[Any] = ...): ...
    def error(self, message: Any) -> None: ...

def handle_default_options(options: Any) -> None: ...
def no_translations(handle_func: Any): ...

class DjangoHelpFormatter(HelpFormatter):
    show_last: Any = ...
    def add_usage(self, usage: Any, actions: Any, *args: Any, **kwargs: Any) -> None: ...
    def add_arguments(self, actions: Any) -> None: ...

class OutputWrapper(TextIOBase):
    @property
    def style_func(self): ...
    @style_func.setter
    def style_func(self, style_func: Any): ...
    style_func: Any = ...
    ending: Any = ...
    def __init__(self, out: Any, style_func: Optional[Any] = ..., ending: str = ...) -> None: ...
    def __getattr__(self, name: Any): ...
    def isatty(self): ...
    def write(self, msg: Any, style_func: Optional[Any] = ..., ending: Optional[Any] = ...) -> None: ...

class BaseCommand:
    help: str = ...
    output_transaction: bool = ...
    requires_migrations_checks: bool = ...
    requires_system_checks: bool = ...
    base_stealth_options: Any = ...
    stealth_options: Any = ...
    stdout: Any = ...
    stderr: Any = ...
    style: Any = ...
    def __init__(self, stdout: Optional[Any] = ..., stderr: Optional[Any] = ..., no_color: bool = ...) -> None: ...
    def get_version(self): ...
    def create_parser(self, prog_name: Any, subcommand: Any): ...
    def add_arguments(self, parser: Any) -> None: ...
    def print_help(self, prog_name: Any, subcommand: Any) -> None: ...
    def run_from_argv(self, argv: Any): ...
    def execute(self, *args: Any, **options: Any): ...
    def check(self, app_configs: Optional[Any] = ..., tags: Optional[Any] = ..., display_num_errors: bool = ..., include_deployment_checks: bool = ..., fail_level: Any = ...): ...
    def check_migrations(self) -> None: ...
    def handle(self, *args: Any, **options: Any) -> None: ...

class AppCommand(BaseCommand):
    missing_args_message: str = ...
    def add_arguments(self, parser: Any) -> None: ...
    def handle(self, *app_labels: Any, **options: Any): ...
    def handle_app_config(self, app_config: Any, **options: Any) -> None: ...

class LabelCommand(BaseCommand):
    label: str = ...
    missing_args_message: Any = ...
    def add_arguments(self, parser: Any) -> None: ...
    def handle(self, *labels: Any, **options: Any): ...
    def handle_label(self, label: Any, **options: Any) -> None: ...
