from typing import Callable, Any, TypeVar, Dict, List

from lambler.base import Handler

T = TypeVar("T", bound=Callable)


class HttpEndpoint(Handler):
    def __init__(self):
        self._handlers: List[Callable] = []

    def get(self, method: str) -> Callable[[Callable], Any]:
        def decorator(f: T) -> T:
            self._handlers.append(f)
            return f

        return decorator

    def handle(self, event: Dict, context: Any):
        for handler in self._handlers:
            handler()
