from src.common.design.interface import Interface


class MessageClientInterface(Interface):
    async def start(
        self,
    ) -> None:
        raise NotImplementedError

    async def stop(
        self,
    ) -> None:
        raise NotImplementedError
