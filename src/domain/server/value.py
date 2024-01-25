from pydantic import Field

from src.domain.base.value import ValueObject


class ServerIdentifier(ValueObject):
    value: str = Field(
        description="ID of server, must be unique and cannot be changed.",
    )
