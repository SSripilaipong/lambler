import json

from lambler import Lambler
from lambler.http import HttpEndpoint


def test_should_call_handler():
    lambler = Lambler()
    endpoint = HttpEndpoint()

    @endpoint.get("/")
    def handle():
        handle.is_called = True

    handle.is_called = False

    lambler.use(
        endpoint,
    )

    with open("./tests/test_http/test_get/event_data/simple.json", "r") as file:
        lambler(json.load(file), ...)

    assert handle.is_called
