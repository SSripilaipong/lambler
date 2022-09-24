# noinspection PyPackageRequirements
from pytest import raises

from lambler import Lambler
from lambler.http import Header
from tests.test_http.http_api_factory import create_http_api_for_test, RequestForTest, \
    create_http_api_for_test_with_request


def test_should_pass_specified_header_value_from_key():
    api = create_http_api_for_test_with_request(RequestForTest("GET", "", headers={"my-name": "CopyPasteEng"}))

    @api.get("")
    def endpoint(my_name: str = Header("my-name")):
        endpoint.my_name = my_name

    lambler = Lambler()
    lambler.handle(api)

    endpoint.my_name = None
    lambler({}, ...)
    assert endpoint.my_name == "CopyPasteEng"


def test_should_pass_multiple_header_values():
    api = create_http_api_for_test_with_request(
        RequestForTest("GET", "", headers={"my-a": "this is a", "my-b": "this is b"}))

    @api.get("")
    def endpoint(a: str = Header("my-a"), b: str = Header("my-b")):
        endpoint.a = a
        endpoint.b = b

    lambler = Lambler()
    lambler.handle(api)

    endpoint.a = endpoint.b = None
    lambler({}, ...)
    assert endpoint.a == "this is a" and endpoint.b == "this is b"


# noinspection PyPep8Naming
def test_should_raise_TypeError_when_type_annotation_is_not_string():
    api = create_http_api_for_test()

    with raises(TypeError) as e:
        @api.get("")
        def endpoint(_: int = Header("my-a")):
            pass

    assert str(e.value) == "Header marker can only be used with type 'str'"
