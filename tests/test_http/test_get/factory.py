import json


def make_get_request(path: str):
    with open("./tests/test_http/test_get/event_data/simple.json", "r") as file:
        event = json.load(file)
    event["rawPath"] = event["requestContext"]["http"]["path"] = path
    return event
