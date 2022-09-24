from lambler import Lambler
from tests.test_http.http_api_factory import create_http_api_for_test_with_response_validator
from tests.test_http.response_validator_mock import ResponseValidatorMock


def test_should_validate_response_from_endpoint():
    validator = ResponseValidatorMock()
    api = create_http_api_for_test_with_response_validator(validator)

    @api.get("")
    def endpoint() -> int:
        return 123

    lambler = Lambler()
    lambler.handle(api)
    lambler({}, ...)

    assert validator.validate__raw == 123


def test_should_return_from_validator():
    validator = ResponseValidatorMock(validate__return={"my": "response", "copy": "paste"})
    api = create_http_api_for_test_with_response_validator(validator)

    @api.get("")
    def endpoint() -> None:
        pass

    lambler = Lambler()
    lambler.handle(api)
    assert lambler({}, ...) == {"my": "response", "copy": "paste"}
