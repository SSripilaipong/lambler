import inspect
from typing import Callable, Dict, Any, Optional

from ._executor import EndpointExecutor
from .._event import HttpEvent
from .._header import Header
from ...content import ContentProvider


class Endpoint:
    def __init__(self, path: str, f: Callable, signature: inspect.Signature):
        self._path = path
        self._f = f
        self._signature = signature

        self._content_provider: Optional[ContentProvider] = None

    @classmethod
    def create(cls, path: str, f: Callable) -> 'Endpoint':
        signature = inspect.signature(f)
        _validate_markers(signature)
        return cls(path, f, signature)

    def match(self, event: Dict, _: Any) -> Optional[EndpointExecutor]:
        http_event = HttpEvent.from_dict(event)
        if http_event.path != self._path:
            return None

        return EndpointExecutor(self._f, self._signature, http_event, content_provider=self._content_provider)

    def set_content_provider(self, provider: ContentProvider):
        self._content_provider = provider


def _validate_markers(signature: inspect.Signature):
    for name, param in signature.parameters.items():
        marker = param.default

        if isinstance(marker, Header):
            marker.validate_param(param)
