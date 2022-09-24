from typing import Dict

from lambler.http import HttpApiBase
from lambler.http import HttpEvent
from lambler.http import HttpRequestValidatorBase
from tests.test_http.request_validator_mock import RequestValidatorMock


class RequestForTest:
    def __init__(self, method: str, path: str, headers: Dict[str, str] = None, query_params: Dict[str, str] = None):
        self.method = method
        self.path = path
        self.headers = headers or {}
        self.query_params = query_params or {}


def create_http_api_for_test() -> HttpApiBase:
    return HttpApiBase(RequestValidatorMock())


def create_http_api_for_test_with_request(request: RequestForTest) -> HttpApiBase:
    return HttpApiBase(RequestValidatorMock(validate__return=HttpEvent(
        method=request.method,
        path=request.path,
        headers=request.headers,
        query_params=request.query_params,
    )))


def create_http_api_for_test_with_request_validator(request_validator: HttpRequestValidatorBase):
    return HttpApiBase(request_validator=request_validator)
