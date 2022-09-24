from http import HTTPStatus

from lambler import Lambler
from lambler.http import HttpResponse, JsonResponse, HtmlResponse
from tests.test_http.http_api_factory import create_http_api_for_test


def test_should_return_empty_response_with_status_code_200_by_default():
    api = create_http_api_for_test()

    @api.get("")
    def endpoint():
        pass

    lambler = Lambler()
    lambler.handle(api)

    assert lambler({}, ...) == {
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
    api = create_http_api_for_test()

    @api.get("")
    def endpoint():
        return HttpResponse(HTTPStatus.CREATED, "ok!", headers={"my-header": "yeah"})

    lambler = Lambler()
    lambler.handle(api)

    assert lambler({}, ...) == {
        "statusCode": 201,
        "headers": {
            "my-header": "yeah"
        },
        "body": "ok!",
        "cookies": [],
        "isBase64Encoded": False,
    }


# noinspection PyPep8Naming
def test_should_return_response_from_JsonResponse_returned_by_endpoint():
    api = create_http_api_for_test()

    @api.get("")
    def endpoint():
        return JsonResponse(HTTPStatus.ACCEPTED, {"message": "ok", "hello": "world"})

    lambler = Lambler()
    lambler.handle(api)

    assert lambler({}, ...) == {
        "statusCode": 202,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {"message": "ok", "hello": "world"},
        "cookies": [],
        "isBase64Encoded": False,
    }


# noinspection PyPep8Naming
def test_should_return_html_response_from_HtmlResponse_returned_by_endpoint():
    api = create_http_api_for_test()

    @api.get("")
    def endpoint():
        return HtmlResponse(HTTPStatus.OK, '<html lang="en"></html>')

    lambler = Lambler()
    lambler.handle(api)

    assert lambler({}, ...) == {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html; charset=UTF-8"
        },
        "body": '<html lang="en"></html>',
        "cookies": [],
        "isBase64Encoded": False,
    }
