from abc import abstractmethod
from typing import Generic

from src.adapter.repository.abc import Repository
from src.adapter.type import RawSessionType
from src.domain.server.entity import Server
from src.domain.server.value import ServerIdentifier


class ServerRepository(Repository, Generic[RawSessionType]):
    @abstractmethod
    async def save(
        self,
        server: Server,
    ) -> Server:
        raise NotImplementedError()

    @abstractmethod
    async def get_latest_by_id(
        self,
        server_id: ServerIdentifier,
    ) -> Server:
        raise NotImplementedError()

    @abstractmethod
    async def get_history_by_id(
        self,
        server_id: ServerIdentifier,
        limit: int,
    ) -> list[Server]:
        raise NotImplementedError()
