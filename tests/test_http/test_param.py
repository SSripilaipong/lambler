from lambler import Lambler
from lambler.http import Param
from tests.test_http.http_api_factory import create_http_api_for_test_with_request, \
    RequestForTest


def test_should_extract_param_from_path():
    api = create_http_api_for_test_with_request(RequestForTest("/entities/abc/attribute"))

    @api.get("/entities/{entity_id}/attribute")
    def endpoint(id_: str = Param("entity_id")):
        endpoint.id_ = id_

    lambler = Lambler()
    lambler.handle(api)

    endpoint.id_ = None
    lambler({}, ...)
    assert endpoint.id_ == "abc"
