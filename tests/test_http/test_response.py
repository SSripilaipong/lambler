from http import HTTPStatus

from lambler import Lambler
from lambler.http import HttpApi, HttpResponse
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
        "isBase64Encoded": False,
    }


# noinspection PyPep8Naming
def test_should_return_response_from_HttpResponse_returned_by_endpoint():
    api = HttpApi()

    @api.get("")
    def endpoint():
        return HttpResponse(HTTPStatus.CREATED, "ok!", headers={"my-header": "yeah"})

    lambler = Lambler()
    lambler.handle(api)

    assert lambler(simple_get_request(""), ...) == {
        "statusCode": 201,
        "headers": {
            "my-header": "yeah"
        },
        "body": "ok!",
        "cookies": [],
        "isBase64Encoded": False,
    }
