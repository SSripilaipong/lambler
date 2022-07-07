from typing import Any, Optional

from lambler.content import ContentProvider


class ContentProviderMock(ContentProvider):

    def __init__(self):
        self.load__scope = None
        self.load__key = None

    def load(self, key: str, scope: Optional[str]) -> Any:
        self.load__key = key
        self.load__scope = scope
