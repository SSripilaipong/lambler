import pytest
import requests

from lambler.resource import get_or_create_lambda_function


@pytest.mark.pull_data
def test_should_pull_event_data():
    fn = get_or_create_lambda_function("lambler-pull-data", "./tests/test_api/echo.zip", "main.handler")

    resp = requests.get(fn.url)
    assert resp.status_code == 200

    with open("./tests/test_http/test_get/event_data/simple.json", "w") as file:
        file.write(resp.text)
