from typing import Any, Dict

from lambler.http import HttpResponseValidatorBase


class ResponseValidatorMock(HttpResponseValidatorBase):
    def __init__(self):
        self.validate__is_called = False
        self.validate__raw = None

    def validate(self, raw: Any) -> Dict:
        self.validate__is_called = True
        self.validate__raw = raw
        return {}
