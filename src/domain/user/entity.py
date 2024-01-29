from src.domain.base.entity import Entity
from src.domain.user.value import (
    UserIdentifier,
    UserNickname,
    UserRecordCreatedAt,
    UserRecordUpdatedAt,
)


class User(Entity):
    created_at: UserRecordCreatedAt
    updated_at: UserRecordUpdatedAt

    identifier: UserIdentifier

    nickname: UserNickname
