import asyncio

from src.di.container import container
from src.infrastructure.message.client import MessageClientInterface


async def main() -> None:
    client: MessageClientInterface = container.get(MessageClientInterface)

    await client.start()


if __name__ == "__main__":
    asyncio.run(main())
