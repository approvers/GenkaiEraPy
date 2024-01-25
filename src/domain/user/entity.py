from src.domain.base.entity import Entity
from src.domain.user.field import UserIdentifier, UserNickname


class User(Entity):
    identifier: UserIdentifier
    nickname: UserNickname
