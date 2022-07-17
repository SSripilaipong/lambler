import inspect
from typing import Callable, Any, Dict, Type, get_origin, get_args

from ._path import EndpointPath
from .._event import HttpEvent
from .._header import Header
from .._param import Param
from .._query import Query
from ...content import Content, ContentProviderSpace
from ...template import Template, TemplateBase


class EndpointExecutor:
    def __init__(self, path: EndpointPath, f: Callable, signature: inspect.Signature, event: HttpEvent, *,
                 content_providers: ContentProviderSpace = None):
        self._path = path
        self._f = f
        self._signature = signature
        self._event = event

        self._content_providers = content_providers

    def execute(self) -> Any:
        return self._f(**self._extract_params())

    def _extract_params(self) -> Dict[str, Any]:
        if len(self._signature.parameters) == 0:
            return {}

        params = {name: self._extract_marker_value(marker=param.default, type_=param.annotation)
                  for name, param in self._signature.parameters.items()}

        return params

    def _extract_marker_value(self, marker: Any, type_: Type) -> Any:
        params = self._path.extract_params(self._event.path)

        if isinstance(marker, Header):
            value = marker.extract_event(self._event)
        elif isinstance(marker, Content):
            value = self._content_providers.get(marker.scope).load(marker.key)
        elif isinstance(marker, Param):
            value = params[marker.key]
        elif isinstance(marker, Query):
            value = _extract_query(marker, self._event, type_)
        elif isinstance(marker, Template):
            assert issubclass(type_, TemplateBase)
            type_.load()
            value = None
        else:
            raise NotImplementedError()
        return value


def _extract_query(marker: Query, event: HttpEvent, type_: Type):
    value = event.query_params[marker.key]
    if type_ is list:
        return value.split(",")
    if get_origin(type_) is list:
        args = get_args(type_)
        if args is ():
            return value.split(",")
        assert len(args) == 1
        cast = args[0]
        return [cast(v) for v in value.split(",")]

    return type_(value)
