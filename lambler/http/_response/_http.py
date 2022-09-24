from typing import Any, Dict


class HttpResponse:
    def __init__(self, status_code: int, body: Any, *, headers: Dict[str, str] = None):
        self.status_code = status_code
        self.body = body
        self.headers = headers or {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "statusCode": self.status_code,
            "headers": self.headers,
            "body": self.body,
            "cookies": [],
            "isBase64Encoded": False,
        }
