from http import HTTPStatus

from lambler.http import AwsHttpResponseValidator, HttpResponse


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
