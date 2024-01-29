from src.domain.base.entity import Entity
from src.domain.member.value import (
    MemberLocalNickname,
    MemberRecordCreatedAt,
    MemberRecordUpdatedAt,
    MemberRecordUID,
)
from src.domain.server.value import ServerIdentifier
from src.domain.user.value import UserIdentifier


class Member(Entity):
    record_uid: MemberRecordUID
    record_created_at: MemberRecordCreatedAt
    record_updated_at: MemberRecordUpdatedAt

    server_id: ServerIdentifier
    user_id: UserIdentifier

    local_nickname: MemberLocalNickname
