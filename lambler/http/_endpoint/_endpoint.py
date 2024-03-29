import inspect
from typing import Callable, Any, Optional

from ._executor import EndpointExecutor
from ._path import EndpointPath
from .._event import HttpEvent
from .._header import Header
from ...content import ContentProviderSpace


class Endpoint:
    def __init__(self, path: EndpointPath, method: str, f: Callable, signature: inspect.Signature):
        self._path = path
        self._method = method
        self._f = f
        self._signature = signature

        self._content_providers: Optional[ContentProviderSpace] = None

    @classmethod
    def create(cls, path: str, method: str, f: Callable) -> 'Endpoint':
        signature = inspect.signature(f)
        _validate_markers(signature)
        return cls(EndpointPath.create(path), method, f, signature)

    def match(self, http_event: HttpEvent, _: Any) -> Optional[EndpointExecutor]:
        if http_event.method != self._method:
            return None
        path_length, match = self._path.match(http_event.path)
        if not match:
            return None

        return EndpointExecutor(self._path, path_length, self._f, self._signature, http_event,
                                content_providers=self._content_providers)

    def set_content_provider_space(self, providers: ContentProviderSpace):
        self._content_providers = providers


def _validate_markers(signature: inspect.Signature):
    for name, param in signature.parameters.items():
        marker = param.default

        if isinstance(marker, Header):
            marker.validate_param(param)
