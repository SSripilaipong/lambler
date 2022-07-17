from lambler import Lambler
from lambler.http import HttpApi
from lambler.template import Template, TemplateBase
from tests.test_http.factory import simple_get_request


class MyTemplateMock(TemplateBase):
    @classmethod
    def load(cls, *_, **__):
        cls.load__is_called = True


def test_should_load_template():
    api = HttpApi()

    @api.get("")
    def endpoint(_: MyTemplateMock = Template()):
        pass

    lambler = Lambler()
    lambler.handle(api)

    MyTemplateMock.load__is_called = False
    lambler(simple_get_request(""), ...)
    assert MyTemplateMock.load__is_called
