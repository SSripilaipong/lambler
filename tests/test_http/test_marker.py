from lambler import Lambler
from lambler.http import HttpApi, Header
from tests.test_http.factory import simple_get_request


def test_should_pass_specified_header_value_from_key():
    api = HttpApi()

    @api.get("")
    def endpoint(my_name: str = Header("my-name")):
        endpoint.my_name = my_name

    lambler = Lambler()
    lambler.use(api)

    endpoint.my_name = None
    lambler(simple_get_request("", extra_headers={"my-name": "CopyPasteEng"}), ...)
    assert endpoint.my_name == "CopyPasteEng"
