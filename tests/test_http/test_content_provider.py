from lambler import Lambler
from lambler.content import Content
from .content_provider_mock import ContentProviderMock
from .http_api_factory import create_http_api_for_test_with_request, RequestForTest


def test_should_load_content_with_key():
    api = create_http_api_for_test_with_request(RequestForTest("GET", ""))

    @api.get("")
    def endpoint(_: str = Content("my-content")):
        pass

    provider = ContentProviderMock()

    lambler = Lambler()
    lambler.handle(api)
    lambler.use_content(provider)

    lambler({}, ...)
    assert provider.load__key == "my-content"


def test_should_load_content_with_key_with_handle_call_after_use_content_call():
    api = create_http_api_for_test_with_request(RequestForTest("GET", ""))

    @api.get("")
    def endpoint(_: str = Content("my-content")):
        pass

    provider = ContentProviderMock()

    lambler = Lambler()
    lambler.use_content(provider)
    lambler.handle(api)

    lambler({}, ...)
    assert provider.load__key == "my-content"


# noinspection PyPep8Naming
def test_should_load_from_provider_in_None_scope_by_default():
    api = create_http_api_for_test_with_request(RequestForTest("GET", ""))

    @api.get("")
    def endpoint(_: str = Content("my-content")):
        pass

    provider = ContentProviderMock()

    lambler = Lambler()
    lambler.use_content({None: provider})
    lambler.handle(api)

    provider.load__scope = "something"
    lambler({}, ...)
    assert provider.load__is_called


def test_should_load_from_provider_with_custom_scope():
    api = create_http_api_for_test_with_request(RequestForTest("GET", ""))

    @api.get("")
    def endpoint(_: str = Content("my-content", scope="here")):
        pass

    provider = ContentProviderMock()

    lambler = Lambler()
    lambler.use_content({"here": provider})
    lambler.handle(api)

    lambler({}, ...)
    assert provider.load__is_called


def test_should_load_only_from_provider_with_specified_scope():
    api = create_http_api_for_test_with_request(RequestForTest("GET", ""))

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

    lambler({}, ...)
    assert provider1.load__is_called and not provider2.load__is_called


def test_should_pass_loaded_content_to_endpoint():
    api = create_http_api_for_test_with_request(RequestForTest("GET", ""))

    @api.get("")
    def endpoint(content: str = Content("my-content")):
        endpoint.content = content

    lambler = Lambler()
    lambler.use_content(ContentProviderMock(load__return="Hello World!"))
    lambler.handle(api)

    lambler({}, ...)
    assert endpoint.content == "Hello World!"
