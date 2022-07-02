from lambler import Lambler
from lambler.http import HttpApi
from tests.test_http.factory import simple_get_request


def test_should_call_endpoint():
    api = HttpApi()

    @api.get("/")
    def endpoint():
        endpoint.is_called = True

    lambler = Lambler()
    lambler.use(api)

    endpoint.is_called = False
    lambler(simple_get_request("/"), ...)
    assert endpoint.is_called


def test_should_select_endpoint_by_path():
    api = HttpApi()

    @api.get("/1")
    def endpoint1():
        endpoint1.is_called = True

    @api.get("/2")
    def endpoint2():
        endpoint2.is_called = True

    lambler = Lambler()
    lambler.use(api)

    endpoint1.is_called = endpoint2.is_called = False
    lambler(simple_get_request("/1"), ...)
    assert endpoint1.is_called and not endpoint2.is_called

    endpoint1.is_called = endpoint2.is_called = False
    lambler(simple_get_request("/2"), ...)
    assert not endpoint1.is_called and endpoint2.is_called
