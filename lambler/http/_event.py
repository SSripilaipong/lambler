from typing import Dict, Any


class HttpEvent:
    def __init__(self, method: str, path: str, headers: Dict[str, Any], query_params: Dict[str, str]):
        self.method = method
        self.path = path
        self.headers = headers
        self.query_params = query_params
