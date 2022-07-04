import inspect
from typing import Callable, Any, Dict

from .._event import HttpEvent
from .._header import Header


class EndpointExecutor:
    def __init__(self, f: Callable, signature: inspect.Signature, event: HttpEvent):
        self._f = f
        self._signature = signature
        self._event = event

    def execute(self):
        self._f(**self._extract_params())

    def _extract_params(self) -> Dict[str, Any]:
        if len(self._signature.parameters) == 0:
            return {}

        params = {}
        for name, param in self._signature.parameters.items():
            marker = param.default
            if isinstance(marker, Header):
                params[name] = marker.extract_event(self._event)

        return params
