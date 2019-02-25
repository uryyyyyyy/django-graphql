# Stubs for django.contrib.auth.password_validation (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def get_default_password_validators(): ...
def get_password_validators(validator_config: Any): ...
def validate_password(password: Any, user: Optional[Any] = ..., password_validators: Optional[Any] = ...) -> None: ...
def password_changed(password: Any, user: Optional[Any] = ..., password_validators: Optional[Any] = ...) -> None: ...
def password_validators_help_texts(password_validators: Optional[Any] = ...): ...

password_validators_help_text_html: Any

class MinimumLengthValidator:
    min_length: Any = ...
    def __init__(self, min_length: int = ...) -> None: ...
    def validate(self, password: Any, user: Optional[Any] = ...) -> None: ...
    def get_help_text(self): ...

class UserAttributeSimilarityValidator:
    DEFAULT_USER_ATTRIBUTES: Any = ...
    user_attributes: Any = ...
    max_similarity: Any = ...
    def __init__(self, user_attributes: Any = ..., max_similarity: float = ...) -> None: ...
    def validate(self, password: Any, user: Optional[Any] = ...) -> None: ...
    def get_help_text(self): ...

class CommonPasswordValidator:
    DEFAULT_PASSWORD_LIST_PATH: Any = ...
    passwords: Any = ...
    def __init__(self, password_list_path: Any = ...) -> None: ...
    def validate(self, password: Any, user: Optional[Any] = ...) -> None: ...
    def get_help_text(self): ...

class NumericPasswordValidator:
    def validate(self, password: Any, user: Optional[Any] = ...) -> None: ...
    def get_help_text(self): ...