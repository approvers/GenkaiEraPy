from abc import abstractmethod
from typing import Generic

from src.adapter.repository.abc import Repository
from src.adapter.type import RawSessionType
from src.domain.member.entity import Member
from src.domain.server.value import ServerIdentifier
from src.domain.user.value import UserIdentifier


class MemberRepository(Repository, Generic[RawSessionType]):
    @abstractmethod
    async def save(
        self,
        member: Member,
    ) -> Member:
        raise NotImplementedError()

    @abstractmethod
    async def get_latest_by_server_id_and_user_id(
        self,
        server_id: ServerIdentifier,
        user_id: UserIdentifier,
    ) -> Member:
        raise NotImplementedError()

    @abstractmethod
    async def get_history_by_server_id_and_user_id(
        self,
        server_id: ServerIdentifier,
        user_id: UserIdentifier,
        limit: int,
    ) -> list[Member]:
        raise NotImplementedError()
