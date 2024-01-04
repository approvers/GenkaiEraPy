import uuid
from typing import Any, Optional
from uuid import UUID

from sqlalchemy import Dialect, String, types


# Name this class "SAUUID" to avoid name conflicts with the standard package uuid.UUID
class SAUUID(types.TypeDecorator[uuid.UUID]):
    impl = String
    cache_ok: bool = True

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        _ = args, kwargs

        self.impl.length = 36
        types.TypeDecorator.__init__(self, length=self.impl.length)

    def process_bind_param(
        self, value: Optional[UUID], dialect: Optional[Dialect] = None
    ) -> Optional[str]:
        if value is None:
            return None

        if isinstance(value, UUID):
            return str(value)

        raise ValueError(
            f"ValueError: value '{value}' is not a valid instance of 'uuid.UUID'."
        )

    def process_result_value(
        self, value: Optional[str], dialect: Optional[Dialect] = None
    ) -> Optional[UUID]:
        if value is None:
            return None

        if isinstance(value, str):
            return UUID(value)

        raise ValueError(
            f"ValueError: value '{value}' is not 'None' or a valid instance of 'uuid.UUID'."
        )

    # noinspection PyMethodMayBeStatic
    def is_mutable(self) -> bool:
        return False
