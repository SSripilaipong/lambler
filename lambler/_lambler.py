from typing import Dict, Any, List, Optional

from .base import Handler
from .content import ContentProvider


class Lambler:
    def __init__(self):
        self._handlers: List[Handler] = []
        self._content_provider: Optional[ContentProvider] = None

    def handle(self, *handlers: Handler):
        self._handlers = handlers

        self._ensure_handler_with_content_provider()

    def __call__(self, event: Dict, context: Any):
        for handler in self._handlers:
            handler.handle(event, context)

    def use_content(self, provider: ContentProvider):
        self._content_provider = provider

        self._ensure_handler_with_content_provider()

    def _ensure_handler_with_content_provider(self):
        if self._content_provider is None:
            return

        for handler in self._handlers:
            handler.set_content_provider(self._content_provider)
