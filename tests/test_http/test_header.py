# noinspection PyPackageRequirements
from pytest import raises

from lambler import Lambler
from lambler.http import HttpApi, Header
from tests.test_http.factory import simple_get_request


def test_should_pass_specified_header_value_from_key():
    api = HttpApi()

    @api.get("")
    def endpoint(my_name: str = Header("my-name")):
        endpoint.my_name = my_name

    lambler = Lambler()
    lambler.handle(api)

    endpoint.my_name = None
    lambler(simple_get_request("", extra_headers={"my-name": "CopyPasteEng"}), ...)
    assert endpoint.my_name == "CopyPasteEng"


def test_should_pass_multiple_header_values():
    api = HttpApi()

    @api.get("")
    def endpoint(a: str = Header("my-a"), b: str = Header("my-b")):
        endpoint.a = a
        endpoint.b = b

    lambler = Lambler()
    lambler.handle(api)

    endpoint.a = endpoint.b = None
    lambler(simple_get_request("", extra_headers={"my-a": "this is a", "my-b": "this is b"}), ...)
    assert endpoint.a == "this is a" and endpoint.b == "this is b"


# noinspection PyPep8Naming
def test_should_raise_TypeError_when_type_annotation_is_not_string():
    api = HttpApi()

    with raises(TypeError) as e:
        @api.get("")
        def endpoint(_: int = Header("my-a")):
            pass

    assert str(e.value) == "Header marker can only be used with type 'str'"
