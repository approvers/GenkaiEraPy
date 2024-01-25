from src.domain.base.entity import Entity
from src.domain.common.value import NullableCreatedAt, NullableUpdatedAt
from src.domain.user.field import UserIdentifier, UserNickname


class User(Entity):
    created_at: NullableCreatedAt
    updated_at: NullableUpdatedAt

    identifier: UserIdentifier
    nickname: UserNickname
