from os import getenv

from pyrogram import filters, types, enums
from pyrorouter import MetaRouter, Client


class Router(MetaRouter):
    def inject(self, func):
        async def wrapper(client: Client, update: types.Update):
            kwargs = {"client": client}
            kwargs.update(client.env)

            await func(update, **self.prepare_args(func, kwargs))

        return wrapper


rt = Router()


@rt.on_message(filters.command("start"))
async def cmd_start(message: types.Message, test: str):
    await message.reply(f"Hello World! Test: {test}")


@rt.on_message(filters.command("test"))
async def cmd_start(message: types.Message, **kwargs):
    await message.reply(f"Kwargs: {kwargs}")


def register(client):
    rt.register(client)


def main() -> None:
    kwargs = {
        "api_id": getenv("API_ID"),
        "api_hash": getenv("API_HASH"),
        "bot_token": getenv("BOT_TOKEN"),
    }

    client = Client("memory", **kwargs, in_memory=True, parse_mode=enums.ParseMode.DISABLED)

    client.env["test"] = "test"

    register(client)

    client.run()


if __name__ == "__main__":
    main()
