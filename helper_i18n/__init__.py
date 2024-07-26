from typing import Any, Optional

from helper_i18n.typing import errors


class CustomException(Exception):
    def __init__(
        self,
        status_code: int,
        i8n_key: str,
        errors: Optional[errors] = None,
        **params: Any,
    ) -> None:
        self.status_code = status_code
        self.i8n_key = i8n_key
        self.errors = errors
        self.params = params
        super().__init__()
