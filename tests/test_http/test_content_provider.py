from lambler import Lambler
from lambler.content import Content
from lambler.http import HttpApi

from .content_provider_mock import ContentProviderMock
from .factory import simple_get_request


def test_should_load_content_with_key():
    api = HttpApi()

    @api.get("")
    def endpoint(_: str = Content("my-content")):
        pass

    provider = ContentProviderMock()

    lambler = Lambler()
    lambler.handle(api)
    lambler.use_content(provider)

    lambler(simple_get_request(""), ...)
    assert provider.load__key == "my-content"


def test_should_load_content_with_key_with_handle_call_after_use_content_call():
    api = HttpApi()

    @api.get("")
    def endpoint(_: str = Content("my-content")):
        pass

    provider = ContentProviderMock()

    lambler = Lambler()
    lambler.use_content(provider)
    lambler.handle(api)

    lambler(simple_get_request(""), ...)
    assert provider.load__key == "my-content"


def test_should_load_with_None_scope_when_not_specified():
    api = HttpApi()

    @api.get("")
    def endpoint(_: str = Content("my-content")):
        pass

    provider = ContentProviderMock()

    lambler = Lambler()
    lambler.use_content(provider)
    lambler.handle(api)

    provider.load__scope = "something"
    lambler(simple_get_request(""), ...)
    assert provider.load__scope is None
