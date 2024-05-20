from abc import ABC, abstractmethod
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class PortfolioControllerInterface(ABC):

    @abstractmethod
    def add_ticker(self, http_request: HttpRequest) -> HttpResponse: pass

    @abstractmethod
    def delete_ticker(self, http_request: HttpRequest) -> HttpResponse: pass

    @abstractmethod
    def check_portfolio(self, http_request: HttpRequest) -> HttpResponse: pass

    @abstractmethod
    def check_price_today(self, http_request: HttpRequest) -> HttpResponse: pass
