from lambler import Lambler
from tests.test_http.http_api_factory import create_http_api_for_test_with_request, \
    RequestForTest


def test_should_match_the_long_path():
    api = create_http_api_for_test_with_request(RequestForTest("GET", "/a"))

    @api.get("")
    def short():
        short.is_called = True

    @api.get("/a")
    def long():
        long.is_called = True

    lambler = Lambler()
    lambler.handle(api)

    long.is_called = short.is_called = False
    lambler({}, ...)

    assert long.is_called and not short.is_called


def test_should_not_match_partially():
    api = create_http_api_for_test_with_request(RequestForTest("GET", "/a"))

    @api.get("")
    def endpoint():
        endpoint.is_called = True

    lambler = Lambler()
    lambler.handle(api)

    endpoint.is_called = False
    lambler({}, ...)
    assert not endpoint.is_called


def test_should_match_even_with_tailing_slash():
    api = create_http_api_for_test_with_request(RequestForTest("GET", "/"))

    @api.get("")
    def endpoint():
        endpoint.is_called = True

    lambler = Lambler()
    lambler.handle(api)

    endpoint.is_called = False
    lambler({}, ...)
    assert endpoint.is_called


def test_should_match_with_post_method():
    api = create_http_api_for_test_with_request(RequestForTest("POST", "/"))

    @api.get("")
    def get_endpoint():
        get_endpoint.is_called = True

    @api.post("")
    def post_endpoint():
        post_endpoint.is_called = True

    lambler = Lambler()
    lambler.handle(api)

    get_endpoint.is_called = post_endpoint.is_called = False
    lambler({}, ...)
    assert post_endpoint.is_called and not get_endpoint.is_called
