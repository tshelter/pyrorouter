# pip install aiosqlite sqlalchemy
import asyncio
from os import getenv

from pyrogram import filters, types, idle, enums
from pyrorouter import MetaRouter, Client

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


class Router(MetaRouter):
    def inject(self, func):
        async def wrapper(client: Client, update: types.Update):
            session_maker = client.env["session_maker"]

            async with session_maker() as session:
                kwargs = {"client": client, "session": session}
                kwargs.update(client.env)
                await func(update, **self.prepare_args(func, kwargs))

        return wrapper


rt = Router()


@rt.on_message(filters.command("start"))
async def cmd_start(message: types.Message, session: AsyncSession):
    await message.reply(f"Hello World! Session: {session}")


def register(client):
    rt.register(client)


async def init_db() -> sessionmaker:
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    return sessionmaker(bind=engine, class_=AsyncSession)


async def main() -> None:
    kwargs = {
        "api_id": getenv("API_ID"),
        "api_hash": getenv("API_HASH"),
        "bot_token": getenv("BOT_TOKEN"),
    }

    client = Client("memory", **kwargs, in_memory=True, parse_mode=enums.ParseMode.DISABLED)

    client.env["session_maker"] = await init_db()

    register(client)

    async with client:
        print("Running...")
        await idle()

if __name__ == "__main__":
    asyncio.run(main())
