from typing import Dict, Any, List

from .base import Handler


class Lambler:
    def __init__(self):
        self._handlers: List[Handler] = []

    def use(self, *handlers: Handler):
        self._handlers = handlers

    def __call__(self, event: Dict, context: Any):
        for handler in self._handlers:
            handler.handle(event, context)
