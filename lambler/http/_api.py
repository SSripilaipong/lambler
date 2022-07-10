from typing import Callable, Any, TypeVar, Dict, List

from lambler.base import Handler
from ._endpoint import Endpoint
from ..content import ContentProviderSpace

T = TypeVar("T", bound=Callable)


class HttpApi(Handler):
    def __init__(self):
        self._endpoints: List[Endpoint] = []

    def get(self, path: str) -> Callable[[Callable], Any]:
        def decorator(f: T) -> T:
            self._endpoints.append(Endpoint.create(path, f))
            return f

        return decorator

    def set_content_provider_space(self, providers: ContentProviderSpace):
        for endpoint in self._endpoints:
            endpoint.set_content_provider_space(providers)

    def handle(self, event: Dict, context: Any):
        for endpoint in self._endpoints:
            executor = endpoint.match(event, context)
            if executor is not None:
                response = executor.execute()
                if response is None:
                    return http_response(200, "")


def http_response(status_code: int, body: str) -> Dict:
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "text/plain",
        },
        "body": body,
        "cookies": [],
        "isBase64Encoded": False
    }
