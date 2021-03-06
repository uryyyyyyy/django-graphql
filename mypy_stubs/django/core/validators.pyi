# Stubs for django.core.validators (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

EMPTY_VALUES: Any

class RegexValidator:
    regex: str = ...
    message: Any = ...
    code: str = ...
    inverse_match: bool = ...
    flags: int = ...
    def __init__(self, regex: Optional[Any] = ..., message: Optional[Any] = ..., code: Optional[Any] = ..., inverse_match: Optional[Any] = ..., flags: Optional[Any] = ...) -> None: ...
    def __call__(self, value: Any) -> None: ...
    def __eq__(self, other: Any): ...

class URLValidator(RegexValidator):
    ul: str = ...
    ipv4_re: str = ...
    ipv6_re: str = ...
    hostname_re: Any = ...
    domain_re: Any = ...
    tld_re: Any = ...
    host_re: Any = ...
    regex: Any = ...
    message: Any = ...
    schemes: Any = ...
    def __init__(self, schemes: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def __call__(self, value: Any) -> None: ...

integer_validator: Any

def validate_integer(value: Any): ...

class EmailValidator:
    message: Any = ...
    code: str = ...
    user_regex: Any = ...
    domain_regex: Any = ...
    literal_regex: Any = ...
    domain_whitelist: Any = ...
    def __init__(self, message: Optional[Any] = ..., code: Optional[Any] = ..., whitelist: Optional[Any] = ...) -> None: ...
    def __call__(self, value: Any) -> None: ...
    def validate_domain_part(self, domain_part: Any): ...
    def __eq__(self, other: Any): ...

validate_email: Any
slug_re: Any
validate_slug: Any
slug_unicode_re: Any
validate_unicode_slug: Any

def validate_ipv4_address(value: Any) -> None: ...
def validate_ipv6_address(value: Any) -> None: ...
def validate_ipv46_address(value: Any) -> None: ...

ip_address_validator_map: Any

def ip_address_validators(protocol: Any, unpack_ipv4: Any): ...
def int_list_validator(sep: str = ..., message: Optional[Any] = ..., code: str = ..., allow_negative: bool = ...): ...

validate_comma_separated_integer_list: Any

class BaseValidator:
    message: Any = ...
    code: str = ...
    limit_value: Any = ...
    def __init__(self, limit_value: Any, message: Optional[Any] = ...) -> None: ...
    def __call__(self, value: Any) -> None: ...
    def __eq__(self, other: Any): ...
    def compare(self, a: Any, b: Any): ...
    def clean(self, x: Any): ...

class MaxValueValidator(BaseValidator):
    message: Any = ...
    code: str = ...
    def compare(self, a: Any, b: Any): ...

class MinValueValidator(BaseValidator):
    message: Any = ...
    code: str = ...
    def compare(self, a: Any, b: Any): ...

class MinLengthValidator(BaseValidator):
    message: Any = ...
    code: str = ...
    def compare(self, a: Any, b: Any): ...
    def clean(self, x: Any): ...

class MaxLengthValidator(BaseValidator):
    message: Any = ...
    code: str = ...
    def compare(self, a: Any, b: Any): ...
    def clean(self, x: Any): ...

class DecimalValidator:
    messages: Any = ...
    max_digits: Any = ...
    decimal_places: Any = ...
    def __init__(self, max_digits: Any, decimal_places: Any) -> None: ...
    def __call__(self, value: Any) -> None: ...
    def __eq__(self, other: Any): ...

class FileExtensionValidator:
    message: Any = ...
    code: str = ...
    allowed_extensions: Any = ...
    def __init__(self, allowed_extensions: Optional[Any] = ..., message: Optional[Any] = ..., code: Optional[Any] = ...) -> None: ...
    def __call__(self, value: Any) -> None: ...
    def __eq__(self, other: Any): ...

def get_available_image_extensions(): ...
def validate_image_file_extension(value: Any): ...

class ProhibitNullCharactersValidator:
    message: Any = ...
    code: str = ...
    def __init__(self, message: Optional[Any] = ..., code: Optional[Any] = ...) -> None: ...
    def __call__(self, value: Any) -> None: ...
    def __eq__(self, other: Any): ...
