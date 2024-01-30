from src.common.design.interface import Interface
from src.domain.message.entity import Message


class OnMessageEventRouter(Interface):
    async def execute(
        self,
        message: Message,
    ) -> None:
        raise NotImplementedError
