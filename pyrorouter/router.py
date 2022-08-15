from abc import ABCMeta, abstractmethod
from typing import Callable
import inspect

from pyrogram import handlers, Client


class MetaRouter(metaclass=ABCMeta):
    def __init__(self):
        self._handlers = []

    def add_handler(self, handler, group=0):
        self._handlers.append((handler, group))

    def register(self, client: Client):
        for handler, group in self._handlers:
            client.add_handler(handler, group)

    @staticmethod
    def prepare_args(func: Callable, kwargs: dict) -> dict:
        spec = inspect.getfullargspec(func)

        if spec.varkw:
            return kwargs

        return {
            k: v for k, v in kwargs.items() if k in spec.args or k in spec.kwonlyargs
        }

    @abstractmethod
    def inject(self, func) -> Callable:
        async def wrapper(client, update):
            kwargs = {"client": client}
            kwargs.update(client.env)

            return await func(update, **self.prepare_args(func, kwargs))

        return wrapper

    def on_message(self, filters=None, group=0):
        def decorator(func: Callable) -> Callable:
            func = self.inject(func)
            self.add_handler(handlers.MessageHandler(func, filters), group)

            return func

        return decorator

    def on_edited_message(self, filters=None, group=0):
        def decorator(func: Callable) -> Callable:
            func = self.inject(func)
            self.add_handler(handlers.EditedMessageHandler(func, filters), group)

            return func

        return decorator

    def on_deleted_messages(self, filters=None, group=0):
        def decorator(func: Callable) -> Callable:
            func = self.inject(func)
            self.add_handler(handlers.DeletedMessagesHandler(func, filters), group)

            return func

        return decorator

    def on_callback_query(self, filters=None, group=0):
        def decorator(func: Callable) -> Callable:
            func = self.inject(func)
            self.add_handler(handlers.CallbackQueryHandler(func, filters), group)

            return func

        return decorator

    def on_inline_query(self, filters=None, group=0):
        def decorator(func: Callable) -> Callable:
            func = self.inject(func)
            self.add_handler(handlers.InlineQueryHandler(func, filters), group)

            return func

        return decorator

    def on_chosen_inline_result(self, filters=None, group=0):
        def decorator(func: Callable) -> Callable:
            func = self.inject(func)
            self.add_handler(handlers.ChosenInlineResultHandler(func, filters), group)

            return func

        return decorator

    def on_chat_member_updated(self, filters=None, group=0):
        def decorator(func: Callable) -> Callable:
            func = self.inject(func)
            self.add_handler(handlers.ChatMemberUpdatedHandler(func, filters), group)

            return func

        return decorator

    def on_user_status(self, filters=None, group=0):
        def decorator(func: Callable) -> Callable:
            func = self.inject(func)
            self.add_handler(handlers.UserStatusHandler(func, filters), group)

            return func

        return decorator

    def on_poll(self, filters=None, group=0):
        def decorator(func: Callable) -> Callable:
            func = self.inject(func)
            self.add_handler(handlers.PollHandler(func, filters), group)

            return func

        return decorator

    def on_disconnect(self):
        def decorator(func: Callable) -> Callable:
            func = self.inject(func)
            self.add_handler(handlers.DisconnectHandler(func))

            return func

        return decorator

    def on_raw_update(self, group=0):
        def decorator(func: Callable) -> Callable:
            func = self.inject(func)
            self.add_handler(handlers.RawUpdateHandler(func), group)

            return func

        return decorator
