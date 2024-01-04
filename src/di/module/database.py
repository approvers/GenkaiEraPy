from injector import Binder, ClassProvider, Module
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.sqlalchemy.model.define import define_sa_models
from src.infrastructure.database.sqlalchemy.session import (
    SAAsyncSessionManager,
    SAAsyncSessionWrapper,
)


class GenkaiEraSADatabaseModule(Module):
    def __init__(
        self,
    ) -> None:
        # Required for type checking
        define_sa_models()

    def configure(
        self,
        binder: Binder,
    ) -> None:
        binder.bind(
            AsyncSessionWrapperInterface[AsyncSession],  # type: ignore
            ClassProvider(SAAsyncSessionManager),
        )

        binder.bind(
            AsyncSessionWrapperInterface[AsyncSession],  # type: ignore
            ClassProvider(SAAsyncSessionWrapper),
        )

        binder.bind(
            AsyncSessionManagerInterface,  # type: ignore
            ClassProvider(SAAsyncSessionManager),
        )

        binder.bind(
            AsyncSessionWrapperInterface,  # type: ignore
            ClassProvider(SAAsyncSessionWrapper),
        )
