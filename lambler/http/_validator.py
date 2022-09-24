from abc import ABC, abstractmethod
from typing import Dict, Any

from ._event import HttpEvent


class HttpRequestValidatorBase(ABC):

    @abstractmethod
    def validate(self, raw: Dict) -> HttpEvent:
        pass


class HttpResponseValidatorBase(ABC):

    @abstractmethod
    def validate(self, raw: Any) -> Dict:
        pass


class AwsHttpRequestValidator(HttpRequestValidatorBase):
    def validate(self, raw: Dict) -> HttpEvent:
        return HttpEvent(
            raw["requestContext"]["http"]["method"],
            raw["rawPath"], raw["headers"],
            raw.get("queryStringParameters", {}),
        )
