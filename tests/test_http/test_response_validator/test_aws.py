from lambler.http import AwsHttpResponseValidator


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
