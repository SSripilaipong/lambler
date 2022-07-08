from lambler import Lambler
from lambler.http import HttpApi, Param
from tests.test_http.factory import simple_get_request


def test_should_extract_param_from_path():
    api = HttpApi()

    @api.get("/entities/{entity_id}/attribute")
    def endpoint(id_: str = Param("entity_id")):
        endpoint.id_ = id_

    lambler = Lambler()
    lambler.handle(api)

    endpoint.id_ = None
    lambler(simple_get_request("/entities/abc/attribute"), ...)
    assert endpoint.id_ == "abc"
