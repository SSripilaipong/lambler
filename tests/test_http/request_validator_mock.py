from typing import Dict

from lambler.http import HttpRequestValidatorBase, HttpEvent


class RequestValidatorMock(HttpRequestValidatorBase):
    def __init__(self, validate__return: HttpEvent = None):
        self._validate__return = validate__return or HttpEvent(path="", headers={}, query_params={})

        self.validate__raw = None

    def validate(self, raw: Dict) -> HttpEvent:
        self.validate__raw = raw
        return self._validate__return
