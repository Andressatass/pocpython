from src.domain.use_cases.portfolio import Portfolio as PortfolioInterface

class Portfolio(PortfolioInterface):
    def __init__(self) -> None:
        pass

    def add_ticker(self, ticker_name: str, token: str) -> None:
        pass

    def delete_ticker(self, ticker_name: str, token: str) -> None:
        pass

    def check_portfolio(self, token: str) -> dict:
        pass
