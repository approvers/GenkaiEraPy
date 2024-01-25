from pydantic import Field

from src.domain.base.value import ValueObject


class UserIdentifier(ValueObject):
    value: str = Field(
        description="ID of user, must be unique and cannot be changed.",
    )


class UserNickname(ValueObject):
    value: str = Field(
        description="Nickname of user, which is displayed as user's name.\n"
                    "Not unique like @username in X ( Twitter ).",
    )
