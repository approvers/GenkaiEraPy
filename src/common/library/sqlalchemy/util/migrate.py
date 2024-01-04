from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm.decl_api import DeclarativeMeta


async def create_all(engine_to_bind: AsyncEngine, base: DeclarativeMeta) -> None:
    async with engine_to_bind.begin() as conn:
        await conn.run_sync(base.metadata.create_all)


async def drop_all(engine_to_bind: AsyncEngine, base: DeclarativeMeta) -> None:
    async with engine_to_bind.begin() as conn:
        await conn.run_sync(base.metadata.drop_all)


async def reset_all(engine_to_bind: AsyncEngine, base: DeclarativeMeta) -> None:
    async with engine_to_bind.begin() as conn:
        await conn.run_sync(base.metadata.drop_all)
        await conn.run_sync(base.metadata.create_all)
