import json


def handler(event, _):
    return json.dumps(event)
