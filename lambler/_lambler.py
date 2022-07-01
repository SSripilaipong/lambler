from typing import Dict, Any, List, Optional

from .base import Handler


class Lambler:
    def __init__(self):
        self._handlers: Optional[List[Handler]] = None

    def use(self, *handlers: Handler):
        self._handlers = handlers

    def __call__(self, event: Dict, context: Any):
        for handler in self._handlers:
            handler.handle(event, context)
