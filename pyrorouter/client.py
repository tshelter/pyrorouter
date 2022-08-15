from typing import Any, Optional

from pyrogram import Client as Client_


class Client(Client_):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._env = {}

    def add_env(self, name: str, value: Any) -> None:
        self._env[name] = value

    def get_env(self, name: str, default: Optional[Any] = None) -> Any:
        return self._env.get(name, default)

    def export_env(self) -> dict:
        return self._env

    @property
    def env(self):
        return self._env
