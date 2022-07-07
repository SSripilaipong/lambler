from abc import ABC, abstractmethod
from typing import Any, Dict

from lambler.content import ContentProvider


class Handler(ABC):
    @abstractmethod
    def handle(self, event: Dict, context: Any):
        pass

    @abstractmethod
    def set_content_provider(self, provider: ContentProvider):
        pass
