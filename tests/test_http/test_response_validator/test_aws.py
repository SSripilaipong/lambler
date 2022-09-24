from http import HTTPStatus

from lambler.http import AwsHttpResponseValidator, HttpResponse, JsonResponse, HtmlResponse


def test_should_return_empty_response_with_status_200_by_default():
    validator = AwsHttpResponseValidator()

    assert validator.validate(None) == {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain"
        },
        "body": "",
        "cookies": [],
        "isBase64Encoded": False,
    }


# noinspection PyPep8Naming
def test_should_return_response_from_HttpResponse():
    validator = AwsHttpResponseValidator()

    raw = HttpResponse(HTTPStatus.CREATED, "ok!", headers={"my-header": "yeah"})

    assert validator.validate(raw) == {
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
    validator = AwsHttpResponseValidator()

    raw = JsonResponse(HTTPStatus.ACCEPTED, {"message": "ok", "hello": "world"})

    assert validator.validate(raw) == {
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
    validator = AwsHttpResponseValidator()

    raw = HtmlResponse(HTTPStatus.OK, '<html lang="en"></html>')

    assert validator.validate(raw) == {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html; charset=UTF-8"
        },
        "body": '<html lang="en"></html>',
        "cookies": [],
        "isBase64Encoded": False,
    }
