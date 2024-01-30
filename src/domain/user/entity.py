from src.domain.base.entity import Entity
from src.domain.user.value import (
    UserIdentifier,
    UserNickname,
    UserRecordCreatedAt,
    UserRecordUpdatedAt,
    UserRecordUID,
)


class User(Entity):
    record_uid: UserRecordUID
    created_at: UserRecordCreatedAt
    updated_at: UserRecordUpdatedAt

    identifier: UserIdentifier

    nickname: UserNickname
