from lambler import Lambler
from lambler.http import HttpApi
from tests.test_http.factory import simple_get_request


def test_should_return_empty_response_with_status_code_200_by_default():
    api = HttpApi()

    @api.get("")
    def endpoint():
        pass

    lambler = Lambler()
    lambler.handle(api)

    assert lambler(simple_get_request(""), ...) == {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain",
        },
        "body": "",
        "cookies": [],
        "isBase64Encoded": False
    }
