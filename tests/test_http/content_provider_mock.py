from typing import Any

from lambler.content import ContentProvider


class ContentProviderMock(ContentProvider):

    def __init__(self, *, load__return=None):
        self._load__return = load__return

        self.load__is_called = False
        self.load__key = None

    def load(self, key: str) -> Any:
        self.load__is_called = True
        self.load__key = key
        return self._load__return
