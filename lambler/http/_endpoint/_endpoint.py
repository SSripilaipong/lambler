import inspect
from typing import Callable, Dict, Any, Optional

from ._executor import EndpointExecutor
from .._event import HttpEvent
from .._header import Header


class Endpoint:
    def __init__(self, path: str, f: Callable, signature: inspect.Signature):
        self._path = path
        self._f = f
        self._signature = signature

    @classmethod
    def create(cls, path: str, f: Callable) -> 'Endpoint':
        signature = inspect.signature(f)
        _validate_markers(signature)
        return cls(path, f, signature)

    def match(self, event: Dict, context: Any) -> Optional[EndpointExecutor]:
        http_event = HttpEvent.from_dict(event)
        if http_event.path != self._path:
            return None

        return EndpointExecutor(self._f, self._signature, http_event)


def _validate_markers(signature: inspect.Signature):
    for name, param in signature.parameters.items():
        marker = param.default

        if isinstance(marker, Header):
            marker.validate_param(param)
