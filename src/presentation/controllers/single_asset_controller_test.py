from src.presentation.controllers.single_asset_controller import SingleAssetController
from src.data.tests.single_asset import SingleAssetSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = {"ticker_name": "meuTeste"}

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = SingleAssetSpy()
    single_asset_controller = SingleAssetController(use_case)

    response = single_asset_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
