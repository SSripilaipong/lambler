from typing import Any

from lambler import Lambler
from lambler.content import Content, ContentProvider
from lambler.http import HttpApi
from lambler.template import Template, TemplateBase
from tests.test_http.factory import simple_get_request


def test_should_load_template():
    class MyTemplateMock(TemplateBase):
        @classmethod
        def load(cls) -> 'MyTemplateMock':
            cls.load__is_called = True
            return cls()

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
        def load(cls, content: str = Content("")) -> 'MyTemplateMock':
            cls.load__content = content
            return cls()

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


def test_should_pass_template_instance():
    class MyTemplateMock(TemplateBase):
        def __init__(self, data: str):
            self.data = data

        @classmethod
        def load(cls) -> 'MyTemplateMock':
            return cls("Hello World")

    api = HttpApi()

    @api.get("")
    def endpoint(template: MyTemplateMock = Template()):
        endpoint.template__data = template.data

    lambler = Lambler()
    lambler.handle(api)

    endpoint.template__data = None
    lambler(simple_get_request(""), ...)
    assert endpoint.template__data == "Hello World"


def test_should_load_another_template_when_required():
    class AnotherTemplate(TemplateBase):
        @classmethod
        def load(cls) -> 'AnotherTemplate':
            cls.load__is_called = True
            return cls()

    class MyTemplateMock(TemplateBase):
        @classmethod
        def load(cls, another_template: AnotherTemplate = Template()) -> 'MyTemplateMock':
            return cls()

    api = HttpApi()

    @api.get("")
    def endpoint(_: MyTemplateMock = Template()):
        pass

    lambler = Lambler()
    lambler.handle(api)

    AnotherTemplate.load__is_called = False
    lambler(simple_get_request(""), ...)
    assert AnotherTemplate.load__is_called


def test_should_pass_another_template_when_required():
    class AnotherTemplate(TemplateBase):
        def __init__(self):
            self.value = "Yeah!"

        @classmethod
        def load(cls) -> 'AnotherTemplate':
            return cls()

    class MyTemplateMock(TemplateBase):
        @classmethod
        def load(cls, another_template: AnotherTemplate = Template()) -> 'MyTemplateMock':
            cls.load__another_template_value = another_template.value
            return cls()

    api = HttpApi()

    @api.get("")
    def endpoint(_: MyTemplateMock = Template()):
        pass

    lambler = Lambler()
    lambler.handle(api)

    MyTemplateMock.load__another_template_value = None
    lambler(simple_get_request(""), ...)
    assert MyTemplateMock.load__another_template_value == "Yeah!"
