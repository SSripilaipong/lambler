import inspect
from typing import Callable, Dict, Any

from ._header import Header


class Endpoint:
    def __init__(self, path: str, f: Callable):
        self._path = path
        self._f = f
        self._signature = inspect.signature(self._f)

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
                params[name] = _extract_header(event, marker.key)

        return params


def _extract_header(event: Dict, key: str) -> Any:
    return event["headers"][key]


def _extract_path(event: Dict) -> str:
    return event["rawPath"]
