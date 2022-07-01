import json

from lambler import Lambler
from lambler.http import HttpEndpoint


def test_should_call_handler():
    endpoint = HttpEndpoint()

    @endpoint.get("/")
    def handle():
        handle.is_called = True

    handle.is_called = False

    with open("./tests/test_http/test_get/event_data/simple.json", "r") as file:
        Lambler().use(endpoint)(json.load(file), ...)

    assert handle.is_called
