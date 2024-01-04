from typing import Optional, Generic

from src.adapter.session import AsyncSessionWrapperInterface
from src.adapter.type import RawSessionType
from src.common.design.interface import Interface


class Repository(
    Interface,
    Generic[RawSessionType],
):
    __session_wrapper: Optional[AsyncSessionWrapperInterface[RawSessionType]] = None

    def set_session_wrapper(
        self,
        session: AsyncSessionWrapperInterface[RawSessionType],
    ) -> None:
        self.__session_wrapper: AsyncSessionWrapperInterface[RawSessionType] = session

    def get_session_wrapper(
        self,
    ) -> AsyncSessionWrapperInterface[RawSessionType]:
        if self.__session_wrapper is None:
            raise RuntimeError("'self.__session' is not set")

        return self.__session_wrapper

    def get_raw_session(
        self,
    ) -> RawSessionType:
        return self.get_session_wrapper().get_raw_session()
