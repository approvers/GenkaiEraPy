from contextlib import asynccontextmanager
from typing import AsyncIterator, Optional

from injector import inject
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from config import GenkaiEraConfig
from src.adapter.session import (
    AsyncSessionManagerInterface,
    AsyncSessionWrapperInterface,
)


class SAAsyncSessionWrapper(AsyncSessionWrapperInterface[AsyncSession]):
    __raw_session: Optional[AsyncSession] = None

    async def commit(
        self,
    ) -> None:
        session: AsyncSession = self.get_raw_session()

        await session.commit()

    async def rollback(
        self,
    ) -> None:
        session: AsyncSession = self.get_raw_session()

        await session.rollback()

    async def close(
        self,
    ) -> None:
        session: AsyncSession = self.get_raw_session()

        await session.close()

    def get_raw_session(
        self,
    ) -> AsyncSession:
        if self.__raw_session is None:
            raise RuntimeError(f"{self.__name__}().__raw_session is not set.")  # type: ignore

        return self.__raw_session

    def set_raw_session(
        self,
        raw_session: AsyncSession,
    ) -> None:
        self.__raw_session = raw_session


class SAAsyncSessionManager(AsyncSessionManagerInterface[AsyncSession]):
    __config: GenkaiEraConfig

    @staticmethod
    def create_engine(
        dsn: str,
        connect_args: dict[str, str],
    ) -> AsyncEngine:
        engine: AsyncEngine = create_async_engine(
            dsn,
            connect_args=connect_args,
        )

        return engine

    @staticmethod
    def create_session_maker(
        engine: AsyncEngine,
        expire_on_commit: bool = False,
        autocommit: bool = False,
        autoflush: bool = False,
    ) -> async_sessionmaker:  # type: ignore
        session_maker: async_sessionmaker = async_sessionmaker(  # type: ignore
            engine,
            expire_on_commit=expire_on_commit,
            autocommit=autocommit,
            autoflush=autoflush,
            class_=AsyncSession,
        )

        return session_maker

    @inject
    def __init__(
        self,
        config: GenkaiEraConfig,
    ) -> None:
        self.__config: GenkaiEraConfig = config

        self.__async_engine: AsyncEngine = self.create_engine(
            dsn=self.__config.get_postgres_dsn(),
            connect_args=self.__config.POSTGRES_CONNECT_ARGS,
        )

        self.__async_session_maker: async_sessionmaker = self.create_session_maker(  # type: ignore
            engine=self.__async_engine,
            expire_on_commit=self.__config.POSTGRES_EXPIRE_ON_COMMIT,
            autocommit=self.__config.POSTGRES_AUTOCOMMIT,
            autoflush=self.__config.POSTGRES_AUTOFLUSH,
        )

    def get_async_engine(self) -> AsyncEngine:
        return self.__async_engine

    def get_async_session_maker(self) -> async_sessionmaker:  # type: ignore
        return self.__async_session_maker

    @asynccontextmanager
    async def get_session(
        self,
    ) -> AsyncIterator[SAAsyncSessionWrapper]:
        raw_async_session: AsyncSession = self.get_async_session_maker()()

        session_wrapper: SAAsyncSessionWrapper = SAAsyncSessionWrapper()
        session_wrapper.set_raw_session(raw_async_session)

        try:
            yield session_wrapper
            await session_wrapper.commit()

        except Exception as e:
            await session_wrapper.rollback()
            raise e

        finally:
            await session_wrapper.close()
