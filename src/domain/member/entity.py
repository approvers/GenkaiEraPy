from src.domain.base.entity import Entity
from src.domain.common.value import NullableCreatedAt
from src.domain.member.value import MemberLocalNickname
from src.domain.server.value import ServerIdentifier
from src.domain.user.field import UserIdentifier


class Member(Entity):
    created_at: NullableCreatedAt
    updated_at: NullableCreatedAt

    server_id: ServerIdentifier
    user_id: UserIdentifier

    local_nickname: MemberLocalNickname
