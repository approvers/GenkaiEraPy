from src.domain.base.entity import Entity
from src.domain.user.field import UserID, UserNickname


class User(Entity):
    id: UserID
    nickname: UserNickname
