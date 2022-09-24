from lambler import Lambler
from tests.test_http.http_api_factory import create_http_api_for_test_with_request_validator
from tests.test_http.request_validator_mock import RequestValidatorMock


def test_should_validate_request():
    validator = RequestValidatorMock()
    api = create_http_api_for_test_with_request_validator(validator)

    @api.get("")
    def endpoint():
        pass

    lambler = Lambler()
    lambler.handle(api)

    endpoint.q = None
    lambler({
        "path": "/my/path",
        "headers": {"my": "header", "hello": "world"},
        "query_params": {"my": "param", "query": 123},
    }, ...)
    assert validator.validate__raw == {
        "path": "/my/path",
        "headers": {"my": "header", "hello": "world"},
        "query_params": {"my": "param", "query": 123},
    }
