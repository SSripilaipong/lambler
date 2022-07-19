import inspect
from abc import abstractmethod, ABC
from typing import Dict

from lambler import content
from lambler.content import ContentProviderSpace, Content


class TemplateBase(ABC):

    @classmethod
    @abstractmethod
    def load(cls, *args, **kwargs):
        pass

    @classmethod
    def do_load(cls, content_providers: ContentProviderSpace):
        cls.load(**_extract_template_params(inspect.signature(cls.load), content_providers))


def _extract_template_params(signature: inspect.Signature, content_providers: ContentProviderSpace) -> Dict:
    params = {}
    for name, param in signature.parameters.items():
        marker = param.default
        if isinstance(marker, Content):
            value = content.build_marked_params(content_providers, marker)
        else:
            raise NotImplementedError()
        params[name] = value
    return params
