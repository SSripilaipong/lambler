from lambler import Lambler
from lambler.http import Param
from tests.test_http.http_api_factory import create_http_api_for_test
from tests.test_http.request_factory import simple_get_request


def test_should_extract_param_from_path():
    api = create_http_api_for_test()

    @api.get("/entities/{entity_id}/attribute")
    def endpoint(id_: str = Param("entity_id")):
        endpoint.id_ = id_

    lambler = Lambler()
    lambler.handle(api)

    endpoint.id_ = None
    lambler(simple_get_request("/entities/abc/attribute"), ...)
    assert endpoint.id_ == "abc"
