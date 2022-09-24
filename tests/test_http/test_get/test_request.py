from lambler import Lambler
from tests.test_http.http_api_factory import create_http_api_for_test_with_request, \
    RequestForTest


def test_should_call_endpoint():
    api = create_http_api_for_test_with_request(RequestForTest("GET", "/"))

    @api.get("/")
    def endpoint():
        endpoint.is_called = True

    lambler = Lambler()
    lambler.handle(api)

    endpoint.is_called = False
    lambler({}, ...)
    assert endpoint.is_called


def test_should_select_first_endpoint_by_path():
    api = create_http_api_for_test_with_request(RequestForTest("GET", "/1"))

    # noinspection DuplicatedCode
    @api.get("/1")
    def endpoint1():
        endpoint1.is_called = True

    @api.get("/2")
    def endpoint2():
        endpoint2.is_called = True

    lambler = Lambler()
    lambler.handle(api)

    endpoint1.is_called = endpoint2.is_called = False
    lambler({}, ...)
    assert endpoint1.is_called and not endpoint2.is_called


def test_should_select_second_endpoint_by_path():
    api = create_http_api_for_test_with_request(RequestForTest("GET", "/2"))

    # noinspection DuplicatedCode
    @api.get("/1")
    def endpoint1():
        endpoint1.is_called = True

    @api.get("/2")
    def endpoint2():
        endpoint2.is_called = True

    lambler = Lambler()
    lambler.handle(api)

    endpoint1.is_called = endpoint2.is_called = False
    lambler({}, ...)
    assert not endpoint1.is_called and endpoint2.is_called
