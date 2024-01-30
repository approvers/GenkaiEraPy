from abc import abstractmethod
from typing import Generic

from src.adapter.repository.abc import Repository
from src.adapter.type import RawSessionType
from src.domain.user.entity import User
from src.domain.user.value import UserIdentifier


class UserRepository(Repository, Generic[RawSessionType]):
    @abstractmethod
    async def save(
        self,
        user: User,
    ) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def get_latest_by_id(
        self,
        user_id: UserIdentifier,
    ) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def get_history_by_id(
        self,
        user_id: UserIdentifier,
        limit: int,
    ) -> list[User]:
        raise NotImplementedError()
