from typing import Any

from lambler.content import ContentProvider


class ContentProviderMock(ContentProvider):

    def __init__(self):
        self.load__key = None

    def load(self, key: str) -> Any:
        self.load__key = key
