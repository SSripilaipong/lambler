from abc import ABC, abstractmethod
from typing import Any, Optional


class ContentProvider(ABC):

    @abstractmethod
    def load(self, key: str, scope: Optional[str]) -> Any:
        pass
