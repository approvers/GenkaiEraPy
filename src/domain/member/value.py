from pydantic import Field

from src.domain.base.value import ValueObject


class MemberLocalNickname(ValueObject):
    value: str = Field(
        description="Nickname of member, which is displayed as member's name.\n"
        "Not unique like @username in X ( Twitter )."
        "This is local nickname, which is used in a specific community like a server in Discord.",
    )
