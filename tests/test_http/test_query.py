from typing import List

from lambler import Lambler
from lambler.http import Query
from tests.test_http.http_api_factory import create_http_api_for_test_with_request, \
    RequestForTest


# noinspection DuplicatedCode
def test_should_pass_query_param_to_endpoint():
    api = create_http_api_for_test_with_request(RequestForTest("GET", "", query_params={"q": "123"}))

    @api.get("")
    def endpoint(q: str = Query("q")):
        endpoint.q = q

    lambler = Lambler()
    lambler.handle(api)

    endpoint.q = None
    lambler({}, ...)
    assert endpoint.q == "123"


# noinspection DuplicatedCode
def test_should_cast_data_type_to_primitives():
    api = create_http_api_for_test_with_request(RequestForTest("GET", "", query_params={"q": "123"}))

    @api.get("")
    def endpoint(q: int = Query("q")):
        endpoint.q = q

    lambler = Lambler()
    lambler.handle(api)

    endpoint.q = None
    lambler({}, ...)
    assert endpoint.q == 123


# noinspection DuplicatedCode
def test_should_cast_data_type_to_list():
    api = create_http_api_for_test_with_request(RequestForTest("GET", "", query_params={"q": "123,456"}))

    @api.get("")
    def endpoint(q: list = Query("q")):
        endpoint.q = q

    lambler = Lambler()
    lambler.handle(api)

    endpoint.q = None
    lambler({}, ...)
    assert endpoint.q == ["123", "456"]


# noinspection DuplicatedCode
def test_should_cast_data_type_to_list_when_using_list_typing():
    api = create_http_api_for_test_with_request(RequestForTest("GET", "", query_params={"q": "123,456"}))

    @api.get("")
    def endpoint(q: List = Query("q")):
        endpoint.q = q

    lambler = Lambler()
    lambler.handle(api)

    endpoint.q = None
    lambler({}, ...)
    assert endpoint.q == ["123", "456"]


# noinspection DuplicatedCode
def test_should_cast_data_type_to_list_when_using_list_typing_with_generic_primitive_type():
    api = create_http_api_for_test_with_request(RequestForTest("GET", "", query_params={"q": "123,456"}))

    @api.get("")
    def endpoint(q: List[int] = Query("q")):
        endpoint.q = q

    lambler = Lambler()
    lambler.handle(api)

    endpoint.q = None
    lambler({}, ...)
    assert endpoint.q == [123, 456]
