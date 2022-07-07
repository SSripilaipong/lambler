import inspect
from typing import Callable, Any, Dict

from .._event import HttpEvent
from .._header import Header
from ...content import ContentProvider, Content


class EndpointExecutor:
    def __init__(self, f: Callable, signature: inspect.Signature, event: HttpEvent, *,
                 content_provider: ContentProvider = None):
        self._f = f
        self._signature = signature
        self._event = event

        self._content_provider = content_provider

    def execute(self):
        self._f(**self._extract_params())

    def _extract_params(self) -> Dict[str, Any]:
        if len(self._signature.parameters) == 0:
            return {}

        params = {name: self._extract_marker_value(marker=param.default)
                  for name, param in self._signature.parameters.items()}

        return params

    def _extract_marker_value(self, marker: Any) -> Any:
        if isinstance(marker, Header):
            value = marker.extract_event(self._event)
        elif isinstance(marker, Content):
            value = self._content_provider.load(marker.key)
        else:
            raise NotImplementedError()
        return value
