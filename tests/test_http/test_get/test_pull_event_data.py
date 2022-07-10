# noinspection PyPackageRequirements
import pytest
# noinspection PyPackageRequirements
import requests

from lambler.resource import get_or_create_lambda_function


@pytest.mark.pull_data
def test_should_pull_event_data():
    fn = get_or_create_lambda_function("lambler-pull-data", "./tests/test_api/echo.zip", "main.handler")

    resp = requests.get(fn.url)
    assert resp.status_code == 200

    with open("./tests/test_http/test_get/event_data/simple.json", "w") as file:
        file.write(resp.text)


@pytest.mark.pull_data
def test_should_pull_event_data_with_query_params():
    fn = get_or_create_lambda_function("lambler-pull-data", "./tests/test_api/echo.zip", "main.handler")

    resp = requests.get(fn.url + "?a=123&b=abc&c=111&c=222")
    assert resp.status_code == 200

    with open("./tests/test_http/test_get/event_data/with_query.json", "w") as file:
        file.write(resp.text)
