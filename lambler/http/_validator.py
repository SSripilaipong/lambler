from abc import ABC, abstractmethod
from typing import Dict, Any

from ._event import HttpEvent
from ._response import HttpResponse


class HttpRequestValidatorBase(ABC):

    @abstractmethod
    def validate(self, raw: Dict) -> HttpEvent:
        pass


class HttpResponseValidatorBase(ABC):

    @abstractmethod
    def validate(self, raw: Any) -> Dict:
        pass


class AwsHttpResponseValidator(HttpResponseValidatorBase):
    def validate(self, raw: Any) -> Dict:
        if isinstance(raw, HttpResponse):
            return {
                "statusCode": raw.status_code,
                "headers": raw.headers,
                "body": raw.body,
                "cookies": [],
                "isBase64Encoded": False,
            }

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/plain"
            },
            "body": "",
            "cookies": [],
            "isBase64Encoded": False,
        }


class AwsHttpRequestValidator(HttpRequestValidatorBase):
    def validate(self, raw: Dict) -> HttpEvent:
        return HttpEvent(
            raw["requestContext"]["http"]["method"],
            raw["rawPath"], raw["headers"],
            raw.get("queryStringParameters", {}),
        )
