from typing import Dict

from lambler.http import HttpApiBase
from lambler.http import HttpEvent
from lambler.http import HttpRequestValidatorBase


def create_http_api_for_test() -> HttpApiBase:
    return HttpApiBase(RequestValidatorForTest())


def create_http_api_for_test_with_request_validator(request_validator: HttpRequestValidatorBase):
    return HttpApiBase(request_validator=request_validator)


class RequestValidatorForTest(HttpRequestValidatorBase):
    def validate(self, raw: Dict) -> HttpEvent:
        return HttpEvent(
            path=raw.get("path", ""),
            headers=raw.get("headers", {}),
            query_params=raw.get("query_params", {}),
        )
