from abc import ABC, abstractmethod
from typing import Dict

from ._event import HttpEvent


class HttpRequestValidatorBase(ABC):

    @abstractmethod
    def validate(self, raw: Dict) -> HttpEvent:
        pass
