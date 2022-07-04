import inspect
from typing import Callable, Dict, Any

from ._header import Header


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

    def execute(self, event: Dict, context: Any):
        params = self._extract_params(event)
        self._f(**params)

    def match(self, event: Dict, context: Any) -> bool:
        return _extract_path(event) == self._path

    def _extract_params(self, event: Dict) -> Dict[str, Any]:
        if len(self._signature.parameters) == 0:
            return {}

        params = {}
        for name, param in self._signature.parameters.items():
            marker = param.default
            if isinstance(marker, Header):
                params[name] = marker.extract_event(event)

        return params


def _validate_markers(signature: inspect.Signature):
    for name, param in signature.parameters.items():
        marker = param.default

        if isinstance(marker, Header):
            marker.validate_param(param)


def _extract_path(event: Dict) -> str:
    return event["rawPath"]
