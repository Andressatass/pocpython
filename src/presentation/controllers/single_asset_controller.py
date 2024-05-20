from src.presentation.interfaces.single_asset_crontroller import ControllerInterface
from src.domain.use_cases.single_asset import SingleAsset as SingleAssetInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class SingleAssetController(ControllerInterface):
    def __init__(self, use_case: SingleAssetInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        ticker_name = http_request.query_params["ticker_name"]

        response = self.__use_case.get_price(ticker_name)

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
