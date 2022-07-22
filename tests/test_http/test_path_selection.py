from lambler import Lambler
from lambler.http import HttpApi
from tests.test_http.factory import simple_get_request


def test_should_match_the_long_path():
    api = HttpApi()

    @api.get("")
    def short():
        short.is_called = True

    @api.get("/a")
    def long():
        long.is_called = True

    lambler = Lambler()
    lambler.handle(api)

    long.is_called = short.is_called = False
    lambler(simple_get_request("/a"), ...)

    assert long.is_called and not short.is_called


def test_should_not_match_partially():
    api = HttpApi()

    @api.get("")
    def endpoint():
        endpoint.is_called = True

    lambler = Lambler()
    lambler.handle(api)

    endpoint.is_called = False
    lambler(simple_get_request("/a"), ...)
    assert not endpoint.is_called
