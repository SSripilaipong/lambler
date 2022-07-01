from abc import ABC, abstractmethod
from typing import Any, Dict


class Handler(ABC):
    @abstractmethod
    def handle(self, event: Dict, context: Any):
        pass
