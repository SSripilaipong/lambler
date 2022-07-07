from abc import ABC, abstractmethod
from typing import Any


class ContentProvider(ABC):

    @abstractmethod
    def load(self, key: str) -> Any:
        pass
