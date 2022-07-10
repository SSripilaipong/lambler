from lambler import Lambler
from lambler.http import HttpApi, Query
from tests.test_http.factory import simple_get_request_with_query


def test_should_pass_query_param_to_endpoint():
    api = HttpApi()

    @api.get("")
    def endpoint(q: str = Query("q")):
        endpoint.q = q

    lambler = Lambler()
    lambler.handle(api)

    endpoint.q = None
    lambler(simple_get_request_with_query("", "q=123", {"q": "123"}), ...)
    assert endpoint.q == "123"


def test_should_cast_data_type_to_primitives():
    # noinspection DuplicatedCode
    api = HttpApi()

    @api.get("")
    def endpoint(q: int = Query("q")):
        endpoint.q = q

    lambler = Lambler()
    lambler.handle(api)

    endpoint.q = None
    lambler(simple_get_request_with_query("", "q=123", {"q": "123"}), ...)
    assert endpoint.q == 123
