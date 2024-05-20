from src.presentation.interfaces.portfolio_controller import PortfolioControllerInterface
from src.domain.use_cases.portfolio import Portfolio
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class PortfolioController(PortfolioControllerInterface):
    def __init__(self, use_case: Portfolio) -> None:
        self.__use_case = use_case

    def add_ticker(self, http_request: HttpRequest) -> HttpResponse:
        ticker_name = http_request.query_params["ticker_name"]
        token = http_request.query_params["token"]

        response = self.__use_case.add_ticker(ticker_name, token)

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )

    def delete_ticker(self, http_request: HttpRequest) -> HttpResponse:
        ticker_name = http_request.query_params["ticker_name"]
        token = http_request.query_params["token"]

        response = self.__use_case.delete_ticker(ticker_name, token)

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )

    def check_portfolio(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.query_params["token"]

        response = self.__use_case.check_portfolio(token)

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )

    def check_price_today(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.query_params["token"]

        response = self.__use_case.check_price_today(token)

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
