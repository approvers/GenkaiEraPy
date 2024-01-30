from injector import Module, Binder, ClassProvider

from src.message.discord.client import DiscordClient
from src.infrastructure.message.client import MessageClientInterface


class GenkaiEraMessageModule(Module):
    def __init__(
        self,
    ) -> None:
        pass

    def configure(
        self,
        binder: Binder,
    ) -> None:
        binder.bind(
            MessageClientInterface,
            ClassProvider(DiscordClient),
        )
