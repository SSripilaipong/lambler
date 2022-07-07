from typing import Callable, Any, TypeVar, Dict, List

from lambler.base import Handler
from ._endpoint import Endpoint
from ..content import ContentProvider

T = TypeVar("T", bound=Callable)


class HttpApi(Handler):
    def __init__(self):
        self._endpoints: List[Endpoint] = []

    def get(self, path: str) -> Callable[[Callable], Any]:
        def decorator(f: T) -> T:
            self._endpoints.append(Endpoint.create(path, f))
            return f

        return decorator

    def set_content_provider(self, provider: ContentProvider):
        for endpoint in self._endpoints:
            endpoint.set_content_provider(provider)

    def handle(self, event: Dict, context: Any):
        for endpoint in self._endpoints:
            executor = endpoint.match(event, context)
            if executor is not None:
                executor.execute()
                break
