from pydantic import HttpUrl

from src.domain.base.value import ValueObject


class UserID(ValueObject):
    value: str


class UserNickname(ValueObject):
    value: str
