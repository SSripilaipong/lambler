from typing import Any

from lambler import Lambler
from lambler.content import Content, ContentProvider
from lambler.http import HttpApi
from lambler.template import Template, TemplateBase
from tests.test_http.factory import simple_get_request


def test_should_load_template():
    class MyTemplateMock(TemplateBase):
        @classmethod
        def load(cls):
            cls.load__is_called = True

    api = HttpApi()

    @api.get("")
    def endpoint(_: MyTemplateMock = Template()):
        pass

    lambler = Lambler()
    lambler.handle(api)

    MyTemplateMock.load__is_called = False
    lambler(simple_get_request(""), ...)
    assert MyTemplateMock.load__is_called


def test_should_pass_content_when_required():
    class MyTemplateMock(TemplateBase):
        @classmethod
        def load(cls, content: str = Content("")):
            cls.load__content = content

    class ContentProviderMock(ContentProvider):
        def load(self, key: str) -> Any:
            return "It's ME"

    api = HttpApi()

    @api.get("")
    def endpoint(_: MyTemplateMock = Template()):
        pass

    lambler = Lambler()
    lambler.use_content(ContentProviderMock())
    lambler.handle(api)

    MyTemplateMock.load__content = None
    lambler(simple_get_request(""), ...)
    assert MyTemplateMock.load__content == "It's ME"
