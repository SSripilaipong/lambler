import pytest

from lambler.resource import get_or_create_lambda_function


@pytest.mark.start_pull_data
def test_create_echo_lambda():
    get_or_create_lambda_function("lambler-pull-data", "./tests/test_api/echo.zip", "main.handler")


@pytest.mark.stop_pull_data
def test_destroy_echo_lambda():
    fn = get_or_create_lambda_function("lambler-pull-data", "./tests/test_api/echo.zip", "main.handler")
    fn.delete_cascade()
