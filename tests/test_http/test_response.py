from http import HTTPStatus

from lambler import Lambler
from lambler.http import HttpResponse, JsonResponse, HtmlResponse
from tests.test_http.http_api_factory import create_http_api_for_test, create_http_api_for_test_with_response_validator
from tests.test_http.response_validator_mock import ResponseValidatorMock


def test_should_validate_response():
    validator = ResponseValidatorMock()
    api = create_http_api_for_test_with_response_validator(validator)

    @api.get("")
    def endpoint():
        pass

    lambler = Lambler()
    lambler.handle(api)
    lambler({}, ...)

    assert validator.validate__is_called


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
