from lambler import Lambler
from tests.test_http.http_api_factory import create_http_api_for_test_with_request, \
    RequestForTest


def test_should_call_endpoint():
    api = create_http_api_for_test_with_request(RequestForTest("POST", "/"))

    @api.post("/")
    def endpoint():
        endpoint.is_called = True

    lambler = Lambler()
    lambler.handle(api)

    endpoint.is_called = False
    lambler({}, ...)
    assert endpoint.is_called
