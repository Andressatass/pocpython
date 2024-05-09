from abc import ABC, abstractmethod

class Portfolio(ABC):

    @abstractmethod
    def add_ticker(self, ticker_name: str, token: str) -> None:
        pass

    @abstractmethod
    def delete_ticker(self, ticker_name: str, token: str) -> None:
        pass

    @abstractmethod
    def check_portfolio(self, token: str) -> dict:
        pass
