from typing import Callable, Dict, Any


class Endpoint:
    def __init__(self, path: str, f: Callable):
        self._path = path
        self._f = f

    def execute(self, event: Dict, context: Any):
        self._f()

    def match(self, event: Dict, context: Any) -> bool:
        return event["rawPath"] == self._path
