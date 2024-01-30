import discord
from discord import Intents
from injector import singleton, inject

from config import GenkaiEraConfig
from src.infrastructure.message.client import MessageClientInterface


@singleton
class DiscordClient(MessageClientInterface):
    __intents = Intents.default()
    __intents.members = True
    __intents.messages = True
    __intents.guild_messages = True
    __intents.message_content = True

    @inject
    def __init__(
        self,
        config: GenkaiEraConfig,
    ) -> None:
        self.__config: GenkaiEraConfig = config

        self.__client: discord.Client = discord.Client(intents=self.__intents)

    async def start(
        self,
    ) -> None:
        await self.__client.start(token=self.__config.DISCORD_TOKEN)

    async def stop(
        self,
    ) -> None:
        await self.__client.close()
