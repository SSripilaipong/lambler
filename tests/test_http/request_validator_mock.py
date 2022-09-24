from typing import Dict

from lambler.http import HttpRequestValidatorBase, HttpEvent


class RequestValidatorMock(HttpRequestValidatorBase):
    def __init__(self):
        self.validate__raw = None

    def validate(self, raw: Dict) -> HttpEvent:
        self.validate__raw = raw
        return HttpEvent(path="", headers={}, query_params={})
