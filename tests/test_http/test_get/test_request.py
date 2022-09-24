from lambler import Lambler
from tests.test_http.http_api_factory import create_http_api_for_test
from tests.test_http.request_factory import simple_get_request


def test_should_call_endpoint():
    api = create_http_api_for_test()

    @api.get("/")
    def endpoint():
        endpoint.is_called = True

    lambler = Lambler()
    lambler.handle(api)

    endpoint.is_called = False
    lambler(simple_get_request("/"), ...)
    assert endpoint.is_called


def test_should_select_endpoint_by_path():
    api = create_http_api_for_test()

    @api.get("/1")
    def endpoint1():
        endpoint1.is_called = True

    @api.get("/2")
    def endpoint2():
        endpoint2.is_called = True

    lambler = Lambler()
    lambler.handle(api)

    endpoint1.is_called = endpoint2.is_called = False
    lambler(simple_get_request("/1"), ...)
    assert endpoint1.is_called and not endpoint2.is_called

    endpoint1.is_called = endpoint2.is_called = False
    lambler(simple_get_request("/2"), ...)
    assert not endpoint1.is_called and endpoint2.is_called
