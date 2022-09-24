from typing import Callable, Any, TypeVar, Dict, List

from lambler.base import Handler
from . import AwsHttpRequestValidator, AwsHttpResponseValidator
from ._endpoint import Endpoint
from ._validator import HttpRequestValidatorBase, HttpResponseValidatorBase
from ..content import ContentProviderSpace

T = TypeVar("T", bound=Callable)


class HttpApiBase(Handler):
    def __init__(self, request_validator: HttpRequestValidatorBase, response_validator: HttpResponseValidatorBase):
        self._request_validator = request_validator
        self._response_validator = response_validator

        self._endpoints: List[Endpoint] = []

    def get(self, path: str) -> Callable[[Callable], Any]:
        def decorator(f: T) -> T:
            self._endpoints.append(Endpoint.create(path, f))
            return f

        return decorator

    def set_content_provider_space(self, providers: ContentProviderSpace):
        for endpoint in self._endpoints:
            endpoint.set_content_provider_space(providers)

    def handle(self, event: Dict, context: Any) -> Dict:
        longest_path_length = 0
        longest_path_executor = None

        http_event = self._request_validator.validate(event)
        for endpoint in self._endpoints:
            executor = endpoint.match(http_event, context)
            if executor is not None and executor.path_length > longest_path_length:
                longest_path_length = executor.path_length
                longest_path_executor = executor

        if longest_path_executor is not None:
            response_raw = longest_path_executor.execute()
            return self._response_validator.validate(response_raw)


class HttpApi(HttpApiBase):
    def __init__(self):
        super(HttpApi, self).__init__(AwsHttpRequestValidator(), AwsHttpResponseValidator())
