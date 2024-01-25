from pydantic import Field

from src.domain.base.value import ValueObject


class ServerIdentifier(ValueObject):
    value: str = Field(
        description="ID of server, must be unique and cannot be changed.",
    )


class ServerName(ValueObject):
    value: str = Field(
        description="Name of server, which is displayed as server's name.\n"
        "Not unique like @username in X ( Twitter ).",
    )
