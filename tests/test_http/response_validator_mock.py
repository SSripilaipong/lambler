from typing import Any, Dict

from lambler.http import HttpResponseValidatorBase


class ResponseValidatorMock(HttpResponseValidatorBase):
    def __init__(self, validate__return: Dict = None):
        self._validate__return = validate__return or {}

        self.validate__is_called = False
        self.validate__raw = None

    def validate(self, raw: Any) -> Dict:
        self.validate__is_called = True
        self.validate__raw = raw
        return self._validate__return
