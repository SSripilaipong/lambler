from typing import Dict, Any


class HttpEvent:
    def __init__(self, path: str, headers: Dict[str, Any]):
        self.path = path
        self.headers = headers

    @classmethod
    def from_dict(cls, raw: Dict) -> 'HttpEvent':
        return cls(raw["rawPath"], raw["headers"])
