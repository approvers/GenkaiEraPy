from abc import abstractmethod
from contextlib import asynccontextmanager
from typing import AsyncIterator, Generic

from src.adapter.type import RawSessionType
from src.common.design.interface import Interface


class AsyncSessionWrapperInterface(
    Generic[RawSessionType],
    Interface,
):
    @abstractmethod
    async def commit(
        self,
    ) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def rollback(
        self,
    ) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def close(
        self,
    ) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_raw_session(
        self,
    ) -> RawSessionType:
        raise NotImplementedError()

    @abstractmethod
    def set_raw_session(
        self,
        raw_session: RawSessionType,
    ) -> None:
        raise NotImplementedError()


class AsyncSessionManagerInterface(
    Generic[RawSessionType],
    Interface,
):
    @asynccontextmanager
    @abstractmethod
    async def get_session(
        self,
    ) -> AsyncIterator[AsyncSessionWrapperInterface[RawSessionType]]:
        yield NotImplementedError()  # type: ignore
