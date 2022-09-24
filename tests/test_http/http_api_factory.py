from dataclasses import dataclass, field
from typing import Dict, Any, List

from lambler.http import HttpApiBase, HttpResponseValidatorBase
from lambler.http import HttpEvent
from lambler.http import HttpRequestValidatorBase
from tests.test_http.request_validator_mock import RequestValidatorMock
from tests.test_http.response_validator_mock import ResponseValidatorMock


class RequestForTest:
    def __init__(self, method: str, path: str, headers: Dict[str, str] = None, query_params: Dict[str, str] = None):
        self.method = method
        self.path = path
        self.headers = headers or {}
        self.query_params = query_params or {}


@dataclass
class ResponseForTest:
    status_code: int
    body: Any = None
    headers: Dict[str, str] = field(default_factory=dict)
    cookies: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, d: Dict) -> 'ResponseForTest':
        return ResponseForTest(
            status_code=d["status_code"],
            body=d["body"],
            headers=d["headers"],
            cookies=d["cookies"],
        )


def create_http_api_for_test() -> HttpApiBase:
    return HttpApiBase(RequestValidatorMock(), response_validator=ResponseValidatorMock())


def create_http_api_for_test_with_request(request: RequestForTest) -> HttpApiBase:
    return HttpApiBase(RequestValidatorMock(validate__return=HttpEvent(
        method=request.method,
        path=request.path,
        headers=request.headers,
        query_params=request.query_params,
    )), response_validator=ResponseValidatorMock())


def create_http_api_for_test_with_response_validator(response_validator: HttpResponseValidatorBase) -> HttpApiBase:
    return HttpApiBase(request_validator=RequestValidatorMock(), response_validator=response_validator)


def create_http_api_for_test_with_request_validator(request_validator: HttpRequestValidatorBase):
    return HttpApiBase(request_validator=request_validator, response_validator=ResponseValidatorMock())
