import discord
from injector import inject

from src.infrastructure.message.client import MessageClientInterface


class OnMessageEventListener:
    @inject
    def __init__(
        self,
        client: MessageClientInterface,
    ) -> None:
        self.__client: MessageClientInterface = client

    async def execute(
        self,
        message: discord.Message,
    ) -> None:
        raise NotImplementedError
