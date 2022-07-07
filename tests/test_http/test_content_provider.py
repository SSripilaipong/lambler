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


# noinspection PyPep8Naming
def test_should_load_from_provider_in_None_scope_by_default():
    api = HttpApi()

    @api.get("")
    def endpoint(_: str = Content("my-content")):
        pass

    provider = ContentProviderMock()

    lambler = Lambler()
    lambler.use_content({None: provider})
    lambler.handle(api)

    provider.load__scope = "something"
    lambler(simple_get_request(""), ...)
    assert provider.load__is_called


def test_should_load_from_provider_with_custom_scope():
    api = HttpApi()

    @api.get("")
    def endpoint(_: str = Content("my-content", scope="here")):
        pass

    provider = ContentProviderMock()

    lambler = Lambler()
    lambler.use_content({"here": provider})
    lambler.handle(api)

    lambler(simple_get_request(""), ...)
    assert provider.load__is_called


def test_should_load_only_from_provider_with_specified_scope():
    api = HttpApi()

    @api.get("")
    def endpoint(_: str = Content("my-content", scope="here")):
        pass

    provider1 = ContentProviderMock()
    provider2 = ContentProviderMock()

    lambler = Lambler()
    lambler.use_content({
        "not here": provider2,
        "here": provider1,
    })
    lambler.handle(api)

    lambler(simple_get_request(""), ...)
    assert provider1.load__is_called and not provider2.load__is_called
