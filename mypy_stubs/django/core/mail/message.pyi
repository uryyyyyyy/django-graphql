# Stubs for django.core.mail.message (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from email.mime.message import MIMEMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any, Optional

utf8_charset: Any
utf8_charset_qp: Any
DEFAULT_ATTACHMENT_MIME_TYPE: str
RFC5322_EMAIL_LINE_LENGTH_LIMIT: int

class BadHeaderError(ValueError): ...

ADDRESS_HEADERS: Any

def forbid_multi_line_headers(name: Any, val: Any, encoding: Any): ...
def split_addr(addr: Any, encoding: Any): ...
def sanitize_address(addr: Any, encoding: Any): ...

class MIMEMixin:
    def as_string(self, unixfrom: bool = ..., linesep: str = ...): ...
    def as_bytes(self, unixfrom: bool = ..., linesep: str = ...): ...

class SafeMIMEMessage(MIMEMixin, MIMEMessage):
    def __setitem__(self, name: Any, val: Any) -> None: ...

class SafeMIMEText(MIMEMixin, MIMEText):
    encoding: Any = ...
    def __init__(self, _text: Any, _subtype: str = ..., _charset: Optional[Any] = ...) -> None: ...
    def __setitem__(self, name: Any, val: Any) -> None: ...
    def set_payload(self, payload: Any, charset: Optional[Any] = ...) -> None: ...

class SafeMIMEMultipart(MIMEMixin, MIMEMultipart):
    encoding: Any = ...
    def __init__(self, _subtype: str = ..., boundary: Optional[Any] = ..., _subparts: Optional[Any] = ..., encoding: Optional[Any] = ..., **_params: Any) -> None: ...
    def __setitem__(self, name: Any, val: Any) -> None: ...

class EmailMessage:
    content_subtype: str = ...
    mixed_subtype: str = ...
    encoding: Any = ...
    to: Any = ...
    cc: Any = ...
    bcc: Any = ...
    reply_to: Any = ...
    from_email: Any = ...
    subject: Any = ...
    body: Any = ...
    attachments: Any = ...
    extra_headers: Any = ...
    connection: Any = ...
    def __init__(self, subject: str = ..., body: str = ..., from_email: Optional[Any] = ..., to: Optional[Any] = ..., bcc: Optional[Any] = ..., connection: Optional[Any] = ..., attachments: Optional[Any] = ..., headers: Optional[Any] = ..., cc: Optional[Any] = ..., reply_to: Optional[Any] = ...) -> None: ...
    def get_connection(self, fail_silently: bool = ...): ...
    def message(self): ...
    def recipients(self): ...
    def send(self, fail_silently: bool = ...): ...
    def attach(self, filename: Optional[Any] = ..., content: Optional[Any] = ..., mimetype: Optional[Any] = ...) -> None: ...
    def attach_file(self, path: Any, mimetype: Optional[Any] = ...) -> None: ...

class EmailMultiAlternatives(EmailMessage):
    alternative_subtype: str = ...
    alternatives: Any = ...
    def __init__(self, subject: str = ..., body: str = ..., from_email: Optional[Any] = ..., to: Optional[Any] = ..., bcc: Optional[Any] = ..., connection: Optional[Any] = ..., attachments: Optional[Any] = ..., headers: Optional[Any] = ..., alternatives: Optional[Any] = ..., cc: Optional[Any] = ..., reply_to: Optional[Any] = ...) -> None: ...
    def attach_alternative(self, content: Any, mimetype: Any) -> None: ...
