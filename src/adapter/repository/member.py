from abc import abstractmethod
from typing import Generic

from src.adapter.repository.abc import Repository
from src.adapter.type import RawSessionType
from src.domain.member.entity import Member
from src.domain.server.value import ServerIdentifier
from src.domain.user.value import UserIdentifier


class MemberRepository(Repository, Generic[RawSessionType]):
    @abstractmethod
    async def create_or_update(
        self,
        member: Member,
    ) -> Member:
        raise NotImplementedError()

    @abstractmethod
    async def get_server_id_and_user_id(
        self,
        server_id: ServerIdentifier,
        user_id: UserIdentifier,
    ) -> Member:
        pass
